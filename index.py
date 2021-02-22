import numpy as np

numEpocas = 40000
q = 6

peso = np.array([113, 122, 107, 98, 115, 120])
pH = np.array([6.8, 4.7, 5.2, 3.6, 2.9, 4.2])

bias = 3

x = np.vstack((peso, pH))
y = np.array([-1, 1, -1, -1, -1, 1])

eta = 0.1

w= np.zeros([1,3])

e= np.zeros(6)

def activationFunction(valor):
  if valor < 0.0:
    return(-1)
  else:
    return(1)

for j in range(numEpocas):
  for k in range(q):
    Xb = np.hstack((bias, x[:,k]))

    v = np.dot(w, Xb)

    Yr = activationFunction(v)

    e[k] = y[k] - Yr

    w = w + eta*e[k]*Xb


print("Vetor de erros (e) = " + str(e))