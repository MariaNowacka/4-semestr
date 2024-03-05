# ćw. 1
# porównać na wykresie rozkład wykładniczy dla 3 różnych lambd
import math, matplotlib.pyplot as plt, numpy as np, seaborn

lambda1 = 0.5
lambda2 = 1
lambda3 = 5

def F(x, lambda0):
    return 1 - math.exp(-lambda0*x)

xs = np.linspace(0,5,100)
y1 = []
for x in xs:
    y1.append(F(x, lambda1))
y2 = []
for x in xs:
    y2.append(F(x, lambda2))
y3 = []
for x in xs:
    y3.append(F(x, lambda3))

plt.plot(xs, y1, color = 'orange', label='lambda1')
plt.plot(xs, y2, color = 'blue', label='lambda2')
plt.plot(xs, y3, color = 'green', label='lambda3')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

# ćw. 2
# próbka z rozkladu wykładniczego o parametrze lambda = 2 i n = 1000 (x1, x2, ..., xn)
lambda0 = 2
n = 1000

# wyznacz dystrybuantę empiryczną i porównaj na wykresie z dystrybuantą teoretyzną F(t) = 1 - e^-2t
# lub 1 - e^1/lambda *x
def F(x, lambda0):
    return 1 - math.exp(-1/lambda0*x)
s = np.random.exponential(2,1000)
xss = np.linspace(0,5,1000)
y = []
for i in xss:
    y.append(F(i,lambda0))
# print(y)

seaborn.ecdfplot(data = s, label = 'empiryczna' )

#plt.plot(xss, y, label = 'empiryczna')
plt.plot(xss, y, label = 'teoretyczna', alpha = 0.5)

plt.legend()
plt.show()

#seaborn
