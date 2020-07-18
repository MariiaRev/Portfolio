import random
import math
signsNum = 4
numPoints = 7
eps = 0.001

def myFunc1(x):
    return round(2*x*x + 4*x - 2, signsNum)

def myFunc2(x):
    return round(-0.2*x*x*x + 2*x - x*x*math.sin(x), signsNum)

def MatyasFunc(x1, x2):
    return round(0.26*(x1*x1+x2*x2)-0.48*x1*x2, signsNum)

def generatePop(countInd, a, b, func):
    x = []
    for i in range(countInd):
        Xi = round(random.uniform(a, b), signsNum)
        if func == 1:
            x.append([Xi, myFunc1(Xi)])
        elif func == 2:
            x.append([Xi, myFunc2(Xi)])
        elif func == 3:
            Xi2 = round(random.uniform(a, b), signsNum)
            x.append([Xi, Xi2, MatyasFunc(Xi, Xi2)])
    return x

def showPop(pop):
    for i in range(len(pop)):
        print (pop[i])

def children(pop, a, b, func):
    sigma = abs((b - a)/len(pop))
    for i in range(0, len(pop)):
        for j in range(0, numPoints):
            x = round(pop[i][0]+random.uniform(-sigma/3, sigma/3), signsNum)
            if func == 1:
                pop.append([x, myFunc1(x)])
            elif func == 2:
                pop.append([x, myFunc2(x)])
            elif func == 3:
                y = round(pop[i][1]+random.uniform(-sigma/3, sigma/3), signsNum)
                pop.append([x, y, MatyasFunc(x, y)])
    return pop

def funcVal(val):
    return val[len(val)-1]

def chooseBest(pop, countInd):
    pop.sort(key=funcVal, reverse=False)
    pop = pop[:countInd]
    return pop

def results(pop, oldPop):
    print(" "*16, "#"*7, "РЕЗУЛЬТАТИ", "#"*7)
    print("Найкращий з попередньої популяції:")
    print(oldPop[0])
    print("Найкращий з даної популяції:")
    print(pop[0])

def mean(pop):
    s = 0
    ind = len(pop[0])-1
    for i in range (0, len(pop)):
        s+=pop[i][ind]
    s/=len(pop)
    return s

def stopCond1(pop, oldPop, countInd, a, b, func):
    gen = 2
    ind = len(pop[0])-1
    while (abs(min(pop, key=funcVal)[ind] - min(oldPop, key=funcVal)[ind]) > eps):
        gen+=1
        oldPop = pop.copy()
        pop = children(pop, a, b, func)
        pop = chooseBest(pop, countInd)
        print(" "*16, "#"*7, "ПОПУЛЯЦІЯ №", gen, "#"*7)
        showPop(pop)
    return pop, oldPop

def stopCond2(pop, oldPop, countInd, a, b, func):
    gen = 2
    while (abs(mean(pop) - mean(oldPop)) > eps):
        gen+=1
        oldPop = pop.copy()
        pop = children(pop, a, b, func)
        pop = chooseBest(pop, countInd)
        print(" "*16, "#"*7, "ПОПУЛЯЦІЯ №", gen, "#"*7)
        showPop(pop)
    return pop, oldPop

def stopCond3(pop, oldPop, countInd, a, b, func):
    countGen = 20
    gen = 2
    for generation in range(gen, countGen):
        gen+=1
        oldPop = pop.copy()
        pop = children(pop, a, b, func)
        pop = chooseBest(pop, countInd)
        print(" "*16, "#"*7, "ПОПУЛЯЦІЯ №", gen, "#"*7)
        showPop(pop)
    return pop, oldPop


def EvolStrat(stopCond, funcKind, a, b):
    countInd = 10
    print(" "*16, "#"*7, "ПЕРША ПОПУЛЯЦІЯ", "#"*7)
    x = generatePop(countInd, a, b, funcKind)
    oldX = x.copy()
    oldX.sort(key=funcVal, reverse=False)
    showPop(x)

    print(" "*16, "#"*7, "ПОПУЛЯЦІЯ № 2", "#"*7)
    x = children(x, a, b, funcKind)
    x = chooseBest(x, countInd)
    showPop(x)

    if stopCond == 1:
        x, oldX = stopCond1(x, oldX, countInd, a, b, funcKind)
    elif stopCond == 2:
        x, oldX = stopCond2(x, oldX, countInd, a, b, funcKind)
    elif stopCond == 3:
        x, oldX = stopCond3(x, oldX, countInd, a, b, funcKind)
    
    results(x, oldX)
    return x
