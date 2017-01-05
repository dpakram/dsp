# -*- coding: utf-8 -*-

# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.

#Goals =  row[5]
#Goals Allowed = row[6]

import csv

f = open('football.csv')
file = csv.reader(f)
input_file = csv.DictReader(open("football.csv"))

'''
for row in input_file:
	print row
'''


#create empty lists and variables
goals = []
goals_allowed = []
difference = []
data = []
goal_value = 0
goal_allowed_value = 0
num = 0
r = 0

#create list of Goals and Goals allowed for each time
for row in input_file:
	goal_value = int(row["Goals"])
	goal_allowed_value = int(row["Goals Allowed"])
	goals.append(goal_value)
	goals_allowed.append(goal_allowed_value)


#find difference in goals and goals allowed, put into list
for i in range(len(goals)):
	d = goals[i] - goals_allowed[i]
	difference.append(d)

#find minum difference and index for value to re-locate
min_d = min(enumerate(difference), key = lambda i: abs(i[1]-1))
#print min_d



#enumerate function caused an error with previous football dictionary
#created new dictionary to fix issue
new_file = csv.DictReader(open("football.csv"))

#find row that matches index from minimum difference (min_d)
#print team with the smallest difference
for row in new_file:
	if num == min_d[0]:
		print row['Team']
		num += 1
	else:
		num += 1






