"temperature information"
"last updated in 03/01/2024"

#this file must exit in the file of targeted folder
#to draw topo, _contents.0, nxnz.o, mesh.o, flac.vts are required

#this code is to show the tempurture variation 
#which includes the temperature per depth on certain path

import sys
import math
import os
sys.path.append("C:/Users/carosn/Desktop/flac.py") #fdirect path of flac
import flac
fl=flac.Flac()
import numpy as np
import matplotlib.pyplot as plt

def temp_per_depth(T):
    x,z = fl.read_mesh(1)
    plc = int(input('where ?'))
    plc,nd = nd_to_km(plc)
    t = T[nd,:]
    znd = z[nd,:]
    draw(znd,t) #plot temp
    return

def nd_to_km(plc):       #convert node to kilometer
    x,z = fl.read_mesh(1)
    for i in range(1,752):
        a = x[i,0]-plc 
        if (abs(a) <= 2):
            b = x[i,0] 
            nd =  i      #nd stands for node
            print(b,"closet km =",x[i,0],"on node =", i)
    return plc, nd
def draw(znd,t):
    #graph result
    plt.title("temperature")
    plt.xlabel("temperature(C)")
    plt.ylabel("depth(km)")
    plt.plot(t,znd)
    plt.savefig(f"C:/Users/carosn/Desktop/model_220/temp", dpi = 300)
    
#main
T = fl.read_temperature(1) # time step = 1, t= 0
#show temperature per depth on a specific place
temp_per_depth(T)
