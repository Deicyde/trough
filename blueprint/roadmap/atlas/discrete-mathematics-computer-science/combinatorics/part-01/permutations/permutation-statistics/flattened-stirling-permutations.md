---
declaration: section
origin: cited
lean: MetaMathlibExt.wordRunStart, MetaMathlibExt.wordRunCount, MetaMathlibExt.IsFlattenedWord, MetaMathlibExt.flattenedStirlingCount, MetaMathlibExt.flattenedStirlingRunCount, MetaMathlibExt.flattenedPermRunCount, MetaMathlibExt.IsTypeBSetPartition, MetaMathlibExt.isFlattenedWord_example
statement: formalized
---

# Flattened Stirling permutations

36 results, 23 proved and 13 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/flattened-stirling-permutations/index.html).

## Start of a run

Position $i$ of a word $w = w_0 w_1 \cdots w_{m-1}$ of natural numbers
starts a run when $i = 0$ or the letter before it is larger, that is, $w_{i-1} > w_i$. Runs are
the maximal contiguous weakly increasing subwords, so these are exactly the positions where a run
begins.

## Sources

- Buck, Elder, Figueroa, Harris, Harry, Simpson, *Flattened Stirling Permutations*, INTEGERS 24 (2024), Article A104, Section 1 (runs).

Formalized by `MetaMathlibExt.wordRunStart`, a definition declared in [WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/flattened-stirling-permutations/index.html#word-run-start).

## Number of runs of a word

A run of a word $w = w_0 w_1 \cdots w_{m-1}$ of natural numbers is
a maximal contiguous weakly increasing subword. The number of runs of $w$ is the number of
positions $i < m$ that start a run, that is, with $i = 0$ or $w_{i-1} > w_i$; the empty word has
no runs.

## Sources

- Buck, Elder, Figueroa, Harris, Harry, Simpson, *Flattened Stirling Permutations*, INTEGERS 24 (2024), Article A104, Section 1 (runs).

Formalized by `MetaMathlibExt.wordRunCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/flattened-stirling-permutations/index.html#word-run-count).

## Flattened words

A word $w = w_1 w_2 \cdots w_m$ of natural numbers is flattened when
the leading letters of its runs, read left to right, are weakly increasing. Here a run is a
maximal contiguous weakly increasing subword, so position $i$ starts a run when $i = 1$ or
$w_{i-1} > w_i$; the condition is that $w_i \le w_j$ whenever $i < j$ and both positions
start runs.

## Sources

- Buck, Elder, Figueroa, Harris, Harry, Simpson, *Flattened Stirling Permutations*, INTEGERS 24 (2024), Article A104, Section 1 (flattened).

Formalized by `MetaMathlibExt.IsFlattenedWord`, a definition declared in [WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/flattened-stirling-permutations/index.html#is-flattened-word).

## Number of flattened Stirling permutations

For a natural number $n$,
$|\mathrm{flat}(Q_n)|$ is the number of flattened Stirling permutations of order $n$: words
$w_1 w_2 \cdots w_{2n}$ of natural numbers that are Stirling permutations of order $n$ and whose
runs (maximal contiguous weakly increasing subwords) have weakly increasing leading letters,
read from left to right.

## Sources

- Buck, Elder, Figueroa, Harris, Harry, Simpson, *Flattened Stirling Permutations*, INTEGERS 24 (2024), Article A104, Section 1.

Formalized by `MetaMathlibExt.flattenedStirlingCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/flattened-stirling-permutations/index.html#flattened-stirling-count).

## Counting flattened Stirling permutations by runs

For natural numbers $n$ and $k$,
$|\mathrm{flat}_k(Q_n)|$ is the number of flattened Stirling permutations of order $n$ with
exactly $k$ runs, where a run is a maximal contiguous weakly increasing subword.

## Sources

- Buck, Elder, Figueroa, Harris, Harry, Simpson, *Flattened Stirling Permutations*, INTEGERS 24 (2024), Article A104, Section 1.

Formalized by `MetaMathlibExt.flattenedStirlingRunCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/flattened-stirling-permutations/index.html#flattened-stirling-run-count).

## Flattened partitions counted by runs

For natural numbers $n$ and $k$, $f_{n,k}$ is the
number of permutations $\sigma$ of $\{0, 1, \dots, n - 1\}$ such that the word
$\sigma(0) \sigma(1) \cdots \sigma(n - 1)$ is flattened (the leading letters of its runs, read
left to right, are weakly increasing) and has exactly $k$ runs, where a run is a maximal
contiguous weakly increasing subword. These are the flattened partitions of length $n$ of
Nabawanda, Rakotondrajao, and Bamunoba, with letters $0, \dots, n - 1$ in place of
$1, \dots, n$.

## Sources

- Buck, Elder, Figueroa, Harris, Harry, Simpson, *Flattened Stirling Permutations*, INTEGERS 24 (2024), Article A104, Section 1 (flattened partitions, after Nabawanda, Rakotondrajao, and Bamunoba).

Formalized by `MetaMathlibExt.flattenedPermRunCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/flattened-stirling-permutations/index.html#flattened-perm-run-count).

## Type $B$ set partitions

For a natural number $n$, a set partition $P$ of the integer
interval $[-n, n] = \{-n, \dots, n\}$ is of type $B$ if for every block $\beta$ of $P$ the set
$-\beta = \{-x : x \in \beta\}$ is again a block of $P$, and exactly one block $\beta$ of $P$
satisfies $-\beta = \beta$.

## Sources

- Buck, Elder, Figueroa, Harris, Harry, Simpson, *Flattened Stirling Permutations*, INTEGERS 24 (2024), Article A104, Definition 1.

Formalized by `MetaMathlibExt.IsTypeBSetPartition`, a definition declared in [WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/flattened-stirling-permutations/index.html#is-type-bset-partition).

## A flattened word with four runs

The word
$w = 1\,1\,2\,2\,9\,9\,3\,8\,8\,3\,4\,6\,6\,7\,7\,4\,5\,5$ of length $18$ is flattened (the
leading letters of its runs, read left to right, are weakly increasing), and it has exactly
$4$ runs, where a run is a maximal contiguous weakly increasing subword.

## Sources

- Buck, Elder, Figueroa, Harris, Harry, Simpson, *Flattened Stirling Permutations*, INTEGERS 24 (2024), Article A104, Section 1 (example).

Formalized by `MetaMathlibExt.isFlattenedWord_example`, a theorem declared in [WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/flattened-stirling-permutations/index.html#is-flattened-word-example).

## A word that is not flattened

The word $123321445566778899$ is not flattened.

This word is a Stirling permutation of order $9$; its runs $1233$, $2$, $1445566778899$ have
leading letters $1, 2, 1$, which do not weakly increase.

## Sources

- Buck, Elder, Figueroa, Harris, Harry, Simpson, *Flattened Stirling Permutations*, INTEGERS 24 (2024), Article A104, Section 1 (example).

Formalized by `MetaMathlibExt.not_isFlattenedWord_example`, a theorem declared in [WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/flattened-stirling-permutations/index.html#not-is-flattened-word-example).

## The one-block partition is of type B

For every natural number $n$, the partition of
the integer interval $[-n, n] = \{-n, \dots, n\}$ into a single block is a type $B$ set
partition: its only block is closed under negation, so it is the unique block equal to its own
negative (the zero-block).

## Sources

- Buck, Elder, Figueroa, Harris, Harry, Simpson, *Flattened Stirling Permutations*, INTEGERS 24 (2024), Article A104, Definition 1; characteristic check of `IsTypeBSetPartition`.

Formalized by `MetaMathlibExt.isTypeBSetPartition_indiscrete`, a theorem declared in [WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/flattened-stirling-permutations/index.html#is-type-bset-partition-indiscrete).

## Recursion for flattened partitions by number of runs

Let $f_{n,k}$ be the number of
flattened partitions of length $n$ with exactly $k$ runs. For all $n \ge 1$ and $k \ge 2$,

$$
f_{n,k} = \sum_{m=1}^{n-2} \left( \binom{n-1}{m} - 1 \right) f_{m,k-1},
$$

where the sum is empty when $n \le 2$. Moreover $f_{n,1} = 1$ for every $n \ge 1$, and
$f_{n,k} = 0$ whenever $2 \le n \le k$.

This is the recursion of Nabawanda, Rakotondrajao, and Bamunoba as quoted in the paper.

## Sources

- Buck, Elder, Figueroa, Harris, Harry, Simpson, *Flattened Stirling Permutations*, INTEGERS 24 (2024), Article A104, Theorem 1 (quoting Nabawanda et al., Theorem 1).

Stated but not proved: `MetaMathlibExt.flattenedPermRunCount_recursion` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/flattened-stirling-permutations/index.html#flattened-perm-run-count-recursion).

## Flattened Stirling permutations and type $B$ set partitions

For every natural number
$n \ge 1$, the set of flattened Stirling permutations of order $n + 1$ is in bijection with the
set of type $B$ set partitions of $[-n, n] = \{-n, \dots, n\}$.

## Sources

- Buck, Elder, Figueroa, Harris, Harry, Simpson, *Flattened Stirling Permutations*, INTEGERS 24 (2024), Article A104, Theorem 2.

Stated but not proved: `MetaMathlibExt.nonempty_flattenedStirling_equiv_typeBSetPartition` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/flattened-stirling-permutations/index.html#nonempty-flattened-stirling-equiv-type-b).

## Flattened Stirling permutations are counted by Dowling numbers

For every $n \ge 1$, the
number $|\mathrm{flat}(Q_{n+1})|$ of flattened Stirling permutations of order $n + 1$ equals the
Dowling number $D_n = \sum_{k=0}^{n} W_{2,1,1}(n, k)$, where $W_{2,1,1}(n, k)$ are the
$(q, r)$-Whitney numbers of the second kind with $m = 2$, $r = 1$ and $q = 1$.

## Sources

- Buck, Elder, Figueroa, Harris, Harry, Simpson, *Flattened Stirling Permutations*, INTEGERS 24 (2024), Article A104, Corollary 1.

Stated but not proved: `MetaMathlibExt.flattenedStirlingCount_succ_eq_dowling` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/flattened-stirling-permutations/index.html#flattened-stirling-count-succ-eq-dowling).

## Maximum number of runs of a flattened Stirling permutation

For every natural number
$n \ge 1$, some flattened Stirling permutation of order $n$ has exactly
$\lceil 2n/3 \rceil$ runs, and no flattened Stirling permutation of order $n$ has more.

## Sources

- Buck, Elder, Figueroa, Harris, Harry, Simpson, *Flattened Stirling Permutations*, INTEGERS 24 (2024), Article A104, Lemma 5.

Stated but not proved: `MetaMathlibExt.isGreatest_flattenedStirling_runCount` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/flattened-stirling-permutations/index.html#is-greatest-flattened-stirling-run-count).

## Exactly one flattened Stirling permutation has one run

For every natural number
$n \ge 1$, exactly one flattened Stirling permutation of order $n$ has exactly one run.

## Sources

- Buck, Elder, Figueroa, Harris, Harry, Simpson, *Flattened Stirling Permutations*, INTEGERS 24 (2024), Article A104, Proposition 2, part 1.

Stated but not proved: `MetaMathlibExt.flattenedStirlingRunCount_one` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/flattened-stirling-permutations/index.html#flattened-stirling-run-count-one).

## Recursion for flattened Stirling permutations with two runs

Write
$|\mathrm{flat}_2(Q_n)|$ for the number of flattened Stirling permutations of order $n$ with
exactly two runs. Then $|\mathrm{flat}_2(Q_1)| = 0$, and for every natural number $n \ge 1$,
$|\mathrm{flat}_2(Q_{n+1})| = 2\,|\mathrm{flat}_2(Q_n)| + 2n - 1$.

## Sources

- Buck, Elder, Figueroa, Harris, Harry, Simpson, *Flattened Stirling Permutations*, INTEGERS 24 (2024), Article A104, Proposition 2, part 2.

Stated but not proved: `MetaMathlibExt.flattenedStirlingRunCount_two_recursion` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/flattened-stirling-permutations/index.html#flattened-stirling-run-count-two-recursi).

## Closed form for flattened Stirling permutations with two runs

For every natural number
$n \ge 1$, the number $|\mathrm{flat}_2(Q_{n+1})|$ of flattened Stirling permutations of order
$n + 1$ with exactly two runs equals $3(2^n - 1) - 2n$.

## Sources

- Buck, Elder, Figueroa, Harris, Harry, Simpson, *Flattened Stirling Permutations*, INTEGERS 24 (2024), Article A104, Corollary 2.

Stated but not proved: `MetaMathlibExt.flattenedStirlingRunCount_two_closed` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/flattened-stirling-permutations/index.html#flattened-stirling-run-count-two-closed).

## A binomial–Stirling formula for flattened Stirling permutations

For every natural number
$n$, the number of flattened Stirling permutations of order $n + 1$ is

$$
|\mathrm{flat}(Q_{n+1})| = \sum_{i=0}^{n} \binom{n}{i} \sum_{k=0}^{n-i} 2^{n-i-k} S(n-i, k),
$$

where $S(a, k)$ are the Stirling numbers of the second kind, with $S(0, 0) = 1$.

## Sources

- Buck, Elder, Figueroa, Harris, Harry, Simpson, *Flattened Stirling Permutations*, INTEGERS 24 (2024), Article A104, Theorem 4.

Stated but not proved: `MetaMathlibExt.flattenedStirlingCount_succ_eq_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/flattened-stirling-permutations/index.html#flattened-stirling-count-succ-eq-sum).

## A binomial–Stirling formula for the Dowling numbers

Let $W_{2,1,1}(n, k)$ be the
$(q, r)$-Whitney numbers of the second kind with $m = 2$, $r = 1$ and $q = 1$, and let
$D_n = \sum_{k=0}^{n} W_{2,1,1}(n, k)$ be the associated Dowling numbers. For every $n \ge 1$,

$$
D_n = \sum_{i=0}^{n} \binom{n}{i} \sum_{k=0}^{n-i} 2^{n-i-k} S(n-i, k),
$$

where $S(a, k)$ are the Stirling numbers of the second kind, with $S(0, 0) = 1$.

## Sources

- Buck, Elder, Figueroa, Harris, Harry, Simpson, *Flattened Stirling Permutations*, INTEGERS 24 (2024), Article A104, Corollary 3, formula.

Stated but not proved: `MetaMathlibExt.dowling_eq_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/flattened-stirling-permutations/index.html#dowling-eq-sum).

## Exponential generating function of the Dowling numbers

For $n \ge 0$ let $D_n$ be the
$n$-th Dowling number of the group of order $2$, that is, the $(q, r)$-Dowling number
$D_n = \sum_{k=0}^{n} W_{2,1,1}(n, k)$ built from the $(q, r)$-Whitney numbers of the second
kind with $m = 2$, $r = 1$, $q = 1$. Then for every complex number $x$ the series
$\sum_{n \ge 0} D_n x^n / n!$ is summable with sum $\exp\bigl(x + (e^{2x} - 1)/2\bigr)$.

## Sources

- Buck, Elder, Figueroa, Harris, Harry, Simpson, *Flattened Stirling Permutations*, INTEGERS 24 (2024), Article A104, Corollary 3, generating function.

Stated but not proved: `MetaMathlibExt.hasSum_dowling_egf` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/flattened-stirling-permutations/index.html#has-sum-dowling-egf).

## The shift map

For a finite set $S$ of integers, $h(S) = \{|i| + 1 : i \in S\}$, a
finite set of natural numbers.

In particular, for every natural number $n$, $h$ sends subsets of $[-n, n]$ to subsets of
$\{1, \dots, n + 1\}$.

## Sources

- Buck, Elder, Figueroa, Harris, Harry, Simpson, *Flattened Stirling Permutations*, INTEGERS 24 (2024), Article A104, Lemma 2 (the map `h`).

Formalized by `MetaMathlibExt.typeBShift`, a definition declared in [WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/flattened-stirling-permutations/index.html#type-bshift).

## Doubled word

For a finite set $S = \{s_1 < s_2 < \dots < s_k\}$ of natural numbers, the
doubled word of $S$ is $f(S) = s_1 s_1 s_2 s_2 \cdots s_k s_k$, which lists the elements of $S$
in increasing order with each one written twice; $f(\emptyset)$ is the empty word.

## Sources

- Buck, Elder, Figueroa, Harris, Harry, Simpson, *Flattened Stirling Permutations*, INTEGERS 24 (2024), Article A104, Lemma 3 (the map `f`).

Formalized by `MetaMathlibExt.doubledWord`, a definition declared in [WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean, line 269](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean#L269). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/flattened-stirling-permutations/index.html#doubled-word).

## Wrapped word of a finite set

For a finite set $S = \{s_1 < s_2 < \dots < s_k\}$ of natural
numbers, the wrapped word $g(S)$ is $s_1 s_2 s_2 \cdots s_k s_k s_1$: the smallest element, then
each larger element written twice in increasing order, then the smallest element again. For
$S = \emptyset$, $g(S)$ is the empty word.

## Sources

- Buck, Elder, Figueroa, Harris, Harry, Simpson, *Flattened Stirling Permutations*, INTEGERS 24 (2024), Article A104, Lemma 3 (the map `g`).

Formalized by `MetaMathlibExt.wrappedWord`, a definition declared in [WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/flattened-stirling-permutations/index.html#wrapped-word).

## An example of the shift map

For the map $h(S) = \{|i| + 1 : i \in S\}$ on finite sets
of integers, $h(\{-2, 0, 1\}) = \{1, 2, 3\}$.

## Sources

- Buck, Elder, Figueroa, Harris, Harry, Simpson, *Flattened Stirling Permutations*, INTEGERS 24 (2024), Article A104, Lemma 2 (the map `h`).

Formalized by `MetaMathlibExt.typeBShift_example`, a theorem declared in [WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/flattened-stirling-permutations/index.html#type-bshift-example).

## The doubled word of a singleton

For every natural number $s$, the doubled word of the
singleton $\{s\}$ is $f(\{s\}) = s\,s$, the word of length two whose letters are both $s$.

## Sources

- Buck, Elder, Figueroa, Harris, Harry, Simpson, *Flattened Stirling Permutations*, INTEGERS 24 (2024), Article A104, Lemma 3 (the map `f`).

Formalized by `MetaMathlibExt.doubledWord_singleton`, a theorem declared in [WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean, line 293](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean#L293). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/flattened-stirling-permutations/index.html#doubled-word-singleton).

## Length of the doubled word

For every finite set $S$ of natural numbers with elements
$s_1 < \dots < s_k$, the doubled word $f(S) = s_1 s_1 s_2 s_2 \cdots s_k s_k$ has length $2|S|$.

## Sources

- Buck, Elder, Figueroa, Harris, Harry, Simpson, *Flattened Stirling Permutations*, INTEGERS 24 (2024), Article A104, Lemma 3 (the map `f`).

Formalized by `MetaMathlibExt.length_doubledWord`, a theorem declared in [WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean, line 300](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean#L300). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/flattened-stirling-permutations/index.html#length-doubled-word).

## Wrapped word of the empty set

The wrapped word $g(\emptyset)$ of the empty set is the
empty word.

## Sources

- Buck, Elder, Figueroa, Harris, Harry, Simpson, *Flattened Stirling Permutations*, INTEGERS 24 (2024), Article A104, Lemma 3 (the map `g`).

Formalized by `MetaMathlibExt.wrappedWord_empty`, a theorem declared in [WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean, line 307](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean#L307). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/flattened-stirling-permutations/index.html#wrapped-word-empty).

## Wrapped word of a singleton

For every natural number $s$, the wrapped word of the
singleton $\{s\}$ is $g(\{s\}) = s\,s$, the word of length two both of whose letters are $s$.

## Sources

- Buck, Elder, Figueroa, Harris, Harry, Simpson, *Flattened Stirling Permutations*, INTEGERS 24 (2024), Article A104, Lemma 3 (the map `g`).

Formalized by `MetaMathlibExt.wrappedWord_singleton`, a theorem declared in [WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean, line 314](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean#L314). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/flattened-stirling-permutations/index.html#wrapped-word-singleton).

## Length of the wrapped word

For every finite set $S$ of natural numbers with elements
$s_1 < \dots < s_k$, the wrapped word $g(S) = s_1 s_2 s_2 \cdots s_k s_k s_1$ (the empty word when
$S = \emptyset$) has length $2|S|$.

## Sources

- Buck, Elder, Figueroa, Harris, Harry, Simpson, *Flattened Stirling Permutations*, INTEGERS 24 (2024), Article A104, Lemma 3 (the map `g`).

Formalized by `MetaMathlibExt.length_wrappedWord`, a theorem declared in [WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean, line 321](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean#L321). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/flattened-stirling-permutations/index.html#length-wrapped-word).

## Adler block labels

Let $n$ be a natural number and $P$ a set partition of the integer
interval $\{-n, \dots, n\}$; for $x$ in this interval write $P(x)$ for the block of $P$
containing $x$. The Adler block labels of $P$ are the integers $p$ with $1 \le p \le n$ such
that $p \le q$ for every positive $q \in P(p)$ and $p < -q$ for every negative $q \in P(p)$;
that is, $p$ is the least positive element of its block and is smaller than the absolute value
of every negative element of that block.

For a type $B$ set partition the block containing $0$ is never labelled, and from each pair of
blocks $\beta \ne -\beta$ exactly the block containing the element of least absolute value as a
positive element is labelled, by its least positive element; sorting the labels orders these
kept blocks as $\beta_1, \dots, \beta_m$.

## Sources

- Buck, Elder, Figueroa, Harris, Harry, Simpson, *Flattened Stirling Permutations*, INTEGERS 24 (2024), Article A104, Notation 2.3 (arXiv:2306.13034).

Formalized by `MetaMathlibExt.adlerBlockLabels`, a definition declared in [WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean, line 336](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean#L336). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/flattened-stirling-permutations/index.html#adler-block-labels).

## Adler labels lie in $\{1, \dots, n\}$

For every natural number $n$ and every set
partition $P$ of $\{-n, \dots, n\}$, every Adler block label $p$ of $P$ is an integer with
$1 \le p \le n$.

## Sources

- Buck, Elder, Figueroa, Harris, Harry, Simpson, *Flattened Stirling Permutations*, INTEGERS 24 (2024), Article A104, Notation 2.3.

Formalized by `MetaMathlibExt.adlerBlockLabels_subset`, a theorem declared in [WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean, line 344](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean#L344). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/flattened-stirling-permutations/index.html#adler-block-labels-subset).

## The word of a set partition of $(-n, n)$, as a list

Let $n$ be a natural number and let
$P$ be a set partition of $[-n, n] = \{-n, \dots, n\}$. For a finite set $S$ of integers let
$h(S) = \{|i| + 1 : i \in S\}$, and for a finite set $T$ of natural numbers with elements
$t_1 < \dots < t_k$ let $f(T) = t_1 t_1 t_2 t_2 \cdots t_k t_k$ and
$g(T) = t_1 t_2 t_2 \cdots t_k t_k t_1$ (both empty when $T = \emptyset$). Let $P_0$ be the set of
nonnegative elements of the block of $P$ containing $0$. Let $p_1 < \dots < p_m$ be the integers $p$
with $1 \le p \le n$ such that every positive element of the block of $P$ containing $p$ is at
least $p$ and every negative element $q$ of that block satisfies $p < -q$, and let $N_i$ and $P_i$
be the sets of negative and of positive elements of the block containing $p_i$. The list of $P$ is
the list of natural numbers

$$g(h(P_0))\, f(h(N_1))\, g(h(P_1)) \cdots f(h(N_m))\, g(h(P_m)).$$

## Sources

- Buck, Elder, Figueroa, Harris, Harry, Simpson, *Flattened Stirling Permutations*, INTEGERS 24 (2024), Article A104, Proposition 1 (map `φ`), with Definition 2.

Formalized by `MetaMathlibExt.typeBFlattenedWordList`, a definition declared in [WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean, line 356](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean#L356). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/flattened-stirling-permutations/index.html#type-bflattened-word-list).

## The word of a set partition of $(-n, n)$

For a natural number $n$ and a set partition
$P$ of $[-n, n] = \{-n, \dots, n\}$, let $L(P)$ be the list of $P$: the list of natural numbers
built from the blocks of $P$ (via the shift map and the doubled and wrapped words). The word
$\varphi(P) = w_1 w_2 \cdots w_{2(n+1)}$ has $w_i$ equal to the $i$-th entry of $L(P)$ when $L(P)$
has at least $i$ entries, and $w_i = 0$ otherwise.

Restricted to type $B$ set partitions, this is the map $\varphi$ of Proposition 1.

## Sources

- Buck, Elder, Figueroa, Harris, Harry, Simpson, *Flattened Stirling Permutations*, INTEGERS 24 (2024), Article A104, Proposition 1 (map `φ`).

Formalized by `MetaMathlibExt.typeBFlattenedWord`, a definition declared in [WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean, line 368](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean#L368). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/flattened-stirling-permutations/index.html#type-bflattened-word).

## The word of a type $B$ set partition is a flattened Stirling permutation

For every
natural number $n$ and every type $B$ set partition $P$ of $[-n, n] = \{-n, \dots, n\}$, the word
$\varphi(P) = w_1 w_2 \cdots w_{2(n+1)}$ of $P$ is a Stirling permutation of order $n + 1$ and is
flattened.

## Sources

- arXiv:2306.13034, Proposition 3.6; the INTEGERS record is truncated after "let `π_i = N_i P_i` be as in", and the statement is completed from the arXiv text.
- Buck, Elder, Figueroa, Harris, Harry, Simpson, *Flattened Stirling Permutations*, INTEGERS 24 (2024), Article A104, Proposition 1.

Stated but not proved: `MetaMathlibExt.typeBFlattenedWord_mem_flattenedStirling` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean, line 379](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean#L379). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/flattened-stirling-permutations/index.html#type-bflattened-word-mem-flattened-stirl).

## The map $\varphi$ is a bijection from type $B$ set partitions onto flattened Stirling permutations

**The map $\varphi$ is a bijection from type $B$ set partitions onto flattened Stirling
permutations.** For a natural number $n$, let $\varphi$ be the map of Buck et al.
(Proposition 1) that sends a set partition $P$ of $\{-n, \dots, n\}$ to a word of length
$2(n + 1)$ over the natural numbers, built from the zero block of $P$ and its Adler-labelled
blocks with each element $i$ replaced by $|i| + 1$. Then $\varphi$ sends the set of type $B$
set partitions of $\{-n, \dots, n\}$ bijectively onto the set of flattened Stirling
permutations of order $n + 1$: $\varphi$ is injective on type $B$ set partitions, sends each
of them to a flattened Stirling permutation of order $n + 1$, and every flattened Stirling
permutation of order $n + 1$ is $\varphi(\pi)$ for some type $B$ set partition $\pi$ of
$\{-n, \dots, n\}$.

## Sources

- Buck, Elder, Figueroa, Harris, Harry, Simpson, *Flattened Stirling Permutations*, INTEGERS 24 (2024), Article A104, Theorem 3.

Stated but not proved: `MetaMathlibExt.bijOn_typeBFlattenedWord` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean, line 388](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean#L388). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/flattened-stirling-permutations/index.html#bij-on-type-bflattened-word).

## Number of runs of the word of a type $B$ set partition

Let $\pi$ be a type $B$ set
partition of $[-n, n]$ and let $\varphi(\pi)$ be the word of length $2(n + 1)$ that the map
$\varphi$ of Proposition 1 assigns to it. Write $P_0$ for the set of nonnegative elements of the
block of $\pi$ containing $0$. Let $\beta_1, \dots, \beta_m$ be the blocks kept by Adler's
labelling, exactly one from each pair $\{\beta, -\beta\}$ of distinct blocks, namely the block
containing the smallest magnitude of the pair as a positive element; write $N_i$ and $P_i$ for
the sets of negative and positive elements of $\beta_i$. Then the number of runs of
$\varphi(\pi)$ is

$$1 + |\{i \ge 1 : |N_i| \ge 1\}| + |\{i \ge 0 : |P_i| \ge 2\}|.$$

The paper states this for a flattened Stirling permutation $w$ of order $n + 1$ and the
partition $\varphi^{-1}(w)$; since $\varphi$ is a bijection from the type $B$ set partitions of
$[-n, n]$ onto these permutations (Theorem 3), this is the same as the statement for
$w = \varphi(\pi)$ over all $\pi$.

## Sources

- Buck, Elder, Figueroa, Harris, Harry, Simpson, *Flattened Stirling Permutations*, INTEGERS 24 (2024), Article A104, Lemma 4.

Stated but not proved: `MetaMathlibExt.wordRunCount_typeBFlattenedWord` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean, line 402](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FlattenedStirlingPermutationsWanted.lean#L402). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/flattened-stirling-permutations/index.html#word-run-count-type-bflattened-word).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Flattened Stirling permutations](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/flattened-stirling-permutations/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/permutations/permutation-statistics/flattened-stirling-permutations)
