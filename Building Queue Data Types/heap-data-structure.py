from heapq import heappush
from heapq import heappop

fruits = []

#Adding Elements
heappush(fruits, "orange")
heappush(fruits, "apple")
heappush(fruits, "banana")

#remove elements
heappop(fruits)

#display the remaining elements
print(fruits)
