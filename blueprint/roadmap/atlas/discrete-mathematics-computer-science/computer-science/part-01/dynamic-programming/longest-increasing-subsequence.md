---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.TimeM.IsLISLength, Cslib.Algorithms.Lean.TimeM.IsLISCell, Cslib.Algorithms.Lean.TimeM.maxAbove, Cslib.Algorithms.Lean.TimeM.lisTable, Cslib.Algorithms.Lean.TimeM.maxEntry, Cslib.Algorithms.Lean.TimeM.longestIncreasingSubsequence, Cslib.Algorithms.Lean.TimeM.maxAbove_time, Cslib.Algorithms.Lean.TimeM.longestIncreasingSubsequence_time
statement: formalized
proof: formalized
---

# Longest increasing subsequence

24 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/longest-increasing-subsequence/index.html).

## Length of a longest increasing subsequence

For a list $xs$ over a preorder and a natural
number $k$, $k$ is the length of a longest strictly increasing subsequence of $xs$ when some
strictly increasing subsequence of $xs$ has length $k$ and every strictly increasing subsequence
of $xs$ has length at most $k$. Here a subsequence need not be contiguous, and strictly increasing
means that each element is strictly less than every later one.

Formalized by `Cslib.Algorithms.Lean.TimeM.IsLISLength`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/LongestIncreasingSubsequence.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/LongestIncreasingSubsequence.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/longest-increasing-subsequence/index.html#is-lislength).

## Table cell of the LIS dynamic program

For an element $x$, lists $s$ and $zs$, and a
natural number $k$, the pair $(k, zs)$ is a table cell for $x$ followed by $s$ when $zs$ is a
subsequence (not necessarily contiguous) of $s$, the list $x$ followed by $zs$ is strictly
increasing (each element strictly less than every later one) and has length $k$, and for every
subsequence $zs'$ of $s$ such that $x$ followed by $zs'$ is strictly increasing, the list $x$
followed by $zs'$ has length at most $k$. So $x$ followed by $zs$ is a longest strictly increasing
subsequence of $x$ followed by $s$ that starts with this $x$.

Formalized by `Cslib.Algorithms.Lean.TimeM.IsLISCell`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/LongestIncreasingSubsequence.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/LongestIncreasingSubsequence.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/longest-increasing-subsequence/index.html#is-liscell).

## Best table entry above a value

Given a value $x$ and a list $t$ of entries $(y, k, zs)$,
where $y$ is a value, $k$ a natural number and $zs$ a list of values, this timed computation
returns the pair of $k$ and the list $y$ followed by $zs$ for an entry of $t$ with $x < y$ whose
$k$ is largest among such entries, provided that $k$ is positive; if no entry with $x < y$ has
$k > 0$, it returns $0$ and the empty list. It costs one unit per entry of $t$.

Formalized by `Cslib.Algorithms.Lean.TimeM.maxAbove`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/LongestIncreasingSubsequence.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/LongestIncreasingSubsequence.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/longest-increasing-subsequence/index.html#max-above).

## Table of the quadratic LIS program

The table of a list is a list of triples $(y, k, zs)$,
built from the right: the empty list has the empty table, and the table of $x$ followed by $rest$
is the table $t$ of $rest$ with the entry $(x, b + 1, w)$ put in front, where $(b, w)$ is the
result of the scan of $t$ for entries above $x$. Building the table costs the total cost of these
scans.

Formalized by `Cslib.Algorithms.Lean.TimeM.lisTable`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/LongestIncreasingSubsequence.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/LongestIncreasingSubsequence.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/longest-increasing-subsequence/index.html#lis-table).

## Table entry of largest length

Given a list $t$ of entries $(y, k, zs)$, where $k$ is a
natural number and $zs$ is a list with elements of the same type as $y$, this timed computation
returns the pair of $k$ and the list $y$ followed by $zs$ for an entry of $t$ whose $k$ is
largest, provided that this $k$ is positive, and returns $0$ and the empty list otherwise (in
particular when $t$ is empty). It costs one unit per entry of $t$.

Formalized by `Cslib.Algorithms.Lean.TimeM.maxEntry`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/LongestIncreasingSubsequence.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/LongestIncreasingSubsequence.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/longest-increasing-subsequence/index.html#max-entry).

## Longest increasing subsequence by dynamic programming

Given a list
$x_0, \dots, x_{n-1}$ of elements of a preorder with decidable $<$, this timed computation
builds, from the right, a table recording for each position $i$ a length and a strictly
increasing subsequence starting with $x_i$ (the longest one, by the recurrence
$L_i = 1 + \max \{ L_j : i < j,\ x_i < x_j \}$ with $\max \emptyset = 0$), and returns the
stored subsequence of an entry of largest length, or the empty list when $n = 0$. The cost
is one unit for each table entry inspected: building the entry for position $i$ scans the
entries to its right, and the final scan inspects each entry once.

Formalized by `Cslib.Algorithms.Lean.TimeM.longestIncreasingSubsequence`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/LongestIncreasingSubsequence.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/LongestIncreasingSubsequence.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/longest-increasing-subsequence/index.html#longest-increasing-subsequence).

## Cost of the scan for the best entry above a value

Let $\alpha$ be a preorder with
decidable $<$. For every value $x \in \alpha$ and every list $t$ of entries $(y, k, zs)$, where
$y \in \alpha$, $k$ is a natural number and $zs$ is a list over $\alpha$, the scan of $t$ for the
best table entry above $x$ costs exactly the length of $t$.

Formalized by `Cslib.Algorithms.Lean.TimeM.maxAbove_time`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/LongestIncreasingSubsequence.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/LongestIncreasingSubsequence.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/longest-increasing-subsequence/index.html#max-above-time).

## Running time of the quadratic LIS program

For every list $xs$ of length $n$ over a
preorder, twice the cost of the quadratic longest-increasing-subsequence program on $xs$ equals
$n(n + 1)$, so the program costs exactly $n(n + 1)/2$.

The cost model charges one unit for each table entry inspected.

Formalized by `Cslib.Algorithms.Lean.TimeM.longestIncreasingSubsequence_time`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/LongestIncreasingSubsequence.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/LongestIncreasingSubsequence.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/longest-increasing-subsequence/index.html#longest-increasing-subsequence-time).

## A subsequence starting with $y$ starts at an occurrence of $y$

For an element $y$ and lists
$zs$ and $l$, if the list $y$ followed by $zs$ is a subsequence (not necessarily contiguous) of $l$,
then there is a list $s$ such that $y$ followed by $s$ is a suffix of $l$ and $zs$ is a subsequence
of $s$.

Formalized by `Cslib.Algorithms.Lean.TimeM.exists_suffix_of_cons_sublist`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/LongestIncreasingSubsequence.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/LongestIncreasingSubsequence.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/longest-increasing-subsequence/index.html#exists-suffix-of-cons-sublist).

## Invariant of the LIS table

A table $t$ of triples $(y, k, zs)$ satisfies the invariant for
a list $l$ when every entry $(y, k, zs)$ of $t$ has a list $s$ such that $y$ followed by $s$ is a
suffix of $l$ and $(k, zs)$ is a table cell for $y$ followed by $s$, and conversely, for every
element $y$ and list $s$ such that $y$ followed by $s$ is a suffix of $l$, some entry $(y, k, zs)$
of $t$ makes $(k, zs)$ a table cell for $y$ followed by $s$.

Formalized by `Cslib.Algorithms.Lean.TimeM.LISTableSpec`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/LongestIncreasingSubsequence.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/LongestIncreasingSubsequence.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/longest-increasing-subsequence/index.html#listable-spec).

## The step of the LIS recurrence

Let $x$ be an element, $rest$ a list, and $t$ a table of
triples $(y, k, zs)$ that satisfies the invariant of the LIS table for $rest$. Let $(b, w)$ be the
result of the scan of $t$ for entries above $x$. Then $(b + 1, w)$ is a table cell for $x$ followed
by $rest$: $w$ is a subsequence of $rest$, the list $x$ followed by $w$ is strictly increasing and
has length $b + 1$, and every strictly increasing list $x$ followed by a subsequence of $rest$ has
length at most $b + 1$.

Formalized by `Cslib.Algorithms.Lean.TimeM.isLISCell_maxAbove`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/LongestIncreasingSubsequence.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/LongestIncreasingSubsequence.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/longest-increasing-subsequence/index.html#is-liscell-max-above).

## Correctness of the quadratic LIS program

For every list $xs$ over a preorder, the list
returned by the quadratic longest-increasing-subsequence program on $xs$ is a subsequence of $xs$,
is strictly increasing (each element strictly less than every later one), and is at least as long
as every strictly increasing subsequence of $xs$.

Formalized by `Cslib.Algorithms.Lean.TimeM.longestIncreasingSubsequence_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/LongestIncreasingSubsequence.lean, line 292](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/LongestIncreasingSubsequence.lean#L292). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/longest-increasing-subsequence/index.html#longest-increasing-subsequence-spec).

## The quadratic LIS program attains the optimal length

For every list $xs$ over a preorder,
the length of the list returned by the quadratic longest-increasing-subsequence program on $xs$ is
the length of a longest strictly increasing subsequence of $xs$.

Formalized by `Cslib.Algorithms.Lean.TimeM.isLISLength_longestIncreasingSubsequence`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/LongestIncreasingSubsequence.lean, line 338](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/LongestIncreasingSubsequence.lean#L338). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/longest-increasing-subsequence/index.html#is-lislength-longest-increasing-subseque).

## Uniqueness of the longest increasing subsequence length

For every list $xs$ of elements
of a preorder and all natural numbers $k$ and $k'$, if both $k$ and $k'$ are the length of a
longest strictly increasing subsequence of $xs$, then $k = k'$.

Formalized by `Cslib.Algorithms.Lean.TimeM.IsLISLength.unique`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/LongestIncreasingSubsequence.lean, line 345](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/LongestIncreasingSubsequence.lean#L345). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/longest-increasing-subsequence/index.html#unique).

## Correctness of the quadratic LIS program, by length

For every list $xs$ over a preorder
and every natural number $k$, the list returned by the quadratic longest-increasing-subsequence
program on $xs$ has length $k$ if and only if $k$ is the length of a longest strictly increasing
subsequence of $xs$.

Formalized by `Cslib.Algorithms.Lean.TimeM.length_longestIncreasingSubsequence_eq_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/LongestIncreasingSubsequence.lean, line 352](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/LongestIncreasingSubsequence.lean#L352). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/longest-increasing-subsequence/index.html#length-longest-increasing-subsequence-eq).

## Patience step

Given an array $t$ of tails and an element $x$ over a linear order, let $i$
be the index returned by the lower-bound binary search for $x$ in $t$. If $i$ is less than the
size of $t$, the step replaces the entry of $t$ at index $i$ by $x$; otherwise it appends $x$ to
$t$. Its cost is the number of comparisons made by the binary search.

When $t$ is sorted increasingly, as it stays throughout the patience scan from the empty array,
$i$ is the first index whose entry is at least $x$, so the step replaces the first entry $\ge x$,
or appends $x$ if there is none. On unsorted input $i$ need not be the first such index.

Formalized by `Cslib.Algorithms.Lean.TimeM.patienceStep`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/PatienceSorting.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/PatienceSorting.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/longest-increasing-subsequence/index.html#patience-step).

## Patience scan

Given an array of tails and a list over a linear order, the patience scan
applies the patience step to the elements of the list in order: on the empty list it returns the
tails unchanged, and on a list $x$ followed by $xs$ it applies the patience step for $x$ to the
tails and then runs the patience scan of $xs$ from the result. Its cost is the total cost of the
steps.

Formalized by `Cslib.Algorithms.Lean.TimeM.patienceScan`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/PatienceSorting.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/PatienceSorting.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/longest-increasing-subsequence/index.html#patience-scan).

## Patience sorting

Given a list $xs$ over a linear order, patience sorting runs the patience
scan of $xs$ starting from the empty array of tails and returns the size of the resulting array.
Its cost is the number of comparisons made by the scan.

Formalized by `Cslib.Algorithms.Lean.TimeM.patienceLength`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/PatienceSorting.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/PatienceSorting.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/longest-increasing-subsequence/index.html#patience-length).

## Patience sorting invariant

For lists $P$ and $t = (t_0, \dots, t_{m-1})$ over a linear
order, the invariant holds for the processed prefix $P$ and the tails $t$ when three conditions
hold: $t$ is strictly increasing; for every $k < m$ some strictly increasing subsequence of $P$ of
length $k + 1$ has last element $t_k$; and every nonempty strictly increasing subsequence of $P$,
of length $\ell$ and with last element $y$, satisfies $\ell \le m$ and $t_{\ell - 1} \le y$.

Formalized by `Cslib.Algorithms.Lean.TimeM.PatienceInv`, a structure declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/PatienceSorting.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/PatienceSorting.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/longest-increasing-subsequence/index.html#patience-inv).

## The patience scan preserves the invariant

Let $P$ be a list and $t$ an array of tails over
a linear order such that the patience sorting invariant holds for $P$ and the entries of $t$. Then
for every list $xs$, the invariant holds for $P$ followed by $xs$ and the entries of the array
returned by the patience scan of $xs$ from $t$.

Formalized by `Cslib.Algorithms.Lean.TimeM.PatienceInv.scan`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/PatienceSorting.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/PatienceSorting.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/longest-increasing-subsequence/index.html#scan).

## Correctness of patience sorting

For every list $xs$ over a linear order, the value
returned by patience sorting on $xs$ is the length of a longest strictly increasing subsequence of
$xs$: some strictly increasing subsequence of $xs$ has this length, and no strictly increasing
subsequence of $xs$ is longer.

Formalized by `Cslib.Algorithms.Lean.TimeM.patienceLength_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/PatienceSorting.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/PatienceSorting.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/longest-increasing-subsequence/index.html#patience-length-spec).

## Patience sorting agrees with the quadratic dynamic program

For every list $xs$ over a
linear order, the value returned by patience sorting on $xs$ equals the length of the list
returned on $xs$ by the quadratic dynamic program for a longest strictly increasing subsequence.

Formalized by `Cslib.Algorithms.Lean.TimeM.patienceLength_eq_length_longestIncreasingSubsequence`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/PatienceSorting.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/PatienceSorting.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/longest-increasing-subsequence/index.html#patience-length-eq-length-longest-increa).

## A patience step grows the tails by at most one

Let $\alpha$ be a linear order. For every
array $t$ over $\alpha$ and every element $x \in \alpha$, the array returned by the patience step
for $x$ on $t$ has size at most the size of $t$ plus $1$.

Formalized by `Cslib.Algorithms.Lean.TimeM.patienceStep_size_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/PatienceSorting.lean, line 283](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/PatienceSorting.lean#L283). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/longest-increasing-subsequence/index.html#patience-step-size-le).

## Comparison bound for patience sorting

For every list $xs$ of length $n$ over a linear
order, patience sorting on $xs$ uses at most $n \lceil \log_2 (n + 1) \rceil$ comparisons.

Formalized by `Cslib.Algorithms.Lean.TimeM.patienceLength_time_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/PatienceSorting.lean, line 313](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/PatienceSorting.lean#L313). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/longest-increasing-subsequence/index.html#patience-length-time-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Longest increasing subsequence](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/longest-increasing-subsequence/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/dynamic-programming/longest-increasing-subsequence)
