# MGAP(Maximizing the Gap Symbols of an Optimal Alignment)

## Problem Description:

For the computation of an alignment score generalizing the edit alignment score, let _m_ denote the score assigned to matched symbols, _d_ denote the score assigned to mismatched non-gap symbols, and _g_ denote the score assigned a symbol matched to a gap symbol \'\-\'.

**Given:** Two DNA strings _s_ and _t_ in FASTA format(each of length at most 5000 bp).

**Return:** The maximum number of gap symbols that can appear in any maximum score alignment of _s_ and _t_ with score parameters satisfying _m > 0, d < 0,_ and _g < 0_.


## Proposed Solution:

As said in the **Return** statement above, the maximum number of gap symbols in any maximum score alignment of two inputs is required for any scoring parameters satisfying the given conditions. We know that the maximum score would maximize the phrase `#matches * m - #gaps * g - #mismatches * d`. Thinking deep, we concluded that in order to have maximum number of gaps for the maximum score, mismatch penalty should be very high and gap penalty should be very low. This is equivalent to _LCS_ of the tow input strings.

So to count the maximum number of gap symbols:
1. Compute length of LCS(using space\-efficient version of it) of _s_ and _t_. Let it be _l_.
2. Number of maximum gap symbols then would be `|s| + |t| - 2 * l`.


## How To Run The Code?

#### Requirements:
* python 3.5.* or above
* sys
* numpy
* copy

#### Run The Code:
Run the code by `python3 main.py data.txt` where `data.txt` is the file containing two DNA strings in FASTA format(as mentioned in _Problem Description_).
