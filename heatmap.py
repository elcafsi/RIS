

import matplotlib.pyplot as plt
import numpy as np

# generate 2 2d grids for the x & y bounds
x, y = np.meshgrid(np.linspace(-5, 5, 100), np.linspace(-5, 5, 100))
r1=np.sqrt((x-3)**2+(y+3)**2)
r2=np.sqrt((x-2)**2+(y-2)**2)
z1 = np.exp(-.5*r1)
z2 = np.exp(-.2*r2)
z=z1+z2
# x and y are bounds, so z should be the value *inside* those bounds.
# Therefore, remove the last value from the z array.

z_min, z_max = -np.abs(z).max(), np.abs(z).max()

fig, ax = plt.subplots()

c = ax.pcolormesh(x, y, z, cmap='jet')
ax.set_title('two Omnidirectional sources ')
# set the limits of the plot to the limits of the data

fig.colorbar(c, ax=ax)
fig.savefig('Attenuation_two_sources3.png', dpi=fig.dpi)
plt.show()
