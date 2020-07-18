import random as r
import math
num_pop = 20                #кількість особин у популяції
num_gen = 40                #кількість поколінь
signsNum = 5                #кількість цифр після коми


def myFunc1(x):
    return round(2*x*x + 4*x - 2, signsNum)

def myFunc2(x):
    return round(-0.2*x*x*x + 2*x - x*x*math.sin(x), signsNum)

def MatyasFunc(x1, x2):
    return round(0.26*(x1*x1+x2*x2)-0.48*x1*x2, signsNum)

def McCormickFunc(x1, x2):
    return round(math.sin(x1+x2) + (x1-x2)*(x1-x2) - 1.5*x1 + 2.5*x2 + 1, signsNum)

def F(func, x, y=0):
    if func == 1:
        return myFunc1(x)
    elif func == 2:
        return myFunc2(x)
    elif func == 3:
        return MatyasFunc(x, y)
    else:
        return McCormickFunc(x, y)
        

def showPop(pop):
    for elem in pop:
        print(elem)
    print()


def funcVal (val):
    return val[len(val)-1]


def SymbioticOrganismsSearch (func, a, b):
    pop = []
    y = 0
    #генеруємо початкову популяцію
    if func>2:
        for i in range (num_pop):
            if isinstance(a, list):
                x = round(r.uniform(a[0], b), signsNum)
                y = round(r.uniform(a[1], b), signsNum)
            else:
                x = round(r.uniform(a, b), signsNum)
                y = round(r.uniform(a, b), signsNum)
            pop.append([x, y, F(func, x, y)])
    elif func<3:
        for i in range (num_pop):
            x = round(r.uniform(a, b), signsNum)
            pop.append([x, F(func, x)])
    #сортуємо
    pop.sort(key=funcVal, reverse = False)
    #знаходимо кращого
    print(" "*16, "#"*7, "ПОЧАТКОВА ПОПУЛЯЦІЯ", "#"*7)
    showPop(pop)
    
    #у циклі
    for gen in range (num_gen-1):
        print(" "*16, "#"*7, "ПОПУЛЯЦІЯ №", gen+2, "#"*7)
        Best = pop[0].copy()
        for i in range (num_pop):
            #мутуалізм
            j=i
            while j == i:
                j = r.randint(0, num_pop -1)
            BF = r.randint(1, 2)        #коефіцієнт вигоди
            m_vect = [0, 0]
            m_vect[0] = (pop[i][0] + pop[j][0])/2
            if func>2:
                m_vect[1] = (pop[i][1] + pop[j][1])/2
                y = round(pop[i][1] + r.random()*(Best[1] - m_vect[1]*BF), signsNum)
            if isinstance(a, list):
                x = b+1
                while x>b or x<a[0]:
                    x = round(pop[i][0] + r.random()*(Best[0] - m_vect[0]*BF), signsNum)
                while y>b or y<a[1]:
                    y = round(pop[i][1] + r.random()*(Best[1] - m_vect[1]*BF), signsNum)
            else:
                x = b+1
                while x>b or x<a:
                    x = round(pop[i][0] + r.random()*(Best[0] - m_vect[0]*BF), signsNum)
            
            f = F(func, x, y)
            if f < pop[i][len(pop[i])-1]:
                if func>2:
                    pop[i]=[round(x, signsNum), round(y, signsNum), f]
                else:
                    pop[i]=[round(x, signsNum), f]
                
            #коменсалізм
            j=i
            while j == i:
                j = r.randint(0, num_pop-1)
            x = b+1
            if isinstance(a, list):
                while x>b or x<a[0]:
                    x = pop[i][0] + r.uniform(-1, 1)*(Best[0]-pop[j][0])
            else:
                while x>b or x<a:
                    x = pop[i][0] + r.uniform(-1, 1)*(Best[0]-pop[j][0])
            if func>2:
                y = b+1
                if isinstance(a, list):
                    while y>b or y<a[1]:
                        y = pop[i][1] + r.uniform(-1, 1)*(Best[1]-pop[j][1])
                else:
                    while y>b or y<a:
                        y = pop[i][1] + r.uniform(-1, 1)*(Best[1]-pop[j][1])
                       
            f = F(func, x, y)
            if f < pop[i][len(pop[i])-1]:
                if func>2:
                    pop[i]=[round(x, signsNum), round(y, signsNum), f]
                else:
                    pop[i]=[round(x, signsNum), f]
            #паразитизм
            Par = pop[i].copy()
            coin = r.random()
            
            if func>2:
                if coin < 0.5:
                    if isinstance(a, list):
                        Par[0] = round(r.uniform(a[0],b), signsNum)
                    else:
                        Par[0] = round(r.uniform(a,b), signsNum)
                else:
                    if isinstance(a, list):
                        Par[1] = round(r.uniform(a[1],b), signsNum)
                    else:
                        Par[1] = round(r.uniform(a,b), signsNum)
                Par[2] = F(func, x, y)
            else:
                if coin < 0.5:
                    Par[0] = r.uniform(a,b)
                Par[1] = F(func, x)

            if Par[len(Par)-1] < pop[i][len(pop[i])-1]:
                    pop[i] = Par[2].copy()    
        pop.sort(key=funcVal, reverse = False)
        showPop(pop)
    print("Найкращий з даної популяції:", pop[0])
    #showPop(pop[:1])    
    return pop
                
    
