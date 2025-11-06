"force on the boundary - timerelationship"
import numpy as np
import matplotlib.pyplot as plt
"setting param"


"writing file"
#forc_GRm11_r01 = np.load('GRm11_r01_forc.npy')
forc_GRm12_r02 = np.load('GRm12_r02_forc.npy')
#forc_GRm13_r03 = np.load('GRm13_r03_forc.npy')


"extract for foc_np array"
#GRm11_time = forc_GRm11_r01[:,1]
#GRm12_time = forc_GRm12_r02[:,1]
#GRm13_time = forc_GRm13_r03[:,1]


"GRm11"
#GRm11_force_l = forc_GRm11_r01[:,2]  
#GRm11_force_r = forc_GRm11_r01[:,3]
GRm12_time_forc= forc_GRm12_r02[:,[1,3]]

"extract time from GRm**_time, with fixed threshold(t = 0.01Myr)"
#inorder to compair different model with the same timestep
#because the size of the time array of orginal data is different for each mode
threshold = float(0.01) #10 kyr
current_time = GRm12_time_forc[0,0]
time_forc_r = []

"getting 1st vaule > threshold"
for row in GRm12_time_forc:
    
    if row[0] >= current_time:
        
        time_round =np.round(row[0]/threshold) * threshold
        time_forc_r.append([time_round,row[1]])    
        current_time = current_time + threshold 

time_forc_r = np.array(time_forc_r, dtype = float)  #this code can be written in a cleaner fashio        

        
         
    
     
    

"GRm12"
#GRm12_force_l = forc_GRm12_r02[:,2]  
#GRm12_force_r = forc_GRm12_r02[:,3]

"GRm13" 
#GRm13_force_l = forc_GRm13_r03[:,2]  
#GRm13_force_r = forc_GRm13_r03[:,3]

"GRm11"
#plt.plot(time, GRm11_force_l, label='GRm11 Left', linestyle='-', color='blue')
#plt.plot(GRm11_time, GRm11_force_r, label='GRm11 Right', linestyle='--', color='blue')

"GRm12"
#plt.plot(time, GRm12_force_l, label='GRm12 Left', linestyle='-', color='red')
plt.plot(time_forc_r[:,0],time_forc_r[:,1], color='b')



"GRm13"
#plt.plot(time, GRm13_force_l, label='GRm13 Left', linestyle='-', color='green')
#plt.plot(time, GRm13_force_r, label='GRm13 Right', linestyle='--', color='green')

# --- Styling ---
#plt.xlabel('Time')
#plt.ylabel('Force')
#plt.title('Right Force vs Time (GRm11–GRm13)')
#plt.legend()
#plt.grid(True)
#plt.tight_layout()
#plt.show()