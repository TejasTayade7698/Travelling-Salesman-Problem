import random
import math
import matplotlib.pyplot as plt
import numpy as np
import math
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

#reference of random points on cicrcle code: https://stackoverflow.com/questions/30564015/how-to-generate-random-points-in-a-circular-distribution
# radius of the circle
circle_r = 5
# center of the circle (x, y)
circle_x = 2
circle_y = 2
pointx=[]
pointy=[]
s=[]
o=[]
p=[]
q=[]
r=[]
# random radius
r = circle_r * math.sqrt(random.random())

for i in range (0,600):
    # random angle
    alpha = 2 * math.pi * random.random()

    # calculating coordinates
    f = r * math.cos(alpha) + circle_x
    k = r * math.sin(alpha) + circle_y

    #print("Random point", (x, y))

    pointx.append(f)
    pointy.append(k)

something=0
max_dist=0
min_dist = 3700
timeout_start = time.time()
timeout = 100   # [seconds]
while time.time() < timeout_start + timeout:
    pointx,pointy = shuffle(pointx,pointy)
    something+=1
    s.append(something)
    dist = eucdist(pointx,pointy)

    if dist<min_dist:
        min_dist=dist
        o.append(min_dist)
        p.append(something)

    if dist>max_dist:
        max_dist=dist
        q.append(something)

    test = 0
    if test == timeout:
        break
    test -= 1
print(dist)
plt.plot(pointx,pointy)
print("total iterations=",s[-1] )
print("Shortest distance is" , p)

plt.show()
