#!/usr/bin/python3
"""
    export_all_users_to_json
"""
import json
import requests


def export_all_users_to_json():

    users = 'https://jsonplaceholder.typicode.com/users'
    request_users = requests.get(users).json()
    info = {}

    for user in request_users:
        user_id = user.get('id')
        username = user.get('username')
        todos = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'
        request_todo = requests.get(todos).json()
        tasks = []

        for todo in request_todo:
            task = {"username": username,
                    "task": todo.get("title"),
                    "completed": todo.get("completed")
                    }
            tasks.append(task)

        info[user_id] = tasks

    with open('todo_all_employees.json', 'w+') as json_file:
        json_file.write(json.dumps(info))


if __name__ == "__main__":
    export_all_users_to_json()
