# Force matplotlib to not use any Xwindows backend.
# https://stackoverflow.com/questions/4706451/how-to-save-a-figure-remotely-with-pylab/4706614#4706614
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

# Create an image to store our visual
fig=plt.figure()

# Create arrays to plot
x=[1,2,3,4]
y=[3,5,7,9]
z=[10,8,6,4]

# Plot settings
plt.grid(True)
plt.title('My Graph Title')
plt.xlabel('My X Label')
plt.ylabel('My Y Label')
plt.axis([0,5,2,11])

# Plot arrays
plt.plot(x,y,'b-o',linewidth=3,markersize=7,label='first line')
plt.plot(x,z,'r:o',linewidth=3,markersize=7,label='second line')
plt.legend(loc='lower right')

# Instead of show (plt.show), save to image instead.
fig.savefig('matBasic1.png')

# On LittleFoot, this would've sfficed
# plt.show()
