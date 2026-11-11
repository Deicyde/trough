---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.SquareSumFreeSetsErdosProblem438Wanted.IsSquareSumFree, MathlibExt.Combinatorics.SquareSumFreeSetsErdosProblem438Wanted.maxSquareSumFreeSize, MathlibExt.Combinatorics.SquareSumFreeSetsErdosProblem438Wanted.maxSquareSumFreeDensity, MathlibExt.Combinatorics.SquareSumFreeSetsErdosProblem438Wanted.maxSquareSumFreeDensity_holds
statement: formalized
---

# Square-sum-free sets

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/square-sum-free-sets/index.html).

## Square-sum-free sets

A finite set $A$ of natural numbers is square-sum-free if for all
$a, b \in A$, not necessarily distinct, the sum $a + b$ is not a perfect square.

Formalized by `MathlibExt.Combinatorics.SquareSumFreeSetsErdosProblem438Wanted.IsSquareSumFree`, a definition declared in [WantedExt/Combinatorics/SquareSumFreeSetsErdosProblem438Wanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SquareSumFreeSetsErdosProblem438Wanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/square-sum-free-sets/index.html#is-square-sum-free).

## Maximum size of a square-sum-free set

For a natural number $N$, the largest size of a set
$A \subseteq \{1, \dots, N\}$ such that no sum $a + b$ with $a, b \in A$, not necessarily distinct,
is a perfect square.

Formalized by `MathlibExt.Combinatorics.SquareSumFreeSetsErdosProblem438Wanted.maxSquareSumFreeSize`, a definition declared in [WantedExt/Combinatorics/SquareSumFreeSetsErdosProblem438Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SquareSumFreeSetsErdosProblem438Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/square-sum-free-sets/index.html#max-square-sum-free-size).

## Erdős Problem 438 (statement)

For a natural number $N$, let $M(N)$ be the largest size of
a set $A \subseteq \{1, \dots, N\}$ such that no sum $a + b$ with $a, b \in A$, not necessarily
distinct, is a perfect square. This is the statement that $M(N) / N \to 11/32$ as
$N \to \infty$.

Formalized by `MathlibExt.Combinatorics.SquareSumFreeSetsErdosProblem438Wanted.maxSquareSumFreeDensity`, a definition declared in [WantedExt/Combinatorics/SquareSumFreeSetsErdosProblem438Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SquareSumFreeSetsErdosProblem438Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/square-sum-free-sets/index.html#max-square-sum-free-density).

## Maximal density of square-sum-free sets (Erdős Problem 438)

For a natural number $N$, let
$M(N)$ be the largest size of a set $A \subseteq \{1, \dots, N\}$ such that no sum $a + b$ with
$a, b \in A$, not necessarily distinct, is a perfect square. Then $M(N) / N \to 11/32$ as
$N \to \infty$.

Khalfalah, Lodha and Szemerédi proved $M(N) \le (11/32 + o(1)) N$, and Massias's example (the
integers congruent to one of $1, 5, 9, 13, 14, 17, 21, 25, 26, 29, 30$ modulo $32$) gives
$M(N) \ge 11N/32 + O(1)$.

## Sources

- T. F. Bloom, Erdős Problems, Problem #438, https://www.erdosproblems.com/438 (status SOLVED); resolution: A. Khalfalah, S. Lodha and E. Szemerédi, Tight bound for the density of sequence of integers the sum of no two of which is a perfect square, Discrete Math. (2002), 243-255, max |A| ≤ (11/32 + o(1)) N; Massias's residues mod 32 give the lower bound (erdosproblems.com/438).

Stated but not proved: `MathlibExt.Combinatorics.SquareSumFreeSetsErdosProblem438Wanted.maxSquareSumFreeDensity_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/SquareSumFreeSetsErdosProblem438Wanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SquareSumFreeSetsErdosProblem438Wanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/square-sum-free-sets/index.html#max-square-sum-free-density-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Square-sum-free sets](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/square-sum-free-sets/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/square-sum-free-sets)
