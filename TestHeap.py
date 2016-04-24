from Heap import *

'''
 * A class to test a heap with handles
 '''

def TestHeap():
    array = [0] * 10
    sortedArray = [0] * 10
    hsize = 9
    asize = 10

    myHeap = Heap()

    print("Inserting the values 4, 8, 3, 7, 2, 6, 9, 1, 5 in that order.\n")

    array[1] = HeapInt(4)
    myHeap.insert(array[1])

    array[2] = HeapInt(8)
    myHeap.insert(array[2])

    array[3] = HeapInt(3)
    myHeap.insert(array[3])

    array[4] = HeapInt(7)
    myHeap.insert(array[4])

    array[5] = HeapInt(2)
    myHeap.insert(array[5])

    array[6] = HeapInt(6)
    myHeap.insert(array[6])

    array[7] = HeapInt(9)
    myHeap.insert(array[7])

    array[8] = HeapInt(1)
    myHeap.insert(array[8])

    array[9] = HeapInt(5)
    myHeap.insert(array[9])

    ("value  handle")
    print("-----  ------")

    for i in range(1, hsize+1):
        print("  " + str(array[i].getKey()) + "       " + str(array[i].getHandle()))
	

    print("\n\nPrinting heap with printHeap(): \n")
	
    myHeap.printHeap()
	
    print("\nChanging value at root from 1 to 11 and heapifying down.")
	
    array[8].setKey(11)
	
    myHeap.heapifyDown(array[8].getHandle())
	
    print("\nRevised handle info:\n")
    print("value  handle")
    print("-----  ------")
	
    for i in range(1, hsize+1):
        print("  " + str(array[i].getKey()) + "       " + str(array[i].getHandle()))

    print("\n\nSorting by removing minimum at each step:\n")

    while (myHeap.getHeapsize() > 0):
        print( str(myHeap.removeMin().getKey()) + "  ")

    print("\n")

    



