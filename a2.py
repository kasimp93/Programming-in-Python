def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna);

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    if len(dna1) > len(dna2):
        return True
    else:
        return False

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    nuc = 0
    for char in dna:
        if char == nucleotide:
            nuc = nuc + 1
    return nuc

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    if dna2 in dna1:
        return True
    else:
        return False

def is_valid_sequence(dna):
        """ (str) -> bool

    Return True if and only if DNA sequence is valid

    >>> is_valid_sequence('ATCGGC')
    True
    >>> is_valid_sequence('ATCGCB')
    False
    """
        non = 0
        for char in dna:
            if char not in 'ATCG':
                non = non + 1
        if non == 0:
            return True
        else:
            return False
            
def insert_sequence(dna1, dna2, index):
    """ (str, str, int) -> str

    Return new dna sequence

    >>> insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    >>> insert_sequence('CCGG', 'AT', 3)
    'CCGATG'
    """
    dna1 = dna1[:index] + dna2 + dna1[index:]
    return dna1

def get_complement(nucleotide):
        """ (str) -> str

    Return nucleotide's complement

    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    """
        if nucleotide == 'A':
            return 'T'
        if nucleotide == 'T':
            return 'A'
        if nucleotide == 'C':
            return 'G'
        if nucleotide == 'G':
            return 'C'

def get_complementary_sequence(dna):
    """ (str) -> str
    get_complementary_sequence('AT')
    'TA'
    """
    return dna[::-1]