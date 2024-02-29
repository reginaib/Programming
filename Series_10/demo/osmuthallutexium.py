class NameGenerator:
    
    """
    >>> chemGen = NameGenerator()
    
    >>> chemGen.addName('Osmium')
    >>> chemGen.prefixes
    {'Osm'}
    >>> chemGen.triples
    {'um': {'_'}, 'iu': {'m'}, 'mi': {'u'}, 'sm': {'i'}}
    
    >>> chemGen.addName('bismuth')
    Traceback (most recent call last):
    AssertionError: invalid name
    >>> chemGen.addName('zINC')
    Traceback (most recent call last):
    AssertionError: invalid name
    >>> chemGen.addName('pH')
    Traceback (most recent call last):
    AssertionError: invalid name
    
    >>> chemGen.addName('Bismuth')
    >>> chemGen.prefixes
    {'Osm', 'Bis'}
    >>> chemGen.triples
    {'mu': {'t'}, 'th': {'_'}, 'mi': {'u'}, 'is': {'m'}, 'iu': {'m'}, 'um': {'_'}, 'sm': {'i', 'u'}, 'ut': {'h'}}
    
    >>> chemGen.addNames('shortlist_elements.txt')
    >>> chemGen.prefixes
    {'Lan', 'Tel', 'Unu', 'Plu', 'Osm', 'Rut', 'Bis', 'Tha'}
    >>> chemGen.triples
    {'el': {'l'}, 'en': {'i'}, 'is': {'m'}, 'iu': {'m'}, 'al': {'l'}, 'an': {'u', 't'}, 'xi': {'u'}, 'ex': {'i'}, 'on': {'i'}, 'er': {'f'}, 'nh': {'e'}, 'ni': {'u'}, 'll': {'i', 'u'}, 'di': {'u'}, 'li': {'u'}, 'rd': {'i'}, 'to': {'n'}, 'rf': {'o'}, 'lu': {'r', 't'}, 'th': {'a', 'e'}, 'fo': {'r'}, 'nt': {'h'}, 'ri': {'u'}, 'nu': {'m', 'n'}, 'ha': {'l', 'n'}, 'he': {'x', 'r', 'n'}, 'um': {'_'}, 'ut': {'h', 'o', '_'}, 'mi': {'u'}, 'ur': {'i'}, 'mu': {'t'}, 'un': {'h'}, 'sm': {'i', 'u'}, 'or': {'d'}}
    
    >>> chemGen.name()
    'Osmuthalluthexium'
    >>> chemGen.name()
    'Ruthanthanium'
    >>> chemGen.name()
    'Lantherfordium'
    >>> chemGen.name()
    'Thanthenium'
    """
    
    def __init__(self):
        
        self.names = set()
        self.prefixes = set()
        self.triples = dict()
        
    def addName(self, name):
        
        # determine of the name exists of an upper case letter followed by two
        # or more lower case letters
        assert (
            len(name) >= 3 and 
            name[0].isupper() and
            name[1:].islower()
        ), 'invalid name'
        
        # remember names that were used to train the name generator
        self.names.add(name)
        
        # mark end of word by appending an underscore to the name
        name += '_'
        
        # add first three letters to the set of prefixes
        self.prefixes.add(name[:3])
        
        # add each bigram as a prefix for the next letter
        for i in range(1, len(name) - 2):
            prefix = name[i:i + 2]
            if prefix not in self.triples:
                self.triples[prefix] = {name[i + 2]}
            else:
                self.triples[prefix].add(name[i + 2])
                
    def addNames(self, filename):
        
        # traverse list of names in file and process each name by calling the
        # method addName with the name as an argument
        for name in open(filename, 'r'):
            self.addName(name.rstrip())
                
    def name(self):
        
        from random import choice
        
        # generate a new name until the name is different from all names that
        # were used to train the name generator
        name = None
        while not name or name in self.names: 
            
            # choose a random prefix       
            name = choice(list(self.prefixes))
            
            # extend name by choosing a random letter that can follow the
            # trailing bigram of the name, until an underscore has been chosen
            while name[-1] != '_':
                choices = list(self.triples[name[-2:]])
                name += choice(choices)[-1]
            
            # remove trailing underscore
            name = name[:-1]
        
        return name
                
if __name__ == '__main__':
    import doctest
    doctest.testmod()