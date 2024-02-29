def aboBloodgroup(allele1, allele2):
    
    if allele1 == allele2:
        return allele1
    elif allele1 == 'O':
        return allele2
    elif allele2 == 'O':
        return allele1
    else:
        return 'AB'
    
def rhesusfactor(allele1, allele2):
    
    return '+' if '+' in {allele1, allele2} else '-'
    
def bloodgroup_child(father, mother):
    
    """
    >>> bloodgroup_child('O+', 'O-')
    {'O+', 'O-'}
    >>> bloodgroup_child('O-', 'O-')
    {'O-'}
    >>> bloodgroup_child('AB-', 'AB+')
    {'A+', 'A-', 'AB+', 'AB-', 'B+', 'B-'}
    """
    
    # determine possible ABO bloodgroups
    abo_allels = {'A':{'A', 'O'}, 'B':{'B', 'O'}, 'AB':{'A', 'B'}, 'O':{'O'}}    
    abo_father, abo_mother = father[:-1], mother[:-1]
    abo_child = {
        aboBloodgroup(allel1, allel2)
        for allel1 in abo_allels[abo_father]
        for allel2 in abo_allels[abo_mother]
    }
    
    # determine possible rhesusfactors
    rhesus_alleles = {'+':{'+', '-'}, '-':{'-'}}
    rhesus_father, rhesus_mother = father[-1], mother[-1]
    rhesus_child = {
        rhesusfactor(allel1, allel2)
        for allel1 in rhesus_alleles[rhesus_father]
        for allel2 in rhesus_alleles[rhesus_mother]
    }
    
    # determine all possible cominations of AB bloodgroups and rhesusfactors
    return {
        abo + rhesus
        for abo in abo_child
        for rhesus in rhesus_child
    }

def bloodgroup_parent(parent, child):
    
    """
    >>> bloodgroup_parent('O+', 'O-')
    {'A-', 'A+', 'B-', 'B+', 'O-', 'O+'}
    >>> bloodgroup_parent('AB+', 'O+')
    set()
    """
    
    # iterate over all bloodgroups for the second parent 
    # and look if the resulting pair could have a child of a given bloodgroup
    return {
        abo + rhesus 
        for abo in ('O', 'A', 'B', 'AB')
        for rhesus in '+-'
        if child in bloodgroup_child(parent, abo + rhesus)
    }

if __name__ == '__main__':
    import doctest
    doctest.testmod()