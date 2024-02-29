class Organism:
    
    """
    >>> organism = Organism('immune_system.txt')
    >>> organism.isResistant(1)
    True
    >>> organism.isResistant(88)
    False
    >>> organism.isResistant(virus=99)
    False
    >>> organism.isResistant(2)
    True
    >>> organism.isResistant(virus=99)
    False
    >>> organism.isResistant(virus=99)
    True
    >>> organism.isResistant(virus=99)
    True
    >>> organism.mutation(virus=1)
    >>> organism.isResistant(virus=1)
    False
    >>> organism.isResistant(virus=1)
    False
    >>> organism.isResistant(virus=1)
    True
    >>> organism.mutation(virus=99)
    >>> organism.isResistant(virus=99)
    False
    >>> organism.isResistant(virus=99)
    False
    >>> organism.isResistant(virus=99)
    True
    """
    
    def __init__(self, filename=None):
        
        self.innate = set()    # innate immune system
        self.adaptive = {}     # adaptive immune system
        if filename:
            # read innate antibodies
            for line in open(filename, 'r'):
                self.innate.add(int(line))
        
    def isResistant(self, virus):
        
        # organism is resistant if there are innate antibodies
        if virus in self.innate:
            return True
        
        # create antibodies as part of the adaptive immune system
        self.adaptive[virus] = self.adaptive.get(virus, 0) + 1
        
        # check if there are suffient adaptive antibodies for resistence
        if self.adaptive[virus] >= 3:
            return True
        else:
            return False
        # return self.adaptive[virus] >= 3
        
    def mutation(self, virus):
        
        # remove antibodies for virus in data structures for the
        # innate and adaptive components of the immune system
        if virus in self.innate:
            self.innate.remove(virus)
        elif virus in self.adaptive:
            del self.adaptive[virus]
        
