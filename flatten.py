import numpy as np

coord = np.loadtxt("Dachlinien.csv", delimiter=",", skiprows=1)

x = coord[:-1,1]
y = coord[:-1,2]
z = coord[:-1,3]

a = 0
b = 0
c = 0

l = len(x)
for i in range(0, l):
    a += (y[i] - y[(i+1)%l])*(z[i] + z[(i+1)%l])
    b += (z[i] - z[(i+1)%l])*(x[i] + x[(i+1)%l])
    c += (x[i] - x[(i+1)%l])*(y[i] + y[(i+1)%l])

n = np.array([a, b, c])
n = n / np.sqrt((n ** 2).sum(-1))
a, b, c = n
d = a * x[0] + b * y[0] + c * z[0]

print("This is the normal and the d coefficient")
print(a, b, c, d)

zp = np.zeros(len(x))

for i in range(0, len(x)):
    # Calculate the sigma value - sort of an error
    s = a * x[i] + b * y[i] + c * z[i] - d
    print("The sigma of point ", i, " is: ", s)
    
    # Calculate the z' according to the plane
    zp[i] = - (a * x[i] + b * y[i] - d) / c
    print("New point is: ", x[i], y[i], zp[i], " (old Z was: ", z[i], ")")

    # Calculate the sigma value - sort of an error
    s = a * x[i] + b * y[i] + c * zp[i] - d
    print("The sigma of point ", i, " is: ", s)

np.savetxt("new_points.csv", np.array([x, y, zp]).T, fmt="%.11f", delimiter=",")
