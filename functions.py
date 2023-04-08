import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.interpolate import interp2d, griddata
import scipy.ndimage.filters

def calculateAngle(a, b):
    dotProduct = a * 10 + b * 0
    modOfVector1 = math.sqrt(a * a + b * b) * math.sqrt(10 * 10 + 0 * 0) 
    angle = dotProduct/modOfVector1
    angle = math.degrees(math.acos(angle))

    return angle

detectedCoordinates = []
detectedX = []
detectedY = []
distDiff = []
angleDiff = []
xDiff = []
yDiff = []

with open('testData2.txt') as f:
    lines = f.readlines()
    for line in lines:
        data = line.split(", ")
        detectedDist = math.sqrt(float(data[2])**2 + float(data[4])**2)
        actualDist = math.sqrt(float(data[3])**2 + float(data[5])**2)
        detectedX.append(float(data[2]))
        detectedY.append(float(data[4]))
        detectedCoordinates.append([float(data[2]), float(data[4])])
        xDiff.append(float(data[3])- float(data[2]))
        yDiff.append(float(data[5])- float(data[4]))
        distDiff.append(actualDist - detectedDist)
        angleDiff.append(calculateAngle(float(data[3]), float(data[5])) - calculateAngle(float(data[2]), float(data[4])))

interp_func_dist = interp2d(detectedX, detectedY, distDiff, kind='cubic')
interp_func_ang = interp2d(detectedX, detectedY, angleDiff, kind='cubic')
interp_func_x = interp2d(detectedX, detectedY, xDiff, kind='cubic')
interp_func_y = interp2d(detectedX, detectedY, yDiff, kind='cubic')

x_interp = np.arange(-21.0, 21.0, 0.1)
y_interp = np.arange(-21.0, 21.0, 0.1)
z_interp = interp_func_dist(x_interp, y_interp)
test1 = interp_func_dist(-9.42, -5.49)
test2 = interp_func_ang(2.34, 5.75)

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# X, Y = np.meshgrid(x_interp, y_interp)
# ax.plot_surface(X, Y, z_interp)

# import numpy as np
# from scipy.interpolate import griddata

# z_interp = griddata((detectedX, detectedY), angleDiff, (1.0, 2.0), method='cubic')

# # Print the interpolated angle difference
# print('Interpolated angle difference at ({}, {}) = {}'.format(1.0, 2.0, z_interp))

x_grid = np.linspace(min(detectedX),max(detectedX), 100)
y_grid = np.linspace(min(detectedY),max(detectedY), 100)
xx, yy = np.meshgrid(x_grid, y_grid)
dist_interp = griddata(detectedCoordinates, distDiff, (xx, yy), method='cubic')
angle_interp = griddata(detectedCoordinates, distDiff, (xx, yy), method='cubic')
test = griddata(detectedCoordinates, distDiff, (-9.42, -5.49), method='linear')

sigma = 1
smoothed = scipy.ndimage.filters.gaussian_filter(dist_interp, sigma)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X, Y = np.meshgrid(x_grid, y_grid)
dist_surf = ax.plot_surface(X, Y, dist_interp)
smoothed_surf = ax.plot_surface(X, Y, smoothed)

dist_surf.set_facecolor((0.2, 0.5, 0.8))
smoothed_surf.set_facecolor((0.5, 0.8, 0.2))

data = np.genfromtxt("testData3.txt", delimiter=", ")
equal = np.sum(data[:,0] == data[:,1])
print(equal)

plt.show()
