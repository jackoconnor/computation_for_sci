from aminoAcids import *

def compBase(N):
    if(N == 'A'):
        return 'T'
    elif(N == 'T'):
        return 'A'
    elif(N == 'G'):
        return 'C'
    elif(N == 'C'):
        return 'G'

def reverse(s):
    #create an empty string that will contain the reversed string
    r = ''
    #loop through the string 
    for c in s:
        #add the next character of s to the beginning of r
        r = c+r
    return r

def reverseComplement(DNA):
    #first reverse the string
    DNA = reverse(DNA)
    #create an empty string to contain the reverse complement
    rc = ''
    for c in DNA:
        rc = rc + compBase(c)
    return rc

def amino(codon):
    for i in range(len(aa)):
        if(codon in codons[i]):
            return aa[i]

def codingStrandToAA(DNA):
    #empty string to hold the amino acids
    aastring = ''
    for i in range(0, len(DNA), 3):
        aastring = aastring + amino(DNA[i:i+3])
    return aastring