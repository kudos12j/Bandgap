﻿import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Data for AZO 20% Al-doped (Oxygen Carrier)
hv = np.array([3.974288915, 3.373176716, 2.930008247, 2.589791626, 2.320337572, 
               2.101675323, 1.920679053, 1.768389468, 1.638466976, 1.526334188, 
               1.428562377, 1.342568908, 1.26633017, 1.198293398, 1.147431004])  # Photon energy (hν)

alpha_hv2 = np.array([4.78289E+11, 1.22695E+11, 62942549798, 28843302585, 8501981348, 
                      2938699448, 1166090015, 713758665.7, 1172617924, 888543807.8, 
                      400122939.5, 297666146, 413780678.8, 1823926094, 3009757178])  # (αhν)^2

# **Sort hv and alpha_hv2 in ascending order**
sorted_indices = np.argsort(hv)  # Get sorted indices based on hv
hv = hv[sorted_indices]  # Sort hv
alpha_hv2 = alpha_hv2[sorted_indices]  # Sort alpha_hv2 accordingly

# Interpolating for smooth curve
hv_smooth = np.linspace(hv.min(), hv.max(), 300)  # Generate 300 points for smoothness
spline = make_interp_spline(hv, alpha_hv2, k=3)  # Cubic spline interpolation
alpha_hv2_smooth = spline(hv_smooth)

# Plot
plt.figure(figsize=(8, 6))  # Adjust figure size
plt.plot(hv_smooth, alpha_hv2_smooth, linewidth=3, color='b', label="Tauc Plot (20% Al-doped ZnO)")  # **Thicker smooth curve**
plt.scatter(hv, alpha_hv2, color='r', label="Data Points", zorder=3, s=60, edgecolor='k')  # **Larger data points**

# Labels and Formatting
plt.xlabel(r'Photon Energy $h\nu$ (eV)', fontsize=14, fontname="Times New Roman", fontweight='bold')
plt.ylabel(r'$(\alpha h\nu)^2$ (eV$^2$/cm$^2$)', fontsize=14, fontname="Times New Roman", fontweight='bold')
plt.title("Tauc Plot for AZO 20% Al-doped (Oxygen Carrier)", fontsize=14, fontname="Times New Roman", fontweight='bold')
plt.xticks(fontsize=12, fontname="Times New Roman", fontweight='bold')
plt.yticks(fontsize=12, fontname="Times New Roman", fontweight='bold')
plt.legend(prop={'size': 12, 'family': "Times New Roman", 'weight': 'bold'})  # **Bold legend**


# Show plot
plt.show()
