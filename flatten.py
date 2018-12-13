import numpy as np



coord = np.loadtxt("DachlinienV2.csv", delimiter=",", dtype={'names': ('id', 'x', 'y', 'z'), 'formats': ('|S50', 'f', 'f', 'f')})

output = np.empty([len(coord)], dtype={'names': ('id', 'x', 'y', 'z'), 'formats': ('|S50', 'f', 'f', 'f')})

polygons = {}

for i in range(0, len(coord)):
    e = coord[i]
    if e['id'] in polygons:
        polygons[e['id']] = np.append(polygons[e['id']], [[e['x'], e['y'], e['z']]], axis=0)
    else:
        polygons[e['id']] = np.array([[e['x'], e['y'], e['z']]])

n = {}

for ii, points in polygons.items():
    n[ii] = np.array([0, 0, 0])
    for i in range(0, len(points) - 1):
        n[ii][0] += (points[i][1] - points[i+1][1])*(points[i][2] + points[i+1][2])
        n[ii][1] += (points[i][2] - points[i+1][2])*(points[i][0] + points[i+1][0])
        n[ii][2] += (points[i][0] - points[i+1][0])*(points[i][1] + points[i+1][1])
    n[ii] = n[ii] / np.sqrt((n[ii] ** 2).sum(-1))

    a, b, c = n[ii]
    d = a * points[0][0] + b * points[0][1] + c * points[0][2]

    zp = np.zeros(len(points))

    x = points[:, 0]
    y = points[:, 1]
    z = points[:, 2]

    for i in range(0, len(points)):
        # Calculate the sigma value - sort of an error
        s = a * x[i] + b * y[i] + c * z[i] - d
    
        # Calculate the z' according to the plane
        zp[i] = - (a * x[i] + b * y[i] - d) / c

        print(ii, ", ", x[i], ", ", y[i], ", ", zp[i])

