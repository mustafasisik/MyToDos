class deque(object):

    def __init__(self, liste=None):
        self.data = liste if liste  else []

    def append(self, arg):
        self.data.append(arg)

    def appendleft(self, arg):
        self.data.insert(0,arg)

    def clear(self):
        self.data = []

    def count(self, arg):
        return self.data.count(arg)

    def extend(self, argList):
        self.data.extend(argList)

    def extendleft(self, myDeque):
        for i in myDeque:
            self.data.insert(0, i)

    def maxlen(self):
        pass

    def pop(self):
        return self.data.pop()

    def popleft(self):
        return self.data.pop(0)

    def remove(self, index):
        self.data.remove(index)

    def reverse(self):
        self.data.reverse()

    def rotate(self, number):
        l = len(self.data)
        number = number%l
        if number==0:
            return
        part1 = self.data[-number:]
        part2 = self.data[:l-number]
        part1.extend(part2)
        self.data = part1

    def __str__(self):
        st = "deque(%s)" %self.data.__str__()
        return st

    def __eq__(self, myDeque):
        if self.__class__.__name__ != myDeque.__class__.__name__:
            return False
        for n, i in enumerate(self.data):
            if i != myDeque.__getitem__(n):
                return False
        return True
    def __copy__(self):
        return deque([i for i in self.data])

if __name__== "__main__":
    from collections import deque as odeque
    deq = deque()
    doq = odeque()

    assert deq.__str__() == "deque([])", "__str__ function error"

    assert deq == doq , "reverse method not working"

    deq.append(3)
    deq.append(2)
    deq.appendleft(4)

    doq.append(3)
    doq.append(2)
    doq.appendleft(4)



    assert deq == doq, "deque append error"

    deq.reverse()
    doq.reverse()

    assert deq == doq, "rotate function error"

    deq.rotate(1)
    doq.rotate(1)

    assert deq == doq, "rotate function error"

    deq.rotate(2)
    doq.rotate(2)

    assert deq == doq, "rotate function error"

    deq.rotate(3)
    doq.rotate(3)

    assert deq == doq, "rotate function error"

    deq.rotate(4)
    doq.rotate(4)

    assert deq == doq, "rotate function error"

    deq.rotate(-1)
    doq.rotate(-1)

    assert deq == doq, "rotate function error"

    deq.remove(2)
    doq.remove(2)

    assert deq == doq, "remove function error"

    assert deq.pop() == doq.pop(), "pop() function error"

    deq.append(5)
    doq.append(5)
    assert deq.append(6) == doq.append(6), "append error"

    assert deq == doq, "append function error"


    assert deq.popleft() == doq.popleft(), "popleft function error"

    assert deq.count(0) == doq.count(0), "count function error"

    assert deq.count(5) == doq.count(5), "count function error"

    print deq, doq

    from copy import copy
    t = copy(deq)
    print "t %s" % t
    deq.extendleft(doq)
    print "t %s" % t
    doq.extendleft(t.data)

    print deq, doq
