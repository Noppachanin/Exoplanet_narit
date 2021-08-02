import matplotlib.pyplot as plt
import os
from ExoParams import Habit_zone, Exo_plot
import pandas as pd
import numpy as np

# Define Root directory
root = 'C:/Users/user/Desktop/Narit_Intern_code/Exo_plot/'

# Import a raw data file (.csv)
raw_data = pd.read_csv(root + 'Raw_data/Kepler_ds_29072021.csv', header=28)
print("Available host names")
print(list(raw_data['hostname']))

while True:
    # Input hostname to search in the file
    target = input("Choose Hostname from list: ")


    # Check whether the star exists 
    if str(target.lower()) in list(raw_data['hostname'].str.lower()):
        print("Target's found")
        break
    else:
        print("Input: " + target)
        print("Target's not found")

# Get the target's parameters
target_data = raw_data[raw_data['hostname'].str.lower() == str(target.lower())] # Normalize all str to lowercase
target_data = target_data.to_dict('records')[0]

# Check whether the destination folder exists
try:
    os.makedirs('figures')    
    print("Directory " , '/figures' ,  " Created ")
except FileExistsError:
    print("Directory " , '/figures' ,  " already exists")  
    pass
# figure, axes = plt.subplots(2)
# Stellar_M: Steller mass unit, 
Habit_zone(host_name='Earth',Stellar_M = 1,a =150e6/(6.957e5),Stellar_R = 1 )
Habit_zone(host_name=target_data['hostname'],Stellar_M = target_data['st_mass'],a =target_data['pl_orbsmax'],Stellar_R = target_data['st_rad'] )
Exo_plot(host_name=target_data['hostname'], Inc = target_data['pl_orbincl'] ,Stellar_R = target_data['st_rad'], a =target_data['pl_orbsmax'], ST=target_data['st_teff'] )

plt.show()