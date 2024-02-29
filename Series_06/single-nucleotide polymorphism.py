def SNP(seq1, seq2):
    
    """
    >>> SNP('AAGCCTA', 'AAGCTTA')
    (4, 'C', 'T')
    >>> SNP('AAGCCTAA', 'AAGCTTA')
    >>> SNP('AAGCTTA', 'AAGCTTA')
    >>> SNP('AAGCCCA', 'AAGCTTA')
    """
    
    # check whether sequences have equal length
    if len(seq1) != len(seq2):
        return None

    # check whether sequences differ at exactly one position
    SNP = None    
    for index, (base1, base2) in enumerate(zip(seq1.upper(), seq2.upper())):
        if base1 != base2:
            if SNP is None:
                # first position where both sequences differ
                SNP = (index, base1, base2)
            else:
                # second position where both sequences differ
                return None
            
    # return position where both sequences differ (if unique and existing)
    return SNP

def SNPs(genome, read):
    
    """
    >>> SNPs('AGCTGATAAGCCTAAGCGCT', 'AAGCTTA')
    [11]
    >>> SNPs('ATCGTAAGCCTAAGGCTACGCTTAGAGATA', 'AAGCTTA')
    [9, 18]
    >>> SNPs('AAGCCTAAGCCTA', 'AAGCTTA')
    [4, 10]
    """
    
    # sliding window traversal of genome in order to find SNPs
    SNPs = []
    m, n = len(genome), len(read)
    for i in range(m - n + 1):
        window = genome[i:i + n]
        snp = SNP(window, read)
        if snp is not None:
            # translate position in read to position in genome
            SNPs.append(i + snp[0])
            
    # sort list of SNPs
    SNPs.sort()
    
    # return sorted list of SNPs
    return SNPs

if __name__ == '__main__':
    import doctest
    doctest.testmod()