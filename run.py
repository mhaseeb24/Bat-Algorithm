import random
import sys 

from Bat_Algorithm_tsp import *
n = int(input("Enter your number of bats: "))
t = int(input("Enter your number of iterations "))
MX = 100000
xbest = [1,2,3,4]
cities = [1, 2, 3, 4]
graph = [[0, 10, 15, 20], [10, 0, 35, 25],
        [15, 35, 0, 30], [20, 25, 30, 0]]
sol = []
R = []
A = []
for i in range(0,n):
    sol.append(random.shuffle(cities))
    R.append(round(random.uniform(0.4, 0.5), 2))
    A.append(round(random.uniform(0.4, 0.5), 2))
for i in range(t):
    c = []
    for i in range(n):
        bat_obj = BatAlgorithm_tsp(n , t , R[i], A[i], cities, graph)
        temp = bat_obj.solve()
        c[i] = temp[0]
        sol[i] = temp[1]
    cbest = 100000
    xcbest = []
    tr=-1
    r = round(random.uniform(0.0, 1.0), 2)
    for i in range (n):
        if(r > R[i]):
            if(c<cbest):
                cbest = c[i]
                xcbest = sol[i] 
                tr=i
    #TT = calculate_cost(xcbest,graph)
    if(cbest<MX):
        MX = cbest
        xbest = xcbest
        R[tr] = min(1,R[tr]+0.15)
        A[tr] = max(0,A[tr]-0.15)
print("The best sequence is ",xbest)
print ("Its cost is ",MX)