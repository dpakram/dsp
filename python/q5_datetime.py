# Hint:  use Google to find python function

from datetime import datetime

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%m-%d-%Y")
    d2 = datetime.strptime(d2, "%m-%d-%Y")
    return abs((d2 - d1).days)

print "Days: %r" %(days_between(date_start, date_stop))

####b)  
date_start = '12312013'  
date_stop = '05282015'  


date_start = date_start[:2] + '-' + date_start[2:4] + "-" + date_start[4:]
date_stop = date_stop[:2] + '-' + date_stop[2:4] + "-" + date_stop[4:]	

print "Days: %r" %(days_between(date_start, date_stop))

####c)  
import calendar

date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

#create dictionary of month abbreviations and corresponding number

month_num = {name: num for num, name in enumerate(calendar.month_abbr) if num}

#creat variable with month abbreviation

month_start = date_start[3:6]
month_stop = date_stop[3:6]

#look up month abbreviation in dictionary
start_month = str(month_num[month_start])

#slice new date together, this time with month number
start_date = date_start[:3] + start_month + date_start[6:]

stop_month = str(month_num[month_stop])
stop_date = date_stop[:3] + stop_month + date_stop[6:]


def days_between2(d1, d2):
    d1 = datetime.strptime(d1, "%d-%m-%Y")
    d2 = datetime.strptime(d2, "%d-%m-%Y")
    return abs((d2 - d1).days)

print "Days: %r" %(days_between2(start_date, stop_date))

