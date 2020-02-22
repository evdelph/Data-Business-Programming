import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pprint import pprint

# Code for changes in approval rates and shootings

#Load data
df = pd.read_csv('ApprovalShootingMonthly.csv')
df = df.set_index(df.Shooting)

#Set SNS style
sns.set(style="whitegrid")

#Set settings and plot data
ax = sns.tsplot([df.Approval, df.Change],ci=[68, 95], color="m")
ax.set_title("% Changes in Approval Ratings and % Changes in Shootings")
ax.set_ylabel('% Monthly Change')
ax.set_xlabel('Month')

#Show figure
plt.show()