def baseballGame(str):
    result = []
    stack = []
    for c in str:
        if c == "C":
            stack.pop()
        elif c == "D":
            x = stack.pop()
            stack.append(x)
            x = x * 2
            stack.append(x)
        elif c == "+":
            b = stack.pop()
            a = stack.pop()
            stack.append(a)
            stack.append(b)
            stack.append(a + b)
        else:
            stack.append(int(c))
    return sum(stack)

str = "52CD+"
print(baseballGame(str))
