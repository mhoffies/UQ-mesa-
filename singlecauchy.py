#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import cauchy

fig, ax = plt.subplots(1,1)
mean,var,skew,kurt = cauchy.stats(moments='mvsk')

x = np.linspace(cauchy.ppf(0.01),cauchy.ppf(0.99),1000000)
y = np.linspace(0.5,6.5,100)
ons = np.ones(100)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

#2c0032
ax.plot(x, cauchy.pdf(x, loc=0.53432, scale=0.0382 ), color='#6ca6cd', lw=3, label='$\Delta=0.0382, \sigma=0.0079$')
#ax.plot(x, cauchy.pdf(x, loc=0.55334, scale=0.0102 ), color='#8c07ee', lw=3, label='$\Delta=0.0102$')
#ax.plot(x, cauchy.pdf(x, loc=0.54545, scale=0.0024 ), color='#ad1927', lw=3, label='$\Delta=0.0024$')
#ax.plot(x, cauchy.pdf(x, loc=0.59613, scale=0.0988 ), color='#f5ce00', lw=3, label='$\Delta=0.0988$')
#ax.plot(x, cauchy.pdf(x, loc=0.53622, scale=0.0349 ), color='#ff6600', lw=3, label='$\Delta=0.0349$')

ax.plot(0.580*ons,y,'-',lw=1,color='#474747')
ax.plot(0.488*ons,y,'-',lw=1,color='#474747')
ax.plot(0.588*ons,y,'--',lw=1,color='#474747')
ax.plot(0.480*ons,y,'--',lw=1,color='#474747')
ax.plot(0.596*ons,y,':',lw=1,color='#7f7f7f')
ax.plot(0.472*ons,y,':',lw=1,color='#7f7f7f')
x1 = np.linspace(0.488,0.580,100)
x2 = np.linspace(0.480,0.588,100)
x3 = np.linspace(0.472,0.596,100)
ax.plot(x1,5*ons,'-',color='r')
ax.plot(x2,3*ons,'--',color='r')
ax.plot(x3,ons,':',color='r')
#ax.plot(x2,5.*ons,lw=1,'r--')
#ax.plot(x3,4.*ons,lw=1,'r--')

ax.legend(loc='best',frameon=False)
ax.set_xlim([0.4,0.68])
ax.set_ylim([0,9])

plt.text(0.495,5.2,'$[y+(\Delta+\sigma),y-(\Delta+\sigma)]$',fontsize=11)
plt.text(0.4925,3.2,'$[y+(\Delta+2\sigma),y-(\Delta+2\sigma)]$',fontsize=11)
plt.text(0.4925,1.2,'$[y+(\Delta+3\sigma),y-(\Delta+3\sigma)]$',fontsize=11)

#ax.set_title('Cauchy PDF')

#plt.text(-2.0,0.2,'$\Delta=0.53$',fontsize=12)
#plt.text(-0.4,0.27,'$\Delta=0.55$',fontsize=12)
#plt.text(0.5,0.3,'$\Delta=0.54$',fontsize=12)
#plt.text(1.7,0.25,'$\Delta=0.59$',fontsize=12)

#plt.text(-11,0.0,'$f(z) = \\frac{\Delta}{\pi(z^2 + \Delta^2)}$', fontsize=20)

fig.savefig('cauchy2.eps',format='eps',dpi=1000)
plt.show()
