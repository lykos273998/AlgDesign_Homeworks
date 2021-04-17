import numpy as np 
from myHeap import Heap

def total_order(a,b):
    return a >= b

a = np.ceil(np.random.rand(10)*100)
print(a)
hh = Heap(a, total_order)
hh.fancyPrint()