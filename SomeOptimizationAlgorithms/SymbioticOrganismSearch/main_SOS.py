from functions_SOS import *

a1 = -2
b1 = 2

a2 = -5
b2 = 5

a3 = -10
b3 = 10

a4 = [-1.5, -3]
b4 = 4

while True:
    func_num = int(input("\nВведіть номер функції (1-4; 0 для виходу): "))
    if func_num == 1:
        #функція 1
        print("-"*80)
        print(" "*18, "@"*7, "ФУНКЦІЯ 1", "@"*7)        
        SymbioticOrganismsSearch(1, a1, b1)
        print("Очікуваний результат: (-1; -4)")
        print()
        
    elif func_num == 2:
        #функція 2
        print("-"*80)
        print(" "*18, "@"*7, "ФУНКЦІЯ 2", "@"*7)
        print()
        SymbioticOrganismsSearch(2, a2, b2)
        print("Очікуваний результат: (-4.636; -10.774)")
        print()
        
    elif func_num == 3:
        #функція 3
        print("-"*80)
        print(" "*18, "@"*7, "ФУНКЦІЯ 3", "@"*7)
        print()
        SymbioticOrganismsSearch(3, a3, b3)
        print("Очікуваний результат: (0; 0; 0)")
        print()
        
    elif func_num == 4:
        #функція 4
        print("-"*80)
        print(" "*18, "@"*7, "ФУНКЦІЯ 4", "@"*7)
        print()
        SymbioticOrganismsSearch(4, a4, b4)
        print("Очікуваний результат: (-0.54719; -1.64719; -1.9133)")
        print()
        
    else:
        break
    

