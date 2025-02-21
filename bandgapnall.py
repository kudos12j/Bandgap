import os
import pandas as pd
import matplotlib.pyplot as plt

# Define the folder path
folder_path = r'C:\Users\KD\Desktop\PYTHON\BG\N'

# List of file names
file_names = ['0$.xlsx', '5%.xlsx', '10%.xlsx', '15%.xlsx', '20%.xlsx']

# Create a figure with 5 subplots
fig, axes = plt.subplots(nrows=5, ncols=1, figsize=(10, 20))

# Loop through each file and plot the data
for i, file_name in enumerate(file_names):
    # Construct the full file path
    file_path = os.path.join(folder_path, file_name)
    
    # Read the Excel file
    df = pd.read_excel(file_path)
    
    # Extract the relevant columns
    wavelength = df['Wavelength']
    alpha = df['α']
    hv = df['hν']
    alpha_hv_squared = df['(αhν)^2']
    
    # Plot the data
    ax = axes[i]
    ax.plot(wavelength, alpha, label='α')
    ax.plot(wavelength, hv, label='hν')
    ax.plot(wavelength, alpha_hv_squared, label='(αhν)^2')
    
    # Set the title and labels
    ax.set_title(f'{file_name} - Undoped ZnO')
    ax.set_xlabel('Wavelength')
    ax.set_ylabel('Value')
    ax.legend()
    ax.grid(True)

# Adjust layout and display the plots
plt.tight_layout()
plt.show()