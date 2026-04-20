def stringManipulation(s):
    result = "".join(reversed(s[0:len(s)//2])) + "".join(reversed(s[len(s)//2:len(s)]))
    print(result)

# stringManipulation("gagan londe")
stringManipulation("gagan l")