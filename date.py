#!/usr/bin/env python3
from enum import Enum
from math import floor

"""
# Why use an Enum for this?
---
1). Class-Level:  Enum members are defined at the class level, making them accessible without needing an instance of
                  the enum class.
2). Immutability: Enum members are immutable, meaning their values cannot be changed after definition.
3). Namespace:    Enums provide a namespace for related constants, helping to organize and access them in a structured
                  manner.
"""
class Epoch(Enum):
    year = 1970
    month = 1
    day = 1


class Date:
    # Kind-a equivalent to Java's static final variables.
    DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    """Represents a year, month, and day"""

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def is_leap_year(self):  # Basic math to determin if this is a leap year.
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)

    def get_days_since_year_start(self):
        days = self.day
        for day_cnt in range( 0, self.month - 1 ):  # month - 1 because the current month is not yet over.
            days += Date.DAYS_IN_MONTH[day_cnt]
            if day_cnt == 1 and self.is_leap_year():  # Got to check if this is a leap year
                days += 1
        return days

    def date_to_int(self):
        years = self.year - Epoch.year.value  # Years since epoch
        leap_years = floor( years / 4 )  # Leap years since epoch
        non_leap_years = years - leap_years  # Non Leap years since epoch
        # LeapYearDays + NonLeapYearDays + MonthDays
        days = (non_leap_years * 365) + (leap_years * 366) + self.get_days_since_year_start()
        return days

    def is_after(self, d2):
        return True if self.date_to_int() > d2.date_to_int() else False

    def __str__(self):  # Overloading string instead of writing print_date.
        return f'{self.year:4d}-{self.month:02d}-{self.day:02d}'
