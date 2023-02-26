while True:
    user_action = input("Type A, S, E, D or X to D Add, Show, Edit, Remove or Exit ToDo: ").strip().upper()
    match user_action:
        case 'A':
            todo = input("Enter Todo: ") + '\n'

            file = open("data/todos.txt", 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open("data/todos.txt", 'w')
            file.writelines(todos)
            file.close()
        case 'S':
            file = open("data/todos.txt", 'r')
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
                print(f"{index + 1}-{item}")
        case 'E':
            number = int(input("Number of the ToDo to Edit: "))
            number = number - 1
            new_todo = input("Enter the New Todo: ")
            todos[number] = new_todo

        case 'D':
            number = int(input("Number of ToDo to Remove: "))
            todos.pop(number - 1)
        case 'X':
            break
print("Bye...")