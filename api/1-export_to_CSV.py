#!/usr/bin/python3
"""
export_to_csv
"""
import requests
import sys


def export_to_csv():

    user_id = sys.argv[1]
    user = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    todos = f'https://jsonplaceholder.typicode.com/todos/?userId={user_id}'
    username = requests.get(user).json().get('username')
    request_todo = requests.get(todos).json()

    with open(f'{user_id}.csv', 'w+') as csv_file:
        for todo in request_todo:
            completed = todo.get('completed')
            title = todo.get('title')
            info = f'"{user_id}","{username}","{completed}","{title}"\n'
            csv_file.write(info)


if __name__ == "__main__":

    if len(sys.argv) == 2:
        export_to_csv()
