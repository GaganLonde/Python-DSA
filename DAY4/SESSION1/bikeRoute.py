
def bikeRoute(arr):
    i, j = 0, 0
    route = []

    if arr[0][0] == 0:
        return False
    while i < len(arr) and j < len(arr[0]) - 1:
        if arr[i][j + 1]:
            route.append("R")
            j += 1
        elif arr[i + 1][j]:
            route.append("D")
            i += 1
    
    return route

arr = [[1, 1, 0, 0],
       [0, 1, 0, 1],
       [1, 1, 1, 0],
       [0, 0, 1, 1]]

arr2 = [[0, 1, 0, 0],
       [0, 1, 0, 1],
       [1, 1, 1, 0],
       [0, 0, 1, 1]]

print(bikeRoute(arr))
        

# class BikeAndThePath:
#     N = 4

#     def findPath(self, maze, row, col, sol):
#         if row == self.N-1 and col == self.N - 1:
#             print(sol)
#             return True
#         if maze[row][col] == 0 and row <= self.N and col <= self.N:
#             return False
        
#         maze[row][col] = 0

#         if self.findPath(maze, row+1, col, sol + "D"):
#             return True
#         if self.findPath(maze, row, col + 1, sol + "R"):
#             return True
        
#         maze[row][col] == 1
#         return False
    


# maze = [[1, 1, 0, 0],
#         [0, 1, 0, 1],
#         [1, 1, 1, 0],
#         [0, 0, 1, 1]]

# sol = ""

# obj = BikeAndThePath()
# obj.findPath(maze, 0, 0, sol)
