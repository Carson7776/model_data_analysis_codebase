"force on the boundary - timerelationship"
#inorder to run this program, the forc file need to be download to where this program is
#download forc file named as the following: GRm**_forc,,,
import glob
import numpy as np
import matplotlib.pyplot as plt

"store forc file from different model to forc dict"
forc = {}


"read forc.0 file into program"
files = sorted(glob.glob("GRm*"))
for filename in files:
#    print("Reading:", filename)
    forc[filename] = np.loadtxt(filename)
        
    
def user_input_model():
    user_input = input("please input the models you with to draw")
    return user_input

def extract_values(user_input):
    keys = user_input.split()
    return keys

def t_forc_r(keys, user_input):
    
    plt.figure()
    #set colors for the line to be draw, maximum = 3 colors
    color = ["red","green","blue"]
    color_index = 0
    for key in keys:
        #initial arrays to prvent previous valuses 
        arr = np.array([])
        time = np.array([])
        forc_l = np.array([])
        forc_r = np.array([])
        #select the model, to plot
        if key in forc:
            arr = forc[key]
            time = arr[:,1]
            forc_l = arr[:,2]
            forc_r = arr[:,3]
            #time_force_right_boundary
            plt.plot(time, forc_r,color = color[color_index], label = key)
            plt.title(f"{user_input}")
            plt.xlabel("time(Myr)")
            plt.ylabel("force right boundary")
            #set the upper limit of the force(top),according to the maximum force you see on graph
            plt.ylim(top = 2.0*(10**13))
            plt.legend()
            plt.savefig(f"output/{user_input}_time_right_boundary_force.png")
            #change the color for the next line
            color_index = color_index + 1
def t_forc_l(keys, user_input):
    
    plt.figure()
    #set colors for the line to be draw, maximum = 3 colors
    color = ["r","g","b"]
    color_index = 0
    for key in keys:
        #initial arrays to prvent previous valuses 
        arr = np.array([])
        time = np.array([])
        forc_l = np.array([])
        forc_r = np.array([])
        #select the model, to plot
        if key in forc:
            arr = forc[key]
            time = arr[:,1]
            forc_l = arr[:,2]
            forc_r = arr[:,3]
            #time_force_left_boundary
            plt.plot(time, forc_l, color = color[color_index], label = key)
            plt.title(f"{user_input}")    
            plt.xlabel("time(Myr)")
            plt.ylabel("force left boundary")
            #set the upper limit of the force(top),according to the maximum force you see on graph
            plt.ylim(top = 2.0*(10**13))
            plt.legend()
            plt.savefig(f"output/{user_input}_time_left_boundary_force.png")
            #change the color for the next line
            color_index = color_index + 1
            
"main program"

user_input = user_input_model()
keys = extract_values(user_input)
t_forc_r(keys,user_input)
t_forc_l(keys,user_input)

