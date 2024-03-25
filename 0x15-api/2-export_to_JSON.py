#!/usr/bin/python3
"""
This module fetches data from the JSONPlaceholder API.
It retrieves the tasks for a specific user
and writes them to a JSON file.
The file is named after the user's ID and contains
their tasks in a specific format.
"""

import json
import requests
from sys import argv


def fetch_data(employee_ID):
    """
    Fetches data from the JSONPlaceholder API for a specific user.
    Writes the user's tasks to a JSON file in a specific format.
    """

    # Get the employee's details
    name_res = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".
        format(employee_ID))
    name = name_res.json().get('name')  # Use get to access
    # dictionary value

    # Get the employee's tasks
    tasks_res = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".
        format(employee_ID))
    tasks = tasks_res.json()

    # Create JSON data to be written to the file
    json_data = {
        employee_ID: [{"task": task.get('title'), "completed":
                       task.get(
            'completed'), "username": name} for task in tasks]
    }

    # Write JSON data to file
    with open('{}.json'.
              format(employee_ID), 'w') as json_file:
        json.dump(json_data, json_file)


if __name__ == "__main__":
    # Only run the following code when the script
    # is executed directly (not imported)
    employee_ID = argv[1]
    fetch_data(employee_ID)
