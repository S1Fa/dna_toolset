# DNA Toolset/Code testing file
from DNAToolkit import *
from utilities import colored
import random

# Creating a random DNA sequence
randDNAStr = ''.join([random.choice(Nucleotides) for _ in range(50)])

dna_seq = validateSeq(randDNAStr)

print(f'Sequence: {colored(dna_seq)}')
print(f'[1] + Sequence Length: {len(dna_seq)}')
print(colored(f'[2] + Nucleotides Frequency: {countNucFrequency(dna_seq)}'))

print(f'[3] + DNA->RNA transcription {colored(transcription(dna_seq))}')

print(f'[4] + DNA Complement:')
print(f"5' {colored(dna_seq)} 3'")
print(f"   {'|'*len(dna_seq)}")
print(f"3' {colored(reverse_complement(dna_seq)[::-1])} 5'")