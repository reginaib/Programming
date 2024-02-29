def isStopCodon(seq):
    return seq.upper() in ('TAG', 'TGA', 'TAA')


def reverseComplement(seq):
    pairs = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G'
    }
    return ''.join(pairs[char] for char in reversed(seq.upper()))


def stopCodons(seq, n):
    return sum(isStopCodon(x) for x in codons(seq, n).split('-'))


def codons(seq, n):
    if n < 0:
        seq = reverseComplement(seq)
        n = -n

    s = '-'.join(seq[ind:ind + 3] for ind in range(n - 1, len(seq), 3))
    if n > 1:
        return seq[:n-1] + '-' + s
    return s




