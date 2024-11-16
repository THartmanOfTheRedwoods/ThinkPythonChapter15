#!/usr/bin/env python3

from date import Date

def main():
    d0 = Date(2024, 11, 15)
    d1 = Date(2024, 6, 22)
    d2 = Date(1933, 6, 22)
    d3 = Date(1900, 6, 22)
    d4 = Date(1600, 6, 22)
    print(d1, d2, d3, d4)
    print("-"*120)
    print(d1.is_leap_year())  # Is a Leap Year
    print(d2.is_leap_year())  # Not a Leap Year
    print(d3.is_leap_year())  # Not a Leap Year
    print(d4.is_leap_year())  # Is a Leap Year
    print("-"*120)
    print(d1.get_days_since_year_start())  # Leap Year
    print(d2.get_days_since_year_start())  # Not a Leap Year
    print("-"*120)
    print( Date(2024, 11,15).date_to_int() )  # 20043 as of 11/15/2024
    print( Date(2024, 10,15).date_to_int() )  # 20012 as of 10/15/2024
    print("-"*120)
    print(d0.is_after(Date(2024, 11, 15)))
    print(d0.is_after(d1))
    print(d0.is_after(Date(2024, 12, 15)))


if __name__ == '__main__':
    main()