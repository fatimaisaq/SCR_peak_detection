#IThis appendix contains the algorithm used to produce 
#Ithe output and the demography of the participants.
#IFor the algorithm, the data from both sensors 
#Iare exported to excel for preprocessing to produce a 
#Idataset with annotated events which includes fixation index, 
#Ifixation points, fixation duration and SCR . 
#IThe dataset is then called into the algorithm using short term time intervals.
 #Import both the SCR  and corresponding fixation points
# from the sync data file
# note before import of the datasets the Synchronized SCR and Eye gaze undergoes
# a form of preprocessing
import fixationSCR
from fixationSCR import Dataset    
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from PIL import Image
import glob, os
from pylab import *
    
data = Dataset('c:\Documents\NewPart\PP2.xlsx','r')
dataF = Dataset('c:\Documents\NewPart\FixationP2.xlsx','r')

# enter specified time interval, each timestamp for SCR (eda) is equivalent to 
# 3x the eye-gaze timestamp, this can easily be adapted in a window based model.

for i in  mslice[1:n]:
 for j in mslice[1:m]:
x = Fixation.MappedFixationPointX(mslice[i:i+1]);
y = Fixation.MappedFixationPointY(mslice[i:i+1]);
eda = data.eda(mslise[j:j+1]);
    print (x,y,eda,j,i)
    
peaks,time = findpeaks(data.eda, 0.03);
# Refer to the function peak_detect
# import time slice for annotations
import time  # this is done, rendering A real real time
D = data.AOI(mslice[j:j + 1])
A = D(time(mslice[1:end]))
label2 = cellstr(A)

Z = data.Data1(mslice[j:j + 1])
F = Z(time(mslice[1:end]))
label3 = cellstr(F)

import pylab as pl
from mpl_toolkits.mplot2d import Axes2D

 subplot(2,1,1)
    x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
    y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5

pl.figure(2, figsize=(8, 6))
pl.clf()

# Plot the SCR in sync with an imported webpage in image or url form
pl.scatter(arrag(peaks)[:, 0], peaks(array)[:, 1], c=Y, cmap=pl.cm.Paired, color='red')
pl.scatter(array(minindex)[:,0], array(minindex)[:,1], color='green')

# Annotate the peaks with corresponding AOI and EVents from the eye gaze data in sync with the SCR
ax.annotate(label2, xy=(2, 1), xytext=(3, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )

ax.annotate(label3, xy=(3, 1), xytext=(4, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
ax.set_ylim(-2,2)
plt.show()

pl.xlabel('Time(sec)')
pl.ylabel('Skin Conductance Response')
pl.xlim(x_min, x_max)
pl.ylim(y_min, y_max)
pl.xticks(())
pl.yticks(())

subplot(2,1,2)
import Image
myImage = Image.open("iGoogle.png");
myImage.show();
set(gcf, mstring('color'), mstring('cyan'))

xi = x(1)
yi = y(1)
A1 = mslice[1:107]
xImg = linspace(min(x), max(x), size(myImage, 2))
yImg = linspace(min(y), max(y), size(myImage, 1))
image(xImg, yImg, myImage, mstring('CDataMapping'), mstring('scaled'))
hold(mstring('on'))

h = plot(xi, yi, mstring('mo'), xi, yi, mstring('r--'), mstring('MarkerEdgeColor'), mstring('k'), mstring('MarkerFaceColor'), mstring('r'), mstring('MarkerSize'), 15, mstring('XDataSource'), mstring('xi'), mstring('YDataSource'), mstring('yi'), mstring('color'), mstring('r'))

ylabel(mstring('MappedFixationPointY'))
xlabel(mstring('MappedFixationPointX'))

for i in mslice[1:length(A1)]:
    yi = y(mslice[1:i])
    xi = x(mslice[1:i])
    edai = eda(mslice[1:i])
    scli = scl(mslice[1:i])
    baselinei = baseline(mslice[1:end])
    indxi = indx(mslice[1:end])
    print (edai,scli,baseline,indxi) # displays the SCR, SCL and baseline for each individual data intervals entered

    htext = text(x(i), y(i), mcat([mstring(' '), num2str(A1(i)), mstring('')]), mstring('Color'), mcat([0, 0, 0]), mstring('FontSize'), 8, mstring('HorizontalAlignment'), mstring('center'), mstring('VerticalAlignment'), mstring('middle'))

    set(htext, mstring('Position'), mcat([x(i), y(i)]))
    savefig('iGoogle1.png',optimize=True,quality=100)
    starttime = time.time()         # this is the initial start time
t = 0                           # this is the relative start time
 
while(t < 16.0):                 #limited ourselves to 16 seconds in this particular case.
                                # this is set to (True) for contiuous loop
    t = time.time() - starttime # determine time interval for simulation
    y = sin(data.eda)*sin(t)        # function for simulation of the SCR signal                       
 quit()
  draw()  
