# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 13:37:50 2023

@author: carosn
"""

# -*- coding: utf-8 -*-

import sys
import os
sys.path.append("C:/Users/carosn/Desktop/ofile")
import flac
fl=flac.Flac()
import glob
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PIL import Image
import glob
 
drive_path = 'D:\lab_test_00\model_220'
folder_name = f'timestep'
folder_path = os.path.join(drive_path, folder_name)

try:
    os.makedirs(folder_path)
    print(f"Folder '{folder_name}' created successfully on the D drive.")
except FileExistsError:
    print(f"Folder '{folder_name}' already exists on the D drive.")
except Exception as e:
    print(f"Error occurred while creating the folder: {e}")
    
    
x = int(input('toatl_number_of_flac ='))
a = x
for i in range(1,x):
 elv = []
 pos = []
 x,z=fl.read_mesh(i)
 for j in range(1,751):
     p = x[j,0]
     h = z[j,0]
     pos.append(p)
     elv.append(h)
    
 plt.title(f"elivation_timestep_{i}")
 plt.xlabel("postion")
 plt.ylabel("elvation")
 plt.plot(pos, elv,  color ="blue")
 plt.xlim(0, 1552)
 plt.ylim(-20, 15)
 plt.savefig(f"D:/lab_test_00/model_220/timestep/time_step_{i}")
 plt.show()
 


images = []

for i in range(1, a):
    filename = f"D:/lab_test_00/model_220/timestep/time_step_{i}.png"
    image = Image.open(filename)
    images.append(image)

model_gif = "D:/lab_test_00/model_220/model_220.gif"  


images[0].save(model_gif,save_all=True,append_images=images[1:],duration=500,loop=0)