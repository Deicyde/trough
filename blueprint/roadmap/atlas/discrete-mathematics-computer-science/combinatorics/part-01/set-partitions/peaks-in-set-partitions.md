---
declaration: section
origin: cited
lean: MetaMathlibExt.IsSurjectiveRestrictedGrowthString, MetaMathlibExt.peak_generating_function_set_partitions, MetaMathlibExt.total_peaks_canonical, MetaMathlibExt.nonSymmetricPeakCount, MetaMathlibExt.symmetricPeakCount_nonSymmetricPeakCount_example, MetaMathlibExt.symmetricPeaks_derivative_generatingFunction, MetaMathlibExt.nonSymmetricPeaks_derivative_generatingFunction, MetaMathlibExt.sum_symmetricPeakCount_setPartitions
statement: formalized
---

# Peaks in set partitions

9 results, 5 proved and 4 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/peaks-in-set-partitions/index.html).

## Surjective restricted-growth strings

A word $w = w_0 w_1 \cdots w_{n-1}$ of length $n$
with letters in $\{0, 1, \dots, k-1\}$ is a surjective restricted-growth string if every letter
$0, \dots, k-1$ occurs in $w$ and, for every position $i$ and every letter $m < w_i$, some
position $j < i$ has $w_j = m$.

Formalized by `MetaMathlibExt.IsSurjectiveRestrictedGrowthString`, a definition declared in [MathlibExt/Combinatorics/Enumerative/Partition/PeakGeneratingFunction.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/Partition/PeakGeneratingFunction.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/peaks-in-set-partitions/index.html#is-surjective-restricted-growth-string).

## Peak generating function for set partitions

Let $k \ge 1$. Work in the fraction field of
the ring $\mathbb{Z}[q][[x]]$ of power series in $x$ with coefficients in $\mathbb{Z}[q]$. For
a word $w = w_0 \cdots w_{n-1}$, let $\mathrm{pk}(w)$ be the number of positions $a$ with
$a + 2 < n$ and $w_a < w_{a+1} > w_{a+2}$, and let $W_{n,k}$ be the set of surjective
restricted-growth strings of length $n$ with letters in $\{0, \dots, k-1\}$. Let
$t = 1 + x^2 (1-q)/2$, let $U_m = U_m(t)$ for $m \in \mathbb{Z}$, where $U_m$ is the Chebyshev
polynomial of the second kind extended to negative indices by its recurrence (so $U_{-1} = 0$
and $U_{-2} = -1$), and let $R_j = (U_j - U_{j-1})/(U_{j-1} - U_{j-2})$. Then

$$\sum_{n \ge 0} \sum_{w \in W_{n,k}} q^{\mathrm{pk}(w)} x^n = x^k (1-q)^k \prod_{j=1}^{k}
\frac{1 + x + x^2 (1-q) - R_j}{1 + x (1-q) - R_j}.$$

Set partitions of $\{1, \dots, n\}$ with $k$ blocks are encoded by the strings in $W_{n,k}$, and
$\mathrm{pk}(w)$ counts the peaks of the encoded partition. Division is total in the fraction
field, so the statement carries no nonvanishing hypotheses.

Proof: Following Mansour and Shattuck, Lemmas 2.1, 2.2, and 2.6 and Theorem 2.7,
the proof combines first-occurrence decompositions with the Chebyshev recurrence.

## Sources

- Toufik Mansour and Mark Shattuck, "Counting Peaks and Valleys in a Partition of a Set," Journal of Integer Sequences 13 (2010), Article 10.6.8, Theorem, lines 313–317, <https://cs.uwaterloo.ca/journals/JIS/VOL13/Shattuck/shattuck3.tex>.

Formalized by `MetaMathlibExt.peak_generating_function_set_partitions`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/Partition/PeakGeneratingFunction.lean, line 1391](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/Partition/PeakGeneratingFunction.lean#L1391). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/peaks-in-set-partitions/index.html#peak-generating-function-set-partitions).

## Total number of peaks over set partitions

For natural numbers $n$ and $k$, call a word
$\pi = \pi_1 \cdots \pi_n$ on the alphabet $\{0, \dots, k-1\}$ a restricted growth word if it uses
every letter and, for every position $i$, every letter smaller than $\pi_i$ occurs among
$\pi_1, \dots, \pi_{i-1}$; these words encode the partitions of $[n]$ into $k$ blocks. A peak of
$\pi$ is a position $i$ with $1 < i < n$ and $\pi_{i-1} < \pi_i > \pi_{i+1}$. Then the total
number of peaks, summed over all restricted growth words of length $n$ on $k$ letters, equals

$$\binom{k}{2} S(n-1, k) + \sum_{j=2}^{k} \left(j \binom{j}{2} - \binom{j+1}{3}\right)
\sum_{i=3}^{n-k} j^{i-3}\, S(n-i, k),$$

where $S(m, k)$ is the Stirling number of the second kind, $n - 1$ is read as $0$ when $n = 0$,
and the inner sum is empty when $n - k < 3$.

## Sources

- Toufik Mansour and Mark Shattuck, "Counting Peaks and Valleys in a Partition of a Set", Journal of Integer Sequences 13 (2010), Article 10.6.8, Corollary 2, lines 388-394, <https://cs.uwaterloo.ca/journals/JIS/VOL13/Shattuck/shattuck3.tex>.

Formalized by `MetaMathlibExt.total_peaks_canonical`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/SetPartitionPeaks.lean, line 988](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/SetPartitionPeaks.lean#L988). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/peaks-in-set-partitions/index.html#total-peaks-canonical).

## Non-symmetric peaks of a word

For a word $w = w_1 w_2 \cdots w_\ell$ of natural numbers,
a non-symmetric peak is a position $i$ with $1 < i < \ell$ such that $w_{i-1} < w_i$,
$w_{i+1} < w_i$ and $w_{i-1} \ne w_{i+1}$. The non-symmetric peak count of $w$ is the number of
such positions; in particular it is $0$ when $\ell < 3$.

A peak with $w_{i-1} = w_{i+1}$ is a symmetric peak instead.

## Sources

- Walaa Asakly and Noor Kezil, *Counting Symmetric and Non-Symmetric Peaks in a Set Partition*, INTEGERS 26 (2026), Article A8, Section 1.

Formalized by `MetaMathlibExt.nonSymmetricPeakCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/SetPartitionSymmetricPeaksWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SetPartitionSymmetricPeaksWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/peaks-in-set-partitions/index.html#non-symmetric-peak-count).

## Peaks of the word $1322141251$

The word $1322141251$ (the list
$1, 3, 2, 2, 1, 4, 1, 2, 5, 1$) has exactly one symmetric peak, the factor $141$, and exactly two
non-symmetric peaks, the factors $132$ and $251$.

## Sources

- Walaa Asakly and Noor Kezil, *Counting Symmetric and Non-Symmetric Peaks in a Set Partition*, INTEGERS 26 (2026), Article A8, Section 1.

Formalized by `MetaMathlibExt.symmetricPeakCount_nonSymmetricPeakCount_example`, a theorem declared in [WantedExt/Combinatorics/Enumerative/SetPartitionSymmetricPeaksWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SetPartitionSymmetricPeaksWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/peaks-in-set-partitions/index.html#symmetric-peak-count-non-symmetric-peak).

## Generating function for the total number of symmetric peaks in set partitions

Fix
$k \in \mathbb{N}$ and, for each $n$, let $P_{n,k}$ be the set of surjective restricted-growth
strings of length $n$ with letters in $\{0, \dots, k-1\}$; these encode the partitions of
$\{1, \dots, n\}$ into exactly $k$ blocks. For $w \in P_{n,k}$ let $\operatorname{sp}(w)$ be the
number of symmetric peaks of $w$. In the ring $\mathbb{Z}[[x]]$ of formal power series let
$F_k(x) = \sum_{n \ge 0} |P_{n,k}| x^n$. Then

$$
\sum_{n \ge 0} \Big(\sum_{w \in P_{n,k}} \operatorname{sp}(w)\Big) x^n =
\max(k - 1, 0)\, x F_k(x) + F_k(x) \sum_{m=1}^{k} \binom{m}{2} \frac{x^3}{1 - m x},
$$

where $1/(1 - m x)$ is the inverse of $1 - m x$ in $\mathbb{Z}[[x]]$.

If $SP_k(x, q) = \sum_{n \ge 0} \sum_{w \in P_{n,k}} q^{\operatorname{sp}(w)} x^n$, then
$F_k(x) = SP_k(x, 1)$ and the left side is the derivative of $SP_k(x, q)$ in $q$ at $q = 1$.

## Sources

- Walaa Asakly and Noor Kezil, *Counting Symmetric and Non-Symmetric Peaks in a Set Partition*, INTEGERS 26 (2026), Article A8, Lemma 1.

Stated but not proved: `MetaMathlibExt.symmetricPeaks_derivative_generatingFunction` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SetPartitionSymmetricPeaksWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SetPartitionSymmetricPeaksWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/peaks-in-set-partitions/index.html#symmetric-peaks-derivative-generating-fu).

## Generating function for the total number of non-symmetric peaks in set partitions

Fix
$k \in \mathbb{N}$ and, for each $n$, let $P_{n,k}$ be the set of surjective restricted-growth
strings of length $n$ with letters in $\{0, \dots, k-1\}$; these encode the partitions of
$\{1, \dots, n\}$ into exactly $k$ blocks. For $w \in P_{n,k}$ let $\operatorname{nsp}(w)$ be the
number of non-symmetric peaks of $w$. In the ring $\mathbb{Z}[[x]]$ of formal power series let
$F_k(x) = \sum_{n \ge 0} |P_{n,k}| x^n$. Then

$$
\sum_{n \ge 0} \Big(\sum_{w \in P_{n,k}} \operatorname{nsp}(w)\Big) x^n =
\binom{k - 1}{2} x F_k(x) + F_k(x) \sum_{m=3}^{k} 2 \binom{m}{3} \frac{x^3}{1 - m x},
$$

where $k - 1$ is read as $0$ when $k = 0$ and $1/(1 - m x)$ is the inverse of $1 - m x$ in
$\mathbb{Z}[[x]]$.

If $NSP_k(x, q) = \sum_{n \ge 0} \sum_{w \in P_{n,k}} q^{\operatorname{nsp}(w)} x^n$, then
$F_k(x) = NSP_k(x, 1)$ and the left side is the derivative of $NSP_k(x, q)$ in $q$ at $q = 1$.

## Sources

- Walaa Asakly and Noor Kezil, *Counting Symmetric and Non-Symmetric Peaks in a Set Partition*, INTEGERS 26 (2026), Article A8, Lemma 2.

Stated but not proved: `MetaMathlibExt.nonSymmetricPeaks_derivative_generatingFunction` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SetPartitionSymmetricPeaksWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SetPartitionSymmetricPeaksWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/peaks-in-set-partitions/index.html#non-symmetric-peaks-derivative-generatin).

## Total number of symmetric peaks over set partitions with $k$ blocks

For natural numbers
$n$ and $k$, let $P_{n,k}$ be the set of surjective restricted-growth strings of length $n$ with
letters in $\{0, \dots, k-1\}$ (these encode the partitions of $\{1, \dots, n\}$ into exactly $k$
blocks). For $w \in P_{n,k}$ let $\operatorname{sp}(w)$ be the number of symmetric peaks of $w$,
and denote by $S(a, b)$ the Stirling numbers of the second kind. Then

$$
\sum_{w \in P_{n,k}} \operatorname{sp}(w) = (k - 1)\, S(n - 1, k) +
\sum_{j=2}^{k} \binom{j}{2} \sum_{i=3}^{n-k} j^{i-3}\, S(n - i, k),
$$

where the differences $k - 1$, $n - 1$ and $n - k$ of natural numbers are truncated at $0$.

## Sources

- Walaa Asakly and Noor Kezil, *Counting Symmetric and Non-Symmetric Peaks in a Set Partition*, INTEGERS 26 (2026), Article A8, Corollary 1.

Stated but not proved: `MetaMathlibExt.sum_symmetricPeakCount_setPartitions` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SetPartitionSymmetricPeaksWanted.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SetPartitionSymmetricPeaksWanted.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/peaks-in-set-partitions/index.html#sum-symmetric-peak-count-set-partitions).

## Total number of non-symmetric peaks over set partitions with $k$ blocks

For natural
numbers $n$ and $k$, let $P_{n,k}$ be the set of surjective restricted-growth strings of length $n$
with letters in $\{0, \dots, k-1\}$ (these encode the partitions of $\{1, \dots, n\}$ into exactly
$k$ blocks). For $w \in P_{n,k}$ let $\operatorname{nsp}(w)$ be the number of non-symmetric peaks
of $w$, and denote by $S(a, b)$ the Stirling numbers of the second kind. Then

$$
\sum_{w \in P_{n,k}} \operatorname{nsp}(w) = \binom{k - 1}{2} S(n - 1, k) +
2 \sum_{j=3}^{k} \binom{j}{3} \sum_{i=3}^{n-k} j^{i-3}\, S(n - i, k),
$$

where the differences $k - 1$, $n - 1$ and $n - k$ of natural numbers are truncated at $0$.

## Sources

- Walaa Asakly and Noor Kezil, *Counting Symmetric and Non-Symmetric Peaks in a Set Partition*, INTEGERS 26 (2026), Article A8, Corollary 2.

Stated but not proved: `MetaMathlibExt.sum_nonSymmetricPeakCount_setPartitions` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SetPartitionSymmetricPeaksWanted.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SetPartitionSymmetricPeaksWanted.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/peaks-in-set-partitions/index.html#sum-non-symmetric-peak-count-set-partiti).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Peaks in set partitions](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/peaks-in-set-partitions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/set-partitions/peaks-in-set-partitions)
