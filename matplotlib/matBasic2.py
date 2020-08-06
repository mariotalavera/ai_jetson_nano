# Force matplotlib to not use any Xwindows backend.
# https://stackoverflow.com/questions/4706451/how-to-save-a-figure-remotely-with-pylab/4706614#4706614
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

# Create an image to store our visual
fig=plt.figure()

# Create arrays to plot
# x=np.arange(-4,4,.1)
x=np.linspace(0,2*np.pi,50)
# y=np.square(x)
y=np.sin(x)
y2=np.cos(x)
# y3=np.square(x-2)-2
# y3=x*x-2

# Plot settings
plt.grid(True)
plt.title('My Graph Title')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
# plt.axis([0,5,2,11])

# Plot arrays
plt.plot(x,y,'b-o',linewidth=3,markersize=7,label='Sin(x)')
plt.plot(x,y2,'y-^',linewidth=3,markersize=7,label='Cos(x)')
# plt.plot(x,y3,'y:o',linewidth=3,markersize=7,label='third line')
plt.legend(loc='upper right')

# Instead of show (plt.show), save to image instead.
fig.savefig('matBasic2.png')

# On LittleFoot, this would've sfficed
# plt.show()
