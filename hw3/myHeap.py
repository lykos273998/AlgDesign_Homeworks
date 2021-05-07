from copy import deepcopy, copy
class Heap():
    """
    Array based implementation of a Heap datastructure,
    The constructor takes as input an array of objects and a total 
    order between them
    *!* This code is a study project *!* 
    """
    def __init__(self,data,total_order):
        """
        Heap constructor, take an array of objects and constructs a heap with 
        data contained in data vector
        """
        self.A = copy(data)
        self.Size = len(self.A)
        self.order = total_order
        self._BuildHeap()

    def __str__(self):
        return str(self.A[:self.Size])

    def _IsValidNode(self, node):
        return node < self.Size

    def Children(self, node):
        L = 2 * node + 1 if self._IsValidNode(2 * node + 1) else None
        R = 2 * node + 2 if self._IsValidNode(2 * node + 2) else None

        return L, R
    
    def parent(self,node):
        return (node - 1)//2

    def _swap(self,i,j):
        #print(i,j)
        self.A[i], self.A[j] = self.A[j], self.A[i]

    def Heapify(self, node):
        M = node
        Lch, Rch = self.Children(node)

        for j in [Lch , Rch]:
            if j != None and self.order(self.A[j],self.A[M]):
                M = j

        if node != M:
            self._swap(node,M)
            self.Heapify(M)


    def _push_up(self,node):
        while(not self.order(self.A[self.parent(node)], self.A[node]) and node != 0):
            #print(node, self.parent(node))
            self._swap(node, self.parent(node))
            node = self.parent(node)

    def Insert(self,val):
        self.A.append(val)
        self.Size += 1
        self._push_up(self.Size - 1)

        

    def _BuildHeap(self):
        for i in  range(self.Size-1, -1, -1):
            #print(i)
            self.Heapify(i)  

    

    def ExtractRoot(self):
        self.A[0], self.A[-1] = self.A[-1], self.A[0]
        minimum = self.A[-1]
        self.Size -= 1
        self.A = [self.A[i] for i in range(self.Size)]
        self.Heapify(0)
        return minimum

    def DropLast(self):
        self.Size -= 1
        self.A = self.A[:self.Size]

    def decrease_key(self, idx, val):
        self.A[idx] = val
        while(not (idx == 0 or self.order(self.A[self.parent(idx)],self.A[idx]))):
            self._swap(idx,self.parent(idx))
            idx = self.parent(idx)
        
class Heap_of_nodes():
    """
    Array based implementation of a Heap datastructure,
    The constructor takes as input an array of objects and a total 
    order between them, implemented for dijjstra algorithm implementation 
    based on heap
    *!* This code is a study project *!* 
    """
    def __init__(self,data,total_order):
        """
        Heap constructor, take an array of objects and constructs a heap with 
        data contained in data vector
        """
        self.A = copy(data)
        self.Size = len(self.A)
        self.order = total_order
        self._BuildHeap()

    def __str__(self):
        return str(self.A[:self.Size])

    def _IsValidNode(self, node):
        return node < self.Size

    def Children(self, node):
        L = 2 * node + 1 if self._IsValidNode(2 * node + 1) else None
        R = 2 * node + 2 if self._IsValidNode(2 * node + 2) else None

        return L, R
    
    def parent(self,node):
        return (node - 1)//2

    def _swap(self,i,j):
        #print(i,j)
        self.A[i], self.A[j] = self.A[j], self.A[i]
        self.A[i].Heap_idx, self.A[j].Heap_idx = self.A[j].Heap_idx, self.A[i].Heap_idx

    def Heapify(self, node):
        M = node
        Lch, Rch = self.Children(node)

        for j in [Lch , Rch]:
            if j != None and self.order(self.A[j],self.A[M]):
                M = j

        if node != M:
            self._swap(node,M)
            self.Heapify(M)


    def _push_up(self,node):
        while(not self.order(self.A[self.parent(node)], self.A[node]) and node != 0):
            #print(node, self.parent(node))
            self._swap(node, self.parent(node))
            node = self.parent(node)

    def Insert(self,val):
        self.A.append(val)
        self.Size += 1
        self._push_up(self.Size - 1)

        

    def _BuildHeap(self):
        for i in  range(self.Size-1, -1, -1):
            #print(i)
            self.Heapify(i)  

    

    def ExtractRoot(self):
        self._swap(0,self.Size - 1)
        minimum = self.A[-1]
        self.Size -= 1
        self.A = [self.A[i] for i in range(self.Size)]
        self.Heapify(0)
        return minimum

    def DropLast(self):
        self.Size -= 1
        self.A = self.A[:self.Size]

    def decrease_key(self, idx, val):
        self.A[idx] = val
        while(not (idx == 0 or self.order(self.A[self.parent(idx)],self.A[idx]))):
            self._swap(idx,self.parent(idx))
            idx = self.parent(idx)


def HeapSort(A,total_order):
    H = Heap(A,total_order)
    SortedArray = [0 for i in range(len(A))]
    for i in range(len(A)):
        SortedArray[i] = H.ExtractRoot()
    return SortedArray

