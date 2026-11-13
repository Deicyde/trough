---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.SuffixArray.suffix, Cslib.Algorithms.Lean.SuffixArray.suffixes, Cslib.Algorithms.Lean.SuffixArray.suffixArray, Cslib.Algorithms.Lean.SuffixArray.suffixArray_perm, Cslib.Algorithms.Lean.SuffixArray.pairwise_suffix_suffixArray, Cslib.Algorithms.Lean.SuffixArray.lcp, Cslib.Algorithms.Lean.SuffixArray.take_lcp_eq, Cslib.Algorithms.Lean.SuffixArray.take_eq_of_le_lcp
statement: formalized
proof: formalized
---

# Suffix array

22 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/suffix-array/index.html).

## Suffix of a list at an index

For a list $s = (s_0, \dots, s_{n-1})$ over a linearly
ordered alphabet and a natural number $i$, the suffix of $s$ at $i$ is the list obtained from
$s$ by dropping its first $i$ entries: it is $(s_i, \dots, s_{n-1})$ when $i < n$ and the empty
list when $i \ge n$.

Formalized by `Cslib.Algorithms.Lean.SuffixArray.suffix`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/SuffixArray.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SuffixArray.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/suffix-array/index.html#suffix).

## Suffixes of a list

For a list $s$ of length $n$ over a linearly ordered alphabet, the
list of suffixes of $s$ is the list, for $i = 0, 1, \dots, n$ in this order, of the lists
obtained from $s$ by dropping its first $i$ entries. It starts with $s$ itself and ends with the
empty list.

Formalized by `Cslib.Algorithms.Lean.SuffixArray.suffixes`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/SuffixArray.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SuffixArray.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/suffix-array/index.html#suffixes).

## Suffix array

For a list $s$ of length $n$ over a linearly ordered alphabet, the suffix
array of $s$ is the list of the indices $0, 1, \dots, n - 1$, sorted so that the suffixes of $s$
starting at them appear in lexicographic order.

Distinct indices below $n$ give suffixes of different lengths, so these suffixes are pairwise
distinct and the sorted order is unique.

Formalized by `Cslib.Algorithms.Lean.SuffixArray.suffixArray`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/SuffixArray.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SuffixArray.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/suffix-array/index.html#suffix-array).

## The suffix array is a permutation of the indices

For a list $s$ of length $n$ over a
linearly ordered alphabet, the suffix array of $s$ is a permutation of the list
$0, 1, \dots, n - 1$ of all indices below $n$.

Formalized by `Cslib.Algorithms.Lean.SuffixArray.suffixArray_perm`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SuffixArray.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SuffixArray.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/suffix-array/index.html#suffix-array-perm).

## The suffix array sorts the suffixes

For a list $s$ over a linearly ordered alphabet,
the suffixes of $s$ taken in suffix-array order are sorted lexicographically: whenever an index
$i$ comes before an index $j$ in the suffix array of $s$, the suffix of $s$ starting at $i$ is
lexicographically less than or equal to the suffix of $s$ starting at $j$.

Formalized by `Cslib.Algorithms.Lean.SuffixArray.pairwise_suffix_suffixArray`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SuffixArray.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SuffixArray.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/suffix-array/index.html#pairwise-suffix-suffix-array).

## Longest common prefix length

For lists $x$ and $y$, $\mathrm{lcp}(x, y)$ is the length
of the longest common prefix of $x$ and $y$: the number of positions, counted from the start, at
which $x$ and $y$ agree before they first differ or one of them ends.

Only equality of letters is tested, so no order on the alphabet is needed.

Formalized by `Cslib.Algorithms.Lean.SuffixArray.lcp`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/SuffixArray.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SuffixArray.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/suffix-array/index.html#lcp).

## Two lists agree on their longest common prefix

For lists $x$ and $y$ over a type with
decidable equality, let $\operatorname{lcp}(x, y)$ be the length of their longest common prefix.
Then the first $\operatorname{lcp}(x, y)$ elements of $x$ and the first $\operatorname{lcp}(x, y)$
elements of $y$ form the same list.

Formalized by `Cslib.Algorithms.Lean.SuffixArray.take_lcp_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SuffixArray.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SuffixArray.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/suffix-array/index.html#take-lcp-eq).

## Common prefixes of every shorter length

Let $x$ and $y$ be lists and let
$\mathrm{lcp}(x, y)$ be the length of their longest common prefix. For every natural number
$q \le \mathrm{lcp}(x, y)$, the first $q$ elements of $x$ and of $y$ agree.

Formalized by `Cslib.Algorithms.Lean.SuffixArray.take_eq_of_le_lcp`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SuffixArray.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SuffixArray.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/suffix-array/index.html#take-eq-of-le-lcp).

## Characterization of the longest common prefix length

For lists $x$ and $y$, let
$\mathrm{lcp}(x, y)$ be the length of the longest common prefix of $x$ and $y$. For every natural
number $q$, we have $q \le \mathrm{lcp}(x, y)$ if and only if $q$ is at most the lengths of both
$x$ and $y$ and the first $q$ elements of $x$ and of $y$ agree.

In particular $\mathrm{lcp}(x, y)$ is the largest such $q$.

Formalized by `Cslib.Algorithms.Lean.SuffixArray.le_lcp_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SuffixArray.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SuffixArray.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/suffix-array/index.html#le-lcp-iff).

## Longest-common-prefix lengths of adjacent suffixes

For a list $s$ and a list of indices
$i_0, i_1, \dots, i_k$, this is the list of length $k$ whose $t$-th entry, for $t < k$, is the
length of the longest common prefix of the suffixes of $s$ starting at $i_t$ and at $i_{t+1}$,
where the suffix starting at an index at or past the end of $s$ is the empty list. It has one
entry per adjacent pair of indices, and it is empty for an empty index list.

Formalized by `Cslib.Algorithms.Lean.SuffixArray.adjLcp`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/SuffixArray.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SuffixArray.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/suffix-array/index.html#adj-lcp).

## The LCP array

For a list $s$ over a linearly ordered alphabet, the LCP array of $s$ is
the list of longest-common-prefix lengths of adjacent suffixes in suffix-array order: if the
suffix array of $s$ is $i_0, i_1, \dots, i_k$, then the LCP array has length $k$ and its $t$-th
entry, for $t < k$, is the length of the longest common prefix of the suffixes of $s$ starting
at $i_t$ and at $i_{t+1}$. It is empty when $s$ is empty.

Formalized by `Cslib.Algorithms.Lean.SuffixArray.lcpArray`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/SuffixArray.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SuffixArray.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/suffix-array/index.html#lcp-array).

## Prefix classes are lexicographic intervals

If `x ≤ y ≤ z` and `P` is a prefix of both
`x` and `z`, then `P` is a prefix of `y`.

Formalized by `Cslib.Bioinformatics.Indexing.SuffixArraySearch.prefix_of_le_of_le`, a theorem declared in [CSLibExt/Bioinformatics/Indexing/SuffixArraySearch.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Indexing/SuffixArraySearch.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/suffix-array/index.html#prefix-of-le-of-le).

## Truncation is monotone for the lexicographic order

Truncation is monotone for the lexicographic order: `x ≤ y → x.take m ≤ y.take m`.

Formalized by `Cslib.Bioinformatics.Indexing.SuffixArraySearch.take_le_take`, a theorem declared in [CSLibExt/Bioinformatics/Indexing/SuffixArraySearch.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Indexing/SuffixArraySearch.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/suffix-array/index.html#take-le-take).

## The occurrences of a pattern are contiguous in the suffix array

If rows `r₁ ≤ r₂ ≤ r₃`
of the suffix array of `s` are in range and the suffixes of rows `r₁` and `r₃` start with `P`,
so does the suffix of row `r₂`.

Formalized by `Cslib.Bioinformatics.Indexing.SuffixArraySearch.prefix_suffixArray_of_le_of_le`, a theorem declared in [CSLibExt/Bioinformatics/Indexing/SuffixArraySearch.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Indexing/SuffixArraySearch.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/suffix-array/index.html#prefix-suffix-array-of-le-of-le).

## Binary search for the boundary of a predicate

Binary search for the boundary of a predicate on `[lo, hi)`: the first index at which `p`
is false, assuming `p` holds on an initial segment of `[lo, hi)` (`lowerBound_spec`). Each call
probes the midpoint and recurses on one half.

Formalized by `Cslib.Bioinformatics.Indexing.SuffixArraySearch.lowerBound`, a definition declared in [CSLibExt/Bioinformatics/Indexing/SuffixArraySearch.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Indexing/SuffixArraySearch.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/suffix-array/index.html#lower-bound).

## Number of probes made by the binary search

The number of probes `lowerBound p lo hi` makes.

Formalized by `Cslib.Bioinformatics.Indexing.SuffixArraySearch.lowerBoundSteps`, a definition declared in [CSLibExt/Bioinformatics/Indexing/SuffixArraySearch.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Indexing/SuffixArraySearch.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/suffix-array/index.html#lower-bound-steps).

## Binary search is correct

If `p` holds on an initial segment of `[lo, hi)` (whenever it
holds at `j`, it holds at every `i` with `lo ≤ i ≤ j`), then `lowerBound p lo hi` is the end `k` of
that segment: `lo ≤ k ≤ hi`, `p` holds on `[lo, k)` and fails on `[k, hi)`.

Formalized by `Cslib.Bioinformatics.Indexing.SuffixArraySearch.lowerBound_spec`, a theorem declared in [CSLibExt/Bioinformatics/Indexing/SuffixArraySearch.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Indexing/SuffixArraySearch.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/suffix-array/index.html#lower-bound-spec).

## Binary search is logarithmic

At most `⌊log₂ (hi - lo)⌋ + 1` probes, for any predicate.

Formalized by `Cslib.Bioinformatics.Indexing.SuffixArraySearch.lowerBoundSteps_le`, a theorem declared in [CSLibExt/Bioinformatics/Indexing/SuffixArraySearch.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Indexing/SuffixArraySearch.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/suffix-array/index.html#lower-bound-steps-le).

## Truncated suffix of a suffix-array row

The suffix of row `r` of the (precomputed) suffix array `sa` of `s`, truncated to
`m` letters: the key compared with the pattern during the search. `sa` is computed once
by `saSearch` and passed in, so probes do not rebuild the suffix array.

Formalized by `Cslib.Bioinformatics.Indexing.SuffixArraySearch.rowKey`, a definition declared in [CSLibExt/Bioinformatics/Indexing/SuffixArraySearch.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Indexing/SuffixArraySearch.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/suffix-array/index.html#row-key).

## Suffix-array search for a pattern's row interval

Suffix-array search (Manber and Myers 1993): the row interval `[sp, ep)` of the suffixes of
`s` that start with `P`, found by two binary searches over the rows `[0, |s|)`. The suffix
array is computed once and shared by both searches.

Formalized by `Cslib.Bioinformatics.Indexing.SuffixArraySearch.saSearch`, a definition declared in [CSLibExt/Bioinformatics/Indexing/SuffixArraySearch.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Indexing/SuffixArraySearch.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/suffix-array/index.html#sa-search).

## Suffix-array search returns a valid row interval

The search returns a genuine interval of rows: `sp ≤ ep ≤ |s|`.

Formalized by `Cslib.Bioinformatics.Indexing.SuffixArraySearch.saSearch_bounds`, a theorem declared in [CSLibExt/Bioinformatics/Indexing/SuffixArraySearch.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Indexing/SuffixArraySearch.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/suffix-array/index.html#sa-search-bounds).

## Suffix-array search is correct

A row `r < |s|` lies in `[sp, ep)` exactly when the suffix
of row `r` starts with `P`.

Formalized by `Cslib.Bioinformatics.Indexing.SuffixArraySearch.saSearch_spec`, a theorem declared in [CSLibExt/Bioinformatics/Indexing/SuffixArraySearch.lean, line 269](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Indexing/SuffixArraySearch.lean#L269). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/suffix-array/index.html#sa-search-spec).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Suffix array](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/suffix-array/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/suffix-array)
