#!/usr/bin/python3
"""
This module fetches data from the JSONPlaceholder API.
It retrieves the tasks for a specific user and prints
the completed tasks.
"""

from sys import argv
import requests


def print_completed_tasks(employee_ID):
    """
    Fetches data from the JSONPlaceholder API for a specific user.
    Prints the user's completed tasks.
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

    # Calculate the number of done tasks and the total number of tasks
    # Use get to access dictionary value
    done_tasks = [task for task in tasks if task.get('completed')]
    number_of_done_tasks = len(done_tasks)
    total_number_of_tasks = len(tasks)

    print("Employee {} is done with tasks({}/{}):".
          format(name,
                 number_of_done_tasks, total_number_of_tasks))
    for task in done_tasks:
        # Use get to access dictionary value
        print("\t {}".
              format(task.get('title')))


if __name__ == "__main__":
    # Only run the following code when the script is executed directly
    # (not imported)
    employee_ID = argv[1]
    print_completed_tasks(employee_ID)
