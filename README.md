Tasker Application
This application processes tasks asynchronously using Flask and Celery. It also has the capability to collect and store data from GitLab groups in a SQLite database.

Features
Processes tasks such as summing two numbers or multiplying three numbers.
Handles tasks asynchronously using Celery.
Stores task results and GitLab data in a SQLite database.
Collects data from GitLab groups, including all projects, all users, and links users to projects.

Prerequisites
Docker (required for containerized deployment)
Docker Compose (for orchestrating multiple services)

Setup and Execution Instructions
1. Extract the ZIP File
After receiving the project, extract the contents of the ZIP file to your desired location on your computer.

2. Set Environment Variables
Before running the application, you need to set the following environment variables:

GITLAB_API_URL: The base URL for the GitLab API. By default, it is set to https://gitlab.com/api/v4.
GITLAB_TOKEN: Your GitLab Personal Access Token, which is required to authenticate API requests.

Linux : 
export GITLAB_API_URL="https://gitlab.com/api/v4"
export GITLAB_TOKEN="your_access_token_here"

Windows:
set GITLAB_API_URL=https://gitlab.com/api/v4
set GITLAB_TOKEN=your_access_token_here

2. Build and Run the Application
   Build the Docker Image:
	Open a terminal and navigate to the directory where the project files were extracted.
	Use the following command to build the Docker image:

	docker build -t tasker-app .

This command will use the Dockerfile to create an image named tasker-app, which includes all the necessary dependencies and the application itself.

Run the Application with Docker Compose:
Once the Docker image is built, you can use Docker Compose to run the application along with the necessary services like Redis and the Celery worker.

	Use the following command to start the services:

	docker-compose up

Docker Compose will automatically start the Flask application, Celery worker, and Redis service. The application will be accessible, and all tasks will be processed asynchronously.

3. Once the containers are running:

The Flask application will be accessible in your web browser at http://localhost:5000.
You can interact with the API, trigger tasks, and manage data directly through this interface.

4. Execute Tasks Using curl
You can use curl to interact with the application by sending HTTP POST requests to the API.

Example 1: Sum Two Numbers
	curl -X POST http://localhost:5000/task -H "Content-Type: application/json" -d "{\"task_name\": \"sum\", \"parameters\": [4, 5]}"

Example 2: Multiply Three Numbers
	curl -X POST http://localhost:5000/task -H "Content-Type: application/json" -d "{\"task_name\": \"multiply\", \"parameters\": [2, 3, 4]}"

Example 3: Collect GitLab Data  *MUST ADD YOU ACCESS TOKEN BEFORE TO TAKS.PY
	curl -X POST http://localhost:5000/task -H "Content-Type: application/json" -d "{\"task_name\": \"multiply\", \"parameters\": [2, 3, 4]}"

5. Stop the Application
	docker-compose down

6. Cleanup (Optional)
	docker-compose down --volumes
