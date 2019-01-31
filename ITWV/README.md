# ITWV(Finding Disjoint Motifs in a Gene)

## Problem Description:

Given three strings _s_, _t_, and _u_, we say that _t_ and _u_ can be interwoven into _s_ if there is some substring of _s_ made up of _t_ and _u_ as disjoint subsequences.

For example, the strings "ACAG" and "CCG" can be interwoven into "GACCACGGTT". However, they cannot be interwoven into "GACCACAAAAGGTT" because of the appearance of the four \'A\'s in the middle of the subsequence. Similarly, even though both "ACACG" is a shortest common supersequence of ACAG and CCG, it is not possible to interwoven these two strings into "ACACG" because the two desired subsequences must be disjoint.

**Given:** A text DNA string _s_ of length at most 10 kbp, followed by a collection of _n_ (_n_ \<\= 10) DNA strings of length at most 10bp acting as patterns.

**Return:** An _n_*_n_ matrix _M_ for which _M[j][k]_ = 1 if the jth and kth pattern strings can be interwoven into _s_ and _M[j][k]_ = 0 otherwise.

## Proposed Solution:

For each pair of motifs A, and B of lengths m, and n respectively, we divide the super dna string into l-m-n+1 blocks of length m+n, where l is the size of super dna, and run a dynamic programming procedure to check if A and B can be interwoven into super dna. The dynamic programming procedure fills a boolean matrix _dp_ of size \(m+1\)\*\(n+1\) where _dp[m][n]_ represents the answer. Index \(i, j\) if _dp_ is filled based on index \(i, j - 1\) or \(i - 1, j\) and checking the condition of super\_dna[i + j - 1] equals A[i - 1] or B[j - 1] or both.

## How To Run The Code?

#### Requirements:

* python 3.5.* or above
* sys
* numpy

#### Run The Code:

Run the code by python3 `main.py data.txt` where `data.txt` is the file containing a super dna string of length at most 10 kbp following at most 10 lines of strings of length at most 10.
