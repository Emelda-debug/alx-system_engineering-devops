#!/usr/bin/python3
"""
script that extend your Python script to export data in the CSV format.

"""

import requests
import sys


if __name__ == "__main__":
    # Get the user ID from the command-line arguments provided to the script
    user_id = sys.argv[1]

    # Define the base URL for the JSON API
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user information from the API and
    # convert response to a JSON object
    user = requests.get(url + "users/{}".format(user_id)).json()

    # Extract  username from the user data
    username = user.get("username")

    # Fetch the to-do list items associated with the
    #   given user ID and convert the response to a JSON object
    to_do = requests.get(url + "to_do", params={"userId": user_id}).json()

    # Use list comprehension to iterate over the to-do list items
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
         ) for t in to_do]
