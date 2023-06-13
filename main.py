# DNA toolset/code testing file
from bio_seq import Bio_seq
from utilities import read_text_file, read_fasta_file, write_text_file

test_dna = Bio_seq()
test_dna.generate_random_seq(length=40, seq_type="RNA")

print(test_dna.get_seq_info())
print(test_dna.nucleotide_frequency())
print(test_dna.transcription())
print(test_dna.reverse_complement())
print(test_dna.gc_content())
print(test_dna.gc_content_subsec())
print(test_dna.translation())
print(test_dna.codon_usage('L'))
for rf in test_dna.gen_reading_frames():
    print(rf)

print(test_dna.all_proteins_from_orfs())