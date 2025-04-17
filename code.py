import numpy as np
import matplotlib.pyplot as plt

# De Broglie wavelengths (in meters)
lambda_A = 4.97e-37  # Object A
lambda_B = 6.53e-8   # Object B

# Create a 1D interference pattern simulation
x = np.linspace(-1e-6, 1e-6, 1000)  # 1 µm range, good for nano-scale interference

# Simulate intensity patterns (assume simple two-slit interference)
def interference_pattern(wavelength, slit_distance=1e-7):
    k = 2 * np.pi / wavelength
    return (np.cos(k * slit_distance * x / (2 * 1e-6)))**2

intensity_A = interference_pattern(lambda_A)
intensity_B = interference_pattern(lambda_B)

# Plotting
plt.figure(figsize=(12, 5))

# Object A (macroscopic)
plt.subplot(1, 2, 1)
plt.plot(x * 1e9, intensity_A, color='red')
plt.title("Object A: Interference Pattern")
plt.xlabel("Position (nm)")
plt.ylabel("Intensity")
plt.grid(True)

# Object B (quantum)
plt.subplot(1, 2, 2)
plt.plot(x * 1e9, intensity_B, color='blue')
plt.title("Object B: Interference Pattern")
plt.xlabel("Position (nm)")
plt.ylabel("Intensity")
plt.grid(True)

plt.tight_layout()
plt.show()
