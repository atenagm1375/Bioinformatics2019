# LSCQ(Finding a Shared Spliced Motif)

## Problem Description:

A string _u_ is a common subsequence of strings _s_ and _t_ if the symbol of _u_ appear in order as a subsequence of both _s_ and _t_. For example, \"ACTG\" is a common subsequence of \"AACCTTGG\" and \"ACACTGTGA\".

Analogously to the definition of longest common substring, _u_ is a longest common subsequence of _s_ and _t_ if there does not exist a longer common subsequence of \"AACCTTGG\" and \"ACACTGTGA\", as is \"AACTGG\".

**Given:** Two DNA strings _s_ and _t_ (each having length at most 1 kbp) in FASTA format.

**Return:** A longest common subsequence of _s_ and _t_. (If more than one solution exists, you may return any one.)

## Proposed Solution:

This problem is just a plain LCS problem. We have implemented it using Manhattan grid. We have also implemented the space\-efficient LCS discussed in class.

## How To Run The Code?

#### Requirements:

* python 3.5.* or above
* sys
* numpy
* copy

#### Run The Code:

Run the code by `python3 main.py data.txt` where `data.txt` is the file containing two DNA strings in FASTA format(as mentioned in _Problem Description_).

#### More:

To toggle between normal LCS and space-efficient LCS solutions, open `main.py`, comment line 127 and uncomment line 128 or vice versa. Line 127 runs the normal LCS while line 128 runs the space\-efficient version.
