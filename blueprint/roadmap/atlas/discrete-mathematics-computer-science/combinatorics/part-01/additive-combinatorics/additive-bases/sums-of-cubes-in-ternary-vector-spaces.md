---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.GreenProblem69Wanted.cubeOrigin, MathlibExt.Combinatorics.GreenProblem69Wanted.IsCube, MathlibExt.Combinatorics.GreenProblem69Wanted.SumsetEqUniv, MathlibExt.Combinatorics.GreenProblem69Wanted.conjecture, MathlibExt.Combinatorics.GreenProblem69Wanted.conjecture_holds
statement: formalized
---

# Sums of cubes in ternary vector spaces

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/sums-of-cubes-in-ternary-vector-spaces/index.html).

## The standard cube in $\mathbb{F}_3^n$

For $n \in \mathbb{N}$, the standard cube is the set
$\{0, 1\}^n \subseteq \mathbb{F}_3^n$ of vectors each of whose coordinates is $0$ or $1$.

Formalized by `MathlibExt.Combinatorics.GreenProblem69Wanted.cubeOrigin`, a definition declared in [WantedExt/Combinatorics/GreenProblem69Wanted.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/GreenProblem69Wanted.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/sums-of-cubes-in-ternary-vector-spaces/index.html#cube-origin).

## Cubes in $\mathbb{F}_3^n$

A set $A \subseteq \mathbb{F}_3^n$ is a cube if there is an
$\mathbb{F}_3$-linear automorphism $e$ of $\mathbb{F}_3^n$ with $A = e(\{0, 1\}^n)$, the image of
the standard cube $\{0, 1\}^n$ under $e$.

Formalized by `MathlibExt.Combinatorics.GreenProblem69Wanted.IsCube`, a definition declared in [WantedExt/Combinatorics/GreenProblem69Wanted.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/GreenProblem69Wanted.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/sums-of-cubes-in-ternary-vector-spaces/index.html#is-cube).

## A sumset of $100$ sets equal to $\mathbb{F}_3^n$

For sets
$A_1, \dots, A_{100} \subseteq \mathbb{F}_3^n$, the property that every $v \in \mathbb{F}_3^n$ can
be written as $v = a_1 + \dots + a_{100}$ with $a_i \in A_i$ for each $i$, that is,
$A_1 + \dots + A_{100} = \mathbb{F}_3^n$.

Formalized by `MathlibExt.Combinatorics.GreenProblem69Wanted.SumsetEqUniv`, a definition declared in [WantedExt/Combinatorics/GreenProblem69Wanted.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/GreenProblem69Wanted.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/sums-of-cubes-in-ternary-vector-spaces/index.html#sumset-eq-univ).

## Green's problem on sums of $100$ cubes in $\mathbb{F}_3^n$

The statement that for every
$n \ge 1$ and every family $A_1, \dots, A_{100}$ of cubes in $\mathbb{F}_3^n$ (not necessarily
distinct), that is, images of $\{0, 1\}^n$ under linear automorphisms of $\mathbb{F}_3^n$, the
sumset $A_1 + \dots + A_{100}$ is all of $\mathbb{F}_3^n$.

Formalized by `MathlibExt.Combinatorics.GreenProblem69Wanted.conjecture`, a definition declared in [WantedExt/Combinatorics/GreenProblem69Wanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/GreenProblem69Wanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/sums-of-cubes-in-ternary-vector-spaces/index.html#conjecture).

## Any $100$ cubes sum to all of $\mathbb{F}_3^n$

For every $n \ge 1$ and every family
$A_1, \dots, A_{100}$ of cubes in $\mathbb{F}_3^n$ (not necessarily distinct), that is, images
of $\{0, 1\}^n$ under linear automorphisms of $\mathbb{F}_3^n$, the sumset
$A_1 + \dots + A_{100}$ is all of $\mathbb{F}_3^n$.

Yang Yu proves that over $\mathbb{F}_3$ the union of any four linear bases is an additive basis,
so any four cubes already sum to $\mathbb{F}_3^n$, and the remaining summands can be taken to be
$0$. Ben Green's author-maintained 100 Open Problems (December 2025) marks this problem, current
Problem 26, solved on that basis; the analogue over $\mathbb{F}_p$ remains open.

## Sources

- Yang Yu, The Permanent Rank of a Matrix (Part Three) Note on the Additive Basis Conjecture, arXiv:2510.01300v2, https://arxiv.org/abs/2510.01300v2.

Stated but not proved: `MathlibExt.Combinatorics.GreenProblem69Wanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/GreenProblem69Wanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/GreenProblem69Wanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/sums-of-cubes-in-ternary-vector-spaces/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sums of cubes in ternary vector spaces](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/sums-of-cubes-in-ternary-vector-spaces/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/additive-combinatorics/additive-bases/sums-of-cubes-in-ternary-vector-spaces)
