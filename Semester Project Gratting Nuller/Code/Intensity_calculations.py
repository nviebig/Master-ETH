import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Constants
lambda_0 = 633e-9  # Wavelength of laser in meters (633 nm)
#N = 800e3  # Grating grooves per meter (300 grooves/mm)
#d = 1 / N  # Grating spacing in meters
#alpha = np.radians(0)  # Angle of incidence in radians, can be changed

# Function to calculate the diffraction angle (theta) for a given order m
def diffraction_angle(m, alpha, lambda_0, d):
    term = m * lambda_0 / d - np.sin(alpha)
    if abs(term) <= 1:
        return np.arcsin(term)
    else:
        return None  # No solution for this order

# Function to calculate intensity after Slit where alpha_0
def intensity(x, theta_m, d, lambda_0,L):
    val_1 = np.sin(np.pi*d*N/(lambda_0*L)*x)**2
    val_2 = (np.sin(np.pi*d/(lambda_0*L)*x))**2
    return val_1/val_2

'''
theta_m = []
i_m= []
for i in range(-3,4):
    val_angle= diffraction_angle(i,alpha,lambda_0, d)
    theta_m.append(val_angle)


X=np.linspace(-1,1,1000)

plt.plot(X,intensity(X, theta_m, d, lambda_0,1))
plt.show()
'''
def h(lambda_0,d,f_3):
    return np.tan(np.arcsin(lambda_0/d))*f_3

Gratings = [1e-3/300, 1e-3/600, 1e-3/830,1e-3/1200] # in m (Sizes are 12,5/25/50 mm)

lenses_25mm = [50.1e-3, 74.9e-3,100e-3,200e-3]
lenses_25_4mm = [49.8e-3, 59.8e-3,74.8e-3,99.7e-3]
lenses_30mm = [39.9e-3,49.8e-3,74.8e-3,99.7e-3]

def determine_hight(Gratings,lenses):
    h_list= []
    for i in range(len(Gratings)):
        h_element = []
        for k in range(len(lenses)):
            h_element.append(h(lambda_0,Gratings[i],lenses[k]))

        h_list.append(h_element)
    return h_list

height_25mm = determine_hight(Gratings,lenses_25mm)
height_25_4mm = determine_hight(Gratings,lenses_25_4mm)
height_30mm = determine_hight(Gratings,lenses_30mm)

df_25mm = pd.DataFrame(height_25mm)
df_25_4mm = pd.DataFrame(height_25_4mm)
df_30mm = pd.DataFrame(height_30mm)

'Naming the DF'
Gratings_string = ["1/300", "1/600", "1/830","1/1200"]

lenses_25mm_string = ["50.1e-3", "74.9e-3", "100e-3", "200e-3"]
lenses_25_4mm_string = ["49.8e-3", "59.8e-3", "74.8e-3", "99.7e-3"]
lenses_30mm_string = ["39.9e-3", "49.8e-3", "74.8e-3", "99.7e-3"]


df_25mm.columns = Gratings_string
df_25mm.index = lenses_25mm_string

df_25_4mm.columns = Gratings_string
df_25_4mm.index = lenses_25_4mm_string

df_30mm.columns = Gratings_string
df_30mm.index = lenses_30mm_string

threshold_df_30mm = 0.03/2

# Replace values smaller than the threshold with 'No'
df_30mm_filtered = df_30mm.applymap(lambda x: "No" if x > threshold_df_30mm else x)

threshold_df_25_4mm = 0.0254/2

# Replace values smaller than the threshold with 'No'
df_25_4mm_filtered = df_25_4mm.applymap(lambda x: "No" if x > threshold_df_25_4mm else x)

threshold_df_25mm = 0.025/2 

# Replace values smaller than the threshold with 'No'
df_25mm_filtered = df_25mm.applymap(lambda x: "No" if x > threshold_df_25mm else x)