#!/usr/bin/python3

"""
    Retrieve completed tasks for a user from the JSONPlaceholder API
    and display the results.

    This script takes an user ID as a command-line argument,
    queries the JSONPlaceholder API
    for user information and their tasks,
    and then displays the count and titles of completed tasks.

    Usage:
        python script_name.py <user_id>

    Args:
        user_id (int): The ID of the user for whom to retrieve completed tasks.

"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:

        user_id = sys.argv[1]
        user = f'https://jsonplaceholder.typicode.com/users/{user_id}'
        todos = f'https://jsonplaceholder.typicode.com/todos/?userId={user_id}'

        response_user = requests.get(user)
        user_data = response_user.json()
        name = user_data.get('name')
        response_todos = requests.get(todos)
        todo_json = response_todos.json()

        complete = []
        for todo in todo_json:
            if todo.get('completed') is True:
                complete.append(todo['title'])

        print(f'Employee {name} is done with tasks({len(complete)}\
              /{len(todo_json)})')

        for todo in complete:
            print('\t', todo)
