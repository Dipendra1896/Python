
# 4.6.13   LAB   The calendar module
# During this course, we took a brief look at the Calendar class. Your task now is to extend its functionality with a new method called count_weekday_in_year, which takes a year and a weekday as parameters, and then returns the number of occurrences of a specific weekday in the year.

# Use the following tips:

# Create a class called MyCalendar that extends the Calendar class;
# Create the count_weekday_in_year method with the year and weekday parameters. The weekday parameter should be a value between 0-6, where 0 is Monday and 6 is Sunday. The method should return the number of days as an integer;
# In your implementation, use the monthdays2calendar method of the Calendar class.
# The following are the expected results:
# Sample arguments:
# year=2019, weekday=0
# Expected output:
# 52

import calendar


class MyCalendar(calendar.Calendar):
    def count_weekday_in_year(self, year, weekday):
        current_month = 1
        number_of_days = 0
        while (current_month <= 12):
            for data in self.monthdays2calendar(year, current_month):
                if data[weekday][0] != 0:
                    number_of_days = number_of_days + 1

            current_month = current_month + 1
        return number_of_days

my_calendar = MyCalendar()
number_of_days = my_calendar.count_weekday_in_year(2020, calendar.MONDAY)

print(number_of_days)

import calendar

calendar.setfirstweekday(calendar.SUNDAY)
print(calendar.weekheader(3))



