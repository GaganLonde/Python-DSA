def printPyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        print("*" * (i * 2  - 1))


printPyramid(10)

def mirroredTriangle(n):
    for i in range(1, n + 1):
        print("*" * (i), end="")
        print(" " * (n - i)*2, end="")
        print("*" * (i))
        
#mirroredTriangle(5)

def butterflyPattern(n):
    for i in range(1, n + 1):
        print("*" * (i), end="")
        print(" " * (n - i)*2, end="")
        print("*" * (i))
    for i in range(n - 1, 0, -1):
        print("*" * (i), end="")
        print(" " * (n - i)*2, end="")
        print("*" * (i))

#butterflyPattern(10)

def diamondPattern(n):
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        print("*" * (i * 2  - 1))
    for i in range(n - 1, 0, -1):
        print(" " * (n - i), end="")
        print("*" * (i * 2  - 1))    

#printPyramid(5)
#mirroredTriangle(5)
#butterflyPattern(5)
#diamondPattern(5)
#sandGlass(5)
#pascalTriangle(5)
#hollow rectangle, triangle, diamond