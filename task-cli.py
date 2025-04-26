import sys
import json
import os
import datetime

file_path = "tasks.json"
def load_tasks(file_path):
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            json.dump([], file)
    else:
        print(f"The file '{file_path}' already exists.")
        with open(file_path, "r") as file:
            try:
                write = json.load(file)
                if isinstance(write, list) == False:
                    with open(file_path, "w") as file:
                        json.dump([], file)
                len(write) == 0
                with open(file_path, "w") as file:
                    json.dump([], file)            
            except json.decoder.JSONDecodeError:
                with open(file_path, "w") as file:
                    json.dump([], file)
                        

load_tasks(file_path)