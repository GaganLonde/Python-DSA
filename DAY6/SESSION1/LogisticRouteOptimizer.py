def logisticRouteOptimiser(list):
    if not list:
        print("Routes are not available")
        return
    connections = {}
    shortest = float('inf')
    longest = float('-inf')
    total = 0
    average = 0
    above_avg = 0

    for i in list:
        if i[0] in connections:
            connections[i[0]] += 1
        else:
            connections[i[0]] = 1
        if i[1] in connections:
            connections[i[1]] += 1
        else:
            connections[i[1]] = 1

        shortest = min(shortest, i[2])
        longest = max(longest, i[2])
        total += i[2]
        average = (total / len(list))
    
    for x in list:
        if x[2] > average:
            above_avg += 1
    
    print(f"\Shortest Path: {shortest}\n Longest Path: {longest}\n total: {total}\n Average: {average}\n Above Average: {above_avg}\n Connections = {connections}" )

routes = [(0, 1, 10), (0, 2, 25), (1, 2, 15), (1, 3, 30), (2, 3, 20)]
routes2 = []
logisticRouteOptimiser(routes)