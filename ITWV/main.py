import numpy as np


def load_data(file_path):
    with open(file_path) as file:
        return {
            "super_dna": file.readline().lower(),
            "short_dna_collection": [line.strip().lower() for line in file.readlines()]
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


def check_feasibility(super_dna, first, second):
    if len(super_dna) == 0:
        return True
    elif first[0] == second[0] == super_dna[0]:
        return check_feasibility(super_dna[1:], first[1:], second) or check_feasibility(super_dna[1:], first, second[1:])
    elif first[0] == super_dna[0]:
        return check_feasibility(super_dna[1:], first[1:], second)
    elif second[0] == super_dna[0]:
        return check_feasibility(super_dna[1:], first, second[1:])
    else:
        return False


def itwv():
    data = load_data("data.txt")

    # sdna stands for super_dna
    sdna = data["super_dna"]

    # sdc stands for short_dna_collection
    sdc = data["short_dna_collection"]

    result = np.zeros((len(sdc), len(sdc)), dtype=int)

    for i in range(len(sdc)):
        for j in range(len(sdc)):
            if i <= j:
                nucleotide_profile = get_nucleotide_count(sdc[i] + sdc[j])

                for z in range(len(sdna) - len(sdc[i]) - len(sdc[j]) + 1):
                    sdna_part = sdna[z:z + len(sdc[i]) + len(sdc[j])]
                    sdna_part_profile = get_nucleotide_count(sdna_part)

                    if is_nucleotide_count_equal(sdna_part_profile, nucleotide_profile):
                        if check_feasibility(sdna_part, sdc[i] + "#", sdc[j] + "#"):
                            result[i][j] = result[j][i] = 1
                            break

    for row in result:
        print(row.__str__().strip("[]"))


if __name__ == "__main__":
    itwv()
