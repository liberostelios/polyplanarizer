import numpy as np

coord = np.loadtxt("Dachlinien.csv", delimiter=",", skiprows=1)

x = coord[:,1]
y = coord[:,2]
z = coord[:,3]

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
