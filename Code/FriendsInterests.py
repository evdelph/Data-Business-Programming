import csv
from pprint import pprint
### PART  1 #####################################################################
# Step 1. load employees first ##################################################

'''
Load employees.csv and parse data into one main list, called list.
Then, parse list into two more lists, employeeid and employeename.
employeeid holds employee ids and employeename holds the employee
names. employeeid and employeename are converted into a list of 
dicionaries using the employee ids and names.

The following shows this coded and executed

'''

list = []
employeeid = []
employeename = []
full_employee_list = []

# Import employee data into list################################################
file_name = 'employees.csv'
with open(file_name) as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        for data in row:
            list.append(data)

# Separate main list into two lists#############################################
for data in list:
    if len(data) < 2:
        employeeid.append(data)
    else:
        employeename.append(data)

# Upload two separate lists into dicitonary#####################################

for i in range(len(employeename)):
    full_employee_list.append({'ID': employeeid[i], 'Name': employeename[i]})
pprint(full_employee_list)

# Step 2. Load friends.csv ######################################################
'''
This friends.csv file is loaded into a dictionary, where the key represents an 
employee (from the friends list). Each key, (employee) has a list of friends.
The dictionary 'people' is used to store this information.

The following code was used to execute creating the dictionary.
'''
people = {}
# Import friendship data into dictionary ########################################
file_name1 = 'friends.csv'
with open(file_name1) as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        for p in row:
            if p not in people:
                people[p] = { 'Friends': []}
        people[row[0]]['Friends'].append(row[1])
        people[row[1]]['Friends'].append(row[0])
    pprint(people)

 # Step 3. Answer Questions #####################################################
 
 # Question 1- How many employees are there?#####################################

def cnt():
    '''
    (None) -> int
    Counts the number of ids in full_employee_list
    to return the number of employees in the list

    >>> print(cnt())
    10
    '''
    counter = 0
    for ids in full_employee_list:
        counter += 1
    return counter

# Qustion 2- What is the average friends per person, most, and few?##############

# 2.1 Average friends############################################################

def avg():
    '''
    (None)-> int
    Loops through the length of friend lists for each
    person and adds up the length of all lists. The sum
    of length of all lists is divided by the return of the
    cnt() function, it returns 10.

    The function returns the average number of friends 
    each person has.
     >>> print(avg())
     2.4
    '''
    how_many_friends = 0
    friends_total = 0
    friends_avg = 0
    for person in people:
        how_many_friends = len(people[person]['Friends'])
        friends_total += how_many_friends
    friends_avg = friends_total/cnt()
    return friends_avg

# 2.2 Max Friends ################################################################

def max_f():
    '''
    (None) -> int
    Loops through the length of each person's friends list and returns
    the maximum number, or the friends with the longest list.

    >>> print(max_f())
    3
    '''
    max_num = 0
    for person in people:
        how_many_friends = len(people[person]['Friends'])
        if how_many_friends > max_num:
            max_num = how_many_friends
    return max_num

# 2.3 Min Friends ###############################################################

def min_f():
    '''
    (None) -> int
    Loops through the length of each person's list and returns the number of the 
    least friends, or the shortest list.

    >>> print(min_f())
    1
    '''
    i = 1
    for person in people:
        for i in people:
            min_num = len(people[person]['Friends'])
            current_num = len(people[i]['Friends'])
            if current_num < min_num:
                min_num = current_num
        return min_num

#### OUTPUT FOR PROBLEMs 1 & 2 ANSWERS #############################################

print('There are',cnt(),'employees.')
print('The average number of friends is',avg(),)

# Max Friends Answer
for person in people:
    if max_f()== len(people[person]['Friends']):
        print(person,':',max_f(),'friends')

# Min Friends Answer 
for person in people:
    if min_f() ==len(people[person]['Friends']):
        print(person,':',min_f(),'friend')


### Question 3- Friends of Friends #################################################
'''
For this part, 'Friends of Friends' list was added to people dictionary.
Below is the following code the shows the creation of the 'Friends of Friends' key
and the data importation through the use of the fof() function.
'''

## Create FOF list #################################################################
for person in people:
    if 'Friends of Friends' not in people[person]:
        people[person]['Friends of Friends'] = []

### Add data to fof through fof function ###########################################
def fof():
    '''
    (None)-> dictionary
    Loops through people dicionary to find everybody's friends of friends.  It
    excludes people that are friends, and there's no duplicates

    >>> print(fof())
    { '0': {'Friends': ['1','2'], 'Friends of Friends':['3']},
    '1': {'Friends': ['0','2','3'], 'Friends of Friends: ['4']},
    '''
    for person in people:
        for friend in people[person]['Friends']:
            for fof in people[friend]['Friends']:
                if fof != person:
                    if fof not in people[person]['Friends']:
                        if fof not in people[person]['Friends of Friends']:
                            people[person]['Friends of Friends'].append(fof)
                        else:
                            pass
    return people

# Question 3 Answer #################################################################
pprint(fof())

# Question 4- Mutual Friends ########################################################
'''
The following code shows function m_f() that returns the count of mutual friends a 
given pair of employees have.
'''
 # Mutual Friends Function ##########################################################
def m_f():
    '''
    (None) -> tuple
    Loops through friends lists and returns the count of mutual frirends.
    Prints the two employee ids and their count of mutual friends.

    >>> m_f()
    ('0','1','1')
    ('0','2','1')
    '''
    mutual_count = 0
    for person1 in people:
        for person2 in people:
            for mutual_f in people[person1]['Friends']:
                if person1 < person2 and mutual_f in people[person2]['Friends']:
                    mutual_count += 1
            if mutual_count > 0:
                print((person1,person2,mutual_count))
            mutual_count = 0
 
# Question 4 Answer #################################################################
m_f()
                            
# Question 5- If NOT friends, print mutual friends ##################################
'''
The following code shows the function nm_f() that loops throughs the employees friends
list and returns the mutual friends. However, the employees are NOT friends.
'''

## Non-Mutual Friends Function #######################################################
def nm_f():
    '''
    (None)-> tuple
    Loops through employees who aren't friends, and loops through their lists to find
    mutual friends.

    Prints out the two employees who aren't friends, and their mutual friend count
    >>> nm_f()
    ('0','3',2)
    ('0','4',1)
    '''
    mutual_count1 = 0
    for person1 in people:
        for person2 in people:
            for mutual in people[person1]['Friends']:
                if person1 < person2 and mutual in people[person2]['Friends'] and person1 not in people[person2]['Friends']:
                    mutual_count1 += 1
            if mutual_count1 > 0:
                print((person1,person2,mutual_count1))
            mutual_count1 = 0

# Question 5 Answer ##################################################################
nm_f()

## Part 2 ############################################################################

## Question 6 ########################################################################
'''
The following code shows the creation of two dictionaries based on imported data from
the interests.csv file. To make the dictionaries the data was loaded into one main list,
called lst. 

Then the data was parsed into two lists, intersts_id and interests. interests_id contains 
the employee ids and the intersts list contains the actual interests.

'''

# Import interest data ###############################################################
interests_id = []
interests = []
file_name = 'interests.txt'

with open(file_name) as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        interests_id.append(row[0][0])
        interests.append(row[0][2:])
lst = []
for i in range(len(interests)):
    lst.append([interests_id[i]] + [interests[i]])
# Question 6.1 Print Interest Dictionary ############################################
'''
From lst, create the dictionary int_dict where the employeeid is the key
and the value is a list of interests
'''
int_d = {}

def int_dict():
    '''
    (None) -> dictionary
    Loops through lst to find ids aren't in the list and append them to the new
    dictionary, int_d

    >>> int_dict()
    {'0': {'interests':['Hadoop', 'Big Data', 'HBas', 'Java', 'Spark', 'Storm', 'Cassandra']}
    '1':{ 'interests':['NoSQL','MongoDB','Cassandra','HBase','Postgres']}
    '''
    for row in lst:
        for p in row:
            if p not in int_d and len(p) == 1 and p != 'R':
                int_d[p] = {'interests': []}
        int_d[row[0]]['interests'].append(row[1])
    pprint(int_d)
## OUTPUT For First Dictionary #######################################################

int_dict()
# Question 6.2 Print Reversed Interest Dictionary ####################################
'''
A second master list of data was created to flip the order in which data entered the
list. Here, interests and the employee ids are appended in reveresed order compared 
to lst, so that when the dictionary is created, the interests are the key and the 
employee ids are in the list.
'''

# Create a new list where interests and employee ids are flipped #####################
lst2 = []
for i in range(len(interests)):
    lst2.append([interests[i]] + [interests_id[i]])

# From lst two, create int_d2 ########################################################

int_d2 = {}
for row in lst2:
    for p in row:
        if p not in int_d2 and len(p) != 1 or p == 'R':
            int_d2[p] = {'interests_id': []}
    int_d2[row[0]]['interests_id'].append(row[1])
pprint(int_d2)


## Question 7: recommending friends based on shared interests (excluding current friendships).

# Add recommendations list to int_d #########################################################
for person in int_d:
    if 'recommendations' not in int_d[person]:
        int_d[person]['recommendations']= []

### Add interests to dictionary ##############################################################
for person1 in people:
    for person2 in people:
        for mutual in people[person1]['Friends']:
            for person1 in int_d:
                for shared in int_d[person1]['interests']:
                    if shared in int_d[person2]['interests']:
                        if person1 < person2 and person1 != person2:
                            if person1 not in people[person2]['Friends']:
                                if person1 not in int_d[person2]['recommendations']:
                                    int_d[person2]['recommendations'].append(person1)
                                    if person2 not in int_d[person1]['recommendations']:
                                        int_d[person1]['recommendations'].append(person2)
                                        
                                       
    break
pprint(int_d)
## Question 8: Listing people who are FOF and have shared interests.#########################
'''
shared1 is a list that will  be added to the dictionary that shows the ids with
shared data science topics
'''
shared1 = []
for person1 in people:
    for fof in people[person1]['Friends of Friends']:
        for shared in int_d[person1]['interests']:
            if shared in int_d[fof]['interests']:
                shared1.append(shared)
                if person1 < fof and person1 != fof:
                    if person1 in people[fof]['Friends of Friends']:
                        if len(shared1) > 1:
                            print((person1, fof, shared1))

################### SAMPLE OUTPUT FOR 6.2, 7, and 8 ##########################################

'''
6.2
{'Big Data': {interests_id ['0','8','9']},
'C++': {'interests_id':[5]},
'Cassandra': {'interests_id':['0','1']}

7
{'0':'interests: ['Hadoop',
                  'Big Data',
                  'HBas',
                  'Java'
                  'Spark'
                  'Storm'
                  'Cassandra']
     'recommendations: ['5','8','9']},
{'1': {'interests: ['NoSQL', 'MongoDB', 'Cassandra', 'HBase', 'Postgres'],
       'recommendations': []}
'2': {'interests': ['Python',
                   'skikit-learn',
                   'numpy'
                   'statsmodels',
                   'pandas'],
     'recommendations': ['5']}

8
('3', '5', ['R','Python'])
('4','7',['R','Python', 'machine learning'])
'''
