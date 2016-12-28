import numpy as np
import matplotlib.pyplot as plt

nx = 41
dx = 2.0/(nx-1)
nu = 0.3
nt = 20
sigma = 0.2
dt = sigma*dx**2/nu

u = np.zeros(nx)
x = np.linspace(0, 2.0, nx)
u[:] = 1
u[int(.5 / dx):int(1 / dx + 1)] = 2

plt.plot(x, u)

for n in range(nt):
    u = u + nu*dt/dx**2*(u[range(1, nx)+[0]]-2*u+u[[nx-1]+range(0, nx-1)]) \
        - u*(u[:]-u[np.arange(nx)-1])*dt / dx

plt.plot(x, u)
plt.ylim(0, 3)
plt.show()
