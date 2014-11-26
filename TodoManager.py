# -*- coding: cp1254 -*-
import os
import argparse
import cPickle as pkl


class TodoManager:
    def __init__(self, fileName):
        self.fileName = fileName

    def writeFile(self, todoList):
        pkl.dump(todoList, open(self.fileName, "wb"))

    def readFile(self):
        return pkl.load(open(self.fileName, "rb"))

    def createTodo(self):
        todo = {}
        d = ["title", "status", "description", "priority", "enddate"]
        for key in d:
            if getattr(a, key):
                todo[key] = getattr(a, key)
        return todo

    def addTodo(self):
        if os.path.exists(self.fileName):
            todoList = self.readFile()
        else:
            todoList = []
        todoList.append(self.createTodo())
        print "new to do added to index %d" % (len(todoList)-1)
        return todoList

    def listTodos(self):
        todoList = self.readFile()
        print "title - status"
        i = 1
        for todo in todoList:
            t = " ".join(todo["title"])
            s = todo["status"]
            print "\n%d- %s - %s " % (i, t, s)
            i += 1

    def detailedList(self):
        todoList = self.readFile()
        print"title - status"
        i = 1
        for todo in todoList:
            t = " ".join(todo["title"])
            s = todo["status"]
            print "\n%d- %s - %s " % (i, t, s)
            print "    : %s" % " ".join(todo["description"])
            i += 1

    def remove(self, index):
        todoList = self.readFile()
        if len(todoList) > index:
            todoList.pop(index)
            print "todo removed at index %d" % index
        else:
            print "There is no todo has index %d\n" \
                  "Index number should be"\
                  "between(0, %d)" % (index, (len(todoList)-1))
        return todoList

    def update(self, index):
        todoList = self.readFile()
        d = ["title", "status", "description", "priority", "enddate"]
        for key in d:
            if getattr(a, key):
                todoList[index][key] = getattr(a, key)
        print "todo at index %s is updated" % index
        return todoList

if __name__ == "__main__":
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
    parser.add_argument("-ld", "--detailedlist",
                        help="lists details of all todos",
                        action="store_true")
    parser.add_argument("-u", "--update", help="updates a todo by index",
                        type=int)
    parser.add_argument("-r", "--remove", dest="remove",
                        help="remove a todo by index", type=int)
    parser.add_argument("-c", "--create", help="creates a new todo program",
                        action="store_true")
    subparsers = parser.add_subparsers(title="subcommands",
                                       description="valid subcommands",
                                       help="additional help")
    subparsers.add_parser("addTodo")
    subparsers.add_parser("listTodos")
    subparsers.add_parser("listDetailed")
    subparsers.add_parser("update")

    a = parser.parse_args()

    todomanager = TodoManager("deneme.txt")

    modified = False
    if a.add:
        td = todomanager.addTodo()
        modified = True
    elif a.remove is not None:
        td = todomanager.remove(a.remove)
        modified = True
    elif a.update is not None:
        td = todomanager.update(a.update)
        modified = True
    elif a.list:
        todomanager.listTodos()
    elif a.detailedlist:
        todomanager.detailedList()

    if modified is True:
        todomanager.writeFile(td)

