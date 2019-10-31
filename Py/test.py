from queue import PriorityQueue as PQ
import heapq

# print(heapq.nlargest(4, [3,2,3,1,2,4,5,5,6]))

x = [1]
x = heapq.heapify(x)
print(x)
