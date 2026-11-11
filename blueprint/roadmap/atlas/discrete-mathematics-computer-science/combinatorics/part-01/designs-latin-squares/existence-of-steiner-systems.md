---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.SteinerSystemExistenceErdosProblem722Wanted.steinerSystemsExistForLargeN, MathlibExt.Combinatorics.SteinerSystemExistenceErdosProblem722Wanted.steinerSystemsExistForLargeN_holds
statement: formalized
---

# Existence of Steiner systems

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/existence-of-steiner-systems/index.html).

## Existence conjecture for Steiner systems

The statement that for all natural numbers
$r < k$ there is an $N$ such that for every $n \ge N$ with
$\binom{k-i}{r-i} \mid \binom{n-i}{r-i}$ for all $0 \le i < r$, there is a Steiner system
$S(r, k, n)$: a family $F$ of $k$-element subsets of $\{0, \dots, n-1\}$ such that every
$r$-element subset of $\{0, \dots, n-1\}$ is contained in exactly one member of $F$
(Erdős Problem 722).

Formalized by `MathlibExt.Combinatorics.SteinerSystemExistenceErdosProblem722Wanted.steinerSystemsExistForLargeN`, a definition declared in [WantedExt/Combinatorics/SteinerSystemExistenceErdosProblem722Wanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SteinerSystemExistenceErdosProblem722Wanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/existence-of-steiner-systems/index.html#steiner-systems-exist-for-large-n).

## Keevash's existence theorem for Steiner systems

For all natural numbers $r < k$ there is
an $N$ such that for every $n \ge N$ with $\binom{k-i}{r-i} \mid \binom{n-i}{r-i}$ for all
$0 \le i < r$, there is a Steiner system $S(r, k, n)$: a family $F$ of $k$-element subsets of
$\{0, \dots, n-1\}$ such that every $r$-element subset of $\{0, \dots, n-1\}$ is contained in
exactly one member of $F$.

Keevash proved the existence conjecture for designs, which gives this statement (earlier cases:
Kirkman for $(r, k) = (2, 3)$, Hanani, Wilson for $r = 2$); erdosproblems.com/722 lists the
problem as proved.

## Sources

- T. F. Bloom, Erdős Problems, Problem #722, https://www.erdosproblems.com/722 (status PROVED); resolution: P. Keevash, The existence of designs, arXiv:1401.3665 (2014), abstract: proves the existence conjecture for combinatorial designs (Steiner's question of 1853): the divisibility conditions suffice for all large n; erdosproblems.com/722: proved by Keevash for all (r, k), https://arxiv.org/abs/1401.3665.

Stated but not proved: `MathlibExt.Combinatorics.SteinerSystemExistenceErdosProblem722Wanted.steinerSystemsExistForLargeN_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/SteinerSystemExistenceErdosProblem722Wanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SteinerSystemExistenceErdosProblem722Wanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/existence-of-steiner-systems/index.html#steiner-systems-exist-for-large-n-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Existence of Steiner systems](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/existence-of-steiner-systems/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/designs-latin-squares/existence-of-steiner-systems)
