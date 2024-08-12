import os
import requests
from celery import Celery
from tasker import db

app = Celery('tasks', broker='redis://localhost:6379/0')

# Retrieve GitLab API URL and Token from environment variables
GITLAB_API_URL = os.getenv("GITLAB_API_URL", "https://gitlab.com/api/v4")
GITLAB_TOKEN = os.getenv("GITLAB_TOKEN")

@app.task
def run_task(task_id, task_name, parameters, requester_ip):
    if task_name == 'sum':
        if len(parameters) != 2:
            raise ValueError("Sum task requires exactly two parameters.")
        result = sum(parameters)

    elif task_name == 'multiply':
        if len(parameters) != 3:
            raise ValueError("Multiply task requires exactly three parameters.")
        result = parameters[0] * parameters[1] * parameters[2]

    elif task_name == 'gitlab_collector':
        group_name = parameters[0]
        collect_gitlab_data(group_name)

    else:
        raise ValueError("Unsupported task name.")

    db.save_task_result(task_id, task_name, parameters, requester_ip, result)

def collect_gitlab_data(group_name):
    headers = {"Authorization": f"Bearer {GITLAB_TOKEN}"}

    # Get all projects in the group
    projects_response = requests.get(f"{GITLAB_API_URL}/groups/{group_name}/projects", headers=headers)
    projects = projects_response.json()

    # Get all users in the group
    users_response = requests.get(f"{GITLAB_API_URL}/groups/{group_name}/members", headers=headers)
    users = users_response.json()

    # Store projects and users in the database
    for project in projects:
        db.save_gitlab_project(group_name, project['id'], project['name'], project['web_url'])

    for user in users:
        db.save_gitlab_user(group_name, user['id'], user['username'], user['name'])

    # Link users to projects
    for project in projects:
        project_id = project['id']
        project_members_response = requests.get(f"{GITLAB_API_URL}/projects/{project_id}/members", headers=headers)
        project_members = project_members_response.json()

        for member in project_members:
            db.save_project_user(project_id, member['id'])
