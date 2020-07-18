from functions_GA import *


print("Enter 'Func1', 'Func2' or 'Func3' with an argument 1,2 or 3 (stop condition)")

def Func1(stopCond = 1):
    print("Очікуваний результат: (-1; -4)")

    #[a1;c1]
    a1 = -1.2
    c1 = 0
    
    countInd = calcIndCount(a1, c1)            #к-ть генів в індивіда
    countPop = 50          #к-ть індивидів у популяції (одне покоління)
    countGen = 10          #макс к-ть поколінь (популяцій) = одна з умов закінчення
    eps = 0.001             #точність для умови зупинки
    populn = []
    oldPop = []

    for i in range (0, countPop):
        X = []
        for j in range (0, countInd):
            X.append(round(random.randint(0, 1), signsNum))
        var = fromBinary_toFloat(X, a1, c1)
        populn.append([X, var, myFitFunc1(var)])

    print(" "*16, "#"*7, "ПЕРША ПОПУЛЯЦІЯ", "#"*7)
    #showPop(populn)
    oldPop = populn.copy()
    oldPop.sort(key=funcVal, reverse=False)
    gen = 2
    populn = solve(populn, countPop, countInd, a1, c1, 1)
    print(" "*16, "#"*7, "ПОПУЛЯЦІЯ № 2", "#"*7)
    #showPop(populn)

    if stopCond == 1:
    #перший варіант умови закінчення алгоритму (min)
        while (abs(min(populn, key=funcVal)[2] - min(oldPop, key=funcVal)[2]) > eps):
            gen+=1
            oldPop = populn.copy()
            populn = solve(populn, countPop, countInd, a1, c1, 1)
            print(" "*16, "#"*7, "ПОПУЛЯЦІЯ №", gen, "#"*7)
            #showPop(populn)
    elif stopCond == 2:
    #другий варіант умови закінчення алгоритму (mean)
        while (abs(mean(populn) - mean(oldPop)) > eps):
            gen+=1
            oldPop = populn.copy()
            populn = solve(populn, countPop, countInd, a1, c1, 1)
            print(" "*16, "#"*7, "ПОПУЛЯЦІЯ №", gen, "#"*7)
            #showPop(populn)
    else:  
    #третій варіант умови закінчення алгоритму (макс. к-ть ітерацій)
        for generation in range(gen, countGen):
            gen+=1
            oldPop = populn.copy()
            populn = solve(populn, countPop, countInd, a1, c1, 1)
            print(" "*16, "#"*7, "ПОПУЛЯЦІЯ №", gen, "#"*7)
            #showPop(populn)


    print(" "*16, "#"*7, "РЕЗУЛЬТАТИ", "#"*7)
    print("Найкращий з попередньої популяції:")
    print(oldPop[0])
    print("Найкращий з даної популяції:")
    print(populn[0])


def Func2(stopCond = 1):
    print("Очікуваний результат: (-4.636; -10.774)")

    #[a1;c1]
    a1 = -5
    c1 = 5
    
    countInd = calcIndCount(a1, c1)            #к-ть генів в індивіда
    countPop = 50          #к-ть індивидів у популяції (одне покоління)
    countGen = 10          #макс к-ть поколінь (популяцій) = одна з умов закінчення
    eps = 0.001             #точність для умови зупинки
    populn = []
    oldPop = []

    for i in range (0, countPop):
        X = []
        for j in range (0, countInd):
            X.append(round(random.randint(0, 1), signsNum))
        var = fromBinary_toFloat(X, a1, c1)
        populn.append([X, var, myFitFunc2(var)])

    print(" "*16, "#"*7, "ПЕРША ПОПУЛЯЦІЯ", "#"*7)
    #showPop(populn)
    oldPop = populn.copy()
    oldPop.sort(key=funcVal, reverse=False)
    gen = 2
    populn = solve(populn, countPop, countInd, a1, c1, 2)
    print(" "*16, "#"*7, "ПОПУЛЯЦІЯ № 2", "#"*7)
    #showPop(populn)

    if stopCond == 1:
    #перший варіант умови закінчення алгоритму (min)
        while (abs(min(populn, key=funcVal)[2] - min(oldPop, key=funcVal)[2]) > eps):
            gen+=1
            oldPop = populn.copy()
            populn = solve(populn, countPop, countInd, a1, c1, 2)
            print(" "*16, "#"*7, "ПОПУЛЯЦІЯ №", gen, "#"*7)
            #showPop(populn)
    elif stopCond == 2:
    #другий варіант умови закінчення алгоритму (mean)
        while (abs(mean(populn) - mean(oldPop)) > eps):
            gen+=1
            oldPop = populn.copy()
            populn = solve(populn, countPop, countInd, a1, c1, 2)
            print(" "*16, "#"*7, "ПОПУЛЯЦІЯ №", gen, "#"*7)
            #showPop(populn)
    else:
    #третій варіант умови закінчення алгоритму (макс. к-ть ітерацій)
        for generation in range(gen, countGen):
            gen+=1
            oldPop = populn.copy()
            populn = solve(populn, countPop, countInd, a1, c1, 2)
            print(" "*16, "#"*7, "ПОПУЛЯЦІЯ №", gen, "#"*7)
            #showPop(populn)

    print(" "*16, "#"*7, "РЕЗУЛЬТАТИ", "#"*7)
    print("Найкращий з попередньої популяції:")
    print(oldPop[0])
    print("Найкращий з даної популяції:")
    print(populn[0])
    
def Func3(stopCond = 1):
    print("Очікуваний результат: (-1.328; -2.71)")
    
    #[a1;c1]
    a1 = -2
    c1 = 2
    
    countInd = calcIndCount(a1, c1)            #к-ть генів в індивіда
    countPop = 50          #к-ть індивидів у популяції (одне покоління)
    countGen = 10          #макс к-ть поколінь (популяцій) = одна з умов закінчення
    eps = 0.001             #точність для умови зупинки
    populn = []
    oldPop = []

    for i in range (0, countPop):
        X = []
        for j in range (0, countInd):
            X.append(round(random.randint(0, 1), signsNum))
        var = fromBinary_toFloat(X, a1, c1)
        populn.append([X, var, myFitFunc2(var)])

    print(" "*16, "#"*7, "ПЕРША ПОПУЛЯЦІЯ", "#"*7)
    #showPop(populn)
    oldPop = populn.copy()
    oldPop.sort(key=funcVal, reverse=False)
    gen = 2
    populn = solve(populn, countPop, countInd, a1, c1, 3)
    print(" "*16, "#"*7, "ПОПУЛЯЦІЯ № 2", "#"*7)
    #showPop(populn)

    if stopCond == 1:
    #перший варіант умови закінчення алгоритму (min)
        while (abs(min(populn, key=funcVal)[2] - min(oldPop, key=funcVal)[2]) > eps):
            gen+=1
            oldPop = populn.copy()
            populn = solve(populn, countPop, countInd, a1, c1, 3)
            print(" "*16, "#"*7, "ПОПУЛЯЦІЯ №", gen, "#"*7)
            #showPop(populn)
    elif stopCond == 2:
    #другий варіант умови закінчення алгоритму (mean)
        while (abs(mean(populn) - mean(oldPop)) > eps):
            gen+=1
            oldPop = populn.copy()
            populn = solve(populn, countPop, countInd, a1, c1, 3)
            print(" "*16, "#"*7, "ПОПУЛЯЦІЯ №", gen, "#"*7)
            #showPop(populn)
    else:
    #третій варіант умови закінчення алгоритму (макс. к-ть ітерацій)
        for generation in range(gen, countGen):
            gen+=1
            oldPop = populn.copy()
            populn = solve(populn, countPop, countInd, a1, c1, 3)
            print(" "*16, "#"*7, "ПОПУЛЯЦІЯ №", gen, "#"*7)
            #showPop(populn)

    print(" "*16, "#"*7, "РЕЗУЛЬТАТИ", "#"*7)
    print("Найкращий з попередньої популяції:")
    print(oldPop[0])
    print("Найкращий з даної популяції:")
    print(populn[0])


def Func4(stopCond = 1):
    print("MATYAS")
    #[a1;c1]
    a1 = -10
    c1 = 10
    
    countInd = calcIndCount(a1, c1)            #к-ть генів в індивіда
    countPop = 50          #к-ть індивидів у популяції (одне покоління)
    countGen = 50          #макс к-ть поколінь (популяцій) = одна з умов закінчення
    eps = 0.001             #точність для умови зупинки
    populn = []
    oldPop = []

    for i in range (0, countPop):
        X = []
        Y = []
        for j in range (0, countInd):
            X.append(random.randint(0, 1))
            Y.append(random.randint(0, 1))
        var1 = fromBinary_toFloat(X, a1, c1)
        var2 = fromBinary_toFloat(Y, a1, c1)
        populn.append([X, Y, var1, var2, MatyasFunc(var1, var2)])

    print(" "*16, "#"*7, "ПЕРША ПОПУЛЯЦІЯ", "#"*7)
    #showPop(populn)
    oldPop = populn.copy()
    oldPop.sort(key=funcVal, reverse=False)
    gen = 2
    populn = solve2(populn, countPop, countInd, a1, c1, 3)
    print(" "*16, "#"*7, "ПОПУЛЯЦІЯ № 2", "#"*7)
    #showPop(populn)

    if stopCond == 1:
    #перший варіант умови закінчення алгоритму (min)
        while (abs(min(populn, key=funcVal)[2] - min(oldPop, key=funcVal)[2]) > eps):
            gen+=1
            oldPop = populn.copy()
            populn = solve2(populn, countPop, countInd, a1, c1, 3)
            print(" "*16, "#"*7, "ПОПУЛЯЦІЯ №", gen, "#"*7)
            #showPop(populn)
    elif stopCond == 2:
    #другий варіант умови закінчення алгоритму (mean)
        while (abs(mean(populn) - mean(oldPop)) > eps):
            gen+=1
            oldPop = populn.copy()
            populn = solve2(populn, countPop, countInd, a1, c1, 3)
            print(" "*16, "#"*7, "ПОПУЛЯЦІЯ №", gen, "#"*7)
            #showPop(populn)
    else:
    #третій варіант умови закінчення алгоритму (макс. к-ть ітерацій)
        for generation in range(gen, countGen):
            gen+=1
            oldPop = populn.copy()
            populn = solve2(populn, countPop, countInd, a1, c1, 3)
            print(" "*16, "#"*7, "ПОПУЛЯЦІЯ №", gen, "#"*7)
            #showPop(populn)

    print(" "*16, "#"*7, "РЕЗУЛЬТАТИ", "#"*7)
    print("Найкращий з попередньої популяції:")
    print(oldPop[0])
    print("Найкращий з даної популяції:")
    print(populn[0])
