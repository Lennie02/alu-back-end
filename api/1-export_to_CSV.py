#!/usr/bin/python3
"""Export employee TODO list data to CSV format."""
import csv
import json
import sys
import urllib.request


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    with urllib.request.urlopen("{}/users/{}".format(base_url, employee_id)) as response:
        user = json.loads(response.read().decode("utf-8"))

    with urllib.request.urlopen("{}/todos?userId={}".format(base_url, employee_id)) as response:
        todos = json.loads(response.read().decode("utf-8"))

    username = user.get("username")
    filename = "{}.csv".format(employee_id)

    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])
