import argparse
import csv

parser = argparse.ArgumentParser(prog="MYTODO",
                                 description="Todo Management Ssytem",
                                 epilog="A new look to time management")
parser.add_argument("-a", "--add", help="add new todo", action="store_true")
parser.add_argument("-t", "--title", help="title of todo", type=str)
parser.add_argument("-d", "--description",
                    help="description of todo", type=str)
parser.add_argument("-p", "--priority", help="priority of todo", type=str)
parser.add_argument("-s", "--status", help="status of todo", type=str)
parser.add_argument("--dd", help="duedate of todo", type=str)
parser.add_argument("-l", help="lists all todos", action="store_true")
parser.add_argument("-ld", help="lists details of all todos",
                    action="store_true")
parser.add_argument("-u", "--update", help="updates a todo by index",
                    action="store_true")
parser.add_argument("-r", help="remove a todo by index", action="store_true")

a = parser.parse_args()


def addTodo():
    todo = {}
    todo["title"] = a.title
    todo["description"] = a.description
    todo["priority"] = a.priority
    todo["status"] = a.status
    todo["duedate"] = a.dd
    return todo


#deneme
if a.add:
    print addTodo()
    w = csv.writer(open("todo.csv", "w"))
    for key, val in addTodo().items():
        w.writerow([key, val])
    print "all done"
