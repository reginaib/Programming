# https://dodona.be/nl/courses/2802/series/29673/activities/1678476530
from datetime import date, timedelta


def first_difference(year1, year2):
    """
    >>> first_difference(2018, 2019)
    datetime.date(2019, 1, 1)
    >>> first_difference(2018, 2024)
    datetime.date(2024, 2, 29)
    >>> first_difference(2018, 2029)
    """
    year1 = date(year1, 1, 1)
    year2 = date(year2, 1, 1)

    if year1.weekday() != year2.weekday():
        return year2

    for delta in range(1, 366):
        day1 = year1 + timedelta(delta)
        day2 = year2 + timedelta(delta)
        if day1.day != day2.day:
            return year2 + timedelta(delta)


def reuse_calendar(year, previous=False):
    """
    >>> reuse_calendar(2018)
    2029
    >>> reuse_calendar(2018, True)
    2007
    >>> reuse_calendar(2019, previous=False)
    2030
    >>> reuse_calendar(2019, previous=True)
    2013
    """
    delta = -1 if previous else 1
    while first_difference(year, year + delta):
        delta += -1 if previous else 1
    return year + delta


def reuse_calendars(year, n, previous=False):
    """
    >>> reuse_calendars(2018, 10)
    [2029, 2035, 2046, 2057, 2063, 2074, 2085, 2091, 2103, 2114]
    >>> reuse_calendars(2018, 10, True)
    [2007, 2001, 1990, 1979, 1973, 1962, 1951, 1945, 1934, 1923]
    >>> reuse_calendars(2019, 10, previous=False)
    [2030, 2041, 2047, 2058, 2069, 2075, 2086, 2097, 2109, 2115]
    >>> reuse_calendars(2019, 10, previous=True)
    [2013, 2002, 1991, 1985, 1974, 1963, 1957, 1946, 1935, 1929]
    """
    result = []
    for _ in range(n):
        # override the year
        year = reuse_calendar(year, previous=previous)
        result.append(year)
    return result
