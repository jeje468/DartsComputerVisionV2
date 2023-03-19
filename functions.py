import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.interpolate import interp2d

xAndDiff = []
yAndDiff= []
datas = []

with open('testData2.txt') as f:
    lines = f.readlines()
    for line in lines:
        data = line.split(", ")
        detectedDist = math.sqrt(float(data[2])**2 + float(data[4])**2)
        actualDist = math.sqrt(float(data[3])**2 + float(data[5])**2)
        datas.append((float(data[2]), float(data[4]), actualDist - detectedDist))
        xAndDiff.append((float(data[2]), float(data[3]), round(float(data[3]) - float(data[2]), 2)))
        yAndDiff.append((float(data[4]), float(data[5]), round(float(data[5]) - float(data[4]), 2)))

# xAndDiff = sorted(xAndDiff)
# yAndDiff = sorted(yAndDiff)

detectedX = list(zip(*xAndDiff))[0]
actualX = list(zip(*xAndDiff))[1]
diffX = list(zip(*xAndDiff))[2]

detectedY = list(zip(*yAndDiff))[0]
actualY = list(zip(*yAndDiff))[1]
diffY = list(zip(*yAndDiff))[2]

diff = list(zip(*datas))[2]


# plt.plot(detectedX, actualX)
# plt.plot(detectedY, actualY)
# fig = plt.figure(figsize=(4,4))
# ax = fig.add_subplot(111, projection='3d')

# for point in xAndDiff:
#     #plt.plot(point[0], point[1], marker="o", markersize=20, markeredgecolor="red", markerfacecolor="green")
#     ax.scatter(point[0], point[1], point[2])

# figure, axis = plt.subplots(2)
# points = arr = np.arange(0.0, 21.0, 0.1)
# interp_func_x = np.interp(points, detectedX, actualX)
# interp_func_y = np.interp(points, detectedY, actualY)
# axis[0].plot(detectedX, actualX, 'o')
# axis[0].plot(points, interp_func_x, '-x')
# axis[1].plot(detectedY, actualY, 'o')
# axis[1].plot(points, interp_func_y, '-x')

interp_func = interp2d(detectedX, detectedY, diff, kind='cubic')
x_interp = np.arange(-21.0, 21.0, 0.1)
y_interp = np.arange(-21.0, 21.0, 0.1)
z_interp = interp_func(x_interp, y_interp)
test = interp_func(17.88, -0.44)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X, Y = np.meshgrid(x_interp, y_interp)
ax.plot_surface(X, Y, z_interp)
plt.show()
