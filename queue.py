__author__ = 'Bhaumik'

print "please enter the size of queue"

n = int(raw_input());


class Queue():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def find(self, item):
        for i in range(0, q.size()):
            d[i] = q.dequeue()
            if d[i] == item:
                return item
            else:
                e.enqueue = d[i]
        else:
            print "function is working"


q = Queue()

print "please enter elements"

for i in range(0,n):
    k = raw_input()
    if k in q.find(k):
        print "already in queue";
    else:
        q.enqueue(k)
        j = q.size()
        print "your value is successfully entered" + " now size of queue is ", j
else:
    p = q.size()


for i in range(0,n):

    m= q.dequeue()
    j = q.size()
    print 'your are poping up elements now',m," now size of queue is ", j
else:
    p = q.size()
