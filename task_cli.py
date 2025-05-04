import sys
import json
import os
from datetime import datetime

file_path = "tasks.json"
def load_tasks(file_path):
    write = []
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            json.dump([], file)
            print(f"The file '{file_path}' has been created.")
    else:
        print(f"The file '{file_path}' already exists.")
        with open(file_path, "r") as file:
            try:
                write = json.load(file)
                if not isinstance(write, list) or len(write) == 0:
                    with open(file_path, "w") as file:
                        json.dump([], file)
                        print(f"The file '{file_path}' has been reset.")
            except json.decoder.JSONDecodeError:
                with open(file_path, "w") as file:
                    json.dump([], file)
                    print(f"The file '{file_path}' has reset due to invalid content.")
    print(write)
    return write

def save_tasks(tasks):
    with open(file_path, "w") as file:
        json.dump(tasks, file)

def add(tasks, user_input):
    existing_id = [task["id"] for task in tasks if "id" in task and task["id"]]
    id_number = max(existing_id) + 1 if existing_id else 1
    
    description = user_input[4:].strip().strip('""')
    now = datetime.now()
    status = "todo"
    new_tasks = {
        "id": id_number,
        "description": description,
        "status": status,
        "createdAt": now.isoformat(),
        "updatedAt": now.isoformat(),
    }
    tasks.append(new_tasks)
    save_tasks(tasks)

def update(tasks, user_input):
    now = datetime.now()
    parts = user_input.split()
    if len(parts) > 2:
        task_id = int(parts[1])
        description = ' '.join(parts[2:]).strip('""')
        for task in tasks:
            if task["id"] == task_id:
                task["description"] = description
                task["updatedAt"] = now.isoformat()
                save_tasks(tasks)

def delete(tasks, user_input):
    parts = user_input.split()
    if len(parts) == 2:
        task_id = int(parts[1])
        for task in tasks:
            if task["id"] == task_id:
                tasks.remove(task)
                save_tasks(tasks)
