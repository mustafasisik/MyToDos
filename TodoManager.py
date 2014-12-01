# -*- coding: cp1254 -*-
from __future__ import print_function
import os
import argparse
import cPickle as pkl
from functools import wraps


""" bu fonksiyon çağrıldığında bir fonksiyon alır ve onun
yerine inner function döner. parametre olarak aldığı fonksiyon
eğer çağrılırsa bunun yerine inner function çalışır"""


def is_modified(f):
    @wraps(f)
    def innerFunction(instance, *args):
        instance.modified = True
        return f(instance, *args)
    return innerFunction


# todomanager class and functions
class TodoManager(object):
    def __init__(self, fileName, parse_args):
        self.parse_args = parse_args
        self.modified = False
        self.fileName = fileName
        self.todoList = []
        if os.path.exists(self.fileName):
            self.todoList = pkl.load(open(self.fileName, "rb"))

    def writeFile(self, todoList):
        pkl.dump(todoList, open(self.fileName, "wb"))

    def create(self):
        todo = {}
        d = ["title", "status", "description", "priority", "enddate"]
        for key in d:
            if hasattr(self.parse_args, key):
                todo[key] = getattr(self.parse_args, key)
        return todo

    @is_modified  # decorator
    def add(self):
        self.todoList.append(self.create())
        print ("new to do added to index %d" % (len(self.todoList)-1))
        return self.todoList

    def list(self):
        print ("no - title - status")
        for i, todo in enumerate(self.todoList):
            t = todo["title"]
            s = todo["status"]
            print ("\n%d - %s - %s " % ((i+1), t, s))

    def detailedList(self):
        print ("no - title - status - enddate")
        for i, todo in enumerate(self.todoList):
            t = todo["title"]
            s = todo["status"]
            d = todo["description"]
            e = todo["enddate"]
            print("\n%d - %s - %s - %s" % ((i+1), t, s, e))
            print("Desc: %s " % d)
            print("priority: %s" % todo["priority"])

    @is_modified  # decorator
    def remove(self, index):
        assert 0 < index <= len(self.todoList),\
            print("There is no todo has index %d\n"
                  "Index number should be"
                  "between(0, %d)" % (index, len(self.todoList)))
        self.todoList.pop(index-1)
        print ("todo removed at index %d" % index)
        return self.todoList

    @is_modified  # decorator
    def update(self, index):
        d = ["title", "status", "description", "priority", "enddate"]
        for key in d:
            if getattr(self.parse_args, key):
                self.todoList[index-1][key] = getattr(self.parse_args, key)
        print ("todo at index %s is updated" % index)
        return self.todoList


#  todo class
class Todo(object):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

#  working area
if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog="MYTODO",
                                     description="Todo Management Ssytem",
                                     epilog="A new look to time management")

    subparsers = parser.add_subparsers(help="additional help")

    parser_addTodo = subparsers.add_parser("add", help="adds new todo")

    parser_addTodo.add_argument("-t", "--title",
                                help="title of todo", type=str)
    parser_addTodo.add_argument("-d", "--description",
                                default="No description",
                                help="description of todo",
                                type=str)
    parser_addTodo.add_argument("-p", "--priority",
                                help="priority of todo",
                                type=str, default="important")
    parser_addTodo.add_argument("-s", "--status", help="status of todo",
                                type=str, default="Not done")
    parser_addTodo.add_argument("-e", "--enddate", help="enddate of todo",
                                type=str, default="Not defined")

    #lists todos
    parser_list = subparsers.add_parser("list", help="help for list todos")
    parser_list.add_argument("list", help="lists all todos",
                             action="store_true")

    #detailed lists todos
    parser_detailedlist = subparsers.add_parser("detailedlist",
                                                help="help for detailedlist")
    parser_detailedlist.add_argument("detailedlist",
                                     help="lists details of all todos",
                                     action="store_true")

    #updating todo by argument
    parser_update = subparsers.add_parser("update",
                                          help="help for update todo")
    parser_update.add_argument("update",
                               help="updates a todo by index", type=int)
    parser_update.add_argument("-t", "--title", help="title of todo",
                               type=str)
    parser_update.add_argument("-d", "--description",
                               help="description of todo",
                               type=str)
    parser_update.add_argument("-p", "--priority",
                               help="priority of todo",
                               type=str)
    parser_update.add_argument("-s", "--status", help="status of todo",
                               type=str)
    parser_update.add_argument("-e", "--enddate", help="enddate of todo",
                               type=str)

    #removing todo by index
    parser_remove = subparsers.add_parser("remove",
                                          help="help for remove todo")
    parser_remove.add_argument("remove", help="remove a todo by index",
                               type=int)

    args = parser.parse_args()

    todomanager = TodoManager("todos.p", args)

    if getattr(args, "title", None):
        td = todomanager.add()
    elif getattr(args, "remove", None) or getattr(args, "remove", None) == 0:
        td = todomanager.remove(args.remove)
    elif getattr(args, "update", None) or getattr(args, "update", None) == 0:
        td = todomanager.update(args.update)
    elif getattr(args, "list", None):
        todomanager.list()
    elif getattr(args, "detailedlist", None):
        todomanager.detailedList()

    if todomanager.modified:
        todomanager.writeFile(td)
