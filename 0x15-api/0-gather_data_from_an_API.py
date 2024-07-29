#!/usr/bin/python3
"""This module gathers data from an API"""

import requests
import sys


if __name__ == "__main__":
    # Defines the URL for the REST API
    url = "https://jsonplaceholder.typicode.com/"

    # sends a GET request to retrieve user info
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()

    # sends a GET request to retrive the TODO list
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    # filters completed TODO list and store titles in a list
    completed = [t.get("title") for t in todos if t.get("completed") is True]

    # prints employee's name, completed tasks & total no of tasks
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    # prints the titles of completed tasks with indentation
    [print("\t {}".format(c)) for c in completed]
