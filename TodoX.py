import os
import argparse
import cPickle as pkl

parser = argparse.ArgumentParser(prog="MYTODO",
                                 description="Todo Management Ssytem",
                                 epilog="A new look to time management")
parser.add_argument("-a", "--add", help="add new todo",
                    action="store_true")
parser.add_argument("-t", "--title", help="title of todo", type=str,
                    nargs='+')
parser.add_argument("-d", "--description", default=["No", "description"],
                    help="description of todo", type=str, nargs='+')
parser.add_argument("-p", "--priority", help="priority of todo",
                    type=str, default="important")
parser.add_argument("-s", "--status", help="status of todo",
                    type=str, default="Not done")
parser.add_argument("-e", "--enddate", help="enddate of todo", type=str)
parser.add_argument("-l", "--list", help="lists all todos",
                    action="store_true")
parser.add_argument("-ld", "--detailedlist", help="lists details of all todos",
                    action="store_true")
parser.add_argument("-u", "--update", help="updates a todo by index",
                    type=int)
parser.add_argument("-r", "--remove", dest="remove",
                    help="remove a todo by index", type=int)
parser.add_argument("-c", "--create", help="creates a new todo program",
                    action="store_true")

a = parser.parse_args()


def writeFile(todoList):
    pkl.dump(todoList, open("todos.p", "wb"))


def readFile():
    return pkl.load(open("todos.p", "rb"))


def createTodo():
    todo = {}
    d = ["title", "status", "description", "priority", "enddate"]
    for key in d:
        if getattr(a, key):
            todo[key] = getattr(a, key)
    return todo


def addTodo():
    if os.path.exists("todos.p"):
        todoList = readFile()
    else:
        todoList = []
    todoList.append(createTodo())
    print "new to do added to index %d" % (len(todoList)-1)
    return todoList


def addSubTodo(index):
    subTodo = createTodo()
    subTodo["parentTodo"] = index
    todoList = readFile()
    todoList.append(subTodo)
    print "subtodo added to index %d" % index


def listTodos():
    todoList = readFile()
    print "title - status"
    i = 1
    for todo in todoList:
        print "\n%d- %s - %s " % (i, " ".join(todo["title"]), todo["status"])
        i += 1


def detailedList():
    todoList = readFile()
    print"title - status"
    i = 1
    for todo in todoList:
        print "\n%d- %s - %s " % (i, " ".join(todo["title"]), todo["status"])
        print "    : %s" % " ".join(todo["description"])
        i += 1


def remove(index):
    todoList = readFile()
    if len(todoList) > index:
        todoList.pop(index)
        print "todo removed at index %d" % index
    else:
        print "There is no todo has index %d\n" \
        "Index number should be between(0, %d)" % (index, (len(todoList)-1))
    return todoList


def update(index):
    todoList = readFile()
    d = ["title", "status", "description", "priority", "enddate"]
    for key in d:
        if getattr(a, key):
            todoList[index][key] = getattr(a, key)
    print "todo at index %s is updated" % index
    return todoList


if __name__ == "__main__":
    if a.add:
        td = addTodo()
        writeFile(td)
    elif a.remove is not None:
        td = remove(a.remove)
        writeFile(td)
    elif a.update is not None:
        td = update(a.update)
        writeFile(td)
    if a.list:
        listTodos()
    elif a.detailedlist:
        detailedList()

