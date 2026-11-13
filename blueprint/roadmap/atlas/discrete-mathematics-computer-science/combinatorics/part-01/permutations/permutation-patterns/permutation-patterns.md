---
declaration: section
origin: cited
lean: MetaMathlibExt.fibonacci_card_parity_alternating_avoiding_312_231, MetaMathlibExt.card_nontrivial_1234_3412_classes, MetaMathlibExt.card_permutations_avoiding_231_with_peak_count
statement: formalized
proof: formalized
---

# Permutation patterns: its own results

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/index.html).

Classical, consecutive, mesh and signed patterns in permutations and in inversion and ascent sequences, pattern-avoidance counts, pattern-replacement classes, stack sorting, and king and separable permutations.

## Fibonacci count of parity-preserving permutations avoiding $312$ and $231$

For every
integer $n \ge 1$, the number of permutations $\pi$ of $\{0, 1, \dots, n-1\}$ such that
$\pi(i) \equiv i \pmod 2$ for every $i$ and that avoid the patterns $312$ and $231$ equals the
Fibonacci number $F_n$, where $F_1 = F_2 = 1$. Here $\pi$ contains $312$ if there are
$i < j < k$ with $\pi(j) < \pi(k) < \pi(i)$, and contains $231$ if there are $i < j < k$ with
$\pi(k) < \pi(i) < \pi(j)$.

Equivalently, these are the parity-alternating permutations of $\{1, \dots, n\}$ that start with
an odd entry and avoid $312$ and $231$.

## Sources

- Per Alexandersson, Samuel Asefa Fufa, and Frether Getachew Kebede, "Pattern-Avoidance and Fuss–Catalan Numbers", Journal of Integer Sequences 26 (2023), Article 23.4.2, Proposition lines 1757-1759, <https://cs.uwaterloo.ca/journals/JIS/VOL26/Getachew/get3.tex>.

Formalized by `MetaMathlibExt.fibonacci_card_parity_alternating_avoiding_312_231`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/FibonacciPAPAvoidance.lean, line 510](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/FibonacciPAPAvoidance.lean#L510). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/index.html#fibonacci-card-parity-alternating-avoidi).

## Nontrivial classes under \{1234, 3412}-pattern replacement

Let $n \ge 7$ and let $S_n$ be
the group of permutations of $\{0, 1, \dots, n - 1\}$. A move takes $\sigma \in S_n$ with positions
$i_1 < i_2 < i_3 < i_4$ such that $\sigma(i_1) < \sigma(i_2) < \sigma(i_3) < \sigma(i_4)$ to the
permutation $\tau$ with $\tau(i_1) = \sigma(i_3)$, $\tau(i_2) = \sigma(i_4)$,
$\tau(i_3) = \sigma(i_1)$, $\tau(i_4) = \sigma(i_2)$ and $\tau(j) = \sigma(j)$ for every other
position $j$; that is, it replaces an occurrence of the pattern $1234$ by one of $3412$. Call two
permutations equivalent when one is reached from the other by a finite sequence of moves and
reverse moves. Then the number of equivalence classes with more than one element is
$(n^3 + 6n^2 - 55n + 54)/6$.

This formula was conjectured by Ma; its values form sequence A330395 in the OEIS. The proof
decomposes the exceptional set into swap classes and a generic part. Kernel-checked finite
certificates handle the $S_5$ and $S_6$ classes, reachability in $S_7$ and the deletion boundary
in $S_8$. Point insertion then gives a recurrence, whose solution is the displayed polynomial.

## Sources

- Quinn Perian, Bella Xu, and Alexander Lu Zhang, "Counting the Nontrivial Equivalence Classes of Sn Under {1234,3412}-Pattern-Replacement", Journal of Integer Sequences 23 (2020), Article 20.10.2, Theorem `thm:nontrivial`, lines 172-175, <https://cs.uwaterloo.ca/journals/JIS/VOL23/Zhang/zhang6.tex>.

Formalized by `MetaMathlibExt.card_nontrivial_1234_3412_classes`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/Nontrivial1234_3412Classes.lean, line 10824](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/Nontrivial1234_3412Classes.lean#L10824). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/index.html#card-nontrivial-1234-3412-classes).

## Peaks of 231-avoiding permutations

Let $n \ge 1$ and $k$ be natural numbers. A permutation
$\sigma$ of $\{0, \dots, n-1\}$ avoids $231$ if there are no positions $i < j < l$ with
$\sigma(l) < \sigma(i) < \sigma(j)$, and $\sigma$ has a peak at a position $i$ with
$0 < i < n - 1$ if $\sigma(i-1) < \sigma(i)$ and $\sigma(i+1) < \sigma(i)$. The number of
231-avoiding permutations of $\{0, \dots, n-1\}$ with exactly $k$ peaks is
$2^{n-2k-1} \binom{n-1}{2k} \binom{2k}{k} / (k+1)$, computed in the natural numbers: the
exponent $n - 2k - 1$ is truncated at $0$ and the division rounds down.

## Sources

- Lara Pudwell, Jacob Roth, and Teresa Wheeland, "Distributions of Statistics over Pattern-Avoiding Permutations", Journal of Integer Sequences 22 (2019), Article 19.2.6, Theorem `T:pk231`, line 228, <https://cs.uwaterloo.ca/journals/JIS/VOL22/Pudwell/pudwell6.tex>.

Formalized by `MetaMathlibExt.card_permutations_avoiding_231_with_peak_count`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/PeakStatistic231.lean, line 1567](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PeakStatistic231.lean#L1567). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/index.html#card-permutations-avoiding-231-with-peak).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Permutation patterns](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/permutations/permutation-patterns)
