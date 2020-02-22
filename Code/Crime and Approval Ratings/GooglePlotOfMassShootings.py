from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, GMapOptions, HoverTool
from bokeh.plotting import gmap
import pandas as pd
import credentials as c
from pprint import pprint

# Code for shootings_on_map.html
df = pd.read_csv('cleansed_shootings.csv')
df = df.set_index('Case')

#Set options
map_options = GMapOptions(lat=39.168451,lng=-86.51891, map_type="roadmap",zoom=4)
p = gmap(c.google_key,map_options,title="Mass Shootings")

#Load data into figure
source = ColumnDataSource(df)
p.circle(y="latitude", x="longitude", size=10, fill_color="cornflowerblue", fill_alpha=0.8, source=source)

#Show figure
show(p)