import constant

def balancer(x):
  return (constant.K / (x ** constant.Wx)) ** (1 / constant.Wy)

# def vBalancer(x):
#   return (constant.vK / (x + constant.Wx * constant.V) ** constant.Wx) ** (1 / constant.Wy) - constant.Wy * constant.V 

def vBalancer(V, x):
  return (constant.vK(V) / (x + constant.Wx * V) ** constant.Wx) ** (1 / constant.Wy) - constant.Wy * V 