from bokeh.io import output_file, show
from bokeh.plotting import figure
import pandas as pd

dates_series = pd.read_csv("Approval.csv",index_col="Survey Date",header=0)

dates=pd.to_datetime(dates_series.index)
app=dates_series["Approve %"]

p = figure(plot_width=800, plot_height=300, x_axis_type='datetime',
           title="Approval over time")

p.line(x=dates, y=app,alpha=1)
show(p)