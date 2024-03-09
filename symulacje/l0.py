import random
def zad1():
    j=0 
    g=0
    n = 10*10**5
    tab = ''
    for _ in range(n):
        X = random.random()
        if X> 0.5:
            tab +='O'
            # print(tab)
        else:
            tab+='R'
            # print(tab)
        if 'OOR' in tab:
            # print('wygrywa Jaś')
            j+=1
            tab = ''
            
        if 'ORR' in tab:
            g+=1
            # print('wygrywa Grześ')
            tab = ''
            
    pr = g/(g+j)
    return pr
#print(zad1())

def gra():
    j=0 
    g=0
    tab = ''
    while True:
        X = random.random()
        if X> 0.5:
            tab +='O'
            # print(tab)
        else:
            tab+='R'
            # print(tab)
        if 'OOR' in tab:
            # print('wygrywa Jaś')
            j+=1
            break
        if 'ORR' in tab:
            g+=1
            # print('wygrywa Grześ')
            break
    return g, j

def bankructwo(g_coins = 25, j_coins = 5, bank_g = 0, bank_j = 0):
    while g_coins >= 0 and j_coins >= 0:
        g_coins -= 1
        j_coins -= 1
        wynik = gra()
        if wynik[0] > 0:
            g_coins += 2
        if wynik[1] > 0:
            j_coins += 2
        if g_coins == 0:
            bank_g += 1
            return (1,0)
        if j_coins == 0:
            bank_j += 1
            return (0,1)

def zad2():
    n = 1000
    g, j = (0,0)
    for i in range(n):
        w = bankructwo()
        g += w[0]
        j += w[1]
    return g/(g+j)

pr2 = zad2()
print('prawd = ',pr2)

