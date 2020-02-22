import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint
import seaborn as sns

# Code for bubble chart, gun regulations versus number of shootings

# Load data
year, laws, shootings = np.loadtxt("shootings_laws.csv", delimiter=",",unpack=True, skiprows=1, usecols=(0,1,2))
colors = ['blue','pink','red','cyan']

# Set figure variable and axis titles
sns.set(style="whitegrid")
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('Increase of Mass Shootings versus Increase in Gun Regulations')
ax.set_xlabel('Year')
ax.set_ylabel('Number of Gun Regulations')

#Plot data and show figure
plt.scatter(x=year,y=laws,s=shootings*20, alpha=0.5,c=colors)
plt.show()