---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.BalancedSignsInfiniteFamilyErdosProblem178Wanted.boundedDiscrepancyInfiniteFamily, MathlibExt.Combinatorics.BalancedSignsInfiniteFamilyErdosProblem178Wanted.boundedDiscrepancyInfiniteFamily_holds
statement: formalized
---

# Balancing infinite families of sequences

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/balancing-infinite-families-of-sequences/index.html).

## Erdős Problem 178 (balancing infinite families of sequences)

The statement that for every
family $a_0, a_1, a_2, \ldots$ of strictly increasing sequences of natural numbers there is a
function $f : \mathbb{N} \to \mathbb{Z}$ taking only the values $1$ and $-1$ such that for every
$d \in \mathbb{N}$ there is a natural number $C$ with $\left|\sum_{j < m} f(a_i(j))\right| \le C$
for all $i < d$ and all $m \in \mathbb{N}$.

Here $a_i$ enumerates the infinite set $A_i = \{a_i(0) < a_i(1) < \cdots\} \subseteq \mathbb{N}$ in
increasing order, and the sum runs over the first $m$ elements of $A_i$.

Formalized by `MathlibExt.Combinatorics.BalancedSignsInfiniteFamilyErdosProblem178Wanted.boundedDiscrepancyInfiniteFamily`, a definition declared in [WantedExt/Combinatorics/BalancedSignsInfiniteFamilyErdosProblem178Wanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BalancedSignsInfiniteFamilyErdosProblem178Wanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/balancing-infinite-families-of-sequences/index.html#bounded-discrepancy-infinite-family).

## Beck's theorem on balancing infinite families of sequences (Erdős Problem 178)

For every
family $a_0, a_1, a_2, \ldots$ of strictly increasing sequences of natural numbers there is a
function $f : \mathbb{N} \to \mathbb{Z}$ taking only the values $1$ and $-1$ such that for every
$d \in \mathbb{N}$ there is a natural number $C$ with $\left|\sum_{j < m} f(a_i(j))\right| \le C$
for all $i < d$ and all $m \in \mathbb{N}$.

Beck proved this; he later showed that the bound $C$ can be taken $\ll d^{4 + \varepsilon}$.

## Sources

- T. F. Bloom, Erdős Problems, Problem #178, https://www.erdosproblems.com/178 (status PROVED (LEAN)); resolution: J. Beck, Balancing families of integer sequences, Combinatorica 1 (1981), 209-216, erdosproblems.com/178: solved by Beck [Be81]; Beck (2017) improved the bound to d^{4+ε}, https://doi.org/10.1007/BF02579326.

Stated but not proved: `MathlibExt.Combinatorics.BalancedSignsInfiniteFamilyErdosProblem178Wanted.boundedDiscrepancyInfiniteFamily_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/BalancedSignsInfiniteFamilyErdosProblem178Wanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BalancedSignsInfiniteFamilyErdosProblem178Wanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/balancing-infinite-families-of-sequences/index.html#bounded-discrepancy-infinite-family-hold).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Balancing infinite families of sequences](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/balancing-infinite-families-of-sequences/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/discrepancy-theory/balancing-infinite-families-of-sequences)
