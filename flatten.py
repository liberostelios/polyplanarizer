import numpy as np

coord = np.loadtxt("Dachlinien.csv", delimiter=",", skiprows=1)

x = coord[:-1,1]
y = coord[:-1,2]
z = coord[:-1,3]

A = np.vstack([x, y, np.ones(len(x))]).T

result = np.linalg.lstsq(A, z, rcond=None)

n = result[0]

print("This is the A matrix:")
print(A)

print("Those are the z values:")
print(z)

print("This is the result:")
print(result)

n = n / np.sqrt((n ** 2).sum(-1))
a, b, c = n
d = a * x[0] + b * y[0] + c * z[0]

print("This is the normal and the d coefficient")
print(a, b, c, d)

zp = np.zeros(len(x))

for i in range(0, 4):
    # Calculate the sigma value - sort of an error
    s = a * x[i] + b * y[i] + c * z[i] - d
    print("The sigma of point ", i, " is: ", s)
    
    # Calculate the z' according to the plane
    zp[i] = - (a * x[i] + b * y[i] - d) / c
    print("New point is: ", x[i], y[i], zp[i], " (old Z was: ", z[i], ")")

np.savetxt("new_points.csv", np.array([x, y, zp]).T, fmt="%.11f", delimiter=",")
