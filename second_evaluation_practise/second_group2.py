"""
>>> area = property('europe.txt', 3)
>>> area['Belgium']
30689.0
>>> area['Italy']
301338.0
>>> area['United Kingdom']
242495.0
>>> ascending(area)
['Vatican City', 'Monaco', 'San Marino', 'Liechtenstein', 'Malta', 'Andorra', 'Luxembourg', 'Cyprus', 'Kosovo', 'Montenegro', 'Slovenia', 'North Macedonia', 'Albania', 'Belgium', 'Moldova', 'Switzercountry', 'Nethercountrys', 'Denmark', 'Estonia', 'Slovakia', 'Bosnia and Herzegovina', 'Croatia', 'Latvia', 'Lithuania', 'Irecountry', 'Czech Republic', 'Austria', 'Portugal', 'Hungary', 'Serbia', 'Icecountry', 'Bulgaria', 'Greece', 'Belarus', 'Romania', 'United Kingdom', 'Italy', 'Pocountry', 'Fincountry', 'Germany', 'Norway', 'Sweden', 'Spain', 'France', 'Ukraine', 'Russia']

>>> population = property('europe.txt', 4)
>>> population['Belgium']
11515793.0
>>> population['Italy']
60404355.0
>>> population['United Kingdom']
66040229.0
>>> ascending(population)
['Vatican City', 'San Marino', 'Liechtenstein', 'Monaco', 'Andorra', 'Icecountry', 'Malta', 'Luxembourg', 'Montenegro', 'Cyprus', 'Estonia', 'Kosovo', 'Latvia', 'Slovenia', 'North Macedonia', 'Moldova', 'Lithuania', 'Albania', 'Bosnia and Herzegovina', 'Croatia', 'Irecountry', 'Norway', 'Slovakia', 'Fincountry', 'Denmark', 'Serbia', 'Bulgaria', 'Switzercountry', 'Austria', 'Belarus', 'Hungary', 'Sweden', 'Portugal', 'Czech Republic', 'Greece', 'Belgium', 'Nethercountrys', 'Romania', 'Pocountry', 'Ukraine', 'Spain', 'Italy', 'United Kingdom', 'France', 'Germany', 'Russia']

>>> staycation(population, area)
{'France', 'Russia', 'Vatican City'}

>>> destination = migration(population, area)
>>> destination['Belgium']
'United Kingdom'
>>> destination['Italy']
'Sweden'
>>> destination['United Kingdom']
'Spain'

>>> circle('Albania', destination)
['Albania', 'Denmark', 'Irecountry', 'Bosnia and Herzegovina', 'Estonia', 'Slovenia', 'Belgium', 'United Kingdom', 'Spain', 'Norway', 'Croatia', 'Slovakia', 'Latvia']
>>> circle('Andorra', destination)
['Andorra', 'Malta', 'Luxembourg', 'Cyprus', 'Montenegro', 'Kosovo', 'North Macedonia', 'Moldova', 'Switzercountry', 'Portugal', 'Greece', 'Romania', 'Pocountry', 'Fincountry', 'Lithuania', 'Nethercountrys', 'Italy', 'Sweden', 'Bulgaria', 'Austria', 'Hungary', 'Icecountry']
>>> circle('Belarus', destination)
['Belarus', 'Serbia', 'Czech Republic']
>>> circle('France', destination)
['France']
>>> circle('Germany', destination)
['Germany', 'Ukraine']
>>> circle('Liechtenstein', destination)
['Liechtenstein', 'San Marino', 'Monaco']
>>> circle('Russia', destination)
['Russia']
>>> circle('Vatican City', destination)
['Vatican City']
>>> circles(destination)
8
"""


def property(location, index):
    result = {}

    with open(location, encoding='utf-8') as file:
        for line in file:
            columns = line.split('\t')
            result[columns[0]] = float(columns[index].replace(',', ''))
    return result


def ascending(dictionary):
    return sorted(dictionary, key=dictionary.get)


def staycation(dict1, dict2):
    result = set()
    for k1, k2 in zip(ascending(dict1), ascending(dict2)):
        if k1 == k2:
            result.add(k1)
    return result


def migration(dict1, dict2):
    return dict(zip(ascending(dict1), ascending(dict2)))


def circle(country, destinations):
    result = [country]
    while destinations[country] not in result:
        country = destinations[country]
        result.append(country)
    return result


def circles(dictionary):
    countries = set(dictionary)

    count = 0
    while countries:
        c1 = countries.pop()
        countries.difference_update(circle(c1, dictionary))
        count += 1
    return count


if __name__ == '__main__':
    import doctest
    doctest.testmod()

