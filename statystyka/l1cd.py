# lista 1
import math, matplotlib.pyplot as plt, seaborn, numpy as np
from  scipy.stats import norm, lognorm,  pareto
# 1
my_file = open("E:/statystyka/dane.txt", 'r')

data = my_file.read().split()
my_file.close()
# print(data)
x1 = range(1,1001)
y = []
x=[]
for i in data:
    y.append(math.exp(float(i)))
    i = float(i)
    x.append(i)

# c
# plt.plot(x1, y)
# plt.show()

# d
# plt.hist(x)
# plt.show()
# plt.hist(y)
# plt.show()

# e
# plt.hist(x, density = True)
# plt.plot(np.linspace(-3,3,1000), norm.pdf(np.linspace(-3,3,1000)))
# plt.show()
# plt.hist(y, density = True)
# plt.plot(np.linspace(0,12,1000), lognorm.pdf(np.linspace(0,12,1000),1))
# plt.show()

# f
# seaborn.kdeplot(x, label= 'gestość empiryczna X')
# plt.plot(np.linspace(-3,3,1000), norm.pdf(np.linspace(-3,3,1000)), label='teoretyczna')
# plt.legend()
# plt.show()
# seaborn.kdeplot(y, label= 'gestość empiryczna Y')
# plt.plot(np.linspace(0,12,1000), lognorm.pdf(np.linspace(0,12,1000),1), label='teoretyczna')
# plt.legend()
# plt.show()

# 2
import random
lambd = 1
alfa = 3
us = []
n=10**3
for u in range(n):
    us.append(random.random())

def F(x,alfa=3, lambd=1):
    return 1-(lambd/(lambd+x)**alfa)
  
def F_1(u, alfa = 3, lambd = 1):    # dystrybuanta odwrotna
    return lambd*(math.sqrt(1-u)**(-1/alfa)-1)
# zadanie 2
K = []
K1 = []

for u in us:
    K.append(lambd*(1/(u**(1/alfa))-1))
    K1.append(F_1(u))
  
plt.plot(us, K, label ='próba n=1000, K')
plt.plot(us, K1, label='próba K1')
plt.legend()
# plt.show()

plt.hist(K)
plt.title('histogram próby pareto')
# plt.show()

# zadanie 3
yss = []
xss = np.linspace(0,10,n)
for x in xss:
    yss.append(F(x)) # do dystrybuanty teretycznej

def demp(X, x):
    n = len(X)
    count = sum(1 for xi in X if xi <= x)
    return count / n
def drewdemp(X): # dodana opcja porównania do tego zadania
    X.append(1)
    # X.append(math.sqrt(len(X)))
    # X.append(-math.sqrt(len(X)))
    x_values = np.sort(X)
    y_values = [demp(x_values, x) for x in x_values]
    plt.plot(x_values, y_values, label='empiryczna')
    # plt.title('dystrybuanta empiryczna')
    # p o   r   ó   w   n   a   n   i   e
    plt.plot(xss, yss, label='teoretyczna')
    # plt.title('dystrybuanta teoretyczna')
    plt.legend()
    plt.show()

drewdemp(K)
