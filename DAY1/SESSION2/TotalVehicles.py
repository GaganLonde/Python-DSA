import math
def totalVehicles(v, w):
    half_vehicles = v / 2
    i = 0
    while(True):
        if(((half_vehicles + i)*2) + ((half_vehicles - i)*4)== w):
            print("2 Wheelers: ", half_vehicles + i, " 4 wheelers: ", half_vehicles-i)
            break
        i += 1

totalVehicles(200, 540)
