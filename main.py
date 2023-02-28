while True:
    user_action = input("Type Add, Show, Edit, Remove or Exit : ")
    user_action = user_action.strip()
    if 'add' in user_action:
        todo = user_action[4:] + '\n'

        with open("data/todos.txt", 'r') as file:
            todos = file.readlines()
        todos.append(todo)

        with open("data/todos.txt", 'w') as file:
            file.writelines(todos)

    elif 'show' in user_action:
        with open("data/todos.txt", 'r') as file:
            todos = file.readlines()
        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1}-{item.strip()}")
    elif 'edit' in user_action:
        number = int(input("Number of the ToDo to Edit: "))
        number = number - 1
        new_todo = input("Enter the New Todo: ")
        with open("data/todos.txt", 'r') as file:
            todos = file.readlines()
        todos[number] = new_todo + "\n"

        # updates the new todo
        with open("data/todos.txt", "w") as file:
            file.writelines(todos)

    elif 'remove' in user_action:
        number = int(input("Number of ToDo to Remove: "))
        with open("data/todos.txt", "r") as file:
            todos = file.readlines()
        todo_to_remove = todos[number - 1].strip("\n")
        todos.pop(number - 1)

        with open("data/todos.txt", "w") as file:
            file.writelines(todos)
        print(f"Todo: '{todo_to_remove}' has been removed")

    elif 'exit' in user_action:
        break
    else:
        print("Invalid Command")
print("Bye...")
