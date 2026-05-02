def McCarthy(n):
    if n > 100:
        return n - 10
    else:
        return McCarthy(McCarthy(n + 11))
    
print(McCarthy(20))

