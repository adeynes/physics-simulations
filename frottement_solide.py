import matplotlib.pyplot as plt
import math

m = 1  # masse kg
g = 9.81  # m.s-2
k = 20  # constante de raideur N.m-1
l_0 = 1  # longueur à vide m
mu_s = 1.8  # statique
mu_d = 1.2 # dynamique
U = 10  # vitesse du ressort m.s-1

x = [l_0+1]
v = [0]

iterations = 50000
pas = 0.0001

for n in range(1, iterations):
    l = x[-1] - U * ((n-1)*pas)  # longueur du ressort
    F = k * (l_0 - l)

    if abs(F) <= mu_s * m * g:
        F = 0
    else:
        F += -F/F * mu_d * m * g

    x.append(x[-1] + v[-1]*pas)
    v.append(v[-1] + F*pas/m)

t = [n*pas for n in range(iterations)]

plt.plot(t, x, label="Poition")
plt.plot(t, v, label="Vitesse")
plt.legend()
plt.show()

