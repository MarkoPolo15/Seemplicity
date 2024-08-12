from flask import Flask, request, jsonify
import uuid
from tasker import tasks, db

app = Flask(__name__)

@app.route('/task', methods=['POST'])
def create_task():
    data = request.json
    task_name = data.get('task_name')
    parameters = data.get('parameters')

    task_id = str(uuid.uuid4())
    requester_ip = request.remote_addr

    # Enqueue the task for background processing
    tasks.run_task.apply_async(args=[task_id, task_name, parameters, requester_ip])

    return jsonify({'task_id': task_id}), 202

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
