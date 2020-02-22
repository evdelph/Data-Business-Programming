from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.models import LinearAxis, Range1d
from bokeh.models import HoverTool
import pandas as pd

#Create data frame
series = pd.read_csv("YearlyApprovalShootings.csv",index_col="Year",header=0)

#Extract data frame pieces to variables for easier use 
dates=pd.to_datetime(series.index)
app=series["Approval"]
no=series["No. Shootings"]

#Attempt a hovertool
hover = HoverTool(tooltips=[
    ("(x,y)", "($x, $y)"),
])

#Create Figure
p = figure(plot_width=1300, plot_height=400, x_axis_type='datetime',
           title="Approval vs. No. of Shootings")

output_file("ApprovalShootings.html")

#Add labels
p.xaxis.axis_label="Time"
p.yaxis.axis_label="No. of Shootings"

#Add an extra y axis
p.extra_y_ranges = {"Approval": Range1d(start=0, end=1)}

#Add to the figure and name it
p.add_layout(LinearAxis(y_range_name="Approval", axis_label="Approval %"), 'right')
#p.add_layout(LinearAxis(y_range_name="Approval"), 'right')

#Add data
p.line(x=dates, y=app,alpha=1,y_range_name="Approval", legend="Approval Rating")
p.line(x=dates,y=no,color="Red",legend="Number of Shootings")

#Move the legend
p.legend.location="top_left"

#Add Hover Tool
p.add_tools(hover)

show(p)