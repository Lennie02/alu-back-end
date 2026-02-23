#!/usr/bin/python3
"""Export all employees TODO list data to JSON format."""
import json
import urllib.request


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"

    users_url = "{}/users".format(base_url)
    with urllib.request.urlopen(users_url) as response:
        users = json.loads(response.read().decode("utf-8"))

    todos_url = "{}/todos".format(base_url)
    with urllib.request.urlopen(todos_url) as response:
        todos = json.loads(response.read().decode("utf-8"))

    all_data = {}
    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        tasks = [{"username": username,
                  "task": task.get("title"),
                  "completed": task.get("completed")}
                 for task in todos if task.get("userId") == user_id]
        all_data[str(user_id)] = tasks

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_data, jsonfile)
