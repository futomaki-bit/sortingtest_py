from geeksforgeeks.binaryinsertionsort import *
from geeksforgeeks.bubblesort import *
from geeksforgeeks.heapsort import *
from geeksforgeeks.mergesort import *
from geeksforgeeks.quicksort import *
from geeksforgeeks.timsort import *

import time
import random

# Edit array here
array = random.sample(range(0, 10000), 10000)
# quicksort breaks with this
# ["quicksort",quick_sort(array)]

funcList = [
    ["binaryinsertionsort", binary_insertion_sort],
    ["bubblesort", bubbleSort],
    ["heapsort", heapSort],
    ["mergesort", mergeSort],
    ["timsort", timSort],
]

print("here")
for f in funcList:
    temparray = array.copy()
    start_time = time.time()
    time.sleep(1)
    f[1](array)
    print(f[0], (time.time() - start_time - 1))
