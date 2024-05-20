#!/usr/bin/python3
"Script to fetch a REST API and return informations in a certain way"
import csv
import json
import requests
from sys import argv


def main():
    usr_id = argv[1]
    usr_link = 'https://jsonplaceholder.typicode.com/users/{}'.format(usr_id)
    todos_link = ('https://jsonplaceholder.typicode.com/todos?userId={}'
                  .format(usr_id))
    usr_res = requests.get(usr_link)
    todos_res = requests.get(todos_link)

    if usr_res.status_code != 200 or todos_res.status_code != 200:
        print("Error Fetching Data!")
        return
    user_data = usr_res.json()
    todos_data = todos_res.json()

    user_name = user_data['username']
    
    csv_file = f'{usr_id}.csv'
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['USER_ID',
                         'USERNAME',
                         'TASK_COMPLETED_STATUS',
                         'TASK_TITLE'])
        for task in todos_data:
            writer.writerow([usr_id,
                             user_name,
                             task['completed'],
                             task['title']])

if __name__ == "__main__":
    main()
