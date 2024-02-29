# https://dodona.be/nl/courses/2802/series/29675/activities/1506545778
"""
>>> born = read_dates('poets.txt13', 1)
>>> born['Emily Brontë']
datetime.date(1818, 7, 30)
>>> born['Walt Whitman']
datetime.date(1819, 5, 31)
>>> born['Phillis Wheatley']
Traceback (most recent call last):
KeyError: 'Phillis Wheatley'

>>> died = read_dates('poets.txt14', 2)
>>> died['Emily Brontë']
datetime.date(1848, 12, 19)
>>> died['Walt Whitman']
Traceback (most recent call last):
KeyError: 'Walt Whitman'
>>> died['Phillis Wheatley']
datetime.date(1784, 12, 5)

>>> lifespan('Emily Brontë', born, died)
[1818, 1819, 1820, 1821, 1822, 1823, 1824, 1825, 1826, 1827, 1828, 1829, 1830, 1831, 1832, 1833, 1834, 1835, 1836, 1837, 1838, 1839, 1840, 1841, 1842, 1843, 1844, 1845, 1846, 1847, 1848]
>>> lifespan('Walt Whitman', born, died)
Traceback (most recent call last):
AssertionError: missing information
>>> lifespan('Phillis Wheatley', born, died)
Traceback (most recent call last):
AssertionError: missing information

>>> poets = alive(born, died)
>>> poets[1798]
{'John Keats', 'Percy Bysshe Shelley'}
>>> poets[1895]
{'Guillaume Apollinaire', 'Rupert Brooke', 'Wilfred Owen'}
>>> poets[1952]
{'Sylvia Plath'}

>>> wonder_years(poets)
{1818, 1819, 1820, 1821, 1893, 1894, 1895, 1896, 1897, 1898, 1899, 1900, 1901, 1902, 1903, 1904, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915}

>>> summarized({2001, 2002, 2003, 2004, 2012, 2015, 2018, 2019, 2020, 2022})
'2001-2004, 2012, 2015, 2018-2020, 2022'
>>> summarized(lifespan('Emily Brontë', born, died))
'1818-1848'
>>> summarized(wonder_years(poets))
'1818-1821, 1893-1915'
"""

from datetime import date


def read_dates(location, field):
    """
    >>> born = read_dates('poets.txt', 1)
    >>> born['Emily Brontë']
    datetime.date(1818, 7, 30)
    >>> born['Walt Whitman']
    datetime.date(1819, 5, 31)
    >>> born['Phillis Wheatley']
    Traceback (most recent call last):
    KeyError: 'Phillis Wheatley'
    """
    result = {}
    with open(location, 'r', encoding='utf8') as file:
        for line in file:
            name, *fields = line.strip().split(',')
            date_num = fields[field - 1]
            if date_num:
                result[name] = date.fromisoformat(date_num)
                # year, month, day = map(int, date_num.split('-'))
                # result[name] = date(year, month, day)
    return result


def lifespan(name, birth, death):
    """
    >>> lifespan('Emily Brontë', birth, death)
    [1818, 1819, 1820, 1821, 1822, 1823, 1824, 1825, 1826, 1827, 1828, 1829, 1830, 1831, 1832, 1833, 1834, 1835, 1836, 1837, 1838, 1839, 1840, 1841, 1842, 1843, 1844, 1845, 1846, 1847, 1848]
    >>> lifespan('Walt Whitman', birth, death)
    Traceback (most recent call last):
    AssertionError: missing information
    >>> lifespan('Phillis Wheatley', birth, death)
    Traceback (most recent call last):
    AssertionError: missing information
    """
    assert name in birth and name in death, 'missing information'
    return list(range(birth[name].year, death[name].year + 1))


def alive(birth, death):
    """
    >>> poets = alive(birth, death)
    >>> poets[1798]
    {'John Keats', 'Percy Bysshe Shelley'}
    >>> poets[1895]
    {'Guillaume Apollinaire', 'Rupert Brooke', 'Wilfred Owen'}
    >>> poets[1952]
    {'Sylvia Plath'}
    """
    alive_dict = {}
    for name in set(birth) & set(death):
        for year in lifespan(name, birth, death):
            if year not in alive_dict:
                alive_dict[year] = set()
            alive_dict[year].add(name)
    return alive_dict


def wonder_years(data):
    most_alive, wonder_years = None, set()
    for year, persons in data.items():
        if most_alive is None or len(persons) > most_alive:
            wonder_years = {year}
            most_alive = len(persons)
        elif len(persons) == most_alive:
            wonder_years.add(year)
    return wonder_years


def summarized(years):
    # group years into periods of successive years
    periods = []
    current_period = []
    for year in sorted(years):
        if not current_period:
            current_period.append(year)
        elif year - current_period[-1] == 1:
            current_period.append(year)
        elif year != current_period[-1]:
            periods.append(current_period)
            current_period = [year]
    if current_period:
        periods.append(current_period)

    # create string from chronologically ordered periods
    return ', '.join(
        str(period[0]) if len(period) == 1 else f'{period[0]}-{period[-1]}'
        for period in periods)


if __name__ == '__main__':
    summarized({2018, 2019, 2020, 2022, 2001, 2002, 2003, 2004, 2012, 2015})
