#4.5.1 Introduction to the datetime module:
# it provides classes for working with date and time.
#Date and time have countless uses and it's probably hard to find a production application that doesn't use them.
#  -> event logging — thanks to the knowledge of date and time, we are able to determine when exactly a critical error occurs in our application. When creating logs, you can specify the date and time format;

#  -> tracking changes in the database — sometimes it's necessary to store information about when a record was created or modified. The datetime module will be perfect for this case;

# -> data validation — you'll soon learn how to read the current date and time in Python. Knowing the current date and time, you'll be able to validate various types of data, e.g., whether a discount coupon entered by a user in our application is still valid;

# -> storing important information — can you imagine bank transfers without storing the information of when they were made? The date and time of certain actions must be preserved, and we must deal with it.


#4.5.2 Getting the current local date and creating date objects
#Example:
from datetime import date

today = date.today()

print("Today:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)

#Output:
# Today: 2025-12-29
# Year: 2025
# Month: 12
# Day: 29


# The today method returns a date object representing the current local date. Note that the date object has three attributes: year, month, and day.

#To create a date object, you must pass the year, month, and day parameters as follows:
from datetime import date
my_date = date(2025,12,29)
print(my_date)


#4.5.3 Creating a date object from a timestamp:
# The date class gives us the ability to create a date object from a timestamp.

# In Unix, the timestamp expresses the number of seconds since January 1, 1970, 00:00:00 (UTC). This date is called the Unix epoch, because this is when the counting of time began on Unix systems.

# The timestamp is actually the difference between a particular date (including time) and January 1, 1970, 00:00:00 (UTC), expressed in seconds.

# To create a date object from a timestamp, we must pass a Unix timestamp to the fromtimestamp method.

# For this purpose, we can use the time module, which provides time-related functions. One of them is a function called time(), which returns the number of seconds from January 1, 1970 to the current moment in the form of a float number. Take a look at the example in the editor.

from datetime import date
import time

timestamp = time.time()
print("Timestamp:", timestamp)

d = date.fromtimestamp(timestamp)
print("Date:", d)

# If you run the sample code several times, you'll be able to see how the timestamp increments itself. It's worth adding that the result of the time function depends on the platform, because in Unix and Windows systems, leap seconds aren't counted.


#4.5.4 Creating a date object using the ISO format:
# The datetime module provides several methods to create a date object. One of them is the fromisoformat method, which takes a date in the YYYY-MM-DD format compliant with the ISO 8601 standard.
# In our example, YYYY is 2019, MM is 11 (November), and DD is 04 (fourth day of November).
# When substituting the date, be sure to add 0 before a month or a day that is expressed by a number less than 10.
from datetime import date

my_date = date(2019, 11, 4)
print(my_date)
    


# 4.5.5 The replace() method:
# Sometimes you may need to replace the year, month, or day with a different value. You can’t do this with the year, month, and day attributes because they're read-only. In this case, you can use the method named replace.
from datetime import date

d = date(1991, 2, 5)
print(d)

d = d.replace(year=1992, month=1, day=16)
print(d)
    
# The year, month, and day parameters are optional. You can pass only one parameter to the replace method, e.g., year, or all three as in the example.
# The replace method returns a changed date object, so you must remember to assign it to some variable.



# 4.5.6 What day of the week is it?
# One of the more helpful methods that makes working with dates easier is the method called weekday. It returns the day of the week as an integer, where 0 is Monday and 6 is Sunday. Run the code in the editor.
from datetime import date

d = date(2019, 11, 4)
print(d.weekday())
    
#The date class has a similar method called isoweekday, which also returns the day of the week as an integer, but 1 is Monday, and 7 is Sunday:
from datetime import date

d = date(2019, 11, 4)
print(d.isoweekday())

# As you can see, for the same date we get a different integer, but expressing the same day of the week. The integer returned by the isodayweek method follows the ISO 85601 specification.




# 4.5.7 Creating time objects:
# You already know how to present a date using the date object. The datetime module also has a class that allows you to present time. Can you guess its name? Yes, it's called time:e.g

# time(hour, minute, second, microsecond, tzinfo, fold)

#Let's look at how to create a time object in practice:

from datetime import time

t = time(14, 53, 20, 1)

print("Time:", t)
print("Hour:", t.hour)
print("Minute:", t.minute)
print("Second:", t.second)
print("Microsecond:", t.microsecond)
    
# In the example, we passed four parameters to the class constructor: hour, minute, second, and microsecond. Each of them can be accessed using the class attributes.



#  4.5.8 The time module:
# In addition to the time class, the Python standard library offers a module called time, which provides a time-related function. You already had the opportunity to learn the function called time when discussing the date class. Now we'll look at another useful function available in this module.

#Example: Let's write a program that simulates a student's short nap. 
import time

class Student:
    def take_nap(self, seconds):
        print("I'm very tired. I have to take a nap. See you later!")
        time.sleep(seconds)
        print("I slept well! I feel fresh now!")

student = Student()
student.take_nap(10)

#Here we used sleep() function-- which suspends program execution for the given number of seconds.
# Note that the sleep function accepts only an integer or a floating point number.


#4.5.9 The ctime() function:
# The time module provides a function called ctime, which converts the time in seconds since January 1, 1970 (Unix epoch) to a string.

#Example:

import time

timestamp = 1572879180
print(time.ctime(timestamp))

# The ctime function returns a string for the passed timestamp. In our example, the timestamp expresses November 4, 2019 at 14:53:00.
# It's also possible to call the ctime function without specifying the time in seconds. In this case, the current time will be returned:E.g.
import time 
print(time.ctime())

# #4.5.10 The gmtime() and localtime() functions:
# Some of the functions available in the time module require knowledge of the struct_time class, but before we get to know them, let's see what the class looks like:
# time.struct_time:
#     tm_year   # Specifies the year.
#     tm_mon    # Specifies the month (value from 1 to 12)
#     tm_mday   # Specifies the day of the month (value from 1 to 31)
#     tm_hour   # Specifies the hour (value from 0 to 23)
#     tm_min    # Specifies the minute (value from 0 to 59)
#     tm_sec    # Specifies the second (value from 0 to 61 )
#     tm_wday    # Specifies the weekday (value from 0 to 6)
#     tm_yday   # Specifies the year day (value from 1 to 366)
#     tm_isdst  # Specifies whether daylight saving time applies (1 – yes, 0 – no, -1 – it isn't known)
#     tm_zone   # Specifies the timezone name (value in an abbreviated form)
#     tm_gmtoff # Specifies the offset east of UTC (value in seconds)

# The struct_time class also allows access to values using indexes. Index 0 returns the value in tm_year, while 8 returns the value in tm_isdst.

# Let's look at how to use the struct_time class in practice.
import time as t

timestamp = 1572879180
print(t.gmtime(timestamp))
print(t.localtime(timestamp))

#Output:
# time.struct_time(tm_year=2019, tm_mon=11, tm_mday=4, tm_hour=14, tm_min=53, tm_sec=0, tm_wday=0, tm_yday=308, tm_isdst=0)
# time.struct_time(tm_year=2019, tm_mon=11, tm_mday=4, tm_hour=20, tm_min=38, tm_sec=0, tm_wday=0, tm_yday=308, tm_isdst=0)


# The example shows two functions that convert the elapsed time from the Unix epoch to the struct_time object. The difference between them is that the gmtime function returns the struct_time object in UTC, while the localtime function returns local time. For the gmtime function, the tm_isdst attribute is always 0.


#4.5.11 The asctime() and mktime() functions:
# The time module has functions that expect a struct_time object or a tuple that stores values according to the indexes presented when discussing the struct_time class. Run the example in the editor.
import time

timestamp = 1572879180
st = time.gmtime(timestamp)

print(time.asctime(st))
print(time.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0)))
    
# # Output:
# Mon Nov 4 14:53:00 2019
# 1572879180.0

# The first of the functions, called asctime, converts a struct_time object or a tuple to a string. Note that the familiar gmtime function is used to get the struct_time object. If you don't provide an argument to the asctime function, the time returned by the localtime function will be used.

# The second function called mktime converts a struct_time object or a tuple that expresses the local time to the number of seconds since the Unix epoch. In our example, we passed a tuple to it, which consists of the following values:

# 2019 => tm_year
# 11 => tm_mon
# 4 => tm_mday
# 14 => tm_hour
# 53 => tm_min
# 0 => tm_sec
# 0 => tm_wday
# 308 => tm_yday
# 0 => tm_isdst


#4.5.12 Creating datetime objects:
#In the datetime module, date and time can be represented either as separate objects or as one object. The class that combines date and time is called datetime.

#datetime(year, month, day, hour, minute, second, microsecond, tzinfo, fold)

import datetime as dt

print("Datetime:" ,dt.datetime(2019, 11, 4, 14, 53, 0))
print("Date:",dt.date(2019, 11, 4))
print("Time", dt.time(14, 53, 0))

# The example creates a datetime object representing November 4, 2019 at 14:53:00. All parameters passed to the constructor go to read-only class attributes. They're year, month, day, hour, minute, second, microsecond, tzinfo, and fold.

# The example shows two methods that return two different objects. The method called date returns the date object with the given year, month, and day, while the method called time returns the time object with the given hour and minute.


#4.5.13 Methods that return the current date and time:
# The datetime class has several methods that return the current date and time. These methods are:

# -> today() — returns the current local date and time with the tzinfo attribute set to None;
# -> now() — returns the current local date and time the same as the today method, unless we pass the optional argument tz to it. The argument of this method must be an object of the tzinfo subclass;
# -> utcnow() — returns the current UTC date and time with the tzinfo attribute set to None.It is depreciated and will be removed in future version
 
#Example:
from datetime import datetime, timezone

print("today:", datetime.today())
print("now:", datetime.now())
print("utcnow:", datetime.now(timezone.utc))
    

#4.5.14 Getting a timestamp:
# There are many converters available on the Internet that can calculate a timestamp based on a given date and time, but how can we do it in the datetime module?
#This is possible with the timestamp method provided by the datetime class.
from datetime import datetime

dt = datetime(2020, 10, 4, 14, 55)
print("Timestamp:", dt.timestamp())
    
# The timestamp method returns a float value expressing the number of seconds elapsed between the date and time indicated by the datetime object and January 1, 1970, 00:00:00 (UTC).    

# 4.5.15 Date and time formatting:  All datetime module classes presented so far have a method called strftime. This is a very important method, because it allows us to return the date and time in the format we specify.
#The strftime method takes only one argument in the form of a string specifying a format that can consist of directives.
# A directive is a string consisting of the character % (percent) and a lowercase or uppercase letter. For example, the directive %Y means the year with the century as a decimal number. Let's see it in an example:

from datetime import date

d = date(2025,12,29)
print(d.strftime('%Y/%m/%d'))

# You can put any characters in the format, but only recognizable directives will be replaced with the appropriate values. In our format we've used the following directives:

# -> %Y – returns the year with the century as a decimal number. In our example, this is 2020.
# -> %m – returns the month as a zero-padded decimal number. In our example, it's 01.
# -> %d – returns the day as a zero-padded decimal number. In our example, it's 04.


# Time formatting works in the same way as date formatting, but requires the use of appropriate directives. Let's take a closer look at a few of them in the editor.
from datetime import time
from datetime import datetime

t = time(14, 53)
print(t.strftime("%H:%M:%S"))

dt = datetime(2020, 11, 4, 14, 53)
print(dt.strftime("%y/%B/%d %H:%M:%S"))
    
# The first of the formats used concerns only time. As you can guess, %H returns the hour as a zero-padded decimal number, %M returns the minute as a zero-padded decimal number, while %S returns the second as a zero-padded decimal number. In our example, %H is replaced by 14, %M by 53, and %S by 00.

# The second format used combines date and time directives. There are two new directives, %Y and %B. The directive %Y returns the year without a century as a zero-padded decimal number (in our example it's 20). The %B directive returns the month as the locale’s full name (in our example, it's November).

# 4.5.16 The strftime() function in the time module:
# You probably won't be surprised to learn that the strftime function is available in the time module. It differs slightly from the strftime methods in the classes provided by the datetime module because, in addition to the format argument, it can also take (optionally) a tuple or struct_time object.

# If you don't pass a tuple or struct_time object, the formatting will be done using the current local time. Take a look at the example in the editor.

import time

timestamp = 1572879180
st = time.gmtime(timestamp)

print(time.strftime("%Y/%m/%d %H:%M:%S", st))
print(time.strftime("%Y/%m/%d %H:%M:%S"))
    
#Output: 
# 2019/11/04 14:53:00      formatting is done using given timestamp
# 2025/12/30 07:32:14      formatting is done using current local time

# 4.5.17 The strptime() method:
# Knowing how to create a format can be helpful when using a method called strptime in the datetime class. Unlike the strftime method, it creates a datetime object from a string representing a date and time.

# The strptime method requires you to specify the format in which you saved the date and time. Let's see it in an example:
from datetime import datetime
print(datetime.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))
    
# In the example, we've specified two required arguments. The first is a date and time as a string: "2019/11/04 14:53:00", while the second is a format that facilitates parsing to a datetime object. Be careful, because if the format you specify doesn't match the date and time in the string, it'll raise a ValueError.


# Note: In the time module, you can find a function called strptime, which parses a string representing a time to a struct_time object. Its use is analogous to the strptime method in the datetime class:
# import time
# print(time.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))

# 4.5.18 Date and time operations:
# Sooner or later you'll have to perform some calculations on the date and time. Fortunately, there's a class called timedelta in the datetime module that was created for just such a purpose.

# To create a timedelta object, just perform a subtraction on the date or datetime objects, just like we did in the example in the editor. Run it.

from datetime import date
from datetime import datetime

d1 = date(2020, 11, 4)
d2 = date(2019, 11, 4)

print(d1 - d2)

dt1 = datetime(2020, 11, 4, 0, 0, 0)
dt2 = datetime(2019, 11, 4, 14, 53, 0)

print(dt1 - dt2)

#Result:
# 366 days, 0:00:00
# 365 days, 9:07:00
# The example shows subtraction for both the date and datetime objects. In the first case, we receive the difference in days, which is 366 days. Note that the difference in hours, minutes, and seconds is also displayed. In the second case, we receive a different result, because we specified the time that was included in the calculations. As a result, we receive 365 days, 9 hours, and 7 minutes.

# 4.5.19 Creating timedelta objects:
# You've already learned that a timedelta object can be returned as a result of subtracting two date or datetime objects.

# Of course, you can also create an object yourself. For this purpose, let's get acquainted with the arguments accepted by the class constructor, which are: days, seconds, microseconds, milliseconds, minutes, hours, and weeks. Each of them is optional and defaults to 0.
#example:
from datetime import timedelta

delta = timedelta(weeks=2, days=2, hours=3)
print(delta)

#Result : 16 days, 3:00:00

# The result of 16 days is obtained by converting the weeks argument to days (2 weeks = 14 days) and adding the days argument (2 days). This is normal behavior, because the timedelta object only stores days, seconds, and microseconds internally. 
#Similarly, the hour argument is converted to minutes. Take a look at the example below:
from datetime import timedelta

delta = timedelta(weeks= 2, days = 2, hours= 3)
print("Days:", delta.days)
print("Seconds:", delta.seconds)
print("Microseconds:", delta.microseconds)

#Result: 
# Days: 16
# Seconds: 10800
# Microseconds: 0

# The result of 10800 is obtained by converting 3 hours into seconds. In this way the timedelta object stores the arguments passed during its creation. Weeks are converted to days, hours and minutes to seconds, and milliseconds to microseconds.

# You already know how the timedelta object stores the passed arguments internally. Let's see how it can be used in practice.Look at some operations supported by the datetime module classes

from datetime import timedelta
from datetime import date
from datetime import datetime

delta = timedelta(weeks = 2, days = 2, hours = 2)
print(delta)

delta2 = delta * 2
print(delta2)

d = date(2019, 10, 4) + delta2
print(d)

dt = datetime(2019, 10, 4, 14, 53) + delta2
print(dt)

# Result:
# 16 days, 2:00:00
# 32 days, 4:00:00
# 2019-11-05
# 2019-11-05 18:53:00

# The timedelta object can be multiplied by an integer. In our example, we multiply the object representing 16 days and 2 hours by 2. As a result, we receive a timedelta object representing 32 days and 4 hours.

# Note that both days and hours have been multiplied by 2. Another interesting operation using the timedelta object is adding. In the example, we've added the timedelta object to the date and datetime objects.

# As a result of these operations, we receive date and datetime objects increased by days and hours stored in the timedelta object.

# The presented multiplication operation allows you to quickly increase the value of the timedelta object, while multiplication can also help you get a date from the future.

# Of course, the timedelta, date, and datetime classes support many more operations. We encourage you to familiarize yourself with them in the documentation.

# 4.5.20   LAB   The datetime and time modules
# During this course, you learned about the strftime method, which requires knowledge of directives to create a format. It's now time to put these directives into practice.

# By the way, you'll have the opportunity to practice working with documentation, because you'll have to find directives that you don't yet know.

# Here's your task:
# Write a program that creates a datetime object for November 4, 2020 , 14:53:00. The object created should call the strftime method with the appropriate format to display the following result:2020/11/04 14:53:00
# 20/November/04 14:53:00 PM
# Wed, 2020 Nov 04
# Wednesday, 2020 November 04
# Weekday: 3
# Day of the year: 309
# Week number of the year: 44

#code for desired output:
from datetime import datetime

my_date = datetime(2020, 11, 4, 14, 53)

print(my_date.strftime("%Y/%m/%d %H:%M:%S"))
print(my_date.strftime("%y/%B/%d %H:%M:%S %p"))
print(my_date.strftime("%a, %Y %b %d"))
print(my_date.strftime("%A, %Y %B %d"))
print(my_date.strftime("Weekday: %w"))
print(my_date.strftime("Day of the year: %j"))
print(my_date.strftime("Week number of the year: %W"))
    