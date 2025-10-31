#!/usr/bin/python3
"""Script to use a REST API, returns information about
all tasks from all employees and export in JSON"""
import json
import requests


if __name__ == "__main__":
    API_URL = "https://jsonplaceholder.typicode.com"

    users = requests.get(f"{API_URL}/users").json()

    dict_users_tasks = {}
    for user in users:
        tasks = requests.get(f"{API_URL}/users/{user['id']}/todos").json()

        dict_users_tasks[user.get("id")] = []
        for task in tasks:
            task_dict = {
                "username": user.get("username"),
                "task": task.get("title"),
                "completed": task.get("completed")}
            dict_users_tasks[user.get("id")].append(task_dict)

    with open("todo_all_employees.json", "w") as file:
        json.dump(dict_users_tasks, file)
