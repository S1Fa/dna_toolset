# DNA Toolkit file
import collections

Nucleotides = ["A", "C", "G", "T"]

# Check the sequence to make sure it is a DNA string
def validateSeq(dna_seq):
    temSeq = dna_seq.upper()
    for nuc in temSeq:
        if nuc not in Nucleotides:
            return False
    return temSeq

def countNucFrequency(seq):
    tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict
    # return dict(collections.Counter(seq))

