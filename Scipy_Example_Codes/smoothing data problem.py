
# Using the data source, make sure to save the data file as a CSV file
# Then import pandas, matplotlib and scipy. Make sure on Thonny under tools,
# select manage packages to make sure pandas, matplotlib.pyplot, scipy and
# IPython.display are all installed.

import pandas as pd
import matplotlib.pyplot as plt
import scipy
from scipy import signal
# from IPython.display import display


# Create a pandas data frame 
data = pd.read_csv ('owid-covid-data.csv')  
df = pd.read_csv('owid-covid-data.csv')

# Filter the data by the relevant columns: location, new_casese and date
  
df = pd.DataFrame(data, columns= ['location','new_cases','date'])
print (df)

# The code below restricts the data frame to a specfic country, in this case Belarus

belarus_data = df.loc[df["location"]=="Belarus"]

# Use February Filter to restruct the data to 2020
february_filter = belarus_data["date"].str.contains("2020",case=False,na=False) 
filtered_belarus_data = belarus_data[february_filter]


# display(filtered_belarus_data)


#Plotting the Raw Data:
df = pd.DataFrame(filtered_belarus_data,columns=['date','new_cases'])

df.plot(x ='date', y='new_cases', kind = 'line')

plt.show(block=False)

#Using Scipy to smooth the data
df = pd.DataFrame(filtered_belarus_data,columns=['date','new_cases'])

#Identify the X and Y variables
x = (df.date)
y = (df.new_cases)

# Identify the number and dimensions of the plots
ig, ax = plt.subplots(4, figsize=(8, 14))
i = 0

#The window size determines the degree to which the raw data is smoothed
#The code below plots both the raw data and the smoothed data with two different colored lines

for w_size in [5, 11, 21, 31]:    
    y_fit = signal.savgol_filter(y, w_size, 3, mode="nearest")
    ax[i].plot(x, y, label="raw_data", color="green")
    ax[i].plot(x, y_fit, label="smoothed_data", color="red")
    ax[i].set_title("Window size: " + str(w_size))
    ax[i].legend()
    ax[i].grid(True)
    i+=1
plt.tight_layout()

plt.show(block=False)


    
    





