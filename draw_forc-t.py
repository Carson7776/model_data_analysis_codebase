"force on the boundary - timerelationship"
import numpy as np
import matplotlib.pyplot as plt
"setting param"



"opening files"
with open("forc.0","r") as file:
    
    content = file.read()
    lines = content.strip().split("\n")
    strip_line = [line.split() for line in lines]
    forc = [[float(value) for value in line]for line in strip_line]
    
"writing files into arrays"
forc_np = np.array(forc)

"extract for foc_np array"
time = forc_np[:,1]

force_l = forc_np[:,2]  
force_r = forc_np[:,3] 

vl = forc_np[:,4]
vr = forc_np[:,5]

"plot"

"force_left boundary"
plt.plot(time, force_l)
plt.xlabel("time")
plt.ylabel("force - left boundary")
plt.show()

"force_right boundary"
plt.plot(time, force_r)
plt.xlabel("time")
plt.ylabel("force - right boundary")
plt.show()

"velocity_left boundary"
plt.plot(time, vl)
plt.xlabel("time")
plt.ylabel("velocity - right boundary")
plt.show()    

"velocity_right boundary"
plt.plot(time, vr)
plt.xlabel("time")
plt.ylabel("velocity - right boundary")
plt.show()
    

    
    
    
    

