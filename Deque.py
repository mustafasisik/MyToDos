class deque(object):
    def __init__(self):
        self.myList = []

    def append(self, arg):
        self.myList.append(arg)
    def appendleft(self, arg):
        self.myList.insert(0,arg)
    def clear(self):
        for i in self.myList:
            self.myList.remove(i)
    def count(self, arg):
        return self.myList.count(arg)
    def extend(self, argList):
        self.myList.extend(argList)
    def extendleft(self, argList):
        for i in argList:
            self.myList.insert(0, i)
    def maxlen(self):
        pass
    def pop(self):
        self.myList.pop()
    def popleft(self):
        self.myList.pop(0)
    def remove(self, index):
        self.myList.remove(index)
    def reverse(self, ):
        self.myList.reverse()
    def rotate(self, number):
        l = len(myList)
        number = number%l
        part1 = self.myList[-number:]
        part2 = self.myList[:l-number-1]
        part1.extend(part2)
    def elements(self):
        for i in self.myList:
            print i
