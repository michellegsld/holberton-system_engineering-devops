#!/usr/bin/python3
"""
Task 0:
0-gather_data_from_an_API.py

Returns information for each given employee ID,
the TODO list progress.
Uses a specific API.
"""
import requests
from sys import argv

if __name__ == "__main__":
    try:
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
        req = requests.get(url)
        name = req.json()["name"]
        req = requests.get(url + '/todos', params={"completed": "true"})
        amount = len(req.json())
        print("Employee {} is done with tasks ({}/20)".format(name, amount))
        for i in range(amount):
            print("{}".format(req.json()[i]["title"]))
    except:
        pass
