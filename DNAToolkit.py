# DNA Toolkit file
from collections import Counter
from structures import *

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
    # return dict(Counter(seq))

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

def translate(seq, init_pos=0):
    """Translates a DNA sequence into a amino acid sequence.
    Inital position is 0."""
    # 切片超过索引最大值是返回 None
    return [DNA_Codons[seq[pos: pos+3]] for pos in range(init_pos, len(seq)-2, 3)]

def codon_usage(seq, aminoacid):
    """Provides the frequency of each codon encoding a given aminoacid in a DNA sequence."""
    tmpList = []
    for i in range(0, len(seq)-2, 3):
        if DNA_Codons[seq[i: i+3]] == aminoacid:
            tmpList.append(seq[i: i+3])
    freqDict = dict(Counter(tmpList))
    totalWight = sum(freqDict.values())
    for codon in tmpList:
        freqDict[codon] = round(freqDict[codon] / totalWight, 2)
    return freqDict

def gen_read_frame(seq):
    frames = []
    frames.append(translate(seq, 0))
    frames.append(translate(seq, 1))
    frames.append(translate(seq, 2))
    frames.append(translate(reverse_complement(seq), 0))
    frames.append(translate(reverse_complement(seq), 1))
    frames.append(translate(reverse_complement(seq), 2))
    return frames