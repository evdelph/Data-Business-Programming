# Data-Business-Programming
Python projects that focus on twitter API usage and data visualizations

## Project 1: Simulating Friend Suggestions by Determining Interests and Friend Groups
This project required taking various CSV files of friends, ids. It matches users to their interests and makes friend recommendations based on those interests. The code to produce the results are from FriendsInterests.py and SimulatingNetworks.py. Below shows some of the sample output:

```
[{'ID': '0', 'Name': 'Hiro'},
 {'ID': '1', 'Name': 'Dunn'},
 {'ID': '2', 'Name': 'Sue'},
 {'ID': '3', 'Name': 'Chi'},
 {'ID': '4', 'Name': 'Thor'},
 {'ID': '5', 'Name': 'Clive'},
 {'ID': '6', 'Name': 'Hicks'},
 {'ID': '7', 'Name': 'Devin'},
 {'ID': '8', 'Name': 'Kate'},
 {'ID': '9', 'Name': 'Klein'}]
 
{'0': {'Friends': ['1', '2']},
 '1': {'Friends': ['0', '2', '3']},
 '2': {'Friends': ['0', '1', '3']},
 '3': {'Friends': ['1', '2', '4']},
 '4': {'Friends': ['3', '5']},
 '5': {'Friends': ['4', '6', '7']},
 '6': {'Friends': ['5', '8']},
 '7': {'Friends': ['5', '8']},
 '8': {'Friends': ['6', '7', '9']},
 '9': {'Friends': ['8']}}
 
{'0': {'Friends': ['1', '2'], 'Friends of Friends': ['3']},
 '1': {'Friends': ['0', '2', '3'], 'Friends of Friends': ['4']},
 '2': {'Friends': ['0', '1', '3'], 'Friends of Friends': ['4']},
 '3': {'Friends': ['1', '2', '4'], 'Friends of Friends': ['0', '5']},
 '4': {'Friends': ['3', '5'], 'Friends of Friends': ['1', '2', '6', '7']},
 '5': {'Friends': ['4', '6', '7'], 'Friends of Friends': ['3', '8']},
 '6': {'Friends': ['5', '8'], 'Friends of Friends': ['4', '7', '9']},
 '7': {'Friends': ['5', '8'], 'Friends of Friends': ['4', '6', '9']},
 '8': {'Friends': ['6', '7', '9'], 'Friends of Friends': ['5']},
 '9': {'Friends': ['8'], 'Friends of Friends': ['6', '7']}}
 
 {'0': {'interests': ['Hadoop',
                     'Big Data',
                     'HBas',
                     'Java',
                     'Spark',
                     'Storm',
                     'Cassandra']},
 '1': {'interests': ['NoSQL', 'MongoDB', 'Cassandra', 'HBase', 'Postgres']},
 '2': {'interests': ['Python',
                     'skikit-learn',
                     'scipy',
                     'numpy',
                     'statsmodels',
                     'pandas']},
 '3': {'interests': ['R', 'Python', 'statistics', 'regression', 'probability']}
 
 {'Big Data': {'interests_id': ['0', '8', '9']},
 'C++': {'interests_id': ['5']},
 'Cassandra': {'interests_id': ['0', '1']},
 'HBas': {'interests_id': ['0']},
 'HBase': {'interests_id': ['1']},
 'Hadoop': {'interests_id': ['0', '9']},
 'Haskell': {'interests_id': ['5']},
 'Java': {'interests_id': ['0', '5', '9']}}
 
 '3': {'interests': ['R', 'Python', 'statistics', 'regression', 'probability'],
       'recommendations': ['5', '6']},
 '4': {'interests': ['machine learning',
                     'regression',
                     'decision trees',
                     'libsvm'],
       'recommendations': ['7']},
 '5': {'interests': ['Python',
                     'R',
                     'Java',
                     'C++',
                     'Haskell',
                     'programming languages'],
       'recommendations': ['0', '2', '3', '9']}}
```
## Project 2: SQLite Database/Histogram Simulation/Bokeh Plot Visualization
This project focused on connected with a sqlite database to query data and create 1) a rudimentary histogram plot and 2) a bokeh plot visualization. The data used is order/product mix data. Below shows the output that ordermix.py produces.

*Summarized data from sqlite database*
```
{'100-299  ': [44],
 '1000-1999': [13],
 '2000-2999': [7],
 '25-49    ': [23],
 '300-599  ': [22],
 '3000-3999': [2],
 '50-74    ': [24],
 '600-999  ': [11],
 '75-99    ': [9],
 '< 25     ': [44],
 '> 4000   ': [1]}
```

*Simulated Histogram*
```
Total Revenue By Amount
2000-2999 : *******
1000-1999 : *************
3000-3999 : **
100-299   : ********************************************
25-49     : ***********************
300-599   : **********************
< 25      : ********************************************
75-99     : *********
600-999   : ***********
50-74     : ************************
> 4000    : *
```
*Bokeh Plot Visualization*
![7](https://github.com/evdelph/Data-Business-Programming/blob/master/Images/ordermix.png)

## Project 3: Chloropeth Map of Indiana
This project was a fun exercise in creating a cloropeth visualization of Indiana unemployment rates for each county. The html image under "images" include hover tool-tip features to see the rates itself. Below shows a snapshot of what IndianaCloropleth.py produces:
![6](https://github.com/evdelph/Data-Business-Programming/blob/master/Images/in-population.png)

## Project 4: Influential Followers Using Twitter API
This project's goal was to find influential followers for a given candidate to determine a competitive political networking strategy. Twitter API libaries were use to retrieve data, summarize follower's information, and organize the followers into bins by their follower's size. Below shows the output from twitter_followers.py
![5](https://github.com/evdelph/Data-Business-Programming/blob/master/Images/followers-1.png)

## Project 5: Analyzing Trends in Shootings and Presidential Approval Ratings
The goal of this project was to visualize and detect if there were any trends in shootings in the US and presidential approval ratings. 

### Visualization Explanations: 
* Approval.html: A graph showing Presidential Approval ratings from 1946 to 2018. Even though this is only using data from one data set, we felt it was a good visual to have for the presentation. 
![1](https://github.com/evdelph/Data-Business-Programming/blob/master/Images/alltime.png)

* ApprovalShootings.html: This chart shows line-plots for both Approval Ratings and the Number of Shootings that year.
![3](https://github.com/evdelph/Data-Business-Programming/blob/master/Images/approvalshootings.png)

* Victims.html: This chart shows line-plots for both Approval Ratings and the Number of victims (of shootings) that year. This one, along with the chart above, allow the viewer to see how/if the approval rating is affected by not only the occurrence of one (or more) shootings, but also the number of victims that year. 
![9](https://github.com/evdelph/Data-Business-Programming/blob/master/Images/victims.png)

* Gun_regulations_shootings.png: This chart shows the correlation between gun laws passed with the increase/decrease of gun shootings throughout the year. The size of each bubble represents the number of shootings, the y axis is the increase in gun regulations passed, and the x axis represents the year.
![2](https://github.com/evdelph/Data-Business-Programming/blob/master/Images/Gun_regulations_shootings.png)

* Changes_in_approval_ratings.png: It shows the relationship between changes in approval ratings versus changes in the rates of gun shootings. The trends between the two are meshed onto one line. The x-axis is across the time represented numerically.
![4](https://github.com/evdelph/Data-Business-Programming/blob/master/Images/changes_in_approval_ratings.png)

* shootings_on_map.html: This is a plot of all the shootings in the data file plotted onto a map using GMPlot. It allows the viewer to see how widespread the issue is. 
![8](https://github.com/evdelph/Data-Business-Programming/blob/master/Images/shootings_on_map.png)

### Data (.csv) Files Explained:
Main Sources:
* Approval.csv: It was obtained by copy and pasting data from The Presidency Project at University of California Santa Barbara. Some data columns (Such as President Names and Number) were discarded, and a column named Survey Month was added to better utilize the data; otherwise, the actual contents of the data were not touched. It can be found at this link:

http://www.presidency.ucsb.edu/data/popularity.php?pres=&sort=time&direct=DESC&Submit=DISPLAY

* shootings.csv: This was obtained from an article on the online news site Mother Jones, and the article will be linked below. It contains extensive information on what they consider to be mass-shootings in the United States. No data columns were added or removed from this set.

https://www.motherjones.com/politics/2012/12/mass-shootings-mother-jones-full-data/

### Other Sources:
* gun-laws.csv: This data set was obtained from StateFirearms.org  and contains the number of gun laws per state over the course of many years. This was an avenue we decided to briefly look at, but because it did not mesh well with our overall focus, we did not pursue it further. We kept the visualization involving it because we felt it would still be an interesting addition, and a lot of time was spent trying to create the chart using it. 
        
https://www.statefirearmlaws.org/table.html

### Other Data Files:
* ApprovalShootingMonthly.csv: This file summarizes information from shootings.csv and approval.csv. It is condensed into a monthly format, and only includes months that had shootings. The first column contains the month and year, the second column contains the average Presidential Approval Rating for that month, and the third column is the rating’s percent change from the prior month.
* MonthlyVictims.csv: This file summarizes the information from shootings.csv. It is condensed into a monthly format, and only includes months that had shootings. The first column contains the month and year, the second column includes the number of victims for that month (victims includes those directly killed or injured in the event).
* YearlyApprovalShootings.csv: This file summarizes information from shootings.csv and approval.csv. It is condensed into a yearly format, and only includes years that had shootings. The first contains the year, the second column contains the average approval rating for that year, and the third is the count of shootings in that year.
* cleansed_shootings.csv: This is a cleansed version of motherjones data, we removed the null values to prevent calculation errors
* shooting_laws.csv: It is from is a combination of just the number of shootings from motherjones and the total laws passed from Statefirearmlaws.org (both linked above).

### Python Files Explained:
* ApprovalVictims.py: This script uses Bokeh to create the chart contained in Victims.html.
* ApprovalShootingsNo.py: This script uses Bokeh to create the chart contained in ApprovalShootings.html.
* ApprovalOverTime.py: This script uses Bokeh to create the chart contained in Approval.html.
* Changes_in_approval_ratings_and_shootings.py: This script uses Seaborn and Matplotlib.pyplot
* Gun_regulations_versus_shootings.py: Uses Matplotlib.pyplot and seaborn to graph the relationship between gun regulations and shootings
* Shootings_on_map.py: This script uses a GoogleMaps api key from credentials.py, as well as the gmaps library to plot points on google maps
* credentials.py: Google api credientials for shootings_on_map

### Important Notes:
* Regardless of the method the data was summarized by (monthly, yearly, etc.), the dates in the data files have been formatted as Short Date. This was done because python, bokeh, and pandas played much more nicely with this format than any other that was tried. In cases where it is summarized monthly, the dates are always set to the first of the month. In yearly cases, they are set to the 1st of January. 
* All data in the summarized data files came from one of the 2 main source files, or the third file mentioned in Other Sources. They were manually created with that data to make creating the charts much simpler. 
* The Python scripts only work when they are in the same folder as the data files they are referencing.
