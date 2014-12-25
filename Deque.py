class deque(object):
    def __init__(self):
        self.data = []

    def append(self, arg):
        self.data.append(arg)
    def appendleft(self, arg):
        self.data.insert(0,arg)
    def clear(self):
        for i in self.data:
            self.data.remove(i)
    def count(self, arg):
        return self.data.count(arg)
    def extend(self, argList):
        self.data.extend(argList)
    def extendleft(self, myDeque):
        for i in myDeque.data:
            self.data.insert(0, i)
    def maxlen(self):
        pass
    def pop(self):
        self.data.pop()
    def popleft(self):
        self.data.pop(0)
    def remove(self, index):
        self.data.remove(index)
    def reverse(self, ):
        self.data.reverse()
    def rotate(self, number):
        l = len(data)
        number = number%l
        part1 = self.data[-number:]
        part2 = self.data[:l-number-1]
        part1.extend(part2)
    def elements(self):
        for i in self.data:
            print i
    def __str__(self):
        return self.data.__str__()
