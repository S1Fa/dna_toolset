from bio_structs import nucleotide_base, dna_codons, rna_codons
from random import choice
from collections import Counter

class Bio_seq:
    """DNA sequence class. Default value: ATCG, DNA, No label"""
    def __init__(self, seq="ATCG", seq_type="DNA", label="no label"):
        """Sequence initialization, validation."""
        self.seq = seq.upper()
        self.label = label
        self.seq_type = seq_type
        self.is_valid = self.__validate()
        assert self.is_valid, f"Provided data does not seem to be a correct {self.seq_type}"

    def __validate(self):
        """Check the sequence to make sure it is a DNA string"""
        return set(nucleotide_base[self.seq_type]).issuperset(self.seq)

    def get_seq_type(self):
        """Returns sequence type."""
        return self.seq_type

    def get_seq_info(self):
        """Returns 4 strings. Full sequence information."""
        return f"[Label]: {self.label}\n[Sequence]: {self.seq}\n[Biotype]: {self.seq_type}\n[Lenght]: {len(self.seq)}"

    def generate_random_seq(self, length=20, seq_type="DNA"):
        """Generate a random DNA sequence, provided the length"""
        seq = "".join([choice(nucleotide_base[seq_type]) for _ in range(length)])

        self.__init__(seq, seq_type, "Random Sequence")

    def nucleotide_frequency(self):
        """Count nucleotides, reture a dictionary."""
        return dict(Counter(self.seq))

    def transcription(self):
        """DNA -> RNA transcription. Replacing thymine with uracil."""
        if self.seq_type == "DNA":
            return self.seq.replace("T", "U")  # won't modify original sequence
        else:
            return "Not a DNA sequence"

    def reverse_complement(self):
        """Swapping adenine with thymine and guanine with cytosine.
        Reversing newly generated string (5' -> 3')"""
        if self.seq_type == "DNA":
            mapping = str.maketrans("ATCG", "TAGC")
        else:
            mapping = str.maketrans("AUCG", "UAGC")
        return self.seq.translate(mapping)[::-1]

    def gc_content(self):
        """GC content in a DNA/RNA sequence (percentage)"""
        return round((self.seq.count('C') + self.seq.count("G")) / len(self.seq) * 100, 2)

    def gc_content_subsec(self, k=20):
        """GC content in a DNA/RNA sub-sequence length k. k=20 by default"""
        res = []
        for i in range(0, len(self.seq)-k+1, k):
            subseq = self.seq[i: i+k]
            res.append(round((subseq.count('C') + subseq.count("G")) / len(subseq) * 100, 2))
        return res

    def translation(self, init_pos=0):
        """Translates a DNA sequence into a amino acid sequence (list). Inital position is 0."""
        # 切片超过索引最大值是返回 None
        if self.seq_type == "DNA":
            return [dna_codons[self.seq[pos: pos+3]] for pos in range(init_pos, len(self.seq)-2, 3)]
        elif self.seq_type == "RNA":
            return [rna_codons[self.seq[pos: pos+3]] for pos in range(init_pos, len(self.seq)-2, 3)]

    def codon_usage(self, aminoacid):
        """Provides the frequency of each codon encoding a given aminoacid in a DNA sequence."""
        tmpList = []
        if self.seq_type == "DNA":
            for i in range(0, len(self.seq)-2, 3):
                if dna_codons[self.seq[i: i+3]] == aminoacid:
                    tmpList.append(self.seq[i: i+3])

        elif self.seq_type == "RNA":
            for i in range(0, len(self.seq)-2, 3):
                if rna_codons[self.seq[i: i+3]] == aminoacid:
                    tmpList.append(self.seq[i: i+3])
        freqDict = dict(Counter(tmpList))
        totalWight = sum(freqDict.values())
        for codon in tmpList:
            freqDict[codon] = round(freqDict[codon] / totalWight, 2)
        return freqDict

    def gen_reading_frames(self):
        """Generating the six reading frames of a DNA sequence, including reverse compliments"""
        frames = []
        frames.append(self.translation(0))
        frames.append(self.translation(1))
        frames.append(self.translation(2))

        tmpseq = bio_seq(self.reverse_complement(), self.seq_type)

        frames.append(tmpseq.translation(0))
        frames.append(tmpseq.translation(1))
        frames.append(tmpseq.translation(2))
        del tmpseq
        return frames

    def proteins_from_rf(self, aa_seq):
        """Compute all possible proteins in an amino acid seq and return a list of possible proteins"""
        current_prot = []
        proteins = []
        for aa in aa_seq:
            # Stop accumulating amino acids if "_" was found
            if aa == "_":
                if current_prot:
                    for p in current_prot:
                        proteins.append(p)
                    current_prot = []
            else:
                # Start accumulating amino acids if "M" was found
                if aa == "M":
                    current_prot.append("")
                for i in range(len(current_prot)):
                        current_prot[i] += aa
        return proteins

    def all_proteins_from_orfs(self, startPos=0, endPos=0, ordered=False):
        """Compute all possible proteins for all open reading frames"""
        """Proteins search database: """
        """API can be used to pull protein info"""
        if endPos > startPos:
            tmp_seq = bio_seq(self.seq[startPos: endPos])
            rfs = tmp_seq.gen_reading_frames()
        else:
            rfs = self.gen_reading_frames()

        res = []
        for rf in rfs:
            prots = self.proteins_from_rf(rf)
            for p in prots:
                res.append(p)

        if ordered:
            return sorted(res, key=len, reverse=True)

        return res
