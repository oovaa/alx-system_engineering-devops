#!/usr/bin/python3
"""
task 1 APIs
the api: https://jsonplaceholder.typicode.com/

"""
import json
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

# Create JSON data to be written to the file
json_data = {
    employee_ID: [{"task": task['title'], "completed": task['completed'],
                   "username": name} for task in tasks]
}

# Write JSON data to file
with open('{}.json'.format(employee_ID), 'w') as json_file:
    json.dump(json_data, json_file)
