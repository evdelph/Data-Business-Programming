import twython
import pprint as p
import numpy as np
import json
import os 
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('credentials.json') as cred_file:
    creds = json.load(cred_file)

twitter = Twython(creds['consumer_key'], creds['consumer_secret'],
                creds['access_token'], creds['access_token_secret'])


who = 'garenbragg'
tweet_count = 200
results = twitter.get_followers_list(screen_name=who, count=tweet_count)


count_of_followers = []
for user in results['users']:
    #p.pprint(users)
    count_of_followers.append({user['name']: user['followers_count']})
             
# Print out this to see dictionary
#p.pprint(count_of_followers)

# Upload dictionary to garen.json
#with open('garen.json', 'w') as output:
#   json.dump(count_of_followers, output)

# Create DataFrame for Bokeh Chart
import pandas as pd

file = 'garen.json'
with open(file) as json_data:
    follower_dict = json.load(json_data)
df = pd.DataFrame(follower_dict)

df = df.stack().reset_index().set_index("level_0").rename(columns={'level_1':"Garen's Followers", 0: "Popularity"})
df['Category'] = np.nan

for index, row in df.iterrows():
    df.loc[df["Popularity"] <25 , 'Category'] = 1
    df.loc[(df["Popularity"] >= 25) & (df["Popularity"] <=99), "Category"] = 2
    df.loc[(df["Popularity"] >= 100) & (df["Popularity"] <=299), "Category"] = 3
    df.loc[(df["Popularity"] >= 300) & (df["Popularity"] <=599), "Category"] = 4
    df.loc[(df["Popularity"] >= 600) & (df["Popularity"] <=799), "Category"] = 5
    df.loc[(df["Popularity"] >= 800) & (df["Popularity"] <=999), "Category"] = 6
    df.loc[(df["Popularity"] >= 1000) & (df["Popularity"] <=1999), "Category"] = 7
    df.loc[(df["Popularity"] >= 2000) & (df["Popularity"] <=5999), "Category"] = 8
    df.loc[df["Popularity"] >= 6000 , 'Category'] = 9


df = df.set_index("Garen's Followers")
df = df.groupby(by=["Category"]).count()
df['Influence'] = np.nan

for index, row in df.iterrows():
    df.loc[df.index == 1 , 'Influence'] = '< 25'
    df.loc[df.index == 2 , 'Influence'] = '25-99'
    df.loc[df.index == 3 , 'Influence'] = '100-299'
    df.loc[df.index == 4 , 'Influence'] = '300-599'
    df.loc[df.index == 5 , 'Influence'] = '600-799'
    df.loc[df.index == 6 , 'Influence'] = '800-999'
    df.loc[df.index == 7 , 'Influence'] = '1000-1999'
    df.loc[df.index == 8 , 'Influence'] = '2000-5999'
    df.loc[df.index == 9 , 'Influence'] = '>= 6000'

# Chart Code
from bokeh.io import output_notebook, show
from bokeh.plotting import figure, output_file, show, save
from bokeh.models import ColumnDataSource
from bokeh.resources import CDN
from bokeh.embed import file_html
from bokeh.palettes import Paired12
from bokeh.models import HoverTool
import squarify

values = squarify.normalize_sizes(df["Popularity"].values, 15, 10)
rects = squarify.squarify(values, x = 0, y = 0, dx = 15, dy = 10)

colors = [Paired12[1],Paired12[2],Paired12[3],Paired12[4],Paired12[5],Paired12[6],Paired12[7],Paired12[8],Paired12[9]]
cmap = {x:y for x,y in zip(df['Influence'].unique(), colors)}

data = pd.DataFrame(rects)

data['top'] = data['y'] + data['dy']
data['right'] = data['x'] + data['dx']
data['Influence'] = df['Influence'].unique()
data['color'] = data['Influence'].map(cmap)
data = data.merge(df)

hover = HoverTool(tooltips=[
    ("Category", "@index"),
    ("Number of Garen's Followers", "@Popularity"),
    ])

source = ColumnDataSource(data = data)

p = figure(tools = [hover], toolbar_location = None, plot_width = 900)

p.quad(bottom = 'y',
    right = 'right',
    top = 'top',
    left = 'x',
    color = 'color',
    line_color = 'white',
    line_width = 2,
    source = source)

p.text(x = 'x', y = 'top',
    x_offset = 10, y_offset = 30,
    text_font_size = '16pt',
    text="Influence", source = source)

p.grid.visible = False
p.axis.visible = False


output_file("Followers.html") 
show(p)
