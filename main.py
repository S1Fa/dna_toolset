# DNA Toolset/Code testing file
from DNAToolkit import *
import random

# Creating a random DNA sequence
randDNAStr = ''.join([random.choice(Nucleotides) for _ in range(50)])

dna_seq = validateSeq(randDNAStr)

print(f'Sequence: {dna_seq}')
print(f'[1] + Sequence Length: {len(dna_seq)}')
print(f'[2] + Nucleotides Frequency: {countNucFrequency(dna_seq)}')

print(f'[3] + DNA->RNA transcription {transcription(dna_seq)}')

print(f"5' {dna_seq} 3'")
print(f"   {'|'*len(dna_seq)}")
print(f"3' {reverse_complement(dna_seq)[::-1]} 5'")