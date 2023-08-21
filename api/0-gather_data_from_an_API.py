#!/usr/bin/python3

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
            if todo.get('completed') == True:
                complete.append(todo['title'])

        print(f'Employee {name} is done with tasks({len(complete)}/{len(todo_json)})')

        for todo in complete:
            print('\t', todo )




