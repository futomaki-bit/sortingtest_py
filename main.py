# import functions here
from geeksforgeeks.binaryinsertionsort import *
from geeksforgeeks.bubblesort import *
from geeksforgeeks.heapsort import *
from geeksforgeeks.mergesort import *
from geeksforgeeks.quicksort import *
from geeksforgeeks.timsort import *

# import time for timer, random for generating array to test
import time
import random

array = random.sample(range(0, 10000), 10000)
# quicksort breaks with this
# ["quicksort",quick_sort(array)]

# Edit list here
funcList = [
    ["sorted()", sorted],
    ["binaryinsertionsort", binary_insertion_sort],
    ["bubblesort", bubbleSort],
    ["heapsort", heapSort],
    ["mergesort", mergeSort],
    ["timsort", timSort],
]

# driver to run all the algorithms in the list with the same array
for f in funcList:
    temparray = array.copy()
    start_time = time.time()
    time.sleep(1)
    f[1](array)
    print('{:<20}  {:<}'.format(f[0], (time.time() - start_time - 1)))
