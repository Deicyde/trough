---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.ConwaySchneebergerFifteenWanted.NumberTheory.ConwaySchneebergerFifteenProblem.evalQ, MathlibExt.NumberTheory.ConwaySchneebergerFifteenWanted.NumberTheory.ConwaySchneebergerFifteenProblem.Represents, MathlibExt.NumberTheory.ConwaySchneebergerFifteenWanted.NumberTheory.ConwaySchneebergerFifteenProblem.IsUniversal, MathlibExt.NumberTheory.ConwaySchneebergerFifteenWanted.NumberTheory.ConwaySchneebergerFifteenProblem.conway_schneeberger_fifteen, MathlibExt.NumberTheory.TwoNinetyTheoremWanted.NumberTheory.TwoNinety.evalQ, MathlibExt.NumberTheory.TwoNinetyTheoremWanted.NumberTheory.TwoNinety.Represents, MathlibExt.NumberTheory.TwoNinetyTheoremWanted.NumberTheory.TwoNinety.IsUniversal, MathlibExt.NumberTheory.TwoNinetyTheoremWanted.NumberTheory.TwoNinety.Integral
statement: formalized
---

# 15 and 290 theorems

10 results, 8 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/15-and-290-theorems/index.html).

## Quadratic form of an integer matrix

For an $n \times n$ matrix $Q$ with integer
entries, the quadratic form of $Q$ is the map $\mathbb{Z}^n \to \mathbb{Z}$ sending $x$ to
$Q(x) = \sum_{i,j} Q_{ij} x_i x_j$, where $i$ and $j$ range over $\{0, \dots, n-1\}$. No
symmetry of $Q$ is assumed.

Formalized by `MathlibExt.NumberTheory.ConwaySchneebergerFifteenWanted.NumberTheory.ConwaySchneebergerFifteenProblem.evalQ`, a definition declared in [WantedExt/NumberTheory/ConwaySchneebergerFifteenWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConwaySchneebergerFifteenWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/15-and-290-theorems/index.html#eval-q).

## Integers represented by an integer-matrix quadratic form

An $n \times n$ matrix $Q$
with integer entries represents an integer $m$ if $Q(x) = m$ for some $x \in \mathbb{Z}^n$,
where $Q(x) = \sum_{i,j} Q_{ij} x_i x_j$.

Formalized by `MathlibExt.NumberTheory.ConwaySchneebergerFifteenWanted.NumberTheory.ConwaySchneebergerFifteenProblem.Represents`, a definition declared in [WantedExt/NumberTheory/ConwaySchneebergerFifteenWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConwaySchneebergerFifteenWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/15-and-290-theorems/index.html#represents).

## Universal integer-matrix quadratic forms

An $n \times n$ matrix $Q$ with integer
entries is universal if its quadratic form $Q(x) = \sum_{i,j} Q_{ij} x_i x_j$ represents every
positive integer, that is, for every positive integer $m$ there is $x \in \mathbb{Z}^n$ with
$Q(x) = m$.

Formalized by `MathlibExt.NumberTheory.ConwaySchneebergerFifteenWanted.NumberTheory.ConwaySchneebergerFifteenProblem.IsUniversal`, a definition declared in [WantedExt/NumberTheory/ConwaySchneebergerFifteenWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConwaySchneebergerFifteenWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/15-and-290-theorems/index.html#is-universal).

## Conway–Schneeberger fifteen theorem

Let $Q$ be a positive definite symmetric
$n \times n$ matrix with integer entries, with quadratic form $Q(x) = \sum_{i,j} Q_{ij} x_i x_j$
on $\mathbb{Z}^n$. Then $Q$ is universal, that is, it represents every positive integer, if and
only if it represents every integer $k$ with $1 \le k \le 15$.

The forward direction is immediate; the content is the converse. Bhargava's refinement reduces
the critical set to $\{1, 2, 3, 5, 6, 7, 10, 14, 15\}$.

## Sources

- Conway–Schneeberger 1993 (unpublished, communicated by Conway in lectures); full proof M. Bhargava, 'On the Conway–Schneeberger fifteen theorem', in *Quadratic Forms and their Applications* (Contemp. Math. 272, AMS 2000). Listed as §95 in O. Knill, *Some Fundamental Theorems in Mathematics* (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Problem `conway_schneeberger_fifteen` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.NumberTheory.ConwaySchneebergerFifteenWanted.NumberTheory.ConwaySchneebergerFifteenProblem.conway_schneeberger_fifteen` is written with `theorem_wanted` in [WantedExt/NumberTheory/ConwaySchneebergerFifteenWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConwaySchneebergerFifteenWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/15-and-290-theorems/index.html#conway-schneeberger-fifteen).

## Quadratic form of a matrix

For a ring $R$ and an $n \times n$ matrix $M$ with entries
in $R$, the value of the quadratic form of $M$ at a vector $x \in R^n$ is
$x \cdot (M x) = \sum_{i,j} x_i M_{ij} x_j$, where $i$ and $j$ range over $\{0, \dots, n-1\}$.

No symmetry of $M$ is assumed, and $R$ need not be commutative.

Formalized by `MathlibExt.NumberTheory.TwoNinetyTheoremWanted.NumberTheory.TwoNinety.evalQ`, a definition declared in [WantedExt/NumberTheory/TwoNinetyTheoremWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoNinetyTheoremWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/15-and-290-theorems/index.html#eval-q-2).

## Natural numbers represented by a quadratic form

For a ring $R$, an $n \times n$ matrix
$M$ with entries in $R$ represents a natural number $m$ if there is an integer vector
$x \in \mathbb{Z}^n$ with $\sum_{i,j} x_i M_{ij} x_j = m$, where the entries of $x$ and the
number $m$ are viewed as elements of $R$.

Formalized by `MathlibExt.NumberTheory.TwoNinetyTheoremWanted.NumberTheory.TwoNinety.Represents`, a definition declared in [WantedExt/NumberTheory/TwoNinetyTheoremWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoNinetyTheoremWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/15-and-290-theorems/index.html#represents-2).

## Universal quadratic forms over a ring

For a ring $R$, an $n \times n$ matrix $M$ with
entries in $R$ is universal if it represents every positive integer: for every positive
integer $m$ there is $x \in \mathbb{Z}^n$ with $\sum_{i,j} x_i M_{ij} x_j = m$ in $R$.

Formalized by `MathlibExt.NumberTheory.TwoNinetyTheoremWanted.NumberTheory.TwoNinety.IsUniversal`, a definition declared in [WantedExt/NumberTheory/TwoNinetyTheoremWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoNinetyTheoremWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/15-and-290-theorems/index.html#is-universal-2).

## Integer-valued quadratic forms

For a ring $R$, an $n \times n$ matrix $M$ with entries
in $R$ is integral if its quadratic form takes integer values at integer vectors: for every
$x \in \mathbb{Z}^n$, the value $\sum_{i,j} x_i M_{ij} x_j$ computed in $R$ lies in the image
of $\mathbb{Z}$ in $R$.

Formalized by `MathlibExt.NumberTheory.TwoNinetyTheoremWanted.NumberTheory.TwoNinety.Integral`, a definition declared in [WantedExt/NumberTheory/TwoNinetyTheoremWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoNinetyTheoremWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/15-and-290-theorems/index.html#integral).

## Critical numbers of the 290 theorem

The critical numbers of the 290 theorem form the
set of the 29 natural numbers $1, 2, 3, 5, 6, 7, 10, 13, 14, 15, 17, 19, 21, 22, 23, 26, 29,
30, 31, 34, 35, 37, 42, 58, 93, 110, 145, 203, 290$.

Formalized by `MathlibExt.NumberTheory.TwoNinetyTheoremWanted.NumberTheory.TwoNinety.criticalNumbers`, a definition declared in [WantedExt/NumberTheory/TwoNinetyTheoremWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoNinetyTheoremWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/15-and-290-theorems/index.html#critical-numbers).

## The 290 theorem

Let $n$ be a natural number and let $M$ be a real $n \times n$ matrix
that is positive definite (symmetric, with $x^{\top} M x > 0$ for every nonzero
$x \in \mathbb{R}^n$) and integral (for every $x \in \mathbb{Z}^n$, the value $x^{\top} M x$ is
an integer). If $M$ represents each of the 29 critical numbers of the 290 theorem, that is,
for each critical number $m$ there is $x \in \mathbb{Z}^n$ with $x^{\top} M x = m$, then $M$
is universal: for every positive integer $m$ there is $x \in \mathbb{Z}^n$ with
$x^{\top} M x = m$.

## Sources

- M. Bhargava, J. Hanke, Universal quadratic forms and the 290-theorem, preprint (2011). See also https://en.wikipedia.org/wiki/15_and_290_theorems. Problem `two_ninety_theorem` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.NumberTheory.TwoNinetyTheoremWanted.NumberTheory.TwoNinety.two_ninety_theorem` is written with `theorem_wanted` in [WantedExt/NumberTheory/TwoNinetyTheoremWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoNinetyTheoremWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/15-and-290-theorems/index.html#two-ninety-theorem).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: 15 and 290 theorems](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/15-and-290-theorems/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/15-and-290-theorems)
