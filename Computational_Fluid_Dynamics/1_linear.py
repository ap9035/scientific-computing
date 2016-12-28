import numpy as np
import matplotlib.pyplot as plt

nx = 41
dx = 2.0/(nx-1)
dt = 0.025
t = 25*dt
c = 1

u = np.zeros(nx)
x = np.linspace(0, 2.0, nx)
u[int(.5 / dx):int(1 / dx + 1)] = 2

plt.plot(x, u)

for tt in np.arange(0, t, dt):
    plt.plot(x, u, label="t={}".format(tt))
    u = u-c*(u[:]-u[np.arange(nx)-1])*dt/dx

plt.ylim(0, 3)
plt.legend()
plt.show()
