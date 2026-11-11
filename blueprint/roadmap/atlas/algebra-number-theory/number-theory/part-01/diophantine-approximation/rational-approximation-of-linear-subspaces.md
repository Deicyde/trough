---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.LinearSubspacesWanted.LinearSubspaces.distLines, MathlibExt.NumberTheory.LinearSubspacesWanted.LinearSubspaces.distLineSubspace, MathlibExt.NumberTheory.LinearSubspacesWanted.LinearSubspaces.distSubspaces, MathlibExt.NumberTheory.LinearSubspacesWanted.LinearSubspaces.intPoints, MathlibExt.NumberTheory.LinearSubspacesWanted.LinearSubspaces.intPointsSubspace, MathlibExt.NumberTheory.LinearSubspacesWanted.LinearSubspaces.IsRational, MathlibExt.NumberTheory.LinearSubspacesWanted.LinearSubspaces.chosenBasis, MathlibExt.NumberTheory.LinearSubspacesWanted.LinearSubspaces.height
statement: formalized
---

# Rational approximation of linear subspaces

10 results, 9 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/rational-approximation-of-linear-subspaces/index.html).

## Distance between lines

For lines $x$ and $y$ through the origin in $\mathbb{R}^d$, the
distance $\operatorname{dist}(x, y)$ is $\sin \theta$, where $\theta \in [0, \pi]$ is the angle
between nonzero vectors spanning $x$ and $y$. This is the usual distance on the projective
space.

Formalized by `MathlibExt.NumberTheory.LinearSubspacesWanted.LinearSubspaces.distLines`, a definition declared in [WantedExt/NumberTheory/LinearSubspacesWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LinearSubspacesWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/rational-approximation-of-linear-subspaces/index.html#dist-lines).

## Distance from a line to a subspace

For a line $x$ through the origin in $\mathbb{R}^d$
and a subspace $y$ of $\mathbb{R}^d$, the distance $\operatorname{dist}(x, y)$ is the infimum,
over all lines $y'$ contained in $y$, of the distance $\operatorname{dist}(x, y')$ between the
lines $x$ and $y'$. When $y = 0$ there is no such line and the value is $0$.

Formalized by `MathlibExt.NumberTheory.LinearSubspacesWanted.LinearSubspaces.distLineSubspace`, a definition declared in [WantedExt/NumberTheory/LinearSubspacesWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LinearSubspacesWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/rational-approximation-of-linear-subspaces/index.html#dist-line-subspace).

## Distance between subspaces

For subspaces $x$ and $y$ of $\mathbb{R}^d$, the distance
$\operatorname{dist}(x, y)$ is defined as follows. If $\dim y \le \dim x$, it is the supremum,
over all lines $y'$ contained in $y$, of the distance $\operatorname{dist}(y', x)$ from the line
$y'$ to the subspace $x$. If $\dim y > \dim x$, it is the supremum, over all lines $x'$ contained
in $x$, of the distance $\operatorname{dist}(x', y)$ from the line $x'$ to the subspace $y$. A
supremum over no lines is $0$.

Formalized by `MathlibExt.NumberTheory.LinearSubspacesWanted.LinearSubspaces.distSubspaces`, a definition declared in [WantedExt/NumberTheory/LinearSubspacesWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LinearSubspacesWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/rational-approximation-of-linear-subspaces/index.html#dist-subspaces).

## The integer lattice

$\mathbb{Z}^d$ is the $\mathbb{Z}$-submodule of $\mathbb{R}^d$
spanned by the standard basis vectors, that is, the lattice of points with integer coordinates.

Formalized by `MathlibExt.NumberTheory.LinearSubspacesWanted.LinearSubspaces.intPoints`, an abbreviation declared in [WantedExt/NumberTheory/LinearSubspacesWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LinearSubspacesWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/rational-approximation-of-linear-subspaces/index.html#int-points).

## Integer points of a subspace

For a subspace $V$ of $\mathbb{R}^d$, this is the set
$V \cap \mathbb{Z}^d$ of integer points of $V$, as a $\mathbb{Z}$-submodule of $V$.

Formalized by `MathlibExt.NumberTheory.LinearSubspacesWanted.LinearSubspaces.intPointsSubspace`, a definition declared in [WantedExt/NumberTheory/LinearSubspacesWanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LinearSubspacesWanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/rational-approximation-of-linear-subspaces/index.html#int-points-subspace).

## Rational subspace

A subspace $V$ of $\mathbb{R}^d$ is rational if $V \cap \mathbb{Z}^d$
is a full-rank lattice in $V$, that is, a discrete subgroup of $V$ that spans $V$ over
$\mathbb{R}$.

The paper does not state which definition of rational subspace it uses; this one is common
and is the most convenient for defining heights of rational subspaces.

Formalized by `MathlibExt.NumberTheory.LinearSubspacesWanted.LinearSubspaces.IsRational`, an abbreviation declared in [WantedExt/NumberTheory/LinearSubspacesWanted.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LinearSubspacesWanted.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/rational-approximation-of-linear-subspaces/index.html#is-rational).

## Chosen basis of a rational subspace

For a rational subspace $V$ of $\mathbb{R}^d$, this
is a fixed choice of a $\mathbb{Z}$-basis of the lattice $V \cap \mathbb{Z}^d$, indexed by
$\{0, \dots, \dim V - 1\}$ and viewed as an $\mathbb{R}$-basis of $V$.

Formalized by `MathlibExt.NumberTheory.LinearSubspacesWanted.LinearSubspaces.chosenBasis`, a definition declared in [WantedExt/NumberTheory/LinearSubspacesWanted.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LinearSubspacesWanted.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/rational-approximation-of-linear-subspaces/index.html#chosen-basis).

## Height of a rational subspace

For a rational subspace $V$ of $\mathbb{R}^d$ of dimension
$k$, let $v_1, \dots, v_k$ be the chosen basis of the lattice $V \cap \mathbb{Z}^d$. The height of
$V$ is $H(V) = \lVert v_1 \wedge \dots \wedge v_k \rVert$, where the exterior power
$\bigwedge^k \mathbb{R}^d$ carries the inner product whose value on decomposable elements
$u_1 \wedge \dots \wedge u_k$ and $w_1 \wedge \dots \wedge w_k$ is the Gram determinant
$\det(\langle u_i, w_j \rangle)_{i,j}$.

Formalized by `MathlibExt.NumberTheory.LinearSubspacesWanted.LinearSubspaces.height`, a definition declared in [WantedExt/NumberTheory/LinearSubspacesWanted.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LinearSubspacesWanted.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/rational-approximation-of-linear-subspaces/index.html#height).

## Diophantine exponent

Let $x$ be a subspace of $\mathbb{R}^d$ and let $k$ be a natural
number. For subspaces $v$ of $\mathbb{R}^d$ write $\operatorname{dist}(v, x)$ for the distance
between the subspaces $v$ and $x$, and for a rational subspace $v$ write $H(v)$ for its height.
The diophantine exponent $\beta_k(x)$ of $x$ for approximation by $k$-dimensional rational
subspaces is the infimum, taken in $[0, \infty]$, of the set of real numbers $\beta > 0$ for
which there is a real number $c > 0$ such that $\operatorname{dist}(v, x) \ge c \, H(v)^{-\beta}$
for every $k$-dimensional rational subspace $v$ of $\mathbb{R}^d$. In particular
$\beta_k(x) = \infty$ when there is no such $\beta$.

Formalized by `MathlibExt.NumberTheory.LinearSubspacesWanted.LinearSubspaces.diophantineExponent`, a definition declared in [WantedExt/NumberTheory/LinearSubspacesWanted.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LinearSubspacesWanted.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/rational-approximation-of-linear-subspaces/index.html#diophantine-exponent).

## Dirichlet's principle in Grassmann varieties

Let $d$, $l$ and $k$ be natural numbers with
$d \ge 2$, $0 < l < d$ and $1 \le k \le l$, and for a subspace $x$ of $\mathbb{R}^d$ write
$\beta_k(x)$ for the diophantine exponent of $x$ for approximation by $k$-dimensional rational
subspaces. Then every $l$-dimensional subspace $x$ of $\mathbb{R}^d$ satisfies
$\beta_k(x) \ge \frac{d}{k(d - l)}$. Moreover, some $l$-dimensional subspace $x$ of
$\mathbb{R}^d$ satisfies $\beta_k(x) = \frac{d}{k(d - l)}$.

## Sources

- N. de Saxcé, `Rational approximations to linear subspaces`, Annals of Math, 203 (3) 2026. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_linear_subspaces` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.NumberTheory.LinearSubspacesWanted.LinearSubspaces.theorem_1` is written with `theorem_wanted` in [WantedExt/NumberTheory/LinearSubspacesWanted.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LinearSubspacesWanted.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/rational-approximation-of-linear-subspaces/index.html#theorem-1).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Rational approximation of linear subspaces](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/rational-approximation-of-linear-subspaces/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/diophantine-approximation/rational-approximation-of-linear-subspaces)
