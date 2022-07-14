from math import sin,cos,pi
import numpy as np

a,b,d = map(int,input().split())

deg = np.deg2rad(d)

cos = np.cos(deg)
sin = np.sin(deg)
x = a*cos - b*sin
y = b*cos+a*sin
print(x,y)