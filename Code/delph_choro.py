from bokeh.plotting import figure, show, output_file
import csv
import bokeh.sampledata
bokeh.sampledata.download()
from bokeh.sampledata.us_counties import data as counties
from bokeh.sampledata.us_states import data as states
from bokeh.sampledata.unemployment import data as unemployment
from pprint import pprint

from bokeh.models import (
    ColumnDataSource,
    LogColorMapper,
    LinearColorMapper,
    HoverTool
)

from bokeh.palettes import RdGy8 as palette
palette.reverse()

## Filter in Indiana only
counties = {
    code: county for code, county in counties.items() if county["state"] == "in"
}

county_xs = [county["lons"] for county in counties.values()]
county_ys = [county["lats"] for county in counties.values()]
county_names = [county['name'] for county in counties.values()]
county_rates = [unemployment[county_id] for county_id in counties]
color_mapper = LogColorMapper(palette=palette)

source = ColumnDataSource(data=dict(
    x=county_xs,
    y=county_ys,
    name=county_names,
    rate=county_rates,
))

TOOLS = 'hover' #"pan,wheel_zoom,reset,hover,save"
p = figure(
    title="Indiana P, 2009", tools=TOOLS, match_aspect=True,
    x_axis_location=None, y_axis_location=None
)

p.grid.grid_line_color = None

p.patches('x', 'y', source=source,
          fill_color={'field': 'rate', 'transform': color_mapper},
          fill_alpha=0.7, line_color="white", line_width=0.5)

hover = p.select_one(HoverTool)
    

output_file('in_population.html')
show(p)
