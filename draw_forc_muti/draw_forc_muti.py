"force on the boundary - timerelationship"
import numpy as np
import matplotlib.pyplot as plt
"setting param"


"writing file"
forc_GRm11_r01 = np.load('GRm11_r01_forc.npy')
forc_GRm12_r02 = np.load('GRm12_r02_forc.npy')
forc_GRm13_r03 = np.load('GRm13_r03_forc.npy')


"extract for foc_np array"
GRm11_time = forc_GRm11_r01[:,1]
GRm12_time = forc_GRm12_r02[:,1]
GRm13_time = forc_GRm13_r03[:,1]

"GRm11"
#GRm11_force_l = forc_GRm11_r01[:,2]  
GRm11_force_r = forc_GRm11_r01[:,3]

"GRm12"
#GRm12_force_l = forc_GRm12_r02[:,2]  
GRm12_force_r = forc_GRm12_r02[:,3]

"GRm13" 
#GRm13_force_l = forc_GRm13_r03[:,2]  
GRm13_force_r = forc_GRm13_r03[:,3]

"GRm11"
#plt.plot(time, GRm11_force_l, label='GRm11 Left', linestyle='-', color='blue')
plt.plot(GRm11_time, GRm11_force_r, label='GRm11 Right', linestyle='--', color='blue')

"GRm12"
#plt.plot(time, GRm12_force_l, label='GRm12 Left', linestyle='-', color='red')
#plt.plot(time, GRm12_force_r, label='GRm12 Right', linestyle='--', color='red')

"GRm13"
#plt.plot(time, GRm13_force_l, label='GRm13 Left', linestyle='-', color='green')
#plt.plot(time, GRm13_force_r, label='GRm13 Right', linestyle='--', color='green')

# --- Styling ---
plt.xlabel('Time')
plt.ylabel('Force')
plt.title('Right Force vs Time (GRm11–GRm13)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()