#!/usr/bin/python3
"""Script to use a REST API for a given employee ID, returns
information about his/her TODO list progress"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"UsageError: python3 {__file__} missing employee_id(int)")
        sys.exit(1)

    API_URL = "https://jsonplaceholder.typicode.com"
    EMPLOYEE_ID = sys.argv[1]

    response = requests.get(
        f"{API_URL}/users/{EMPLOYEE_ID}/todos",
        params={"_expand": "user"} 
    )
    data = response.json()

    if response.status_code == 404:
        print("RequestError:", 404)
        sys.exit(1)
    elif not data:
        print("No tasks found for that employee ID.")
        sys.exit(1)

    EMPLOYEE_NAME = data[0].get("user", {}).get("name")
    done_tasks = [task for task in data if task.get("completed")]
    NUMBER_OF_DONE_TASKS = len(done_tasks)
    TOTAL_NUMBER_OF_TASKS = len(data)

    print(f"Employee {EMPLOYEE_NAME} is done with tasks"
          f"({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
    for task in done_tasks:
        TASK_TITLE = task.get("title")
        print(f"\t {TASK_TITLE}")