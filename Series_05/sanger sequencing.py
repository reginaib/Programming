def sanger(seq):
    
    """
    >>> sanger('ATGCTTCGG')
    '123456789\\nA--------\\n---C--C--\\n--G----GG\\n-T--TT---\\n=========\\nATGCTTCGG'
    >>> print(sanger('ATGCTTCGG'))
    123456789
    A--------
    ---C--C--
    --G----GG
    -T--TT---
    =========
    ATGCTTCGG
    >>> print(sanger('ATGCTTCGGCAAGACTCAAAAAATA'))
             1111111111222222
    1234567890123456789012345
    A---------AA-A---AAAAAA-A
    ---C--C--C----C-C--------
    --G----GG---G------------
    -T--TT---------T-------T-
    =========================
    ATGCTTCGGCAAGACTCAAAAAATA
    """

    # format positions
    format = ''
    l = len(seq)                       # length of DNA sequence
    for n in range(len(str(l))):
        for i in range(1, l + 1):
            format += '{:>{}}'.format(i, len(str(l)))[n]
        format += '\n'
        
    # format individual detector signals
    for X in 'ACGT':
        for base in seq:
            format += X if base == X else '-'
        format += '\n' 
        
    # format line containing equal signs
    format += '=' * len(seq) + '\n'
    
    # format DNA sequence
    return format + seq

if __name__ == '__main__':
    import doctest
    doctest.testmod()