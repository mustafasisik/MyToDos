import argparse
import cPickle as pkl

parser = argparse.ArgumentParser(prog="MYTODO",
                                 description="Todo Management Ssytem",
                                 epilog="A new look to time management")
parser.add_argument("-a", "--add", help="add new todo",
                    action="store_true")
parser.add_argument("-t", "--title", help="title of todo", type=str,
                    nargs='+')
parser.add_argument("-d", "--description",
                    help="description of todo", type=str, nargs='+')
parser.add_argument("-p", "--priority", help="priority of todo", type=str)
parser.add_argument("-s", "--status", help="status of todo", type=str)
parser.add_argument("-e", "--enddate", help="enddate of todo", type=str)
parser.add_argument("-l", "--list", help="lists all todos",
                    action="store_true")
parser.add_argument("-ld", help="lists details of all todos",
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


def addTodo():
    todoList = readFile()
    todo = {}
    if a.title:
        todo["title"] = a.title
    if a.status:
        todo["status"] = a.status
    if a.description:
        todo["description"] = a.description
    if a.priority:
        todo["priority"] = a.priority
    if a.enddate:
        todo["enddate"] = a.enddate
    todoList.append(todo)
    writeFile(todoList)
    print "new to do added"


def create():
    todoList = []
    todo = {}
    if a.title:
        todo["title"] = a.title
    if a.status:
        todo["status"] = a.status
    if a.description:
        todo["description"] = a.description
    if a.priority:
        todo["priority"] = a.priority
    if a.enddate:
        todo["enddate"] = a.enddate
    todoList.append(todo)
    writeFile(todoList)
    print "new todo program created"


def listTodos():
    todoList = readFile()
    print "title - status"
    for todo in todoList:
        print "%s - %s " % (" ".join(todo["title"]), todo["status"])


def remove(index):
    todoList = readFile()
    try:
        todoList.remove(todoList[index])
    except ValueError:
        print "there is no such todo has index %s" % index
    writeFile(todoList)
    print "todo removed at index %d" % index


def update(index):
    todoList = readFile()
    if a.title:
        todoList[index]["title"] = a.title
    if a.status:
        todoList[index]["status"] = a.status
    if a.description:
        todoList[index]["description"] = a.description
    if a.priority:
        todoList[index]["priority"] = a.priority
    if a.enddate:
        todoList[index]["enddate"] = a.enddate
    writeFile(todoList)
    print "todo at index %s is updated" % index

if a.create:
    create()
elif a.add:
    addTodo()
elif a.list:
    listTodos()
elif type(a.remove) == int:
    remove(a.remove)
elif type(a.update) == int:
    update(a.update)


print a.remove
