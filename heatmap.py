import matplotlib.pyplot as plt
import numpy as np


x, y = np.meshgrid(np.linspace(-30, 30, 100), np.linspace(-30, 30, 100))
r=np.sqrt(x**2+(y)**2)
theta=np.arctan(y/x)
z=r
angle_min = np.deg2rad(-45)
angle_max = np.deg2rad(45)


# Create mask for sector
sector_mask = (r < 20) & (y>0) & (x<0) 



fig, ax = plt.subplots()

c = ax.pcolormesh(x, y,0.5*r*sector_mask,cmap='jet')
plt.title(' Radiation pattern with beamwidth of 90°')


fig.colorbar(c, ax=ax)
plt.show()
