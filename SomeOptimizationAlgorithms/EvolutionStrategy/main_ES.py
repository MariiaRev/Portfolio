from functions_ES import *

a1 = -2
b1 = 2

a2 = -5
b2 = 5

a3 = -10
b3 = 10



#функція 1
print("-"*80)
print(" "*18, "@"*7, "ФУНКЦІЯ 1", "@"*7)
print("Очікуваний результат: (-1; -4)")
print()
print(" "*14, "$"*7, "АЛГОРИТМ ЗУПИНКИ 1", "$"*7)
print()
x = EvolStrat(1, 1, a1, b1)
print()
print(" "*14, "$"*7, "АЛГОРИТМ ЗУПИНКИ 2", "$"*7)
print()
EvolStrat(2, 1, a1, b1)
print()
print(" "*14, "$"*7, "АЛГОРИТМ ЗУПИНКИ 3", "$"*7)
print()
EvolStrat(3, 1, a1, b1)
print()

#функція 2
print("-"*80)
print(" "*18, "@"*7, "ФУНКЦІЯ 2", "@"*7)
print("Очікуваний результат: (-4.636; -10.774)")
print()
print(" "*14, "$"*7, "АЛГОРИТМ ЗУПИНКИ 1", "$"*7)
print()
EvolStrat(1, 2, a2, b2)
print()
print(" "*14, "$"*7, "АЛГОРИТМ ЗУПИНКИ 2", "$"*7)
print()
EvolStrat(2, 2, a2, b2)
print()
print(" "*14, "$"*7, "АЛГОРИТМ ЗУПИНКИ 3", "$"*7)
print()
EvolStrat(3, 2, a2, b2)
print()

#функція 3
print("-"*80)
print(" "*18, "@"*7, "ФУНКЦІЯ 3", "@"*7)
print("Очікуваний результат: (0; 0; 0)")
print()
print(" "*14, "$"*7, "АЛГОРИТМ ЗУПИНКИ 1", "$"*7)
print()
EvolStrat(1, 3, a3, b3)
print()

print(" "*14, "$"*7, "АЛГОРИТМ ЗУПИНКИ 2", "$"*7)
print()
EvolStrat(2, 3, a3, b3)
print()
print(" "*14, "$"*7, "АЛГОРИТМ ЗУПИНКИ 3", "$"*7)
print()
EvolStrat(3, 3, a3, b3)
