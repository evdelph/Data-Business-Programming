rom bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.models import LinearAxis, Range1d
from bokeh.models import HoverTool
import pandas as pd

output_file("Victims.html")

#Create data frames
series = pd.read_csv("ApprovalShootingMonthly.csv",index_col="Shooting",header=0)
other_series = pd.read_csv("MonthlyVictims.csv",index_col="Shooting Month",header=0)

#Extract data frame pieces to variables for easier use 
dates=pd.to_datetime(series.index)
app=series["Approval"]
victims=other_series["Victims"]

#Attempt a hovertool
hover = HoverTool(tooltips=[
    ("(x,y)", "($x, $y)"),
])

#Create figure
p = figure(plot_width=1300, plot_height=400, x_axis_type='datetime',
           title="Approval vs. Number of Victims")

#Add labels
p.xaxis.axis_label="Time"
p.yaxis.axis_label="No. of Victims"

#Add an extra y axis
p.extra_y_ranges = {"Approval": Range1d(start=0, end=1)}

#Add to the figure and name it  
p.add_layout(LinearAxis(y_range_name="Approval",axis_label="Approval %"), 'right')

#Add data
p.line(x=dates, y=app,alpha=1,y_range_name="Approval", legend="Approval Rating")
p.line(x=dates,y=victims,color="Red",legend="Number of Victims")


#Add Hover Tool
p.add_tools(hover)

#Move the legend
p.legend.location="top_left"

show(p)

