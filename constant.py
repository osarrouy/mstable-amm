K  = 100   # invariant constant
Wx = 0.25  # weight of token X
Wy = 0.75  # weight ot token Y

Xe = K  * (Wx / Wy) ** Wy
Ye = Xe *  Wy / Wx

# vK = ((Wy * V + (K / (Xe ** Wx)) ** (1 / Wy)) ** Wy) * (Xe + Wx * V) ** Wx

def vK(V):
  return ((Wy * V + (K / (Xe ** Wx)) ** (1 / Wy)) ** Wy) * (Xe + Wx * V) ** Wx
