# #4.5.1 Introduction to the datetime module:
# # it provides classes for working with date and time.
# #Date and time have countless uses and it's probably hard to find a production application that doesn't use them.
# #  -> event logging — thanks to the knowledge of date and time, we are able to determine when exactly a critical error occurs in our application. When creating logs, you can specify the date and time format;

# #  -> tracking changes in the database — sometimes it's necessary to store information about when a record was created or modified. The datetime module will be perfect for this case;

# # -> data validation — you'll soon learn how to read the current date and time in Python. Knowing the current date and time, you'll be able to validate various types of data, e.g., whether a discount coupon entered by a user in our application is still valid;

# # -> storing important information — can you imagine bank transfers without storing the information of when they were made? The date and time of certain actions must be preserved, and we must deal with it.


# #4.5.2 Getting the current local date and creating date objects
# #Example:
# from datetime import date

# today = date.today()

# print("Today:", today)
# print("Year:", today.year)
# print("Month:", today.month)
# print("Day:", today.day)

# #Output:
# # Today: 2025-12-29
# # Year: 2025
# # Month: 12
# # Day: 29


# # The today method returns a date object representing the current local date. Note that the date object has three attributes: year, month, and day.

# #To create a date object, you must pass the year, month, and day parameters as follows:
# from datetime import date
# my_date = date(2025,12,29)
# print(my_date)


# #4.5.3 Creating a date object from a timestamp:
# # The date class gives us the ability to create a date object from a timestamp.

# # In Unix, the timestamp expresses the number of seconds since January 1, 1970, 00:00:00 (UTC). This date is called the Unix epoch, because this is when the counting of time began on Unix systems.

# # The timestamp is actually the difference between a particular date (including time) and January 1, 1970, 00:00:00 (UTC), expressed in seconds.

# # To create a date object from a timestamp, we must pass a Unix timestamp to the fromtimestamp method.

# # For this purpose, we can use the time module, which provides time-related functions. One of them is a function called time(), which returns the number of seconds from January 1, 1970 to the current moment in the form of a float number. Take a look at the example in the editor.

# from datetime import date
# import time

# timestamp = time.time()
# print("Timestamp:", timestamp)

# d = date.fromtimestamp(timestamp)
# print("Date:", d)

# # If you run the sample code several times, you'll be able to see how the timestamp increments itself. It's worth adding that the result of the time function depends on the platform, because in Unix and Windows systems, leap seconds aren't counted.


# #4.5.4 Creating a date object using the ISO format:
# # The datetime module provides several methods to create a date object. One of them is the fromisoformat method, which takes a date in the YYYY-MM-DD format compliant with the ISO 8601 standard.
# # In our example, YYYY is 2019, MM is 11 (November), and DD is 04 (fourth day of November).
# # When substituting the date, be sure to add 0 before a month or a day that is expressed by a number less than 10.
# from datetime import date

# my_date = date(2019, 11, 4)
# print(my_date)
    


# # 4.5.5 The replace() method:
# # Sometimes you may need to replace the year, month, or day with a different value. You can’t do this with the year, month, and day attributes because they're read-only. In this case, you can use the method named replace.
# from datetime import date

# d = date(1991, 2, 5)
# print(d)

# d = d.replace(year=1992, month=1, day=16)
# print(d)
    
# The year, month, and day parameters are optional. You can pass only one parameter to the replace method, e.g., year, or all three as in the example.
# The replace method returns a changed date object, so you must remember to assign it to some variable.



# # 4.5.6 What day of the week is it?
# # One of the more helpful methods that makes working with dates easier is the method called weekday. It returns the day of the week as an integer, where 0 is Monday and 6 is Sunday. Run the code in the editor.
# from datetime import date

# d = date(2019, 11, 4)
# print(d.weekday())
    
# #The date class has a similar method called isoweekday, which also returns the day of the week as an integer, but 1 is Monday, and 7 is Sunday:
# from datetime import date

# d = date(2019, 11, 4)
# print(d.isoweekday())

# # As you can see, for the same date we get a different integer, but expressing the same day of the week. The integer returned by the isodayweek method follows the ISO 85601 specification.




# # 4.5.7 Creating time objects:
# # You already know how to present a date using the date object. The datetime module also has a class that allows you to present time. Can you guess its name? Yes, it's called time:e.g

# # time(hour, minute, second, microsecond, tzinfo, fold)

# #Let's look at how to create a time object in practice:

# from datetime import time

# t = time(14, 53, 20, 1)

# print("Time:", t)
# print("Hour:", t.hour)
# print("Minute:", t.minute)
# print("Second:", t.second)
# print("Microsecond:", t.microsecond)
    
# # In the example, we passed four parameters to the class constructor: hour, minute, second, and microsecond. Each of them can be accessed using the class attributes.



# #  4.5.8 The time module:
# # In addition to the time class, the Python standard library offers a module called time, which provides a time-related function. You already had the opportunity to learn the function called time when discussing the date class. Now we'll look at another useful function available in this module.

# #Example: Let's write a program that simulates a student's short nap. 
# import time

# class Student:
#     def take_nap(self, seconds):
#         print("I'm very tired. I have to take a nap. See you later!")
#         time.sleep(seconds)
#         print("I slept well! I feel fresh now!")

# student = Student()
# student.take_nap(10)

# #Here we used sleep() function-- which suspends program execution for the given number of seconds.
# # Note that the sleep function accepts only an integer or a floating point number.



# #4.5.9 The ctime() function:
# # The time module provides a function called ctime, which converts the time in seconds since January 1, 1970 (Unix epoch) to a string.

# #Example:

# import time

# timestamp = 1572879180
# print(time.ctime(timestamp))

# # The ctime function returns a string for the passed timestamp. In our example, the timestamp expresses November 4, 2019 at 14:53:00.
# # It's also possible to call the ctime function without specifying the time in seconds. In this case, the current time will be returned:E.g.
# import time 
# print(time.ctime())

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

# # The struct_time class also allows access to values using indexes. Index 0 returns the value in tm_year, while 8 returns the value in tm_isdst.

# # Let's look at how to use the struct_time class in practice.
# import time as t

# timestamp = 1572879180
# print(t.gmtime(timestamp))
# print(t.localtime(timestamp))

# #Output:
# # time.struct_time(tm_year=2019, tm_mon=11, tm_mday=4, tm_hour=14, tm_min=53, tm_sec=0, tm_wday=0, tm_yday=308, tm_isdst=0)
# # time.struct_time(tm_year=2019, tm_mon=11, tm_mday=4, tm_hour=20, tm_min=38, tm_sec=0, tm_wday=0, tm_yday=308, tm_isdst=0)


# # The example shows two functions that convert the elapsed time from the Unix epoch to the struct_time object. The difference between them is that the gmtime function returns the struct_time object in UTC, while the localtime function returns local time. For the gmtime function, the tm_isdst attribute is always 0.


# #4.5.11 The asctime() and mktime() functions:
# # The time module has functions that expect a struct_time object or a tuple that stores values according to the indexes presented when discussing the struct_time class. Run the example in the editor.
# import time

# timestamp = 1572879180
# st = time.gmtime(timestamp)

# print(time.asctime(st))
# print(time.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0)))
    
# # # Output:
# # Mon Nov 4 14:53:00 2019
# # 1572879180.0

# # The first of the functions, called asctime, converts a struct_time object or a tuple to a string. Note that the familiar gmtime function is used to get the struct_time object. If you don't provide an argument to the asctime function, the time returned by the localtime function will be used.

# # The second function called mktime converts a struct_time object or a tuple that expresses the local time to the number of seconds since the Unix epoch. In our example, we passed a tuple to it, which consists of the following values:

# # 2019 => tm_year
# # 11 => tm_mon
# # 4 => tm_mday
# # 14 => tm_hour
# # 53 => tm_min
# # 0 => tm_sec
# # 0 => tm_wday
# # 308 => tm_yday
# # 0 => tm_isdst


# 4.5.12 Creating datetime objects:

