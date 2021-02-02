import numpy as np
import matplotlib.pyplot as plt
import logging
import constant
import formula

X  = np.linspace(0.01, 500, num = 10000)
Y0 = []
Y1 = []
Y2 = []
Y3 = []


V0 = 0
V1 = 100
V2 = 300
V3 = 600

# vK = (1 / (wx / wy) ** wy) * (wx * X + constant.K * (wx / wy) ** wy) ** (1 / wy)


print('equilibrium point =  [', constant.Xe, ',', constant.Ye, ']')


for i in range(len(X)):
  Y0.append(formula.vBalancer(V0, X[i]))
  Y1.append(formula.vBalancer(V1, X[i]))
  Y2.append(formula.vBalancer(V2, X[i]))
  Y3.append(formula.vBalancer(V3, X[i]))


plt.ylim(0, 250)
plt.xlim(0, 250)

plt.plot(X, Y0, label='V = %.2f' %V0)
plt.plot(X, Y1, label='V = %.2f' %V1)
plt.plot(X, Y2, label='V = %.2f' %V2)
plt.plot(X, Y3, label='V = %.2f' %V3)

plt.legend()


# plt.plot(x2,fx3)

plt.grid()
# plt.axvline()
# plt.axhline()
plt.axhline(y=0, color='black')
plt.axvline(x=0, color='black')
plt.show()

