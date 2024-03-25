#!/usr/bin/python3
"""
This module fetches data from the JSONPlaceholder API.
It retrieves the tasks for a specific user and writes them to a CSV file.
"""

import csv
import requests
from sys import argv


def fetch_data_and_write_to_csv(employee_id):
    """
    Fetches data from the JSONPlaceholder API for a specific user.
    Writes the user's tasks to a CSV file.
    """

    # Get the employee's details
    name_res = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".
        format(employee_id))
    name = name_res.json().get('name')  # Use get to access dictionary value

    # Get the employee's tasks
    tasks_res = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".
        format(employee_id))
    tasks = tasks_res.json()

    # Open the CSV file and write the tasks to it
    with open('{}.csv'.format(employee_id), 'w', newline='') as csvfile:
        taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in tasks:
            taskwriter.writerow(
                [employee_id, name, task.get('completed'), task.get('title')])


if __name__ == "__main__":
    # Only run the following code when the script is executed directly
    # (not imported)
    employee_id = argv[1]
    fetch_data_and_write_to_csv(employee_id)
