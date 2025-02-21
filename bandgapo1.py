import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Data (from your provided table)
hv = np.array([3.974288915, 3.373176716, 2.930008247, 2.589791626, 2.320337572, 
               2.101675323, 1.920679053, 1.768389468, 1.638466976, 1.526334188, 
               1.428562377, 1.342568908, 1.26633017, 1.198293398, 1.147431004])  # Photon energy (hν)

alpha_hv2 = np.array([4.8436E+11, 41091063333, 1175966318, 163213641.1, 47078245.37, 
                      22407677, 9315274.505, 4729619.787, 2883289.753, 1249514.73, 
                      1221982.108, 1544945.461, 1676670.503, 3022701.825, 4400618.566])  # (αhν)^2

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
plt.plot(hv_smooth, alpha_hv2_smooth, linewidth=3, color='b', label="Tauc Plot")  # **Thicker smooth curve**
plt.scatter(hv, alpha_hv2, color='r', label="Data Points", zorder=3, s=60, edgecolor='k')  # **Larger data points**

# Labels and Formatting
plt.xlabel(r'Photon Energy $h\nu$ (eV)', fontsize=14, fontname="Times New Roman", fontweight='bold')
plt.ylabel(r'$(\alpha h\nu)^2$ (eV$^2$/cm$^2$)', fontsize=14, fontname="Times New Roman", fontweight='bold')
plt.title("Tauc Plot for Undoped ZnO (Oxygen Carrier)", fontsize=14, fontname="Times New Roman", fontweight='bold')
plt.xticks(fontsize=12, fontname="Times New Roman", fontweight='bold')
plt.yticks(fontsize=12, fontname="Times New Roman", fontweight='bold')
plt.legend(prop={'size': 12, 'family': "Times New Roman", 'weight': 'bold'})  # **Bold legend**


# Show plot
plt.show()
