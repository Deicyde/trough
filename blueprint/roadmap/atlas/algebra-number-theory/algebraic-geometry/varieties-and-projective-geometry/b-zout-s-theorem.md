---
declaration: section
origin: cited
lean: MathlibExt.AlgebraicGeometry.BezoutWanted.AlgebraicGeometry.ProjSpace, MathlibExt.AlgebraicGeometry.BezoutWanted.AlgebraicGeometry.vanishingSet, MathlibExt.AlgebraicGeometry.BezoutWanted.AlgebraicGeometry.chartIndex, MathlibExt.AlgebraicGeometry.BezoutWanted.AlgebraicGeometry.affineConeCoord, MathlibExt.AlgebraicGeometry.BezoutWanted.AlgebraicGeometry.evalAt, MathlibExt.AlgebraicGeometry.BezoutWanted.AlgebraicGeometry.maxIdealAt, MathlibExt.AlgebraicGeometry.BezoutWanted.AlgebraicGeometry.localRingAt, MathlibExt.AlgebraicGeometry.BezoutWanted.AlgebraicGeometry.intersectionMultiplicity
statement: formalized
---

# Bézout's theorem

9 results, 8 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/b-zout-s-theorem/index.html).

## Projective space

For a division ring $K$ and $n \in \mathbb{N}$, the projective space
$\mathbb{P}^n(K)$ is the projectivization of $K^{n+1}$: the set of nonzero vectors of $K^{n+1}$
modulo multiplication by nonzero scalars, equivalently the lines through the origin.

Formalized by `MathlibExt.AlgebraicGeometry.BezoutWanted.AlgebraicGeometry.ProjSpace`, an abbreviation declared in [WantedExt/AlgebraicGeometry/BezoutWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/AlgebraicGeometry/BezoutWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/b-zout-s-theorem/index.html#proj-space).

## Projective vanishing set

For a field $K$ and a polynomial $f \in K[X_0, \dots, X_n]$, the
vanishing set of $f$ is the set of points $p \in \mathbb{P}^n(K)$ such that $f(v) = 0$, where
$v \in K^{n+1} \setminus \{0\}$ is the chosen representative of $p$.

When $f$ is homogeneous of degree $d$, $f(\lambda v) = \lambda^d f(v)$, so this set does not depend
on the choice of representatives.

Formalized by `MathlibExt.AlgebraicGeometry.BezoutWanted.AlgebraicGeometry.vanishingSet`, a definition declared in [WantedExt/AlgebraicGeometry/BezoutWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/AlgebraicGeometry/BezoutWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/b-zout-s-theorem/index.html#vanishing-set).

## Chart index of a projective point

For a field $K$ and a point $p \in \mathbb{P}^n(K)$
with chosen representative $v = (v_0, \dots, v_n) \in K^{n+1} \setminus \{0\}$, the chart index of
$p$ is a fixed choice of an index $i \in \{0, \dots, n\}$ with $v_i \neq 0$.

Formalized by `MathlibExt.AlgebraicGeometry.BezoutWanted.AlgebraicGeometry.chartIndex`, a definition declared in [WantedExt/AlgebraicGeometry/BezoutWanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/AlgebraicGeometry/BezoutWanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/b-zout-s-theorem/index.html#chart-index).

## Affine coordinates of a projective point

For a field $K$ and a point
$p \in \mathbb{P}^n(K)$, let $v = (v_0, \dots, v_n) \in K^{n+1} \setminus \{0\}$ be the chosen
representative of $p$ and $i$ its chart index (a chosen index with $v_i \neq 0$). The affine cone
coordinates of $p$ are the vector $q \in K^{n+1}$ with $q_j = v_j / v_i$ for every $j$; in
particular $q_i = 1$.

Formalized by `MathlibExt.AlgebraicGeometry.BezoutWanted.AlgebraicGeometry.affineConeCoord`, a definition declared in [WantedExt/AlgebraicGeometry/BezoutWanted.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/AlgebraicGeometry/BezoutWanted.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/b-zout-s-theorem/index.html#affine-cone-coord).

## Evaluation at an affine point

For a field $K$ and a point
$q = (q_0, \dots, q_n) \in K^{n+1}$, this is the ring homomorphism $K[X_0, \dots, X_n] \to K$
sending each polynomial $g$ to its value $g(q)$; it fixes $K$ and sends $X_j$ to $q_j$.

Formalized by `MathlibExt.AlgebraicGeometry.BezoutWanted.AlgebraicGeometry.evalAt`, a definition declared in [WantedExt/AlgebraicGeometry/BezoutWanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/AlgebraicGeometry/BezoutWanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/b-zout-s-theorem/index.html#eval-at).

## Maximal ideal of an affine point

For a field $K$ and a point $q \in K^{n+1}$, this is the
ideal of $K[X_0, \dots, X_n]$ consisting of the polynomials $g$ with $g(q) = 0$, that is, the
kernel of evaluation at $q$.

It is a maximal ideal, since evaluation at $q$ is surjective onto $K$.

Formalized by `MathlibExt.AlgebraicGeometry.BezoutWanted.AlgebraicGeometry.maxIdealAt`, a definition declared in [WantedExt/AlgebraicGeometry/BezoutWanted.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/AlgebraicGeometry/BezoutWanted.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/b-zout-s-theorem/index.html#max-ideal-at).

## Local ring of affine space at a point

For a field $K$ and a point $q \in K^{n+1}$, this is
the localization of $K[X_0, \dots, X_n]$ at the maximal ideal of $q$ (the ideal of polynomials
vanishing at $q$), that is, the local ring of affine space $\mathbb{A}^{n+1}$ at $q$.

Formalized by `MathlibExt.AlgebraicGeometry.BezoutWanted.AlgebraicGeometry.localRingAt`, an abbreviation declared in [WantedExt/AlgebraicGeometry/BezoutWanted.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/AlgebraicGeometry/BezoutWanted.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/b-zout-s-theorem/index.html#local-ring-at).

## Intersection multiplicity at a projective point

Let $K$ be a field and
$f_1, \dots, f_n \in K[X_0, \dots, X_n]$. For a point $p \in \mathbb{P}^n(K)$, let $i$ be its chart
index, $q \in K^{n+1}$ its affine cone coordinates (so $q_i = 1$), and $\mathcal{O}_q$ the
localization of $K[X_0, \dots, X_n]$ at the maximal ideal of $q$. The intersection multiplicity
of $f_1, \dots, f_n$ at $p$ is the length, as an $\mathcal{O}_q$-module, of the quotient of
$\mathcal{O}_q$ by the ideal generated by $f_1, \dots, f_n$ and $X_i - 1$; it is an element of
$\mathbb{N} \cup \{\infty\}$.

The value is $\infty$ exactly when this quotient does not have finite length, for example along
a positive-dimensional component of the common zero set.

Formalized by `MathlibExt.AlgebraicGeometry.BezoutWanted.AlgebraicGeometry.intersectionMultiplicity`, a definition declared in [WantedExt/AlgebraicGeometry/BezoutWanted.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/AlgebraicGeometry/BezoutWanted.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/b-zout-s-theorem/index.html#intersection-multiplicity).

## Bézout's theorem (with multiplicity)

Let $K$ be an algebraically closed field, let
$n \in \mathbb{N}$, and let $f_1, \dots, f_n \in K[X_0, \dots, X_n]$ and integers
$d_1, \dots, d_n \ge 1$ be such that each $f_k$ is homogeneous of degree $d_k$ and has total
degree exactly $d_k$. Suppose the common projective zero set
$Z = V(f_1) \cap \dots \cap V(f_n) \subseteq \mathbb{P}^n(K)$ is finite. Then
$\sum_{p \in Z} i_p(f_1, \dots, f_n) = d_1 d_2 \cdots d_n$ in $\mathbb{N} \cup \{\infty\}$,
where $i_p(f_1, \dots, f_n)$ is the intersection multiplicity of $f_1, \dots, f_n$ at $p$.

The total degree hypothesis rules out $f_k = 0$, which is homogeneous of every degree but has
total degree $0$.

## Sources

- É. Bézout, *Théorie générale des équations algébriques*, Paris, 1779. Modern projective formulation: see Eisenbud, *Commutative Algebra*, Chapter 12, or Hartshorne, *Algebraic Geometry*, Ch. I §7. Listed as §50 in O. Knill, *Some Fundamental Theorems in Mathematics* (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Problem `bezout_projective_multiplicity` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.AlgebraicGeometry.BezoutWanted.AlgebraicGeometry.bezout_multiplicity` is written with `theorem_wanted` in [WantedExt/AlgebraicGeometry/BezoutWanted.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/AlgebraicGeometry/BezoutWanted.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/b-zout-s-theorem/index.html#bezout-multiplicity).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bézout's theorem](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/b-zout-s-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/b-zout-s-theorem)
