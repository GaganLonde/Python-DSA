import heapq
import math
def kClosest(points, k):
    points.sort(key=lambda x: math.sqrt(x[0] ** 2 + x[1] ** 2))
    return points[:k]

def kColsestOptimised(points, k):
    def dist(x, y):
        return math.sqrt(x ** 2 + y ** 2)
    
    heap = []
    for x, y in points:
        d = dist(x, y)

        if len(heap) < k:
            heapq.heappush(heap, (-d, x, y))
        else:
            heapq.heappushpop(heap, (-d, x, y))

    return [(x, y) for d, x, y in heap]

points = [[3, 3], [5, -1], [-2, 4]]
print(kColsestOptimised(points, 2))