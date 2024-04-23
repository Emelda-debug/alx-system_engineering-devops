#!/usr/bin/python3
"""
script that extend your Python script to export data in the JSON format.
"""

if __name__ == "__main__":

    user_id = sys.argv[1]


    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user information using the provided employee ID
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")

    # Fetching the to-do list for the employee using the provided employee ID
    params = {"userId": user_id}
    to_do = requests.get(url + "to_do", params).json()

    # Creating a dictionary containing the user and to-do list information
    data_to_export = {
        user_id: [
            {
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            }
            for t in to_do
        ]
    }

    # Writing data to a JSON file with the employee ID as the filename
    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)
