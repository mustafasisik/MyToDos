from sys import argv
#coding: utf-8
usage = """Usage:
        1) In order to add todo first type -a and than type -command
        such as -t, -s etc after the command type your text as string
        (-t "I should go") these commands are:
        -t, -d, -s, -dd, -p and you can create your commands.

        2) If you want to list all todo type -l and for detailed type -ld
        3) you can remove a todo by typing -r index (-r 3)
        4) -u 4 -s "Done" updates 4. todo's status
        """


def addToDo():
    fileObject = open("todos.txt", "a")
    for i in argv[2:]:
        fileObject.write("%s " % i)
    fileObject.write("\n")
    fileObject.close()
    print "New Todo Added"


def readToDoFile():
    todoList = []
    fileObject = open("todos.txt", "r")
    for line in fileObject:
        line = line.lstrip("-").rstrip("\n")
        elements = line.split("-")
        todo = {}
        for e in elements:
            spaceIndex = e.index(" ")
            command = e[:spaceIndex]
            content = e[spaceIndex+1:-1]
            todo[command] = content
        todoList.append(todo)
    return todoList


def listToDos(todoList):
    for todo in todoList:
        print todoList.index(todo), todo["t"]


def detailedList(todoList):
    for todo in todoList:
        print todoList.index(todo), "%s - %s" % (todo["t"], todo["p"])
        print "     %s" % todo["d"]


def remove(index):
    fileObject = open("todos.txt", "r")
    lines = fileObject.readlines()
    fileObject.close()
    fileObject = open("todos.txt", "w")
    lines.remove(lines[index])
    for line in lines:
        fileObject.write(line)
    fileObject.close()
    print "todo %d removed" % index


def update(index, command, content):
    fileObject = open("todos.txt", "r")
    lines = fileObject.readlines()
    fileObject.close()
    line = lines[index]

    startIndex = line.index(command)
    endIndex = startIndex + line[startIndex + 1:].find("-")

    lineStartPart = line[:startIndex]
    lineUpdatedPart = "%s %s " % (command, content)
    lineEndPart = line[endIndex:]
    newLine = "%s%s%s" % (lineStartPart, lineUpdatedPart, lineEndPart)
    lines[index] = newLine

    fileObject = open("todos.txt", "w")
    for line in lines:
        fileObject.write(line)
    print "todo %s's %s is updated" % (index, command)


def work():
    if argv[1] == "-a":
        addToDo()
    elif argv[1] == "-l":
        listToDos(readToDoFile())
    elif argv[1] == "-ld":
        detailedList(readToDoFile())
    elif argv[1] == "-r":
        remove(int(argv[2]))
    elif argv[1] == "-u":
        update(int(argv[2]), argv[3], argv[4])
    else:
        print usage

work()
