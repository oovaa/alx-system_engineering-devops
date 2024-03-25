#!/usr/bin/python3
"""Exports data in the JSON format"""


import json
import requests


def get_all_tasks():
    """
    Fetches data from the JSONPlaceholder API for all users.
    Stores the tasks in a dictionary and writes it to a JSON file.
    """

    # Get all users
    users_res = requests.get("https://jsonplaceholder.typicode.com/users")
    users = users_res.json()

    # Get all tasks
    tasks_res = requests.get("https://jsonplaceholder.typicode.com/todos")
    tasks = tasks_res.json()

    user_data = {}

    for user in users:
        user_data[user['id']] = []
        for task in tasks:
            if task['userId'] == user['id']:
                task_dict = {
                    "username": user['username'],
                    "task": task['title'],
                    "completed": task['completed']
                }
                user_data[user['id']].append(task_dict)

    with open('todo_all_employees.json', 'w') as f:
        json.dump(user_data, f)


if __name__ == "__main__":
    get_all_tasks()
