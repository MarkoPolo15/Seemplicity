import sqlite3
from datetime import datetime

def connect_db():
    conn = sqlite3.connect('tasker.db')
    return conn

def save_task_result(task_id, task_name, parameters, requester_ip, result):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks
                      (id TEXT PRIMARY KEY, name TEXT, parameters TEXT,
                       ip TEXT, timestamp TEXT, result TEXT)''')

    timestamp = datetime.utcnow().isoformat()
    cursor.execute('''INSERT INTO tasks (id, name, parameters, ip, timestamp, result)
                      VALUES (?, ?, ?, ?, ?, ?)''', 
                   (task_id, task_name, str(parameters), requester_ip, timestamp, str(result)))

    conn.commit()
    conn.close()

def save_gitlab_project(group_name, project_id, project_name, web_url):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS gitlab_projects
                      (group_name TEXT, project_id INTEGER PRIMARY KEY,
                       project_name TEXT, web_url TEXT)''')

    cursor.execute('''INSERT INTO gitlab_projects (group_name, project_id, project_name, web_url)
                      VALUES (?, ?, ?, ?)''', 
                   (group_name, project_id, project_name, web_url))

    conn.commit()
    conn.close()

def save_gitlab_user(group_name, user_id, username, name):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS gitlab_users
                      (group_name TEXT, user_id INTEGER PRIMARY KEY,
                       username TEXT, name TEXT)''')

    cursor.execute('''INSERT INTO gitlab_users (group_name, user_id, username, name)
                      VALUES (?, ?, ?, ?)''', 
                   (group_name, user_id, username, name))

    conn.commit()
    conn.close()

def save_project_user(project_id, user_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS project_users
                      (project_id INTEGER, user_id INTEGER)''')

    cursor.execute('''INSERT INTO project_users (project_id, user_id)
                      VALUES (?, ?)''', 
                   (project_id, user_id))

    conn.commit()
    conn.close()
