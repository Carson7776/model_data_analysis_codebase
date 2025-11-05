"velocity information"
"last updated on 02/08/2024"
# _contents.0, nxnz.o, mesh.o, vel.0 flac.vts are required

#this code is written to provide calculation and show  velocity of an given model
#which includes surface velocity, etc. 

import os
import sys
import math
sys.path.append("C:/Users/carosn/Desktop/flac.py")

import flac
fl=flac.Flac()
import numpy as np
import matplotlib.pyplot as plt

def read_data(vx,vz, nfl):
    for i in range(1,nfl+1):  
      vx, vz = fl.read_vel(i)
      x,z = fl.read_mesh(i)
      survel(vx,vz, i,x) #plot the surface velocity
      
    return vx,vz

def survel(vx,vz, i,x):    #survel is short for surface velocity

    velx0 = vx[:,0]
    dsx = x[:,0]
    draw(velx0,dsx,i) #graph the result of survel
    return 

def draw(velx0,dsx,i):
    
    plt.title(f'velocity_on_the_surface_time_step_{i}') #graph result 
    plt.xlabel("width(km)")
    plt.ylabel("velocity(cm/s)")
    plt.plot(dsx,velx0)
    plt.savefig(f'C:/Users/carosn/Desktop/model_220/velocity/velocity_on_the_surface_timesetep_{i}', dpi = 300)
    plt.clf()
    return

#main
vx = 0
vz = 0
nfl = int(input('number of flac = '))
read_data(vx,vz, nfl) #read data and plot all of it on a graph
