#I started to write it now.. 15.11.2014 --- 04:36
#coding: utf-8
ToDoList = []


def createTodo():
    completed = "Not completed"
    todo = raw_input("Write your todo:")
    precedence = raw_input("write precedence: ")
    todo = {"todo": todo, "precedence": precedence, "Completed": completed}
    return todo


def save(ToDos):
    for todo in ToDos:
        fileObject = open("Todos.txt", "a")
        fileObject.write("%s %s %s\n" %(todo["todo"], todo["precedence"], todo["Completed"]))
        fileObject.close()


if __name__ == "__main__":
    command = ""
    while command != "save":
        command = raw_input("add/delete or save: ")
        if command == "add":
            todo = createTodo()
            ToDoList.append(todo)
            print "new todo added"
            print todo["todo"], todo["precedence"], todo["Completed"]
        elif command == "delete":
            print "delete :)"
    for todo in ToDoList:
        print todo["todo"]
    save(ToDoList)
    print "saved all changes"
