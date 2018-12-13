import numpy as np

coord = np.array([[-101539.71423499999,259547.87545000002,535.5710331500641],[-101537.72423499999,259543.92045,533.6495331500636],[-101505.05123499999,259560.37345,533.802033150064],[-101507.05423499999,259564.33245000002,535.555783150064]])

x = coord[:,0]
y = coord[:,1]
z = coord[:,2]

A = np.vstack([x, y, np.ones(len(x))]).T

n = np.linalg.lstsq(A, z, rcond=None)[0]

# n0 * x0 + n1 * y0 + n2 * z0 = d

print("This is the A matrix:")
print(A)

n = n / np.sqrt((n ** 2).sum(-1))
a, b, c = n
d = a * x[0] + b * y[0] + c * z[0]

print("This is the normal and the d coefficient")
print(a, b, c, d)

for i in range(1, 4):
    s = a * x[i] + b * y[i] + c * z[i] - d

    print("This is the 'distance' of point ", i)
    print(s)
