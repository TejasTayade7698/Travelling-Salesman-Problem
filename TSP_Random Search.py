import numpy  as np
import matplotlib.pyplot as plt
import math
import random
import time

def eucdist(x,y):
    l=0
    for i in range(len(x)-1):
        dist=np.sqrt(((x[i]-x[i+1])**2 + (y[i]-y[i+1])**2))
        l=l+dist
    return l

def shuffle(x,y):
    c = list(zip(x, y))
    random.shuffle(c)
    x, y = zip(*c)
    return x, y

data = np.loadtxt('tsppts.txt')

x = data[:, 0]
y = data[:, 1]
x=np.append(x, x[0])
y=np.append(y, y[0])
a=[]
b=[]
h=[]
c=[]
d=[]
count=0
max_dist=0
min_dist = 600
timeout = 1200   # [seconds]
timeout_start = time.time()
while time.time() < timeout_start + timeout:
    x,y = shuffle(x,y)
    count+=1
    a.append(count)
    dist = eucdist(x,y)

    if dist<min_dist:
        min_dist=dist
        b.append(count)
        h.append(min_dist)

    if dist>max_dist:
        max_dist=dist
        d.append(count)
        c.append(max_dist)
    test = 0
    if test == timeout:
        break
    test -= 1


yerr = np.linspace(2, 3, len(b))

print("Total Number of iterations=", a[-1])
print("Total iterations for minimum path=", b[-1])
print("Total iterations for maximum path=", d[-1])
print("The Minimum distance is:" , min_dist)
print("The Maximum distance is:", max_dist)
reci_h=np.reciprocal(h)
reci_c=np.reciprocal(c)

fig, axis = plt.subplots(2)

plt.title("Path & Learning Curve of shortest and longest path: Random search")
axis[0].plot(x,y)
axis[1].plot(b,h, "-g", label="Minimum Distance")
plt.gca().invert_yaxis()
plt.errorbar(b,h,uplims = True, yerr = yerr, lolims = True, label="Errorbar min. dist for shortest path")

yerr = np.linspace(2, 3, len(d))
axis[1].plot(d,c, "-r", label="Maximum Distance")
plt.errorbar(d,c,uplims = True, yerr = yerr, lolims = True, label="Errorbar max. dist for longest path")

plt.ylabel("Length of path")
plt.xlabel("Iterations")
plt.legend()

fig.tight_layout()
plt.show()
