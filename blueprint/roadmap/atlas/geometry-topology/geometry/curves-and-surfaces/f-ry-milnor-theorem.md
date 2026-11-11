---
declaration: section
origin: cited
lean: MathlibExt.Geometry.FaryMilnorWanted.Geometry.FaryMilnorProblem.Space, MathlibExt.Geometry.FaryMilnorWanted.Geometry.FaryMilnorProblem.period, MathlibExt.Geometry.FaryMilnorWanted.Geometry.FaryMilnorProblem.velocity, MathlibExt.Geometry.FaryMilnorWanted.Geometry.FaryMilnorProblem.acceleration, MathlibExt.Geometry.FaryMilnorWanted.Geometry.FaryMilnorProblem.curvature, MathlibExt.Geometry.FaryMilnorWanted.Geometry.FaryMilnorProblem.totalCurvature, MathlibExt.Geometry.FaryMilnorWanted.Geometry.FaryMilnorProblem.standardCircle, MathlibExt.Geometry.FaryMilnorWanted.Geometry.FaryMilnorProblem.IsSmoothKnot
statement: formalized
---

# Fáry–Milnor theorem

10 results, 9 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/f-ry-milnor-theorem/index.html).

## Euclidean 3-space for the Fáry–Milnor theorem

Euclidean 3-space is the real vector
space $\mathbb{R}^3$ with the Euclidean inner product and norm.

Formalized by `MathlibExt.Geometry.FaryMilnorWanted.Geometry.FaryMilnorProblem.Space`, an abbreviation declared in [WantedExt/Geometry/FaryMilnorWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/FaryMilnorWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/f-ry-milnor-theorem/index.html#space).

## Period of a parametrised knot

The period used for parametrised knots is the real number
$2\pi$.

Formalized by `MathlibExt.Geometry.FaryMilnorWanted.Geometry.FaryMilnorProblem.period`, a definition declared in [WantedExt/Geometry/FaryMilnorWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/FaryMilnorWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/f-ry-milnor-theorem/index.html#period).

## Velocity of a space curve

For a curve $r \colon \mathbb{R} \to \mathbb{R}^3$ and a real
number $t$, the velocity of $r$ at $t$ is its derivative $r'(t)$, taken to be $0$ when $r$ is not
differentiable at $t$.

Formalized by `MathlibExt.Geometry.FaryMilnorWanted.Geometry.FaryMilnorProblem.velocity`, a definition declared in [WantedExt/Geometry/FaryMilnorWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/FaryMilnorWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/f-ry-milnor-theorem/index.html#velocity).

## Acceleration of a space curve

For a curve $r \colon \mathbb{R} \to \mathbb{R}^3$ and a real
number $t$, the acceleration of $r$ at $t$ is the derivative at $t$ of its velocity
$s \mapsto r'(s)$, that is $r''(t)$, where a derivative that does not exist is taken to be $0$.

Formalized by `MathlibExt.Geometry.FaryMilnorWanted.Geometry.FaryMilnorProblem.acceleration`, a definition declared in [WantedExt/Geometry/FaryMilnorWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/FaryMilnorWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/f-ry-milnor-theorem/index.html#acceleration).

## Curvature of a space curve

For a curve $r \colon \mathbb{R} \to \mathbb{R}^3$ with velocity
$r'$ and acceleration $r''$, the curvature of $r$ at a real number $t$ is
$\kappa(t) = \lVert r'(t) \times r''(t) \rVert / \lVert r'(t) \rVert^3$, where $\times$ is the cross
product and $\lVert \cdot \rVert$ is the Euclidean norm; the quotient is $0$ when $r'(t) = 0$.

Formalized by `MathlibExt.Geometry.FaryMilnorWanted.Geometry.FaryMilnorProblem.curvature`, a definition declared in [WantedExt/Geometry/FaryMilnorWanted.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/FaryMilnorWanted.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/f-ry-milnor-theorem/index.html#curvature).

## Total curvature of a space curve

For a curve $r \colon \mathbb{R} \to \mathbb{R}^3$ with
velocity $r'$ and curvature $\kappa$, the total curvature of $r$ is the arc-length integral
$\int_0^{2\pi} \kappa(t) \, \lVert r'(t) \rVert \, dt$ over one period, where the integral is taken
to be $0$ if the integrand is not integrable.

Formalized by `MathlibExt.Geometry.FaryMilnorWanted.Geometry.FaryMilnorProblem.totalCurvature`, a definition declared in [WantedExt/Geometry/FaryMilnorWanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/FaryMilnorWanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/f-ry-milnor-theorem/index.html#total-curvature).

## Standard circle

The standard circle is the curve $\mathbb{R} \to \mathbb{R}^3$ given by
$t \mapsto (\cos t, \sin t, 0)$: the unit circle centred at the origin in the $xy$-plane.

Formalized by `MathlibExt.Geometry.FaryMilnorWanted.Geometry.FaryMilnorProblem.standardCircle`, a definition declared in [WantedExt/Geometry/FaryMilnorWanted.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/FaryMilnorWanted.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/f-ry-milnor-theorem/index.html#standard-circle).

## Smooth knot

A curve $r \colon \mathbb{R} \to \mathbb{R}^3$ is a smooth knot when it is
real-analytic, periodic with period $2\pi$, injective on $[0, 2\pi)$, and regular, that is, its
velocity $r'(t)$ is nonzero for every real number $t$.

Formalized by `MathlibExt.Geometry.FaryMilnorWanted.Geometry.FaryMilnorProblem.IsSmoothKnot`, a structure declared in [WantedExt/Geometry/FaryMilnorWanted.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/FaryMilnorWanted.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/f-ry-milnor-theorem/index.html#is-smooth-knot).

## Unknotted curve

A curve $r \colon \mathbb{R} \to \mathbb{R}^3$ is unknotted when there is
a real-analytic map $R \colon \mathbb{R} \times \mathbb{R} \to \mathbb{R}^3$ such that
$R(t, 0) = r(t)$ and $R(t, 1) = (\cos t, \sin t, 0)$, the standard circle, for every real
number $t$, and for every $s \in [0, 1]$ the curve $t \mapsto R(t, s)$ is a smooth knot.

Formalized by `MathlibExt.Geometry.FaryMilnorWanted.Geometry.FaryMilnorProblem.IsUnknotted`, a definition declared in [WantedExt/Geometry/FaryMilnorWanted.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/FaryMilnorWanted.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/f-ry-milnor-theorem/index.html#is-unknotted).

## Fáry–Milnor theorem

Let $r \colon \mathbb{R} \to \mathbb{R}^3$ be a smooth knot, that is,
a real-analytic, $2\pi$-periodic curve that is injective on $[0, 2\pi)$ and has nonzero velocity
everywhere. If the total curvature of $r$ is at most $4\pi$, then $r$ is unknotted: there is a
real-analytic isotopy from $r$ to the standard circle through smooth knots.

## Sources

- I. Fáry, 'Sur la courbure totale d'une courbe gauche faisant un nœud', Bull. Soc. Math. France 77 (1949) 128–138; J. Milnor, 'On the total curvature of knots', Ann. of Math. (2) 52 (1950) 248–257. §161 in O. Knill, *Some Fundamental Theorems in Mathematics* (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Problem `fary_milnor` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.FaryMilnorWanted.Geometry.FaryMilnorProblem.fary_milnor_total_curvature` is written with `theorem_wanted` in [WantedExt/Geometry/FaryMilnorWanted.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/FaryMilnorWanted.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/f-ry-milnor-theorem/index.html#fary-milnor-total-curvature).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fáry–Milnor theorem](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/f-ry-milnor-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Geometry/curves-and-surfaces/f-ry-milnor-theorem)
