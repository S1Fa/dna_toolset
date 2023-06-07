nucleotides = ["A", "T", "C", "G"]

def validSeq(seq):
    for nuc in seq.upper():
        if nuc not in nucleotides:
            return False
    return seq