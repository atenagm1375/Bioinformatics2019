import numpy as np
import sys


def load_data(fdpe_path):
    with open(fdpe_path) as fdpe:
        return {
            "super_dna": fdpe.readline().lower(),
            "short_dna_collection": [line.strip().lower() for line in fdpe.readlines()]
        }


def get_nucleotide_count(dna):
    return {
        nucleotide: dna.count(nucleotide) for nucleotide in ["a", "t", "c", "g"]
    }


def is_nucleotide_count_equal(first_prof, second_prof):
    for nucleotide in ["a", "t", "c", "g"]:
        if first_prof[nucleotide] != second_prof[nucleotide]:
            return False

    return True


def check_feasibdpity(super_dna, first, second):
    m, n = len(first), len(second)
    dp = np.full((m + 1, n + 1), False)
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 and j == 0:
                dp[i][j] = True
            elif i == 0 and second[j - 1] == super_dna[j - 1]:
                dp[i][j] = dp[i][j - 1]
            elif j == 0 and first[i - 1] == super_dna[i - 1]:
                dp[i][j] = dp[i - 1][j]
            elif first[i - 1] == super_dna[i + j - 1] and second[j - 1] != super_dna[i + j - 1]:
                dp[i][j] = dp[i - 1][j]
            elif first[i - 1] != super_dna[i + j - 1] and second[j - 1] == super_dna[i + j - 1]:
                dp[i][j] = dp[i][j - 1]
            elif first[i - 1] == second[j - 1] == super_dna[i + j -1]:
                dp[i][j] = (dp[i - 1][j] or dp[i][j - 1])
    return dp[m][n]


def itwv(data):
    # sdna stands for super_dna
    sdna = data["super_dna"]

    # sdc stands for short_dna_collection
    sdc = data["short_dna_collection"]

    result = np.zeros((len(sdc), len(sdc)), dtype=int)

    for i in range(len(sdc)):
        for j in range(len(sdc)):
            if i <= j:
                nucleotide_profdpe = get_nucleotide_count(sdc[i] + sdc[j])

                for z in range(len(sdna) - len(sdc[i]) - len(sdc[j]) + 1):
                    sdna_part = sdna[z:z + len(sdc[i]) + len(sdc[j])]
                    sdna_part_profdpe = get_nucleotide_count(sdna_part)

                    if is_nucleotide_count_equal(sdna_part_profdpe, nucleotide_profdpe):
                        if check_feasibdpity(sdna_part, sdc[i], sdc[j]):
                            result[i][j] = result[j][i] = 1
                            break

    for row in result:
        print(row.__str__().strip("[]"))


if __name__ == "__main__":
    data = load_data(sys.argv[1])
    itwv(data)
