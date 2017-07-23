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
    return dna1>dna2

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count(nucleotide)

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna1.find(dna2) !=-1
def is_valid_sequence (dna):

    '''
    (str) -> bool
    Returns True if dna is a valid DNA sequence i.e. contains A, T, C or G only
    >>> is_valid_sequence('ATCGA')
    True
    >>>is_valid_sequence('XYAT')
    False
    '''
    sequence = True
    for char in dna:
        if char not in 'ATCGatcg':
            sequence = False

    return sequence

def insert_sequence (dna1, dna2, index):
    '''
    (str,str,int) -> str
    The first two parameters, dna1 and dna2 are DNA sequences and the third
    parameter index is an index. Return the DNA sequence obtained by
    inserting the second DNA sequence into the first DNA sequence at the given index
    >>> insert_sequence('ATCG', 'AT', 1)
    AATTCG
    >>>insert_sequence('ATCG', 'GC', 0)
    GCATCG
    '''
    combined_dna=dna1[:index]+dna2+dna1[index:]
    return combined_dna    

def get_complement(nucleotide):
    '''
    (str) -> str
    Functions returns the complement of nucleotide; A<>T and C<>G
    >>> get_complement('A')
    T
    >>>get_complement('C')
    G
    '''
    seq1='ATCG'
    seq2='TAGC' #stores complemented sequence
    index=0
    for char in seq1:
        if char!=nucleotide:
            index=index+1
        else:
            break
    return seq2[index]


def get_complementary_sequence(dna):
    '''
    (str) -> str
    returns comlementary sequence for dna ; 
    >>>get_complementary_sequence('ATCG')
    TAGC
    >>>get_complementary_sequence('CGTAGT')
    GCATCA
    >>>get_complementary_sequence('AT')
    TA
    '''
    comp_dna=''
    for char in dna:
        comp_dna=comp_dna+get_complement(char)

    return comp_dna
    
