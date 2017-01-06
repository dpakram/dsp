#Part II - Write CSV File

#Q5 Write email addresses from Part I to csv file called emails.csv

import csv

file = csv.DictReader(open('faculty.csv'))

#create list of emails
l_email = []
for row in file:
	l_email.append(row[' email'])


#create csv file with list of emails
f = open("emails.csv", "wb")
writer = csv.writer(f)
for email in l_email:
	writer.writerow([email,])
f.close()

