import sys
from numpy import zeros
import copy


def get_max_gap_count(x, y):
    return len(x) + len(y) - 2 * lcs_length(x, y)


def lcs_length(x, y):
    row = y
    col = x
    minLen = len(y)
    prev = [0 for i in range(minLen + 1)]
    current = [0 for i in range(minLen + 1)]

    for j in range(1, len(col) + 1):
        for i in range(1, minLen + 1):
            if row[i-1] == col[j-1]:
                current[i] = max(current[i-1], prev[i-1] + 1, prev[i])
            else:
                current[i] = max(current[i-1], prev[i-1], prev[i])
        prev = copy.deepcopy(current) # for python its very import to use deepcopy here

    return current[minLen]


def load_data(path):
    with open(path, "r") as file:
        dna_list = []

        index = -1
        for line in file:
            if line.startswith(">"):
                index += 1
                dna_list.append("")
                continue
            dna_list[index] += line.replace("\n", "")

    return dna_list


dna_sequences = load_data(sys.argv[1])
print(get_max_gap_count(*dna_sequences))
