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
parser.add_argument("--dd", help="duedate of todo", type=str)
parser.add_argument("-l", "--list", help="lists all todos",
                    action="store_true")
parser.add_argument("-ld", help="lists details of all todos",
                    action="store_true")
parser.add_argument("-u", "--update", help="updates a todo by index",
                    action="store_true")
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
    todo["title"] = a.title
    todo["description"] = a.description
    todo["priority"] = a.priority
    todo["status"] = a.status
    todo["duedate"] = a.dd
    todoList.append(todo)
    writeFile(todoList)
    print "new to do added"


def create():
    todoList = []
    todo = {}
    todo["title"] = a.title
    todo["description"] = a.description
    todo["priority"] = a.priority
    todo["status"] = a.status
    todo["duedate"] = a.dd
    todoList.append(todo)
    writeFile(todoList)
    print "new to do added"


def listTodos():
    todoList = readFile()
    for todo in todoList:
        for t in todo["title"]:
            print "%s " % t
        print todo["status"]


def remove(index):
    todoList = readFile()
    todoList.remove(todoList[index])
    writeFile(todoList)
    print "todo removed at index %d" % index

if a.create:
    create()
if a.add:
    addTodo()
elif a.list:
    listTodos()
elif a.remove:
    print a.remove
    remove(a.remove)
