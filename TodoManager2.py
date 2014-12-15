# -*- coding: cp1254 -*-
from __future__ import print_function
import sqlite3
import argparse
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
    def __init__(self, parse_args):
        self.parse_args = parse_args
        self.con = sqlite3.connect("Todos.db")
        self.cur = self.con.cursor()
        self.modified = False

    def createTable(self):
        self.cur.execute("""CREATE TABLE todos
             (id INTEGER PRIMARY KEY,title text, status text, description text,
              priority text, enddate real)""")

    def add(self):
        self.cur.execute("""INSERT INTO todos (title, status, description,
                         priority, enddate) VALUES(?,?,?,?,?)""",
                        (getattr(self.parse_args, "title", "title"),
                         getattr(self.parse_args, "status", "status"),
                         getattr(self.parse_args, "description", "descr:"),
                         getattr(self.parse_args, "priority", "priority"),
                         getattr(self.parse_args, "enddate", "enddate")))
        self.con.commit()

    @is_modified  # decorator
    def remove(self, index):
        self.cur.execute("DELETE FROM todos WHERE id=?", [index])
        self.con.commit()

    @is_modified  # decorator
    def update(self, index):
        for key, value in self.parse_args:
            sql = "UPDATE todos SET %s=? WHERE id=?" % key
            self.cur.execute(sql, [value, index])

    def list(self):
        self.cur.execute("SELECT * FROM todos")
        for i in self.cur.fetchall():
            for j in i:
                print(j)

    def detailedList(self):
        self.cur.execute("SELECT * FROM todos")
        for i in self.cur.fetchall():
            for j in i:
                print(j)


#  todo class
class Todo(object):
    def __init__(self):
        self.title = "sampe title"
        self.status = "sample status"
        self.description = "sample description"
        self.priority = "sample priority"
        self.enddate = "sample enddate"

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
    manager = TodoManager(args)

    if getattr(args, "title", None):
        manager.add()
    elif getattr(args, "remove", None) or getattr(args, "remove", None) == 0:
        manager.remove(args.remove)
    elif getattr(args, "update", None) or getattr(args, "update", None) == 0:
        manager.update(args.update)
    elif getattr(args, "list", None):
        manager.list()
    elif getattr(args, "detailedlist", None):
        manager.detailedList()
