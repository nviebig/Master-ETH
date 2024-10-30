import numpy as np
import matplotlib.pyplot as plt

# Constants
groove_density = 300  # grooves per mm
d = 1e-3 / groove_density  # grating spacing in meters
wavelength = 633e-9  # wavelength in meters (e.g., 633 nm for HeNe laser)
N = 1000  # number of grooves illuminated
L = 0.005  # distance to screen in meters
s = 0.1e-3  # slit width
alpha_deg = 0  # incident angle in degrees

# Angle of incidence (in degrees and converted to radians)
alpha = np.radians(alpha_deg)

# Calculate intensity distribution based on angles
def calculate_intensity(theta, N, d, s, wavelength, alpha):
    p = np.sin(theta) - np.sin(alpha)
    interference_function = (np.sin((N * np.pi * d * p / wavelength)) / np.sin((np.pi * d * p / wavelength)))**2
    intensity_function_slit = (np.sin((np.pi * s * p / wavelength)) / (np.pi * s * p / wavelength))**2
    I_p = interference_function
           
    return I_p

# Calculate diffraction angles for orders -2 to 2
def angle(d, alpha, m, wavelength):
    sin_theta = np.sin(alpha) + (m * wavelength) / d
    if np.abs(sin_theta) <= 1:
        return np.arcsin(sin_theta)
    else:
        return None

angles = []
for m in range(-2, 3):
    angle_m = angle(d, alpha, m, wavelength)
    if angle_m is not None:
        angles.append(angle_m)


x = np.linspace(-0.005, 0.005, 10000)  # Extend the range of x
theta = np.arctan(x / L)
y = calculate_intensity(theta, N, d, s, wavelength, alpha)

# Plot intensity distribution
plt.figure(figsize=(12, 10))
plt.plot(x, y, label="Intensity distribution")

# Plot vertical lines at calculated diffraction angles
'''
screen_positions = L * np.tan(angles)
i = -2
for pos in screen_positions:
    plt.axvline(x=pos, color='red', linestyle='--', linewidth=2, label=f'{i}th order at {round(pos, 4)} m')
    i += 1
'''

plt.title(f'Simulated Interference Pattern on Screen (Grating, Incident Angle {alpha_deg}°)')
plt.xlabel('Position on Screen (m)')
plt.ylabel('Intensity (Arbitrary Units)')
plt.grid(True)
plt.legend(loc='upper left')
plt.show()
