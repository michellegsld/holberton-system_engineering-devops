#!/usr/bin/python3
"""
Task 2:
2-export_to_JSON.py

Exports tasks for a given employee ID,
the TODO list progress.
This information is exported in JSON format.
Uses a specific API.
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    req = requests.get(url)
    username = req.json()["username"]
    total = len((requests.get(url + '/todos')).json())
    req = requests.get(url + '/todos')
    amount = len(req.json())

    data = {}
    data[argv[1]] = []

    for i in range(amount):
        completed = req.json()[i]["completed"]
        title = req.json()[i]["title"]
        data[argv[1]].append({
            "task": title,
            "completed": completed,
            "username": username
        })

    with open('{}.json'.format(argv[1]), 'w') as file:
        json.dump(data, file)
