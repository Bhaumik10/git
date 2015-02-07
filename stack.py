__author__ = 'Bhaumik'

print "enter the size of stack"
n = int(raw_input())


class stack():
    def __init__(self):
        self.item = []

    def isEmpty(self):
        return self.item == []

    def push(self, item):
        self.item.append(item)

    def pop(self, item):
        self.item.pop()

    def peek1(self):
        return self.item[len(self.item) - 1]

    def size(self):
        return len(self.item)


s = stack()

for i in range(0, n):
    print "enter your", i, "th item"
    k = raw_input()
    j = s.push(k)
    m = s.size()
    print "size of stack is", m
    # s.push(12)
else:
    "Stack has no space any more"

#print "if you want to peek anything please enter that"
#f = int(raw_input())
f = s.peek1()
print "peek item is ",f

for i in range(0, m):
    print "pop up", i, "th item"
    j = s.pop(i)
    m = s.size()
    print "size of stack is", m
else:
    "Stack has no space any more"

