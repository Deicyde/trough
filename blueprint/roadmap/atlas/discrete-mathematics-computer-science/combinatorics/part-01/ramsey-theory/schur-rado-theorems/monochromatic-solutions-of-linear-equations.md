---
declaration: section
origin: cited
lean: MetaMathlibExt.HasCancelingPartition, MetaMathlibExt.hasCancelingPartition_one_two_neg_one_neg_two, MetaMathlibExt.not_hasCancelingPartition_one_one, MetaMathlibExt.IsUncommonOverFiniteGroup, MetaMathlibExt.not_isUncommonOverFiniteGroup_one, MetaMathlibExt.IsUncommonOverIntegers, MetaMathlibExt.not_isUncommonOverIntegers_one, MetaMathlibExt.isUncommonOverFiniteGroup_of_odd
statement: formalized
---

# Monochromatic solutions of linear equations

12 results, 7 proved and 5 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/monochromatic-solutions-of-linear-equations/index.html).

## Canceling partition

Let $a_1, \dots, a_k$ be integers, the coefficients of the
linear equation $a_1x_1 + \cdots + a_kx_k = 0$. The equation has a canceling partition when
its indices split into pairs of distinct indices $i, j$ with $a_i + a_j = 0$; precisely,
when there is a permutation $\sigma$ of the indices $1, \dots, k$ such that for every $i$
we have $\sigma(\sigma(i)) = i$, $\sigma(i) \ne i$ and $a_i + a_{\sigma(i)} = 0$.

## Sources

- Laurence P. Wijaya, *On Monochromatic Solutions of Linear Equations Using at Least Three Colors*, INTEGERS 25 (2025), Article A88, Section 1 (definition of canceling partition).

Formalized by `MetaMathlibExt.HasCancelingPartition`, a definition declared in [WantedExt/Combinatorics/MonochromaticLinearEquationsWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/MonochromaticLinearEquationsWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/monochromatic-solutions-of-linear-equations/index.html#has-canceling-partition).

## A canceling partition for $x_1 + 2x_2 - x_3 - 2x_4 = 0$

The equation
$x_1 + 2x_2 - x_3 - 2x_4 = 0$, with coefficient vector $(1, 2, -1, -2)$, has a canceling
partition.

## Sources

- Laurence P. Wijaya, *On Monochromatic Solutions of Linear Equations Using at Least Three Colors*, INTEGERS 25 (2025), Article A88, Section 1.

Formalized by `MetaMathlibExt.hasCancelingPartition_one_two_neg_one_neg_two`, a theorem declared in [WantedExt/Combinatorics/MonochromaticLinearEquationsWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/MonochromaticLinearEquationsWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/monochromatic-solutions-of-linear-equations/index.html#has-canceling-partition-one-two-neg-one).

## The equation $x_1 + x_2 = 0$ has no canceling partition

The equation
$x_1 + x_2 = 0$, with coefficient vector $(1, 1)$, has no canceling partition.

## Sources

- Laurence P. Wijaya, *On Monochromatic Solutions of Linear Equations Using at Least Three Colors*, INTEGERS 25 (2025), Article A88, Section 1.

Formalized by `MetaMathlibExt.not_hasCancelingPartition_one_one`, a theorem declared in [WantedExt/Combinatorics/MonochromaticLinearEquationsWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/MonochromaticLinearEquationsWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/monochromatic-solutions-of-linear-equations/index.html#not-has-canceling-partition-one-one).

## Uncommon equations over a finite abelian group

Let $G$ be a finite abelian group,
let $a_1, \dots, a_k$ be integers, let $r$ be a natural number, and let $S \subseteq G^k$ be
the set of solutions of $a_1x_1 + \cdots + a_kx_k = 0$. The equation is $r$-uncommon over
$G$ when there are functions $w_1, \dots, w_r \colon G \to \mathbb{R}$ with $w_c(x) \ge 0$ for
all $c$ and $x$, and $w_1(x) + \cdots + w_r(x) = 1$ for every $x \in G$, such that

$$r^{k-1} \sum_{c=1}^{r} \sum_{(x_1, \dots, x_k) \in S} \prod_{i=1}^{k} w_c(x_i) < |S|,$$

where $r^{k-1}$ is read as $1$ when $k = 0$.

The functions $w_c$ form a fractional $r$-colouring of $G$, and the double sum is its
weighted count of monochromatic solutions. For $k \ge 1$ the condition says that this count
is below $r^{1-k}|S|$, its value for the uniform weights $w_c(x) = 1/r$.

## Sources

- Laurence P. Wijaya, *On Monochromatic Solutions of Linear Equations Using at Least Three Colors*, INTEGERS 25 (2025), Article A88, Sections 1-2 (equation (2.1)).

Formalized by `MetaMathlibExt.IsUncommonOverFiniteGroup`, a definition declared in [WantedExt/Combinatorics/MonochromaticLinearEquationsWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/MonochromaticLinearEquationsWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/monochromatic-solutions-of-linear-equations/index.html#is-uncommon-over-finite-group).

## No equation is 1-uncommon over a finite abelian group

For every finite abelian group
$G$, every $k \ge 0$ and all integers $a_1, \dots, a_k$, the equation
$a_1 x_1 + \dots + a_k x_k = 0$ is not $1$-uncommon over $G$.

## Sources

- Laurence P. Wijaya, *On Monochromatic Solutions of Linear Equations Using at Least Three Colors*, INTEGERS 25 (2025), Article A88, Sections 1-2.

Formalized by `MetaMathlibExt.not_isUncommonOverFiniteGroup_one`, a theorem declared in [WantedExt/Combinatorics/MonochromaticLinearEquationsWanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/MonochromaticLinearEquationsWanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/monochromatic-solutions-of-linear-equations/index.html#not-is-uncommon-over-finite-group-one).

## Uncommon equations over the integers

Let $a_1, \dots, a_k$ be integers and let $r$
be a natural number. For each $n$, write $[n]$ for the set of integers $1, \dots, n$ and
$S_n$ for the set of solutions $(x_1, \dots, x_k) \in [n]^k$ of
$a_1x_1 + \cdots + a_kx_k = 0$; for a colouring $\chi$ of the integers with $r$ colours, let
$M_\chi(n)$ be the number of solutions in $S_n$ whose entries all have the same colour.
The equation is $r$-uncommon over the integers when there is $\varepsilon > 0$ such that
for infinitely many $n$ some such colouring $\chi$ satisfies
$r^{k-1} M_\chi(n) < (1 - \varepsilon)|S_n|$, where $r^{k-1}$ is read as $1$ when $k = 0$.

For $k \ge 1$ this says that the equation is not $r$-common: it is not the case that every
$r$-colouring of $[n]$ has at least $(1 - o(1)) r^{1-k}|S_n|$ monochromatic solutions.

## Sources

- Laurence P. Wijaya, *On Monochromatic Solutions of Linear Equations Using at Least Three Colors*, INTEGERS 25 (2025), Article A88, Section 1 (`r`-common over the integers).

Formalized by `MetaMathlibExt.IsUncommonOverIntegers`, a definition declared in [WantedExt/Combinatorics/MonochromaticLinearEquationsWanted.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/MonochromaticLinearEquationsWanted.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/monochromatic-solutions-of-linear-equations/index.html#is-uncommon-over-integers).

## No equation is 1-uncommon over the integers

For every $k \ge 0$ and all integers
$a_1, \dots, a_k$, the equation $a_1 x_1 + \dots + a_k x_k = 0$ is not $1$-uncommon over the
integers.

## Sources

- Laurence P. Wijaya, *On Monochromatic Solutions of Linear Equations Using at Least Three Colors*, INTEGERS 25 (2025), Article A88, Section 1.

Formalized by `MetaMathlibExt.not_isUncommonOverIntegers_one`, a theorem declared in [WantedExt/Combinatorics/MonochromaticLinearEquationsWanted.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/MonochromaticLinearEquationsWanted.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/monochromatic-solutions-of-linear-equations/index.html#not-is-uncommon-over-integers-one).

## Uncommonness of odd-length equations over finite abelian groups

Let $G$ be a
nontrivial finite abelian group, let $m \ge 1$, and let $a_1, \dots, a_{2m+1}$ be integers
each coprime to the order $|G|$. Then for every $r \ge 3$ the equation
$a_1x_1 + \cdots + a_{2m+1}x_{2m+1} = 0$ is $r$-uncommon over $G$.

Since $|G| \ge 2$, coprimality forces every $a_i$ to be nonzero.

## Sources

- Laurence P. Wijaya, *On Monochromatic Solutions of Linear Equations Using at Least Three Colors*, INTEGERS 25 (2025), Article A88, Theorem 1.

Stated but not proved: `MetaMathlibExt.isUncommonOverFiniteGroup_of_odd` is written with `theorem_wanted` in [WantedExt/Combinatorics/MonochromaticLinearEquationsWanted.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/MonochromaticLinearEquationsWanted.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/monochromatic-solutions-of-linear-equations/index.html#is-uncommon-over-finite-group-of-odd).

## Uncommonness of odd-length equations over the integers

Let $m \ge 1$ and let
$a_1, \dots, a_{2m+1}$ be nonzero integers, at least one negative and at least one positive.
Then for every $r \ge 3$ the equation $a_1x_1 + \cdots + a_{2m+1}x_{2m+1} = 0$ is
$r$-uncommon over the integers.

The sign condition excludes equations such as $x_1 + x_2 + x_3 = 0$, which have no solutions
in positive integers and for which the proportion of monochromatic solutions is undefined.

## Sources

- Laurence P. Wijaya, *On Monochromatic Solutions of Linear Equations Using at Least Three Colors*, INTEGERS 25 (2025), Article A88, Corollary 1.

Stated but not proved: `MetaMathlibExt.isUncommonOverIntegers_of_odd` is written with `theorem_wanted` in [WantedExt/Combinatorics/MonochromaticLinearEquationsWanted.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/MonochromaticLinearEquationsWanted.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/monochromatic-solutions-of-linear-equations/index.html#is-uncommon-over-integers-of-odd).

## Two-colour uncommonness over the integers extends to more colours

Let
$k \ge 3$ and let $a_1, \dots, a_k$ be nonzero integers. If the equation
$a_1x_1 + \cdots + a_kx_k = 0$ is $2$-uncommon over the integers, then it is $r$-uncommon
over the integers for every $r \ge 3$.

## Sources

- Laurence P. Wijaya, *On Monochromatic Solutions of Linear Equations Using at Least Three Colors*, INTEGERS 25 (2025), Article A88, Theorem 2.

Stated but not proved: `MetaMathlibExt.isUncommonOverIntegers_of_two` is written with `theorem_wanted` in [WantedExt/Combinatorics/MonochromaticLinearEquationsWanted.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/MonochromaticLinearEquationsWanted.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/monochromatic-solutions-of-linear-equations/index.html#is-uncommon-over-integers-of-two).

## Uncommonness of even-length equations without a canceling partition

Let $m \ge 2$
and let $a_1, \dots, a_{2m}$ be nonzero integers, at least one negative and at least one
positive, such that the equation $a_1x_1 + \cdots + a_{2m}x_{2m} = 0$ has no canceling
partition. Then this equation is $r$-uncommon over the integers for every $r \ge 2$.

The sign condition excludes equations such as $x_1 + x_2 + x_3 + x_4 = 0$, which has no
canceling partition and no solutions in positive integers.

## Sources

- Laurence P. Wijaya, *On Monochromatic Solutions of Linear Equations Using at Least Three Colors*, INTEGERS 25 (2025), Article A88, Corollary 2.

Stated but not proved: `MetaMathlibExt.isUncommonOverIntegers_of_not_hasCancelingPartition` is written with `theorem_wanted` in [WantedExt/Combinatorics/MonochromaticLinearEquationsWanted.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/MonochromaticLinearEquationsWanted.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/monochromatic-solutions-of-linear-equations/index.html#is-uncommon-over-integers-of-not-has-can).

## Uncommonness of $x + 2y - z - 2w = 0$ over the integers

For every $r \ge 2$,
the equation $x + 2y - z - 2w = 0$ is $r$-uncommon over the integers.

## Sources

- Laurence P. Wijaya, *On Monochromatic Solutions of Linear Equations Using at Least Three Colors*, INTEGERS 25 (2025), Article A88, Corollary 2.

Stated but not proved: `MetaMathlibExt.isUncommonOverIntegers_one_two_neg_one_neg_two` is written with `theorem_wanted` in [WantedExt/Combinatorics/MonochromaticLinearEquationsWanted.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/MonochromaticLinearEquationsWanted.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/monochromatic-solutions-of-linear-equations/index.html#is-uncommon-over-integers-one-two-neg-on).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Monochromatic solutions of linear equations](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/monochromatic-solutions-of-linear-equations/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/monochromatic-solutions-of-linear-equations)
