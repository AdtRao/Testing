def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return get_length(dna1)>get_length(dna2)

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    if nucleotide!='':
        return dna.count(nucleotide)
    else:
        return 0

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    if dna1!='' and dna2!='':
        return dna2 in dna1
    else:
        return False
    

def is_valid_sequence(dna):
    '''(str) -> bool
    Return True if and only if DNA sequence is valid ie contains only "A","T","G","C". Test is case sensitive.

    >>> is_valid_sequence('ATCGGC')
    True
    >>> is_valid_sequence('ATCGGCR')
    False
    >>> is_valid_sequence('atcggc')
    False
    >>> is_valid_sequence('')
    False
    '''
    if dna.isupper() and len(dna)!=0:
        for char in dna:
            if char not in 'ATCG':
                return False
        return True
    return False

def insert_sequence(dna1,dna2,index):
    '''(str, str, int) -> str
    Returns a DNA sequence by inserting dna2 in dna1 at the given index(starting from 0).

    >>> insert_sequence('CCGG','AT',2)
    CCATGG
    >>> insert_sequence('CCGG','AT',0)
    ATCCGG
    >>> insert_sequence('CCGG','AT',-1)
    CCGGAT
    '''
    if index == 0:
        dna1 = dna2 + dna1
    elif index == -1 or index == len(dna1)-1:
        dna1 = dna1 + dna2
    else:
        dna1 = dna1[:index] + dna2 + dna1[index:]

    return dna1

def get_complement(nucleotide):
    '''(str) -> str
    Returns complement of the nucleotide given in the argument nucleotide.

    >>> get_complement('C')
    G
    >>> get_complement('A')
    T
    >>> get_complement('T')
    A '''
    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'C':
        return 'G'
    elif nucleotide == 'T':
        return 'A'
    elif nucleotide == 'G':
        return 'C'

    
def get_complementary_sequence(dna):
    '''(str) -> str
    Returns complement of the dna given in the argument dna.
    >>> get_complementary_sequence('AT')
    G
    >>> get_complementary_sequence('ACGTACG')
    TGCATGC
    >>> get_complementary_sequence('')
    Not valid
    '''
    comp_dna =''
    if is_valid_sequence(dna):
        for char in dna:
            comp_dna = comp_dna + get_complement(char)
        return comp_dna
    return ''
 


