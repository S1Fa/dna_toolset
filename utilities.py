def colored(seq):
    """Colorize terminal output"""
    bcolors = {
        "A": "\033[92m",
        "C": "\033[94m",
        "G": "\033[93m",
        "T": "\033[91m",
        "U": "\033[91m",
        "reset": "\033[0;0m"
    }

    tmpStr = ""

    for nuc in seq:
        if nuc in bcolors:
            tmpStr += bcolors[nuc] + nuc
        else:
            tmpStr += bcolors['reset'] + nuc

    return tmpStr + '\033[0;0m'

def read_text_file(file_path):
    """.txt file only"""
    with open(file_path, "r") as f:
        return "".join([line.strip() for line in f.readlines()])

def write_text_file(file_path, seq, mode="w"):
    """.txt file only"""
    with open(file_path, mode) as f:
        f.write(seq + "\n")

def read_fasta_file(file_path):
    """reture a dictionary which keys are the labels and values are sequences."""
    with open(file_path, "r") as f:
        fasta_file = [line.strip() for line in f.readlines()]

    fasta_dict = {}
    fasta_label = ''

    for line in fasta_file:
        if ">" in line:
            fasta_label = line
            fasta_dict[fasta_label] = ''
        else:
            fasta_dict[fasta_label] += line

    return fasta_dict