#Part I: Regular Expressions

import csv
from scipy.stats import itemfreq
import re
#from collections import Counter


f = csv.DictReader(open('faculty.csv'))

#--------------------------------------------------------------

'''

#Q1. Find how many different degrees there are, and their frequencies: 
#Ex: PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

#create list of degrees
l_degree = []
l_degree_split = []
f_degree = []
count = 0

for row in f:
	l_degree.append(row[' degree'])

#Separate each degree into separate list item
l_degree_split = [words for segments in l_degree for words in segments.split()]

#show individual degrees and frequence
print itemfreq(l_degree_split)

#count number of individual degrees
s_degree = set(l_degree_split)

for d in s_degree:
	if d != '0':
		count += 1

print "There are %d unique degrees" % count
'''
#--------------------------------------------------------------

#Q2 Find how many different titles there are, and their frequencies: 
#Ex: Assistant Professor, Professor
'''
l_titles = []

#create list of titles
for row in f:
	l_titles.append(row[' title'])

#create list of lists with title and frequency of title
print itemfreq(l_titles)

s_title = set(l_titles)

c_titles = len(s_title)

print "There are %d unique titles" % c_titles
'''
#--------------------------------------------------------------

#Q3 Search for email addresses and put them in a list. Print the list of email addresses.


l_email = []

for row in f:
	l_email.append(row[' email'])

l_email


#--------------------------------------------------------------

#Q4 Find how many different email domains there are 
#(Ex: mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.). 
#Print the list of unique email domains.

#l_email from Q3 has list of emails
l_domain = []

for e in l_email:
	match = re.search("@[\w.]+", e)
	domain = match.group()
	domain = domain[1:]
	l_domain.append(domain)

#print l_domain

s_domain = set(l_domain)
u_domain = len(s_domain)

print "There are %d unique email domains" % u_domain
print s_domain


