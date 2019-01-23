import sys
from numpy import zeros
import copy


def longest_common_subsequence(dna_list):
    row, col = dp_lcs(*dna_list)
    return lcs_from_alignment(row, col)


def space_efficient_lcs(dna_list):
    row, col = linear_space_lcs(*dna_list)
    return lcs_from_alignment(row, col)


def lcs_from_alignment(row, col):
    lcs = ""
    # print(row)
    # print(col)
    for i in range(len(row)):
        if row[i] == col[i]:
            lcs += row[i]
    return lcs


def dp_lcs(x, y):
    m, n = len(x), len(y)
    grid = zeros((m + 1, n + 1))
    for i in range(m):
        for j in range(n):
            if x[i] == y[j]:
                grid[i + 1][j + 1] = grid[i][j] + 1
            else:
                grid[i + 1][j + 1] = max(grid[i][j + 1], grid[i + 1][j])

    row = ""
    col = ""
    while m * n > 0:
        if grid[m][n] == grid[m][n - 1]:
            col = "{}{}".format("-", col)
            row = "{}{}".format(y[n - 1], row)
            n -= 1
        elif grid[m][n] == grid[m - 1][n]:
            row = "{}{}".format("-", row)
            col = "{}{}".format(x[m - 1], col)
            m -= 1
        else:
            row = "{}{}".format(y[n - 1], row)
            col = "{}{}".format(x[m - 1], col)
            m -= 1
            n -= 1

    return row, col


def linear_space_lcs(x, y):
    row = ""
    col = ""
    if len(x) == 0:
        col = '-' * len(y)
        row = y
    elif len(y) == 0:
        row = '-' * len(x)
        col += x
    elif len(x) == 1 or len(y) == 1:
        row, col = dp_lcs(x, y)
    else:
        xlen = len(x)
        ylen = len(y)
        xmid = xlen // 2
        scoreL = nw_score(x[:xmid], y)
        scoreR = nw_score(x[xmid:][::-1], y[::-1])
        ymid = partitionY(scoreL, scoreR)
        row_l, col_u = linear_space_lcs(x[:xmid], y[:ymid])
        row_r, col_d = linear_space_lcs(x[xmid:], y[ymid:])
        row = row_l + row_r
        col = col_u + col_d

    return row, col


def nw_score(x, y):
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

    return current


def partitionY(scoreL, scoreR):
    max_index = 0
    max_sum = float('-Inf')
    for i, (l, r) in enumerate(zip(scoreL, scoreR[::-1])):
        if sum([l, r]) > max_sum:
            max_sum = sum([l, r])
            max_index = i
    return max_index


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
# print(space_efficient_lcs(dna_sequences))
