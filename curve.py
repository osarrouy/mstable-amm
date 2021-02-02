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
P  = []
Wx = []
Wy = []

V0 = 0
V1 = 100
V2 = 400
V3 = 50000

# vK = (1 / (wx / wy) ** wy) * (wx * X + constant.K * (wx / wy) ** wy) ** (1 / wy)


print('equilibrium point =  [', constant.Xe, ',', constant.Ye, ']')

def price(V, x):
  y = formula.vBalancer(V, x)
  Y = y + constant.Wy * V
  X = x + constant.Wx * V

  return Y * constant.Wx / (X * constant.Wy)

def weight(V, x):
  y = formula.vBalancer(V, x)
  w = y / (y + x)
  return w / constant.Wy

for i in range(len(X)):
  Y0.append(formula.vBalancer(V0, X[i]))
  Y1.append(formula.vBalancer(V1, X[i]))
  Y2.append(formula.vBalancer(V2, X[i]))
  Y3.append(formula.vBalancer(V3, X[i]))
  P.append(price(V3, X[i]))
  Wy.append(weight(V3, X[i]))



fig, ax = plt.subplots()
ax2     = ax.twinx()

ax.set_xlim([0, 300])
ax.set_ylim([0, 300])
ax.set_ylabel("y")


# plt.ylim(100, 150)
# plt.xlim(20, 60)

ax.plot(X, Y0, label='V = %.2f' %V0)
ax.plot(X, Y3, label='V = %.2f' %V3)
ax.legend()
ax2.set_xlim([0, 300])
ax2.set_ylim([0.7, 1.3])
ax2.set_ylabel("price and weight deviation")
# plt.plot(X, Y1, label='V = %.2f' %V1)
# plt.plot(X, Y2, label='V = %.2f' %V2)
ax2.plot(X, P,  label='price', color="red", linestyle='dashed')
ax2.plot(X, Wy,  label='weight deviation', color="green", linestyle='dashed')
ax2.legend(bbox_to_anchor=(1,0), loc="lower right")


# ax2.plot(X, Wy,  label='Y weight x100')


# plt.legend()


# plt.plot(x2,fx3)

plt.grid()
plt.axvline()
plt.axhline()
# plt.axhline(y=0, color='black')
# plt.axvline(x=0, color='black')
# plt.gca().set_aspect("equal")
plt.show()

