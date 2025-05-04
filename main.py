from task_cli import load_tasks, add, update, delete


def main():
    file_path = 'tasks.json'
    while True:
        tasks = load_tasks(file_path)
        user_input = input("task-cli ")
        if user_input == "exit":
            exit()
        elif user_input.startswith("add "):
            add(tasks, user_input)
        elif user_input.startswith("update"):
            update(tasks, user_input)
        elif user_input.startswith("delete"):
            delete(tasks, user_input)
if __name__ == "__main__":
    main()