import matplotlib.pyplot as plt
import numpy as np
from shapes import Shape

# Data for plotting
# t = np.arange(0.0, 4.0, 0.01)
# s = 1 + np.sin(1 * np.pi * t)

t = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
s = [0, 2, 4, 6, 10, 10, 12, 14, 16, 4]

shape1 = Shape(t, s)

t = np.arange(0.0, 2.0 * np.pi, 0.01)
y = np.sin(t)
x = np.cos(t)

shape2 = Shape(x, y)

t = np.arange(0.0, 2.0 * np.pi, 0.01)
y = np.sin(t)
x = np.cos(t) + 7

shape3 = Shape(x, y)

x = []
y = []
for i in range(200):
    x.append(i / 100)
    y.append((i / 100) ** 2)
shape4 = Shape(x, y)

x = [20, 21, 22, 24, 26, 28, 30, 31, 32]
y = [20, 25, 21, 22, 22, 22, 21, 25, 20]
shape5 = Shape(x, y)

# shape6 = Shape([5,5], [1,5])
# shape7 = Shape(
#        [5,1],
#        [5,1])


fig, ax = plt.subplots()
# shape1.paint(ax)
# shape2.paint(ax)
# shape3.paint(ax)
# shape4.paint(ax)
shape5.paint(ax)
# shape6.paint(ax)
# shape7.paint(ax)


# ax.scatter(t,s, c="#ebe783")
ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='Hahahaha')
# ax.grid()

fig.savefig("test.png")
plt.show()
