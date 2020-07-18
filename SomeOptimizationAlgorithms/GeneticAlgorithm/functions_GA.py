import random
import math
signsNum = 4


def calcIndCount(a, c):
    res = math.ceil((c-a)*1000)
    nast = 0
    i = 0
    while (nast<res):
        nast=pow(2, i)
        i+=1
    return (i-1)

def fromBinary_toFloat(x, a, c):
    genes = []
    indCount = len(x)
    z = 0
    b = round((c-a)/(pow(2, indCount) - 1), signsNum)
    #reverse 
    for j in range (indCount-1, -1, -1):
        genes.append(x[j])
    
    #to decimal
    for j in range(0, indCount):
        z+=pow(2, j)*genes[j]

    #to float
    z=round(a + b*z, signsNum)

    return(z)
    
def myFitFunc1(x):
    return round(2*x*x + 4*x - 2, signsNum)

def myFitFunc2(x):
    return round(-0.2*x*x*x + 2*x - x*x*math.sin(x), signsNum)

def myFitFunc3(x):
    return round(x*x*x - x - 4*x*x*math.cos(x), signsNum)

def MatyasFunc(x1, x2):
    return round(0.26*(x1*x1+x2*x2)-0.48*x1*x2, signsNum)

def mutate(x, countInd):
    rand = random.randint(0, countInd-1)
    if (x[rand]==0):
        x[rand]=1
    else:
        x[rand]=0
    return x

def crossingover(x, y):
    cut = random.randint(1, len(x)-1)
    res = x[:cut] + y[cut:]
    return res

def funcVal(val):               #значення фітнесс-функції
    return val[len(val)-1]

def showPop(pop):
    print(" "*15, "[гени]", "[змінна]", "[фітнесс-функція]")
    for i in range (0, len(pop)):
        print(pop[i])
    print()

def mean(pop):
    s = 0
    for i in range (0, len(pop)):
        s+=pop[i][2]
    s/=len(pop)
    return s

def solve(pop, countPop, countInd, a, c, numFitFunc):
    for i in range(0, len(pop)):
        #обираємо рандомно різних батька та матір
        X = pop[random.randint(0, countPop-1)][0]        #батько
        Y = pop[random.randint(0, countPop-1)][0]        #мати
        while (X==Y):
            Y = pop[random.randint(0, countPop-1)][0]

        #робимо кросинговер
        Z = crossingover(X, Y)
        #робимо мутацію з ймовірністю 5%
        if(random.random()<0.05):               
            Z = mutate(Z, countInd)
            
        #додаємо дитину до популяції
        var = fromBinary_toFloat(Z, a, c)
        if numFitFunc == 1:
            pop.append([Z, var, myFitFunc1(var)])
        elif numFitFunc == 2:
            pop.append([Z, var, myFitFunc2(var)])
        elif numFitFunc == 3:
            pop.append([Z, var, myFitFunc3(var)])
        else:
            print("Помилка")
        
    #обираємо кращих    
    pop.sort(key=funcVal, reverse=False)
    pop = pop[:countPop]

    return pop

def solve2(pop, countPop, countInd, a, c, numFitFunc):
    for i in range(0, len(pop)):
        #обираємо рандомно різних батька та матір для X
        X1 = pop[random.randint(0, countPop-1)][0]        #батько 
        X2 = pop[random.randint(0, countPop-1)][0]        #мати
        #обираємо рандомно різних батька та матір для Y
        Y1 = pop[random.randint(0, countPop-1)][1]        #батько 
        Y2 = pop[random.randint(0, countPop-1)][1]        #мати
        while (X1==X2):
            X2 = pop[random.randint(0, countPop-1)][0]
        while (Y1==Y2):
            Y2 = pop[random.randint(0, countPop-1)][1]

        #робимо кросинговер
        Z1 = crossingover(X1, X2)
        Z2 = crossingover(Y1, Y2)
        #робимо мутацію з ймовірністю 5%
        if(random.random()<0.05):               
            Z1 = mutate(Z1, countInd)
        if(random.random()<0.05):               
            Z2 = mutate(Z2, countInd)  
            
        #додаємо дитину до популяції
        var1 = fromBinary_toFloat(Z1, a, c)
        var2 = fromBinary_toFloat(Z2, a, c)
        if numFitFunc == 1:
            pop.append([Z1, Z2, var1, var2, MatyasFunc(var1, var2)])
        elif numFitFunc == 2:
            pop.append([Z1, Z2, var1, var2, MatyasFunc(var1, var2)])
        elif numFitFunc == 3:
            pop.append([Z1, Z2, var1, var2, MatyasFunc(var1, var2)])
        else:
            print("Помилка")
        
    #обираємо кращих    
    pop.sort(key=funcVal, reverse=False)
    pop = pop[:countPop]

    return pop
