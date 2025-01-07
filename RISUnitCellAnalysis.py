import numpy as np
import matplotlib.pyplot as plt
pi=np.pi
c=1*10**-12
f0=5.8*10**9
l=1/(f0**2*4*pi**2*c)
f=np.linspace(1,8,100)
theta=np.linspace(-pi,pi,100)

def impedance(frequency):
    Zl=(1j*l*2*pi*frequency)
    Zc= (1/(1j*c*2*pi*frequency))
    return (Zl*Zc)/(Zl+Zc)
FreeSpaceTE=377*np.cos(theta)
FreeSpaceTM=377/np.cos(theta)
gammaTM = (FreeSpaceTE-impedance(f*10**9))/(FreeSpaceTE+impedance(f*10**9))

gammaTE = (FreeSpaceTM-impedance(f*10**9))/(FreeSpaceTM+impedance(f*10**9))
plt.subplot(1,2,1)
plt.figure
plt.plot(f,10*np.log10(np.abs(np.real(gammaTE))),f,10*np.log10(np.abs(np.real(gammaTM))))
plt.xlabel("Frequency Ghz")
plt.ylabel("Amplitude S11")
plt.legend(['TE','TM'])
plt.title('Amplitude S11 Unit Cell ')
plt.subplot(1,2,2)
plt.figure
plt.plot(f,np.rad2deg(np.imag(gammaTE)),f,np.rad2deg(np.imag(gammaTM)))
plt.xlabel("Frequency Ghz")
plt.ylabel("Phase S11")
plt.legend(['TE','TM'])
plt.title('Phase S11 Unit Cell ')
plt.show()

