"topo information"
"last updated in 02/03/2024"
#this file must exit in the file of targeted folder
#to draw topo, _contents.0, nxnz.o, mesh.o, flac.vts are required

#this code is to calculate and show the topo of an given flac file
#which includes global, local relief, and local maxium, minmun heights(mountain & trench)

import sys
import math
import os
sys.path.append("C:/Users/carosn/Desktop/flac.py") #fdirect path of flac
import flac
fl=flac.Flac()
import numpy as np
import matplotlib.pyplot as plt

def topo_spf(x,z):
    
    time_step = int(input('time_step = '))  #timestep start from 1,  
    x,z = fl.read_mesh(time_step)           #enter the time step you want to see
    rlf = z[:,0] #relief in km
    dsx = x[:,0] #real distance in km
    #graph result
    plt.title("initial topography")
    plt.xlabel("width(km)")
    plt.ylabel("depth(km)")
    plt.plot(dsx, rlf)
    plt.savefig(f"C:/Users/carosn/Desktop/model_220/topo_initial", dpi = 300)

    return 
def topo_chng(x,z):
    
    lth = int(input('how many flac files?'))
    
    for i in range(1,lth+1):
               
        x,z = fl.read_mesh(i)
        rlf = z[:,0]
        dsx = x[:,0]
        
        plt.title(f'topography_time_step_{i}') #graph result 
        plt.xlabel("width(km)")
        plt.ylabel("depth(km)")
        plt.plot(dsx, rlf)
        plt.savefig(f'C:/Users/carosn/Desktop/model_220/timestep/time_step_{i}', dpi = 300)
        plt.clf()  #clear the old plot

    return
def topo_local(x,z):
    
    lths = int(input('from which time_step?')) #lenth start
    lthe = int(input('to which time_step?')) #lenth end
    xs = int(input('from where?(node)')) #x start
    xe = int(input('to where?(node)'))    #x end   
    for i in range(lths, lthe+1):
        
        x,z = fl.read_mesh(i) 
        
        lcrlf = z[xs:xe,0] #local relief
        lcdsx = x[xs:xe,0] #local width
        lcmx = np.max(lcrlf)  #find the highest point and lowest point in the given region
        lcmi = np.min(lcrlf)
        vrdis = abs(lcmx-lcmi) #vertical displacement of from the lowest point to the height
        indxmx = np.argmax(lcrlf)
        indxmi = np.argmin(lcrlf)
        
        print("trench to heightest point = ",round(vrdis*1000), "(m)")
        
        plt.title(f'local_topography_time_step_{i}') #graph result 
        plt.xlabel("width(km)")
        plt.ylabel("depth(km)")
        plt.plot(lcdsx, lcrlf)
        plt.scatter(lcdsx[indxmx],lcmx, label ='max') #show local maximun
        plt.scatter(lcdsx[indxmi],lcmi, label = 'min')#show local minimun
        plt.text(lcdsx[indxmx],lcmx, f'{lcmx}(km)',)
        plt.text(lcdsx[indxmi],lcmi,f'{lcmi}(km)')
        plt.savefig(f'C:/Users/carosn/Desktop/model_220/local_relief/local_relief_time_step_{i}', dpi = 300)
        plt.clf()  #clear old plot 
    return    

x,z = fl.read_mesh(1) #initial time step
nxnz = x.shape # number of nodes  for given model nx, nz

nx = nxnz[0] #number of node for x 
nz = nxnz[1] #number of node for z 

print("number of node")
print("nx = ",nx,"nz = ",nz)


#change in topopraphy with each time step(total timestep)
#topo_chng(x,z)
#topo for specific
#topo_spf(x,z)
#topo for local reigon
topo_local(x,z)







    

