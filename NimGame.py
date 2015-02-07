__author__ = 'Bhaumik'
import random
from array import *

K = random.sample((3,5,7),1); #choose the heap randomly

heap = []

for i in range(0,K[0]):
	heap.append(random.sample((9,11,13),1))		#Insert the data into the heap

heap = [l[0] for l in heap]
print "size of heap is",K[0]," and objects are",heap

def playerTurn():
    print "After Computer Turn,heap with available object is", heap
    print "Human Turn: Please enter Number of object and heaps"

    y = raw_input()	# of objects
    Y = int(y)
    x = raw_input()		# heap number
    X = int(x)
    if((Y > heap[X] | X > len(heap)) | Y == 0 ):
        print "Enter valid value for Heap or object"
        playerTurn()
    else:
        Z = heap[X] - Y
        heap[X] = Z
        print "Now length of heap is ",heap
        if(sum(heap) > 0):
            computerTurn()
        else:
            print "Player is winner"

def computerTurn():
	print "player computer took"
	print heap
        print "length of heap is",len(heap)
	A = random.randrange(0,len(heap),1)
	print "Heap number",A
        if(heap[A] > 0):
            B = random.randrange(1,heap[A],1)
            print "Computer wants to take ",B," objects"
            if (A >len(heap) | B > heap[A] | B == 0 ):
                "Please enter value again"
                computerTurn()
            else:
                newobj = heap[A] - B;
                heap[A] = newobj
                print heap
                if(sum(heap) > 0):
                    playerTurn()
                else:
                    print "Player is winner"
        else:
            "please choose another heap"
            computerTurn()

m = random.sample((1,2),1);		#choose first time computer vs. human

if( m[0] == 1 ):
	playerTurn()
else:
	computerTurn()
