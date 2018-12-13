import numpy as np

x = # here goes are x-values
y = # here goes are y-values
z = # here goes are z-values

A = np.vstack([x, y, np.ones(len(x))]).T

n = np.linalg.lstsq(A, z, rcond=None)[0]

print(n)
