"force on the boundary - timerelationship"
import numpy as np
import matplotlib.pyplot as plt
"setting param"


"writing file"
forc_GRm11_r01 = np.load('GRm11_r01_forc.npy')
forc_GRm12_r02 = np.load('GRm12_r02_forc.npy')
forc_GRm13_r03 = np.load('GRm13_r03_forc.npy')





"GRm11"
GRm11_time_forc= forc_GRm11_r01[:,[1,3]]
GRm12_time_forc= forc_GRm12_r02[:,[1,3]]
GRm13_time_forc= forc_GRm13_r03[:,[1,3]]

"extract time from GRm**_time, with fixed threshold(t = 0.01Myr)"
#inorder to compair different model with the same timestep
#because the size of the time array of orginal data is different for each mode
threshold = float(0.01) #10 kyr

GRm11_current_time = GRm11_time_forc[0,0]
GRm12_current_time = GRm12_time_forc[0,0]
GRm13_current_time = GRm13_time_forc[0,0]

GRm11_time_forc_r = []
GRm12_time_forc_r = []
GRm13_time_forc_r = []

"getting 1st vaule > threshold"
for row in GRm11_time_forc:
    
    if row[0] >= GRm11_current_time:
        
        time_round =np.round(row[0]/threshold) * threshold
        GRm11_time_forc_r.append([time_round,row[1]])    
        GRm11_current_time = GRm11_current_time + threshold 
        
for row in GRm12_time_forc:
    
    if row[0] >= GRm12_current_time:
        
        time_round =np.round(row[0]/threshold) * threshold
        GRm12_time_forc_r.append([time_round,row[1]])    
        GRm12_current_time = GRm12_current_time + threshold 
        
for row in GRm13_time_forc:
    
    if row[0] >= GRm13_current_time:
        
        time_round =np.round(row[0]/threshold) * threshold
        GRm13_time_forc_r.append([time_round,row[1]])    
        GRm13_current_time = GRm13_current_time + threshold 


GRm11_time_forc_r = np.array(GRm11_time_forc_r, dtype = float)  #this code can be written in a cleaner fashio        
GRm12_time_forc_r = np.array(GRm12_time_forc_r, dtype = float)
GRm13_time_forc_r = np.array(GRm13_time_forc_r, dtype = float)        
         
"GRm11"

plt.plot(GRm11_time_forc_r[:,0],GRm11_time_forc_r[:,1], color='r')
"GRm12"

plt.plot(GRm12_time_forc_r[:,0],GRm12_time_forc_r[:,1], color='b')

"GRm13"
plt.plot(GRm13_time_forc_r[:,0],GRm13_time_forc_r[:,1], color='g')




