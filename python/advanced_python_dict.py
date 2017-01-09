#Part III - Dictionary

#--------------------------------------------------------

#Q6. Create a dictionary from faculty csv file
#{'key- last name': [['degree', 'title', 'email']]}

import csv
import re
import random
from collections import OrderedDict



file = csv.DictReader(open('faculty.csv'))

l_first_last = []
l_last = []
faculty_dict = {}
ld = []

#create list of dictionaries
def open_file(file):
	for row in file:
		ld.append(row)
	return ld

ld = open_file(file)

#create dictionary
def create_faculty_dict(data):
	faculty_dict = {}
	for row in data:
		names = row['name'].split()
		last_name = names[-1]
		if last_name in faculty_dict:
			faculty_dict[last_name].append(row[' degree'])
			faculty_dict[last_name].append(row[' title'])
			faculty_dict[last_name].append(row[' email'])
		else:
			faculty_dict[last_name] = []
			faculty_dict[last_name].append(row[' degree'])
			faculty_dict[last_name].append(row[' title'])
			faculty_dict[last_name].append(row[' email'])
	return faculty_dict

faculty_dict = create_faculty_dict(ld)
#print faculty_dict

#print a random sample with 3 keys and values in the dictionary 
def sample(d, n):
	random_entry = random.sample(d, n)
	sample_dict = {}
	for name in random_entry:
		if name in faculty_dict:
			sample_dict[name] = faculty_dict[name]
	return sample_dict

#print sample(faculty_dict, 3)

#--------------------------------------------------------
'''
Q7. The previous dictionary does not have the best design for keys. Create a new dictionary with keys as:

professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], 
('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'], 
('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], 
('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], 
('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu'] }
'''

#create dictionary
def create_professor_dict(data):
	professor_dict = {}
	for row in data:
		names = row['name'].split()
		last_name = names[-1]
		if len(names) == 3:
			first_name = names[0] + ' ' + names[1]
		else:
			first_name = names[0]
		last_first_names = (first_name, last_name)
		
		professor_dict[last_first_names] = []
		professor_dict[last_first_names].append(row[' degree'])
		professor_dict[last_first_names].append(row[' title'])
		professor_dict[last_first_names].append(row[' email'])
		
		
	return professor_dict

professor_dict = create_professor_dict(ld)

def sample(d, n):
	random_entry = random.sample(d, n)
	sample_dict = {}
	for name in random_entry:
		if name in professor_dict:
			sample_dict[name] = professor_dict[name]
	return sample_dict

#print sample(professor_dict, 3)

#--------------------------------------------------------

#Q8. It looks like the current dictionary is printing by first name. 
#Print out the dictionary key value pairs based on alphabetical orders 
#of the last name of the professors

from operator import itemgetter
from collections import OrderedDict

print OrderedDict(sorted(professor_dict.items(), key=lambda t: t[0][-1]))





