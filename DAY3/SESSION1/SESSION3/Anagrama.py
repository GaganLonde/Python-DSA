def anagrams(strlist):
    d = {}
    for i in strlist:
        for j in i:
            if j in d:
                d[j] += 1
            else:
                d[j] = 1
    result = []
anagrams(["tea", "ate", "bat", "tab"])
        