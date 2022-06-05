import random
from Bat_Algorithm_tsp import *
n = input("Enter your number of bats: ")
t = input("Enter your number of iterations ")
MX = sys.maxint
xbest = [1,2,3,4]
cities = [1, 2, 3, 4]
graph = [[0, 10, 15, 20], [10, 0, 35, 25],
        [15, 35, 0, 30], [20, 25, 30, 0]]
sol = []
R = []
A = []
for i in range(n):
    sol[i] = random.shuffle(cities)
    R[i] = round(random.uniform(0.4, 0.5), 2)
    A[i] = round(random.uniform(0.4, 0.5), 2)
for i in range(t):
    c = []
    for i in range(n):
        bat_obj = BatAlgorithm_tsp(n , t , R[i], A[i], cities, graph)
        temp = bat_obj.solve()
        c[i] = temp[0]
        sol[i] = temp[1]
    cbest = sys.maxint
    xcbest = []
    r = round(random.uniform(0.0, 1.0), 2)
    for i in range (n):
        if(r > R[i]):
            if(c<cbest):
                cbest = c[i]
                xcbest = sol[i] 
    TT = calculate_cost(xcbest,graph)
    if(TT<MX):
        MX = TT
        xbest = xcbest
print("The best sequence is ",xbest)
print ("Its cost is ",MX)