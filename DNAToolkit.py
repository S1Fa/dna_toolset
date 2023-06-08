# DNA Toolkit file
import collections
from structures import DNA_ReverseComplement, Nucleotides

def validateSeq(dna_seq):
    """Check the sequence to make sure it is a DNA string"""
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

def transcription(seq):
    """DNA -> RNA transcription. Replacng Thymine with Uracil"""
    return seq.replace("T", "U")

def reverse_complement(seq):
    """Swapping adenine with thymine and guanine with cytosine.
    Reversing newly generated string"""
    # return ''.join([DNA_ReverseComplement[nuc] for nuc in seq])[::-1]

    # Pythonic approach. A little bit faster solution.
    mapping = str.maketrans("ATCG", "TAGC")
    return seq.translate(mapping)[::-1]

def gc_content(seq):
    """GC content in a DNA/RNA sequence (percentage)"""
    return round((seq.count('C') + seq.count("G")) / len(seq) * 100, 6)

def gc_content_subsec(seq, k=20):
    """GC content in a DNA/RNA sub-sequence length k. k=20 by default"""
    res = []
    for i in range(0, len(seq)-k+1, k):
        res.append(gc_content(seq[i: i+k]))
    
    return res
