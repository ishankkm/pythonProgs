'''
Created on Mar 27, 2018
@author: ishank

x(t) = (R+r)*cos((r/R)*t) - a*cos((1+r/R)*t)
y(t) = (R+r)*sin((r/R)*t) - a*sin((1+r/R)*t)

'''
import math

n = 16
rad = 0.0
x_t, y_t = [], []
R, r, a = 8, 1, 4
lat, lon = 34.021274 , -118.289267

while rad < n * math.pi:

    x_t.append(lat + ((R + r) * math.cos((r / R) * rad) - a * math.cos((1 + r / R) * rad)))
    y_t.append(lon + ((R + r) * math.sin((r / R) * rad) - a * math.sin((1 + r / R) * rad)))
    rad += 0.01

with open('coord.txt', 'w') as f:

    for i in range(len(x_t)):
        f.write('          %f,%f,1.\n' % (y_t[i], x_t[i]))

