#!/usr/bin/python3
"""
script that for a given employee ID, returns information about his/her
TODO list progress  using this REST API,
"""
import requests
import sys

if __name__ == "__main__":
# Base URL for the JSONPlaceholder API
url = "https://jsonplaceholder.typicode.com/"

#Retrieving employee information using the provided employee ID
employee_id = sys.argv[1]
user = requests.get(url + "users/{}".format(employee_id)).json()

#retrieving o-do list for the employee using the provided employee ID
params = {"userId": employee_id}
to_do = requests.get(url + "todos", params).json()

#Filtering completed tasks and counting them
completed = [t.get("title") for t in todos if t.get("completed") is True]

#Printing employee's name and the number of completed tasks
print("Employee {} is done with tasks({}/{}):".format(
    user.get("name"), len(completed), len(to_do)))

#Printing completed tasks one by one with indentation
 [print("\t {}".format(complete)) for complete in completed]


