#!/usr/bin/python3

"""_summary_

This an example script on how to plot aeronet products using the downloaded CSV file using this library

"""

import pandas as pd
from matplotlib import pyplot as plt

#--------------------------------------------------------------------------------------------------
# Local functions
#--------------------------------------------------------------------------------------------------

def plot_aeronet_data(plot_key, ax=None, fig=None, **kwargs):
    """_summary_

    This function reads the aeronet data and plots the data

    Args:
        file_path (str): The path to the aeronet data file

    Returns:
        None

    """

    if ax is None:
        fig_, ax_ = plt.subplots(nrows=3, ncols=1, dpi=300)
    else:
        ax_ = ax
    
    # plot the data
    if 'Total' in plot_key:
        ax_[0].plot(aero['Day_of_Year(Fraction)'], '.',aero[plot_key], label=plot_key, **kwargs)
    elif 'Fine' in plot_key:
        ax_[1].plot(aero['Day_of_Year(Fraction)'], '.',aero[plot_key], label=plot_key, **kwargs)
    elif 'Coarse' in plot_key:
        ax_[2].plot(aero['Day_of_Year(Fraction)'], '.',aero[plot_key], label=plot_key, **kwargs)
    else:
        ax_.plot(aero['Day_of_Year(Fraction)'], aero[plot_key], label=plot_key, **kwargs)

# Define the path to the .aod file
file_path = '2024/20240305_20240922_Amazon_ATTO_Tower_level15.aod'

# Read the file, skipping the initial metadata lines
aero = pd.read_csv(file_path, skiprows=6)

# interested keys
keys_ = ['AOD_Extinction', 'Extinction_Angstrom_Exponent', 'Inversion_Data_Quality_Level']

# find the keys with keys_ str
keys = [key for key in aero.keys() if any([k in key for k in keys_])]

# find the keys with keys_ str and plot them
ext_key = [key for key in keys if 'AOD_Extinction' in key]

fig, ax = plt.subplots(nrows=4, ncols=1, figsize=(16,9), dpi=300)
# plot the data
for key in ext_key:
    plot_aeronet_data(key, ax=ax, lw=1)

# add legend
ax[2].legend(fontsize=8)

# plot the AE
# find the keys with keys_ str and plot them
ae_key = [key for key in keys if 'Extinction_Angstrom_Exponent' in key]
plot_aeronet_data(ae_key, ax=ax[3], lw=1)
ax[3].legend(fontsize=8)
# add labels
ax[0].set_ylabel('AOD Extinction \n (Total)')
ax[1].set_ylabel('AOD Extinction \n (Fine)')
ax[2].set_ylabel('AOD Extinction \n (Coarse)')
ax[3].set_ylabel('Extinction \n Angstrom Exponent')
ax[3].set_xlabel('Day of Year \n (Fraction)')

# save the figure
plt.savefig('aeronet_data.png')