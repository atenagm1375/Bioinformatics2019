import sys


def load_data(path):
    with open(path, "r") as file:
        dna_list = []

        index = -1
        for line in file:
            if line.startswith(">"):
                index += 1
                dna_list.append("")
                continue
            dna_list[index] += line

    return dna_list


dna_sequences = load_data(sys.argv[1])
