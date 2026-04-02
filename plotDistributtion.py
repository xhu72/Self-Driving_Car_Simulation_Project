import pandas as pd
import matplotlib.pyplot as plt

path_csv = r"best_car_recordings_comp_vision\driving_log.csv"

data = pd.read_csv(path_csv, header=None)

#columns in driving_log.csv
data.columns = ['Center', 'Left', 'Right', 'Steering', 'Throttle', 'Brake', 'Speed']


#EXTRACT (TAKE) steering angles 
angles_when_steering = data["Steering"]

plt.hist(angles_when_steering, bins=25, edgecolor="white")
plt.title("Distribution for steering angle")
plt.ylabel("Number of Samples")
plt.xlabel("Steering Angle ")
plt.grid(True)
plt.show()


