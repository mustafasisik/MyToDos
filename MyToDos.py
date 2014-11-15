#I started to write it now.. 15.11.2014 --- 04:36
#coding: utf-8
ToDoList = []
todo = {}

fileObject = open("Todos.txt", "a")


def createTodo():
    todo = raw_input("Write your todo:")
    precedence = raw_input("write precedence: ")
    subtodo = raw_input("Add a subtodo: ")
    todo = {"todo": todo, "precedence": precedence, "subtodo": subtodo}
    return todo

if __name__ == "__main__":
    command = ""
    while command != "save":
        command = raw_input("add/delete or save: ")
        if command == "add":
            todo = createTodo()
            ToDoList.append(todo)
            print "new todo added"
            print todo
        elif command == "delete":
            print "delete :)"
    for todo in ToDoList:
        print todo["todo"]
    print "saved all changes"
