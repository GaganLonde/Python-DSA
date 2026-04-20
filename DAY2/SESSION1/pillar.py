pillar = [2, 1, 2, 2, 0, 0]
def canJump(pillars):
    i = 0
    while i < (len(pillar)-1):
        jump = pillar[i]
        i += jump
        if i > ((len(pillar)-1)):
            print(True)
            break
        if (pillar[i] == 0):
            i = -1
            print(False)
            break
canJump(pillars=pillar)