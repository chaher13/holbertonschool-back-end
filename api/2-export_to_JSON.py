#!/usr/bin/python3
"""
    export_to_json
"""
import json
import requests
import sys


def export_to_json():

    user_id = sys.argv[1]
    user = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    todos = f'https://jsonplaceholder.typicode.com/todos/?userId={user_id}'
    username = requests.get(user).json().get('username')
    request_todo = requests.get(todos).json()
    tasks = []

    with open(f'{user_id}.json', 'w+') as json_file:
        for todo in request_todo:
            task = {"task": todo.get("title"),
                    "completed": todo.get("completed"), "username": username}
            tasks.append(task)
        info = {user_id: tasks}
        json_file.write(json.dumps(info))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        export_to_json()
