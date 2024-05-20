#!/usr/bin/python3
"Script to fetch a REST API and return informations in a certain way"
from sys import argv
import json
import requests



def main():
    usr_id = argv[1]
    usr_link = 'https://jsonplaceholder.typicode.com/users/{}'.format(usr_id)
    todos_link = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(usr_id)
    usr_res = requests.get(usr_link)
    todos_res = requests.get(todos_link)
    
    if usr_res.status_code != 200 or todos_res.status_code != 200:
        print("Error Fetching Data!")
        return
    user_data = usr_res.json()
    todos_data = todos_res.json()

    user_name = user_data['name']
    total_tasks = len(todos_data)
    done_tasks = len([task for task in todos_data if task['completed']])
    print('Employee {} is done with tasks({}/{}):'.format(
              user_name, done_tasks, total_tasks))
    for task in todos_data:
        if task['completed']:
            print(f"\t {task['title']}")

if __name__ == "__main__":
    main()
