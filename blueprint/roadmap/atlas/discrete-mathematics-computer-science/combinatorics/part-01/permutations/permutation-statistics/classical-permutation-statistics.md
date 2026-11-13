---
declaration: section
origin: cited
lean: MetaMathlibExt.permLeftToRightMaxCount, MetaMathlibExt.permRightToLeftMaxCount, MetaMathlibExt.permLeftToRightMinCount, MetaMathlibExt.permRightToLeftMinCount, MetaMathlibExt.IsDoubleAscentAt, MetaMathlibExt.IsDoubleDescentAt, MetaMathlibExt.IsPeakAt, MetaMathlibExt.IsValleyAt
statement: formalized
proof: formalized
---

# Classical permutation statistics

15 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/classical-permutation-statistics/index.html).

## Left-to-right and right-to-left extrema

## Number of left-to-right maxima

For a permutation $\sigma$ of $\{0, 1, \dots, n-1\}$,
$\mathrm{lmax}(\sigma)$ is the number of positions $i$ such that $\sigma(j) < \sigma(i)$ for
every position $j < i$, that is, the number of entries larger than every entry to their left.

## Sources

- Dan Li and Sergey Kitaev, *King Permutations and Partially Ordered Patterns*, INTEGERS 26 (2026), Article A59, Section 1 (statistics).

Formalized by `MetaMathlibExt.permLeftToRightMaxCount`, a definition declared in [MathlibExt/Combinatorics/Enumerative/PermutationStatistics.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PermutationStatistics.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/classical-permutation-statistics/index.html#perm-left-to-right-max-count).

## Number of right-to-left maxima

For a permutation $\sigma$ of $\{0, 1, \dots, n - 1\}$
written in one-line notation, $\operatorname{rmax}(\sigma)$ is the number of positions $i$ such
that $\sigma(j) < \sigma(i)$ for every position $j > i$, that is, the number of entries larger
than every entry to their right.

## Sources

- Dan Li and Sergey Kitaev, *King Permutations and Partially Ordered Patterns*, INTEGERS 26 (2026), Article A59, Section 1 (statistics).

Formalized by `MetaMathlibExt.permRightToLeftMaxCount`, a definition declared in [MathlibExt/Combinatorics/Enumerative/PermutationStatistics.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PermutationStatistics.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/classical-permutation-statistics/index.html#perm-right-to-left-max-count).

## Number of left-to-right minima

For a permutation $\sigma$ of $\{0, 1, \dots, n - 1\}$
written in one-line notation, $\operatorname{lmin}(\sigma)$ is the number of positions $i$ such
that $\sigma(i) < \sigma(j)$ for every position $j < i$, that is, the number of entries smaller
than every entry to their left.

## Sources

- Dan Li and Sergey Kitaev, *King Permutations and Partially Ordered Patterns*, INTEGERS 26 (2026), Article A59, Section 1 (statistics).

Formalized by `MetaMathlibExt.permLeftToRightMinCount`, a definition declared in [MathlibExt/Combinatorics/Enumerative/PermutationStatistics.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PermutationStatistics.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/classical-permutation-statistics/index.html#perm-left-to-right-min-count).

## Number of right-to-left minima

For a permutation $\sigma$ of $\{0, 1, \dots, n - 1\}$
written in one-line notation, $\operatorname{rmin}(\sigma)$ is the number of positions $i$ such
that $\sigma(i) < \sigma(j)$ for every position $j > i$, that is, the number of entries smaller
than every entry to their right.

## Sources

- Dan Li and Sergey Kitaev, *King Permutations and Partially Ordered Patterns*, INTEGERS 26 (2026), Article A59, Section 1 (statistics).

Formalized by `MetaMathlibExt.permRightToLeftMinCount`, a definition declared in [MathlibExt/Combinatorics/Enumerative/PermutationStatistics.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PermutationStatistics.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/classical-permutation-statistics/index.html#perm-right-to-left-min-count).

## Double ascent of a permutation

Let $\sigma$ be a permutation of $\{0, 1, \dots, n-1\}$.
A position $i$ is a double ascent of $\sigma$ if $i + 2 < n$ and
$\sigma(i) < \sigma(i+1) < \sigma(i+2)$.

## Sources

- Han, *Joint Distributions of 10 Classical Statistics over Permutations Avoiding Two Patterns of Length 3*, INTEGERS 26 (2026), Article A18, Section 1 (`dasc`).

Formalized by `MetaMathlibExt.IsDoubleAscentAt`, a definition declared in [MathlibExt/Combinatorics/Enumerative/PermutationStatistics.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PermutationStatistics.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/classical-permutation-statistics/index.html#is-double-ascent-at).

## Double descent of a permutation

Let $\sigma$ be a permutation of $\{0, 1, \dots, n-1\}$.
A position $i$ is a double descent of $\sigma$ if $i + 2 < n$ and
$\sigma(i) > \sigma(i+1) > \sigma(i+2)$.

## Sources

- Han, *Joint Distributions of 10 Classical Statistics over Permutations Avoiding Two Patterns of Length 3*, INTEGERS 26 (2026), Article A18, Section 1 (`ddes`).

Formalized by `MetaMathlibExt.IsDoubleDescentAt`, a definition declared in [MathlibExt/Combinatorics/Enumerative/PermutationStatistics.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PermutationStatistics.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/classical-permutation-statistics/index.html#is-double-descent-at).

## Peak of a permutation

Let $\sigma$ be a permutation of $\{0, 1, \dots, n-1\}$.
A position $i$ is a peak of $\sigma$ if $i + 2 < n$ and $\sigma(i) < \sigma(i+1) > \sigma(i+2)$.
Thus the peak entry is $\sigma(i+1)$, and the position recorded is $i$, that of the first of
the three entries.

## Sources

- Han, *Joint Distributions of 10 Classical Statistics over Permutations Avoiding Two Patterns of Length 3*, INTEGERS 26 (2026), Article A18, Section 1 (`pk`).

Formalized by `MetaMathlibExt.IsPeakAt`, a definition declared in [MathlibExt/Combinatorics/Enumerative/PermutationStatistics.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PermutationStatistics.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/classical-permutation-statistics/index.html#is-peak-at).

## Valley of a permutation

Let $\sigma$ be a permutation of $\{0, 1, \dots, n-1\}$.
A position $i$ is a valley of $\sigma$ if $i + 2 < n$ and
$\sigma(i) > \sigma(i+1) < \sigma(i+2)$. Thus the valley entry is $\sigma(i+1)$, and the
position recorded is $i$, that of the first of the three entries.

## Sources

- Han, *Joint Distributions of 10 Classical Statistics over Permutations Avoiding Two Patterns of Length 3*, INTEGERS 26 (2026), Article A18, Section 1 (`vl`).

Formalized by `MetaMathlibExt.IsValleyAt`, a definition declared in [MathlibExt/Combinatorics/Enumerative/PermutationStatistics.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PermutationStatistics.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/classical-permutation-statistics/index.html#is-valley-at).

## Number of double ascents

For a permutation $\sigma$ of $\{0, 1, \dots, n-1\}$,
$\mathrm{dasc}(\sigma)$ is the number of positions $i$ that are double ascents of $\sigma$.

## Sources

- Han, *Joint Distributions of 10 Classical Statistics over Permutations Avoiding Two Patterns of Length 3*, INTEGERS 26 (2026), Article A18, Section 1 (`dasc`).

Formalized by `MetaMathlibExt.permDoubleAscents`, a definition declared in [MathlibExt/Combinatorics/Enumerative/PermutationStatistics.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PermutationStatistics.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/classical-permutation-statistics/index.html#perm-double-ascents).

## Number of double descents

For a permutation $\sigma$ of $\{0, 1, \dots, n-1\}$,
$\mathrm{ddes}(\sigma)$ is the number of positions $i$ that are double descents of $\sigma$.

## Sources

- Han, *Joint Distributions of 10 Classical Statistics over Permutations Avoiding Two Patterns of Length 3*, INTEGERS 26 (2026), Article A18, Section 1 (`ddes`).

Formalized by `MetaMathlibExt.permDoubleDescents`, a definition declared in [MathlibExt/Combinatorics/Enumerative/PermutationStatistics.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PermutationStatistics.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/classical-permutation-statistics/index.html#perm-double-descents).

## Number of peaks of a permutation

For a permutation $\sigma$ of $\{0, 1, \dots, n - 1\}$
written in one-line notation, $\operatorname{pk}(\sigma)$ is the number of positions $i$ with
$i + 2 < n$ and $\sigma(i) < \sigma(i + 1) > \sigma(i + 2)$, that is, the number of peaks of
$\sigma$.

## Sources

- Han, *Joint Distributions of 10 Classical Statistics over Permutations Avoiding Two Patterns of Length 3*, INTEGERS 26 (2026), Article A18, Section 1 (`pk`).

Formalized by `MetaMathlibExt.permPeaks`, a definition declared in [MathlibExt/Combinatorics/Enumerative/PermutationStatistics.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PermutationStatistics.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/classical-permutation-statistics/index.html#perm-peaks).

## Number of valleys of a permutation

For a permutation $\sigma$ of
$\{0, 1, \dots, n - 1\}$ written in one-line notation, $\operatorname{vl}(\sigma)$ is the number
of positions $i$ with $i + 2 < n$ and $\sigma(i) > \sigma(i + 1) < \sigma(i + 2)$, that is, the
number of valleys of $\sigma$.

## Sources

- Han, *Joint Distributions of 10 Classical Statistics over Permutations Avoiding Two Patterns of Length 3*, INTEGERS 26 (2026), Article A18, Section 1 (`vl`).

Formalized by `MetaMathlibExt.permValleys`, a definition declared in [MathlibExt/Combinatorics/Enumerative/PermutationStatistics.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PermutationStatistics.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/classical-permutation-statistics/index.html#perm-valleys).

## Number of positions with two successors

For every natural number $n$, exactly $n - 2$ of
the positions $i \in \{0, 1, \dots, n-1\}$ satisfy $i + 2 < n$, where $n - 2$ is truncated
subtraction (it is $0$ when $n < 2$).

These are the positions at which a permutation of $\{0, 1, \dots, n-1\}$ can have a double
ascent, a double descent, a peak or a valley.

## Sources

- Han, *Joint Distributions of 10 Classical Statistics over Permutations Avoiding Two Patterns of Length 3*, INTEGERS 26 (2026), Article A18, Section 1.

Formalized by `MetaMathlibExt.card_filter_add_two_lt`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/PermutationStatistics.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PermutationStatistics.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/classical-permutation-statistics/index.html#card-filter-add-two-lt).

## Local shape of a position in a permutation

Let $\sigma$ be a permutation of
$\{0, 1, \dots, n-1\}$ and let $i$ be a position. If $i + 2 < n$, then $i$ is exactly one of a
double ascent, a double descent, a peak or a valley of $\sigma$; otherwise $i$ is none of them.
That is, the number of these four properties that $i$ has is $1$ when $i + 2 < n$ and $0$
otherwise.

## Sources

- Han, *Joint Distributions of 10 Classical Statistics over Permutations Avoiding Two Patterns of Length 3*, INTEGERS 26 (2026), Article A18, Section 1.

Formalized by `MetaMathlibExt.ite_isDoubleAscentAt_add_ite_isDoubleDescentAt_add_ite_isPeakAt_add_ite_isValleyAt`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/PermutationStatistics.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PermutationStatistics.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/classical-permutation-statistics/index.html#ite-is-double-ascent-at-add-ite-is-doubl).

## Sum of the four local statistics of a permutation

Let $\sigma$ be a permutation of
$\{0, 1, \dots, n-1\}$, and write $\mathrm{dasc}(\sigma)$, $\mathrm{ddes}(\sigma)$,
$\mathrm{pk}(\sigma)$ and $\mathrm{vl}(\sigma)$ for its numbers of double ascents, double
descents, peaks and valleys. Then
$\mathrm{dasc}(\sigma) + \mathrm{ddes}(\sigma) + \mathrm{pk}(\sigma) + \mathrm{vl}(\sigma) = n - 2$,
where $n - 2$ is truncated subtraction (it is $0$ when $n < 2$).

## Sources

- Han, *Joint Distributions of 10 Classical Statistics over Permutations Avoiding Two Patterns of Length 3*, INTEGERS 26 (2026), Article A18, Section 1.

Formalized by `MetaMathlibExt.permDoubleAscents_add_permDoubleDescents_add_permPeaks_add_permValleys`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/PermutationStatistics.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PermutationStatistics.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/classical-permutation-statistics/index.html#perm-double-ascents-add-perm-double-desc).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Classical permutation statistics](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/classical-permutation-statistics/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/permutations/permutation-statistics/classical-permutation-statistics)
