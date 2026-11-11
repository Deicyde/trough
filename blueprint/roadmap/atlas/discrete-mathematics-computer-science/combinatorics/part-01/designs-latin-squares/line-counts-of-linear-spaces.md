---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.LinearSpaceLineCountGapErdosProblem903Wanted.IsTwoDesign, MathlibExt.Combinatorics.LinearSpaceLineCountGapErdosProblem903Wanted.lineCountGapAboveProjectivePlane, MathlibExt.Combinatorics.LinearSpaceLineCountGapErdosProblem903Wanted.lineCountGapAboveProjectivePlane_holds
statement: formalized
---

# Line counts of linear spaces

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/line-counts-of-linear-spaces/index.html).

## Linear spaces (2-designs)

A family $A_1, \dots, A_t$ of subsets of $\{1, \dots, v\}$ is a
$2$-design (also called a pairwise balanced design or a linear space) when every block $A_i$ has
at least two points and every pair of distinct points of $\{1, \dots, v\}$ lies in exactly one
block.

Formalized by `MathlibExt.Combinatorics.LinearSpaceLineCountGapErdosProblem903Wanted.IsTwoDesign`, a definition declared in [WantedExt/Combinatorics/LinearSpaceLineCountGapErdosProblem903Wanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/LinearSpaceLineCountGapErdosProblem903Wanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/line-counts-of-linear-spaces/index.html#is-two-design).

## Erdős Problem 903: line counts just above a projective plane

This is the statement that
for every prime power $p$, with $n = p^2 + p + 1$, every $2$-design $A_1, \dots, A_t$ on
$\{1, \dots, n\}$ with more than $n$ blocks has at least $n + p$ blocks. Here a $2$-design is a
family of subsets in which every block has at least two points and every pair of distinct points
lies in exactly one block.

Formalized by `MathlibExt.Combinatorics.LinearSpaceLineCountGapErdosProblem903Wanted.lineCountGapAboveProjectivePlane`, a definition declared in [WantedExt/Combinatorics/LinearSpaceLineCountGapErdosProblem903Wanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/LinearSpaceLineCountGapErdosProblem903Wanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/line-counts-of-linear-spaces/index.html#line-count-gap-above-projective-plane).

## Erdős–Fowler–Sós–Wilson gap above a projective plane (Erdős Problem 903)

Let $p$ be a prime
power and $n = p^2 + p + 1$. Let $A_1, \dots, A_t$ be a $2$-design on $\{1, \dots, n\}$: every
block $A_i$ has at least two points and every pair of distinct points lies in exactly one block.
If $t > n$, then $t \ge n + p$.

Erdős, Fowler, Sós and Wilson prove this for every natural number $p$, not only prime powers.

## Sources

- T. F. Bloom, Erdős Problems, Problem #903, https://www.erdosproblems.com/903 (status PROVED); resolution: P. Erdős, J. C. Fowler, V. T. Sós and R. M. Wilson, On 2-designs, J. Combin. Theory Ser. A 38 (1985), 131-142, Theorem 2: for v = p² + p + 1 (p not necessarily a prime power) there is no 2-design with v points and b lines when p² + p + 1 < b < p² + 2p + 1, where a 2-design has every pair of points in exactly one block and every block of size > 1, https://users.renyi.hu/~p_erdos/1985-22.pdf.

Stated but not proved: `MathlibExt.Combinatorics.LinearSpaceLineCountGapErdosProblem903Wanted.lineCountGapAboveProjectivePlane_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/LinearSpaceLineCountGapErdosProblem903Wanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/LinearSpaceLineCountGapErdosProblem903Wanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/line-counts-of-linear-spaces/index.html#line-count-gap-above-projective-plane-ho).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Line counts of linear spaces](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/line-counts-of-linear-spaces/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/designs-latin-squares/line-counts-of-linear-spaces)
