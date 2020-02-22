# Part One ##########################################################################################################
import pprint as p 
import sqlite3
from pprint import pprint
from bokeh.io import show, output_file
from bokeh.plotting import figure

con = sqlite3.connect('C:\\Users\\evdelph\\Desktop\\355\\sqmight.sqlite3')
cur = con.cursor()

# Initialize dictionary
revenue = dict()

# Initialize bins for revenue dictionary

bin1 = 0 # Less than $25
bin2 = 0 # Between 25 and 49
bin3 = 0 # Between 50 and 74
bin4 = 0 # Between 75 and 99
bin5 = 0 # Between 100 and 299
bin6 = 0 # Between 300 and 599
bin7 = 0 # Between 600 and 999
bin8 = 0 # Between 1000 and 1999
bin9 = 0 # Between 2000 and 2999
bin10 = 0 # Between 3000 and 3999
bin11 = 0 # Above 4000

# Update revenue dictionary
for row in cur.execute('SELECT SUM(price_each * quantity), order_id FROM order_products GROUP BY order_id'):
    if row[0] < 25:
        revenue['< 25'] = []
        bin1 += 1
        revenue['< 25'].append(bin1)
    if row[0] >= 25 and row[0] <= 49:
        revenue['25-49'] = []
        bin2 += 1
        revenue['25-49'].append(bin2)
    if row[0] >= 50 and row[0] <= 74:
        revenue['50-74'] = []
        bin3 += 1
        revenue['50-74'].append(bin3)
    if row[0] >= 75 and row[0] <= 99:
        revenue['75-99'] = []
        bin4 += 1
        revenue['75-99'].append(bin4)
    if row[0] >= 100 and row[0] <= 299:
        revenue['100-299'] = []
        bin5 += 1
        revenue['100-299'].append(bin5)
    if row[0] >= 300 and row[0] <= 599:
        revenue['300-599'] = []
        bin6 += 1
        revenue['300-599'].append(bin6)
    if row[0] >= 600 and row[0] <= 999:
        revenue['600-999'] = []
        bin7 += 1
        revenue['600-999'].append(bin7)
    if row[0] >= 1000 and row[0] <= 1999:
        revenue['1000-1999'] = []
        bin8 += 1
        revenue['1000-1999'].append(bin8)
    if row[0] >= 2000 and row[0] <= 2999:
        revenue['2000-2999'] = []
        bin9 += 1
        revenue['2000-2999'].append(bin9)
    if row[0] >= 3000 and row[0] <= 3999:
        revenue['3000-3999'] = []
        bin10 += 1
        revenue['3000-3999'].append(bin10)
    if row[0] > 4000:
        revenue['> 4000'] = []
        bin11 += 1
        revenue['> 4000'].append(bin11)

# For formatting purposes, make keys the same length as the longest key length

# Returns the longest length in keys
def max_length():
    '''
    None-> (int)
    returns the max length of keys in revenue
    >>>print(max_length())
    10
    '''
    max_num = 0
    for k,v in revenue.items():
        current_num = len(k)
        if current_num > max_num:
            max_num = current_num
        else:
            pass
    return max_num

# Swaps new key with old key
for k in revenue.copy():
    num = len(k)
    k1 = k
    while num < max_length():
        k1 += ' '
        num += 1
        if num >= max_length():
            revenue[k1]=revenue.pop(k)
            pass


# Print dictionary
p.pprint(revenue)

# Print Histrogram
def print_histogram(key, val):
    size = val[0]
    print(key,':','*'*size)
print()

print("Total Revenue By Amount")
for key ,value in revenue.items():
    print_histogram(key,value)
print()

# Observations
print('Observations:\n\tI noticed that there are more frequent purchases for items that \
cost between $100-$299 and less than $25. \n\tThey have the same frequency.More people \
are mainly buying around less than $25 to $599 more often. There are only a handful\n\t\
of purchases that occur beyond that price range.')


# Part 2 ####################################################################################################


# Specify the x and y-values on the histogram
# Use your dictionary here
x_values = list(revenue.keys())
y_values = list(revenue.values())

# To use bokeh, first make a 'figure' object
fig = figure(x_range=x_values, \
 plot_height=250, \
 title="Order Mix", \
 toolbar_location=None, tools="")

# Draw the vertical bars in your figure
fig.vbar(x=x_values, top=y_values, width=0.9)

# These are just some settings for the chart that's being printed.
# Try (un)commenting these lines and see what happens.
fig.xgrid.grid_line_color = None
fig.ygrid.grid_line_color = None
fig.y_range.start = 0

output_file("ordermix.html") 
show(fig)
