while True:
    user_action = input("Type A, S, E, D or X to D Add, Show, Edit, Remove or Exit ToDo: ").strip().upper()
    match user_action:
        case 'A':
            todo = input("Enter Todo: ") + '\n'

            with open("data/todos.txt", 'r') as file:
                todos = file.readlines()
            todos.append(todo)

            with open("data/todos.txt", 'w') as file:
                file.writelines(todos)

        case 'S':
            with open("data/todos.txt", 'r') as file:
                todos = file.readlines()
            for index, item in enumerate(todos):
                item = item.strip("\n")
                print(f"{index + 1}-{item.strip()}")
        case 'E':
            number = int(input("Number of the ToDo to Edit: "))
            number = number - 1
            new_todo = input("Enter the New Todo: ")
            with open("data/todos.txt", 'r') as file:
                todos = file.readlines()
            todos[number] = new_todo + "\n"

            # updates the new todo
            with open("data/todos.txt", "w") as file:
                file.writelines(todos)

        case 'D':
            number = int(input("Number of ToDo to Remove: "))
            with open("data/todos.txt", "r") as file:
                todos = file.readlines()
            todo_to_remove = todos[number - 1].strip("\n")
            todos.pop(number - 1)

            with open("data/todos.txt", "w") as file:
                file.writelines(todos)
            print(f"Todo: '{todo_to_remove}' has been removed")

        case 'X':
            break
print("Bye...")
