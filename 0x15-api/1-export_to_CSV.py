#!/usr/bin/python3
"""
task 1 APIs
the api: https://jsonplaceholder.typicode.com/

"""
import csv
from sys import argv
import requests

employee_ID = argv[1]

name_res = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(employee_ID))

name = name_res.json()['name']

tasks_res = requests.get(
    "https://jsonplaceholder.typicode.com/todos?userId={}".
    format(employee_ID))
tasks = tasks_res.json()

# Calculate the number of done tasks and the total number of tasks
done_tasks = [task for task in tasks if task['completed']]
number_of_done_tasks = len(done_tasks)
total_number_of_tasks = len(tasks)

print("Employee {} is done with tasks({}/{}):".
      format(name, number_of_done_tasks, total_number_of_tasks))
for task in done_tasks:
    print("\t {}".format(task['title']))

    # Open the CSV file and write the tasks to it
with open('{}.csv'.format(employee_ID), 'w', newline='') as csvfile:
    taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    for task in tasks:
        taskwriter.writerow(
            [employee_ID, name, task['completed'], task['title']])
