import sqlite3


class TodoDatabase(object):
    def __init__(self, todo):
        self.con = sqlite3.connect("Todos.db")
        self.cur = self.con.cursor()
        self.todo = todo

    def createTable(self):
        self.cur.execute("""CREATE TABLE todos
             (id INTEGER PRIMARY KEY,title text, status text, description text,
              enddate real)""")

    def addTodo(self):
        self.c.execute("""INSERT INTO todos VALUES
                       ('2006-01-05','BUY','RHAT',100,35.14)""")

    def listTodos(self):
        self.cur.execute("SELECT title, status, enddate FROM todos")


class Todo(object):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
