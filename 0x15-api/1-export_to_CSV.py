#!/usr/bin/python3
"""
Task 1:
1-export_to_CSV.py

Exports tasks for a given employee ID,
the TODO list progress.
This information is exported in CSV format.
Uses a specific API.
"""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    req = requests.get(url)
    name = req.json()["name"]
    total = len((requests.get(url + '/todos')).json())
    req = requests.get(url + '/todos')
    amount = len(req.json())

    with open('USER_ID.csv', mode='w') as f:
        w = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        for i in range(amount):
            completed = req.json()[i]["completed"]
            title = req.json()[i]["title"]
            w.writerow([argv[1], name, completed, title])
