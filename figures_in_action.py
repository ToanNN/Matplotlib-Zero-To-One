import matplotlib.pyplot as plt
import matplotlib.lines as lines
import numpy as np

fig = plt.figure(layout ='constrained', facecolor='lightskyblue')
fig.suptitle('Figure')

figL, figR = fig.subfigures(1,2)
figL.set_facecolor('red')
axL = figL.subplots(2,1, sharex = True)
axL[1].set_xlabel('x [m]')
figL.suptitle('Left subfigure')
figR.set_facecolor('paleturquoise')
axR = figR.subplots(1, 2, sharey=True)
axR[0].set_title('Axes 1')
figR.suptitle('Right subfigure')

plt.show()