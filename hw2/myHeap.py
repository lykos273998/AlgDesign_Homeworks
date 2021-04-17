from copy import deepcopy
class Heap():
    """
    Array based implementation of a Heap datastructure,
    The constructor takes as input an array of objects and a total 
    order between them

    *!* This code is a study project *!* 
    I have done the best I could but if some one finds that code randomly
    please take into account that the probability of it having errors is 
    very very high
    """
    def __init__(self,data,total_order):
        """
        Heap constructor, take an array of objects and constructs a heap with 
        data contained in data vector
        """
        self.A = data
        self.Size = len(self.A)
        self.order = total_order
        self.__BuildHeap__()

    def __str__(self):
        return str(self.A[:self.Size])

    def IsValidNode(self, node):
        return node < self.Size

    def Children(self, node):
        L = 2 * node + 1 if self.IsValidNode(2 * node + 1) else None
        R = 2 * node + 2 if self.IsValidNode(2 * node + 2) else None

        return L, R

    def swap(self,i,j):
        self.A[i], self.A[j] = self.A[j], self.A[i]

    def Heapify(self, node):
        M = node
        Lch, Rch = self.Children(node)

        for j in [Lch , Rch]:
            if j != None and self.order(self.A[j],self.A[M]):
                M = j

        if node != M:
            self.swap(node,M)
            self.Heapify(M)
    
    def InsertVal(self,val):
        pass 

    def __BuildHeap__(self):
        for i in  range(self.Size-1, -1, -1):
            #print(i)
            self.Heapify(i)  

    def RemoveMin(self):
        pass

    def ExtractMin(self):
        self.A[0], self.A[-1] = self.A[-1], self.A[0]
        minimum = self.A[-1]
        self.Size -= 1
        self.A = [self.A[i] for i in range(self.Size)]
        self.Heapify(0)
        return minimum

    def fancyPrint(self):
        """
        Higly experimental, 
        do not use it
        """

        from numpy import log2
        lvl_max = int(log2(self.Size))+ 1
        h = '*!* work in progress\n'
        h += str(self.A[0]) + '\n'
        i = 1
        lvl = 1
        while i < self.Size:
            for i in range(i, min(i*2 + 1, self.Size - 1)):
                h += (str(self.A[i]) + '    '*(lvl_max - lvl))
            h += ('\n')
            lvl += 1
            i = 2**lvl - 1
        print(h)
    def swap(self,i,j):
        self.A[i], self.A[j] = self.A[j], self.A[i]

    def DropLast(self):
        self.Size -= 1
        self.A = self.A[:self.Size]

def HeapSort(A,total_order):
    H = Heap(A,total_order)
    SortedArray = [0 for i in range(len(A))]
    for i in range(len(A)):
        SortedArray[i] = H.ExtractMin()
    return SortedArray

if __name__ == "main":
    import numpy as np 
    from myHeap import Heap

    def total_order(a,b):
        return a >= b

    a = int(np.random.rand(10)*100)

    hh = Heap(a, total_order)
    print(2)
