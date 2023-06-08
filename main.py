# DNA Toolset/Code testing file
from DNAToolkit import *
from utilities import colored
import random

# Creating a random DNA sequence
randDNAStr = ''.join([random.choice(Nucleotides) for _ in range(50)])

dna_seq = validateSeq(randDNAStr)

# === colorize ===

# print(f'Sequence: {colored(dna_seq)}')
# print(f'[1] + Sequence Length: {len(dna_seq)}')
# print(colored(f'[2] + Nucleotides Frequency: {countNucFrequency(dna_seq)}'))

# print(f'[3] + DNA->RNA transcription {colored(transcription(dna_seq))}')

# print(f'[4] + DNA Complement:')
# print(f"5' {colored(dna_seq)} 3'")
# print(f"   {'|'*len(dna_seq)}")
# print(f"3' {colored(reverse_complement(dna_seq)[::-1])} 5'")

print(f'Sequence: {dna_seq}')
print(f'[1] + Sequence Length: {len(dna_seq)}')
print(f'[2] + Nucleotides Frequency: {countNucFrequency(dna_seq)}')

print(f'[3] + DNA->RNA transcription {transcription(dna_seq)}')

print(f'[4] + DNA Complement:')
print(f"5' {dna_seq} 3'")
print(f"   {'|'*len(dna_seq)}")
print(f"3' {reverse_complement(dna_seq)[::-1]} 5'")

print(f'[5] + GC content: {gc_content(dna_seq)}%')

print(f'[6] + GC content in subsection k=5: {gc_content_subsec(dna_seq, k=5)}')