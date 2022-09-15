#1

from datetime import *

from time import *
now = datetime.now()

print("now is: ",now)

print("current year: ",datetime.today().year)

print("current weekday: ", datetime.today().strftime('%A'))


"""

year = int(input("enter a year: "))

# To get year (integer input) from the user
# year = int(input("Enter a year: "))

# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))

# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))

# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
    print("{0} is not a leap year".format(year))

"""
datetime_str = '09/19/18 13:55:26'

datetime_object = datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')

print(type(datetime_object))
print(datetime_object)


#2.1

#substract 15 days from today    
current_datetime = datetime.today() - timedelta(days=15)
previos_datetime = datetime.strftime(current_datetime,'%y-%m-%d')
print("15 days ago was: ",previos_datetime)


#2.2

current_datetime = datetime.today() + timedelta(days=7)
next_week = datetime.strftime(current_datetime,'%y-%m-%d')
print("in one week will be: ",next_week)

#2.3
start_date = datetime(year=2021, month=1, day=1) 
payday = start_date + timedelta(days=24)

payday_conv = datetime.strftime(payday,'%d %B, %Y')

print(f"Hello Friedrich, your rent of 300 € is due on {payday_conv}.")