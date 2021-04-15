
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
        self.Size = len(A)
        self.order = total_order
        self.__BuildHeap__()

    def __str__(self):
        return str(A)

    def IsValidNode(self, index):
        return index < self.Size

    

    def __BuildHeap__(self):
        pass

    def Heapify(self):
        pass

    def RemoveMin(self):
        pass

    def ExtractMin(self):
