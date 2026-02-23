#!/usr/bin/python3
"""Export employee TODO list data to JSON format."""
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

    username = user.get("username")
    filename = "{}.json".format(employee_id)

    tasks = [{"task": task.get("title"),
              "completed": task.get("completed"),
              "username": username} for task in todos]

    with open(filename, "w") as jsonfile:
        json.dump({str(employee_id): tasks}, jsonfile)
