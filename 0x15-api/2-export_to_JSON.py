#!/usr/bin/python3
"Script to retrieve data from API and Export it into CSV file"
from sys import argv
import json
import requests


def main():
    usr_id = argv[1]
    user_link = f'https://jsonplaceholder.typicode.com/users/{usr_id}'
    todos_link = (
        f'https://jsonplaceholder.typicode.com/'
        f'todos?userId={usr_id}'
    )

    try:
        user_res = requests.get(user_link)
        todos_res = requests.get(todos_link)

        if user_res.status_code != 200 or todos_res.status_code != 200:
            print("Error fetching data from API")
            return

        user_data = user_res.json()
        todos_data = todos_res.json()

        user_name = user_data['username']

        tasks = [{"task": task["title"],
                  "completed": task["completed"],
                  "username": user_name} for task in todos_data]
        data = {usr_id: tasks}
        json_file = f"{usr_id}.json"
        with open(json_file, mode='w') as file:
            json.dump(data, file)

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")


if __name__ == "__main__":
    main()
