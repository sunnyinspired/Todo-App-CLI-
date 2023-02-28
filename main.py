while True:
    user_action = input("Type Add, Show, Edit, Remove or Exit : ")
    user_action = user_action.strip()
    if user_action.startswith("add"):
        todo = user_action[4:]

        with open("data/todos.txt", 'r') as file:
            todos = file.readlines()
        todos.append(todo + "\n")

        with open("data/todos.txt", 'w') as file:
            file.writelines(todos)

    elif user_action.startswith("show"):
        with open("data/todos.txt", 'r') as file:
            todos = file.readlines()
        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1}-{item.strip()}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1
            new_todo = input("Enter the New Todo: ")
            with open("data/todos.txt", 'r') as file:
                todos = file.readlines()
            todos[number] = new_todo + "\n"

            # updates the new todo
            with open("data/todos.txt", "w") as file:
                file.writelines(todos)
        except ValueError:
            print("Invalid Command")
            continue
        except IndexError:
            print("There is no Todo Item with that Number")
            continue

    elif user_action.startswith("remove"):
        try:
            number = int(input("Number of ToDo to Remove: "))
            with open("data/todos.txt", "r") as file:
                todos = file.readlines()
            todo_to_remove = todos[number - 1].strip("\n")
            todos.pop(number - 1)

            with open("data/todos.txt", "w") as file:
                file.writelines(todos)
            print(f"Todo: '{todo_to_remove}' has been removed")
        except IndexError:
            print("There is no Todo Item with that Number")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Invalid Command")
print("Bye...")
