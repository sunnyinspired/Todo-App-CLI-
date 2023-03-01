def get_todos(filepath="data/todos.txt"):
    """ This function gets the todos from a text file """
    with open(filepath, 'r') as fl:
        td = fl.readlines()
        return td


def write_todos(td, filepath="data/todos.txt"):
    """ This function writes a new todo item to the text file """
    with open(filepath, 'w') as fl:
        fl.writelines(td)


while True:
    user_action = input("Type Add, Show, Edit, Remove or Exit : ")
    user_action = user_action.strip()
    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos()
        todos.append(todo + "\n")
        write_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos()
        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1}-{item.strip()}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1
            new_todo = input("Enter the New Todo: ")
            todos = get_todos()
            todos[number] = new_todo + "\n"

            # updates the new todo
            write_todos(todos)
        except ValueError:
            print("Invalid Command")
            continue
        except IndexError:
            print("There is no Todo Item with that Number")
            continue

    elif user_action.startswith("remove"):
        try:
            # get the number of index to remove
            number = int(input("Number of ToDo to Remove: "))
            todos = get_todos()
            todo_to_remove = todos[number - 1].strip("\n")
            # remove the todo
            todos.pop(number - 1)
            # update the list after removal
            write_todos(todos)
            print(f"Todo: '{todo_to_remove}' has been removed")
        except IndexError:
            print("There is no Todo Item with that Number")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Invalid Command")
print("Bye...")
