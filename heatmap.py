

import matplotlib.pyplot as plt
import numpy as np


x, y = np.meshgrid(np.linspace(-5, 5, 100), np.linspace(-5, 5, 100))
r1=np.sqrt((x-3)**2+(y+3)**2)
r2=np.sqrt((x-2)**2+(y-2)**2)
z1 = np.exp(-.5*r1)
z2 = np.exp(-.2*r2)
z=z1+z2


z_min, z_max = -np.abs(z).max(), np.abs(z).max()

fig, ax = plt.subplots()

c = ax.pcolormesh(x, y, z, cmap='jet')
ax.set_title('two Omnidirectional sources ')


fig.colorbar(c, ax=ax)
fig.savefig('Attenuation_two_sources3.png', dpi=fig.dpi)
plt.show()
