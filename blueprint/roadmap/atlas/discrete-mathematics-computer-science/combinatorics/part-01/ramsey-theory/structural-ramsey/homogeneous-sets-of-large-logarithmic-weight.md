---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.HomogeneousSetLogWeightErdosProblem191Wanted.homogeneousSetLargeLogWeight, MathlibExt.Combinatorics.HomogeneousSetLogWeightErdosProblem191Wanted.homogeneousSetLargeLogWeight_holds
statement: formalized
---

# Homogeneous sets of large logarithmic weight

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/homogeneous-sets-of-large-logarithmic-weight/index.html).

## Erdős Problem 191

The statement that for every real $C > 0$ there is an $N$ such that for
every $n \ge N$ and every graph $G$ on the natural numbers (its edges and non-edges 2-colour the
pairs of $\{2, \dots, n\}$) there is a finite set $X \subseteq \{2, \dots, n\}$ that is a clique
or an independent set of $G$ (a monochromatic set) with $\sum_{x \in X} 1 / \log x \ge C$.

Formalized by `MathlibExt.Combinatorics.HomogeneousSetLogWeightErdosProblem191Wanted.homogeneousSetLargeLogWeight`, a definition declared in [WantedExt/Combinatorics/HomogeneousSetLogWeightErdosProblem191Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/HomogeneousSetLogWeightErdosProblem191Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/homogeneous-sets-of-large-logarithmic-weight/index.html#homogeneous-set-large-log-weight).

## Monochromatic sets of large logarithmic weight exist

For every real $C > 0$ there is an
$N$ such that for every $n \ge N$ and every graph $G$ on the natural numbers there is a finite
set $X \subseteq \{2, \dots, n\}$ that is a clique or an independent set of $G$ and satisfies
$\sum_{x \in X} 1 / \log x \ge C$.

Rödl proved this, and Conlon, Fox and Sudakov later showed that the best such $X$ has weight at
least $2^{-8} \log \log \log n$ for large $n$, which is sharp by Rödl's construction.

## Sources

- T. F. Bloom, Erdős Problems, Problem #191, https://www.erdosproblems.com/191 (status PROVED (LEAN)); resolution: V. Rödl, On homogeneous sets of positive integers, J. Combin. Theory Ser. A 102 (2003), 229-240, erdosproblems.com/191: proved by Rödl [Ro03]; Conlon, Fox and Sudakov (2013) gave the sharp bound 2^{-8} log log log n, https://doi.org/10.1016/S0097-3165(03)00026-8.

Stated but not proved: `MathlibExt.Combinatorics.HomogeneousSetLogWeightErdosProblem191Wanted.homogeneousSetLargeLogWeight_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/HomogeneousSetLogWeightErdosProblem191Wanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/HomogeneousSetLogWeightErdosProblem191Wanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/homogeneous-sets-of-large-logarithmic-weight/index.html#homogeneous-set-large-log-weight-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Homogeneous sets of large logarithmic weight](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/homogeneous-sets-of-large-logarithmic-weight/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/ramsey-theory/structural-ramsey/homogeneous-sets-of-large-logarithmic-weight)
