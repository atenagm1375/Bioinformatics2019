import sys
from numpy import zeros


def longest_common_subsequence(dna_list):
    m = len(dna_list[0])
    n = len(dna_list[1])
    grid = zeros((m + 1, n + 1))

    # filling the grid
    for i in range(m):
        for j in range(n):
            if dna_list[0][i] == dna_list[1][j]:
                grid[i + 1][j + 1] = grid[i][j] + 1
            else:
                grid[i + 1][j + 1] = max(grid[i][j + 1], grid[i + 1][j])

    # find LCS using the grid
    lcs = ""
    while m * n > 0:
        if grid[m][n] == grid[m][n - 1]:
            n -= 1
        elif grid[m][n] == grid[m - 1][n]:
            m -= 1
        else:
            lcs += dna_list[0][m - 1]
            m -= 1
            n -= 1
    return lcs[::-1]


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
print(longest_common_subsequence(dna_sequences))
