#!/usr/bin/python3
"""Gather data from an API to display employee TODO list progress."""
import json
import sys
import urllib.request


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    user_url = "{}/users/{}".format(base_url, employee_id)
    with urllib.request.urlopen(user_url) as response:
        user = json.loads(response.read().decode("utf-8"))

    todos_url = "{}/todos?userId={}".format(base_url, employee_id)
    with urllib.request.urlopen(todos_url) as response:
        todos = json.loads(response.read().decode("utf-8"))

    employee_name = user.get("name")
    done_tasks = [task for task in todos if task.get("completed")]
    total = len(todos)
    done = len(done_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, done, total))
    for task in done_tasks:
        print("\t {}".format(task.get("title")))
