from HeapInt import *

'''*
 * Robert "Bobby" Cowen
 * CSCI311 - 10AM
 * HW2
 *
 * An implementation of a minimum heap with handles
 '''

class Heap:

    def __init__(self):
        '''
          The constructor has been set up with an initial array of size 4
          so that your doubleHeap() method will be tested.  Don't change
          this!
        '''
        self.array = [0]*4
        self.heapsize = 0
        self.arraysize = 4
 

    def exchange(self, pos1, pos2):
        '''
          Exchanges that values at positions pos1 and pos2 in the heap array.
          Handles must be exchanged correctly as well.

          Running time = O(1)
        '''
        
        temp = self.array[pos1]                 #O(1)
        self.array[pos1] = self.array[pos2]     #O(1)
        self.array[pos2] = temp                 #O(1)
        
        self.array[pos1].setHandle(pos1)        #O(1)
        self.array[pos2].setHandle(pos2)        #O(1)
   

    def doubleHeap(self):
        '''
          Doubles the size of the array.  A new array is created, the elements in
          the heap are copied to the new array, and the array data member is set
          to the new array.  Data member arraysize is set to the size of the
          new array.

          Running time = O(n)
        '''
        
        newArray = [0] * (self.arraysize * 2)   #O(1)
        
        for i in range(0, self.arraysize):      #O(n)
            newArray[i] = self.array[i]             #O(1)
            
        self.arraysize = self.arraysize * 2     #O(1)
        self.array = newArray                   #O(1)


    def heapifyDown(self, pos):
        '''
          Fixes the heap if the value at position pos may be bigger than one of
          its children.  Using exchange() to swap elements will simplify your
          implementation.  HeapElts contain records, and records contain
          keys; you will need to decide how to handle comparisons.

          Running time = O(lgn)
        '''
        
        l = self.left(pos)              #O(1)
        r = self.right(pos)             #O(1)

        if l <= self.heapsize and self.array[l].getKey() < self.array[pos].getKey():    #O(1)
            smallest = l                                                                #O(1)
        else:
            smallest = pos                                                              #O(1)

        if r <= self.heapsize and self.array[r].getKey() < self.array[smallest].getKey(): #O(1)
            smallest = r                                                                  #O(1)

        if smallest != pos:                                                             #O(1)
            self.exchange(pos, smallest)                                                #O(1)
            self.heapifyDown(smallest)                                                  #O(lgn)



    def heapifyUp(self, pos):
        """
          Fixes the heap if the value at position pos may be smaller than its
          parent.  Using exchange() to swap elements will simplify your
          implementation.  HeapElts contain records, and records contain
          keys; you will need to decide how to handle comparisons.

          Running time = O(lgn)
        """

        while pos > 1 and self.array[self.parent(pos)].getKey() > self.array[pos].getKey(): #O(lgn)
            self.exchange(pos, self.parent(pos))        #O(1)
            pos = self.parent(pos)                      #O(1)
    


    def insert(self, inElt):
        '''
          Insert inElt into the heap.  Before doing so, make sure that there is
          an open spot in the array for doing so.  If you need more space, call
          doubleHeap() before doing the insertion.

          Running time = O(lgn) if the heap doesn't need to be increased
                         O(n + lgn) if the heap needs to increase in size
        '''

        if (self.heapsize + 1) >= self.arraysize:       #O(1)
            self.doubleHeap()                               #O(n)
            
        self.heapsize = self.heapsize + 1               #O(1)
        
        self.array[self.heapsize] = inElt               #O(1)
        inElt.setHandle(self.heapsize)                  #O(1)
        
        self.heapifyUp(self.heapsize)                   #O(lgn)
        
        


    def removeMin(self):
        '''
          Remove the minimum element from the heap and return it.  Restore
          the heap to heap order.  Assumes heap is not empty, and will
          cause an exception if the heap is empty.

          Running time = O(lgn)
        '''

        self.exchange(self.heapsize, 1)         #O(1)

        self.heapsize = self.heapsize - 1       #O(1)
        self.heapifyDown(1)                     #O(lgn)

        return self.array[self.heapsize + 1]    #O(1)


    def getHeapsize(self):
        '''
          Return the number of elements in the heap..

          Running time = O(1)
        '''

        return self.heapsize        #O(1)


    def printHeap(self):
        '''
          Print out the heap for debugging purposes.  It is recommended to 
          print both the key from the record and the handle.

          Running time = O(n)
        '''

        for i in self.array:        #O(n)
            if i != 0:                  #O(1)
                print(i)                #O(1)


    def parent(self, heapElt):
        '''
          Return the parent of the given location

          Running time = O(1)
        '''
        
        if heapElt == 0:            #O(1)
            return -1                   #O(1)
        else:                       
            return (heapElt // 2)        #O(1)


    def left(self, heapElt):
        '''
          Return the left child of the given location

          Running time = O(1)
        '''

        return (2 * heapElt)        #O(1)


    def right(self, heapElt):
        '''
          Return the right child of the given location

          Running time = O(1)
        '''
     
        return ((2 * heapElt) + 1)  #O(1)
