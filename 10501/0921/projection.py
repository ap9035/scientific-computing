import math


def proj(v0, theta, t):
    x = v0*math.cos(theta)*t
    y = v0*math.sin(theta)*t-0.5*9.81*t**2
    return x, y


print proj(10, math.pi/6, 5)
