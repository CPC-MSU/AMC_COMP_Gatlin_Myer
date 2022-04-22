from posixpath import split


def getInput():
    file = open("input.txt", "r")
    lines = file.readlines()
    
    now_lines = []
    index = -1 
    for line in lines:
        new_line = list(map(int, line.split(" ")  ))
        if  len(new_line) == 1:
            now_lines.append([])
            index += 1 
            continue
        now_lines[index].append(new_line)
    services = [] 
    



    return now_lines 


def calc():
    for group in getInput():
        print(customcost(group))
    
   
from math import inf

def customcost(services):
    maxes = [] 
    totals = [] 
    for serv in range(0, len(services)):

        serv_tests = [] 

        for test in range(0, len(services)):
            if serv == test:
                continue 
            x = services[test][0] - services[serv][0]
            y  = services[test][1] - services[serv][1]
            z = services[test][2] - services[serv][2]
            
            x = 0 if x < 0 else x 
            y = 0 if y < 0 else y 
            z = 0 if z < 0 else z 
            serv_tests.append([x, y, z]) 
        maxes.append(max(sum(x) for x in serv_tests)) 
    min_val = min(maxes)
    return min_val, maxes.index(min_val) + 1


calc()