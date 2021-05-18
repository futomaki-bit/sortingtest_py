from geeksforgeeks.timsort import *
from geeksforgeeks.quicksort import *
from geeksforgeeks.mergesort import *
from geeksforgeeks.heapsort import *
import time
import random

# Edit array here
array = random.sample(range(0, 10000), 10000)
# quicksort breaks with this
# ["Quicksort", quicksort(array)]

funcList = [
    ["sorted()", sorted(array)],
    ["Heapsort", heapSort(array)],
    ["Mergesort", mergeSort(array)],
    ["Timsort", timSort(array)],
]

for f in funcList:
    temparray = array.copy()
    start_time = time.time()
    time.sleep(1)
    f[1]
    print(f[0], (time.time() - start_time - 1))
