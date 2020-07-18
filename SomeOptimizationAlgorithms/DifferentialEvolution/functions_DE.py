import random as r
import math

signsNum = 5
K = round(r.uniform(0, 2), signsNum)
eps = 0.001


def myFunc1(x):
    return round(2*x*x + 4*x - 2, signsNum)

def myFunc2(x):
    return round(-0.2*x*x*x + 2*x - x*x*math.sin(x), signsNum)

def MatyasFunc(x1, x2):
    return round(0.26*(x1*x1+x2*x2)-0.48*x1*x2, signsNum)

def f(func, x, y = 0):
    if func == 1:
        return myFunc1(x)
    elif func == 2:
        return myFunc2(x)
    else:
        return MatyasFunc(x, y)
    
def generatePop(countInd, a, b, func):
    x = []
    for i in range(countInd):
        Xi = round(r.uniform(a, b), signsNum)
        if func == 1:
            x.append([Xi, myFunc1(Xi)])
        elif func == 2:
            x.append([Xi, myFunc2(Xi)])
        elif func == 3:
            Xi2 = round(r.uniform(a, b), signsNum)
            x.append([Xi, Xi2, MatyasFunc(Xi, Xi2)])
    return x

def V(pop, i):
    r1 = i
    r2 = i
    r3 = i
    while r1==i:
        r1 = r.randint (0, len(pop)-1)
    while r2==i or r2==r1:
        r2 = r.randint(0,len(pop)-1)
    while r3==i or r3==r2 or r3==r1:
        r3 = r.randint(0, len(pop)-1)
    v1 = pop[r1]
    v2 = pop[r2]
    v3 = pop[r3]
    v = []
    for j in range(len(v1)-1):
        v.append(0)
        v[j] = round(v1[j] + K*(v2[j]-v3[j]), signsNum)
    return v

def newVect(pop, func, a, b):
    
    for i in range(len(pop)):
        v = V(pop, i)
        for k in range(len(v)):
            while v[k]<a or v[k]>b:
                v = V(pop, i)
        #print("x =", pop[i])
        if len(v) == 3:
            rand = r.randint(0, 1)
            #print("r =", rand)
            v[rand]=pop[i][rand]
            v.append(f(func, v[0], v[1]))
        else:
            v.append(f(func, v[0]))
        #print("v =", v)
        if v[len(v)-1]<pop[i][len(v)-1]:
            pop[i]=v
    pop.sort(key=funcVal, reverse=False)
    return pop

def showPop(pop):
    for i in range(len(pop)):
        print(pop[i])

def mean(pop):
    s = 0
    ind = len(pop[0])-1
    for i in range (0, len(pop)):
        s+=pop[i][ind]
    s/=len(pop)
    return s

def funcVal(val):
    return val[len(val)-1]

def results(pop, oldPop):
    print(" "*16, "#"*7, "РЕЗУЛЬТАТИ", "#"*7)
    print("Найкращий з попередньої популяції:")
    print(oldPop[0])
    print("Найкращий з даної популяції:")
    print(pop[0])

def stopCond1(pop, oldPop, func, a, b):
    gen = 2
    ind = len(pop[0])-1
    while (abs(min(pop, key=funcVal)[ind] - min(oldPop, key=funcVal)[ind]) > eps):
        gen+=1
        oldPop = pop.copy()
        pop = newVect(pop, func, a, b)
        print(" "*16, "#"*7, "ПОПУЛЯЦІЯ №", gen, "#"*7)
        showPop(pop)
    return pop, oldPop

def stopCond2(pop, oldPop, func, a, b):
    gen = 2
    ind = len(pop[0])-1
    while (abs(mean(pop) - mean(oldPop)) > eps):
        gen+=1
        oldPop = pop.copy()
        pop = newVect(pop, func, a, b)
        print(" "*16, "#"*7, "ПОПУЛЯЦІЯ №", gen, "#"*7)
        showPop(pop)
    return pop, oldPop

def stopCond3(pop, oldPop, func, a, b):
    countGen = 10
    gen = 2
    ind = len(pop[0])-1
    for generation in range(gen, countGen):
        gen+=1
        oldPop = pop.copy()
        pop = newVect(pop, func, a, b)
        print(" "*16, "#"*7, "ПОПУЛЯЦІЯ №", gen, "#"*7)
        showPop(pop)
    return pop, oldPop

def DifferentialEvol(stopCond, func, a, b):
    countInd = 10
    print(" "*16, "#"*7, "ПЕРША ПОПУЛЯЦІЯ", "#"*7)
    x = generatePop(countInd, a, b, func)
    x.sort(key=funcVal, reverse=False)
    oldX = x.copy()
    showPop(x)
    print(" "*16, "#"*7, "ПОПУЛЯЦІЯ № 2", "#"*7)
    x = newVect(x, func, a, b)
    showPop(x)
    if stopCond == 1:
        x, oldX = stopCond1(x, oldX, func, a, b)
    elif stopCond == 2:
        x, oldX = stopCond2(x, oldX, func, a, b)
    elif stopCond == 3:
        x, oldX = stopCond3(x, oldX, func, a, b)

    results(x, oldX)
    return x

    
#DifferentialEvol(3, 3, -10, 10)  
