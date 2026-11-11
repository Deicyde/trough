---
declaration: section
origin: cited
lean: MathlibExt.Geometry.UlamWanted.Ulam.S, MathlibExt.Geometry.UlamWanted.Ulam.IsOriginSymmetric, MathlibExt.Geometry.UlamWanted.Ulam.IsCentrallySymmetric, MathlibExt.Geometry.UlamWanted.Ulam.centerOfMass, MathlibExt.Geometry.UlamWanted.Ulam.H_minus, MathlibExt.Geometry.UlamWanted.Ulam.CuttingHyperplaneAtLevel, MathlibExt.Geometry.UlamWanted.Ulam.CuttingHyperplaneAtLevel.lineThroughCentersOfMass, MathlibExt.Geometry.UlamWanted.Ulam.FloatsInEquilibriumInDirectionAtLevel
statement: formalized
---

# Ulam's floating body problem

13 results, 12 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/ulam-s-floating-body-problem/index.html).

## Unit sphere

For a natural number $d$, the unit sphere
$S^{d-1} = \{x \in \mathbb{R}^d : \|x\| = 1\}$ in $\mathbb{R}^d$, centered at the origin.

Formalized by `MathlibExt.Geometry.UlamWanted.Ulam.S`, an abbreviation declared in [WantedExt/Geometry/UlamWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/UlamWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/ulam-s-floating-body-problem/index.html#s).

## Origin-symmetric set

A set $K \subseteq \mathbb{R}^d$ is origin-symmetric if $K = -K$,
where $-K = \{-x : x \in K\}$.

Formalized by `MathlibExt.Geometry.UlamWanted.Ulam.IsOriginSymmetric`, an abbreviation declared in [WantedExt/Geometry/UlamWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/UlamWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/ulam-s-floating-body-problem/index.html#is-origin-symmetric).

## Centrally symmetric set

A set $K \subseteq \mathbb{R}^d$ is centrally symmetric if there
is a point $p \in \mathbb{R}^d$ such that the translate $K - p = \{x - p : x \in K\}$ is
origin-symmetric, that is, $K - p = -(K - p)$.

Formalized by `MathlibExt.Geometry.UlamWanted.Ulam.IsCentrallySymmetric`, an abbreviation declared in [WantedExt/Geometry/UlamWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/UlamWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/ulam-s-floating-body-problem/index.html#is-centrally-symmetric).

## Center of mass

The center of mass of a set $K \subseteq \mathbb{R}^d$ is the average
$\frac{1}{\operatorname{vol}(K)} \int_K x \, dx$, where $dx$ is Lebesgue measure on $\mathbb{R}^d$.
By convention it is $0$ when $\operatorname{vol}(K)$ is $0$ or infinite, or when $x \mapsto x$ is
not integrable on $K$. For a compact convex body this is the usual center of mass.

Formalized by `MathlibExt.Geometry.UlamWanted.Ulam.centerOfMass`, an abbreviation declared in [WantedExt/Geometry/UlamWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/UlamWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/ulam-s-floating-body-problem/index.html#center-of-mass).

## Lower half-space

For a unit vector $\xi \in \mathbb{R}^d$ and $t \in \mathbb{R}$, the
closed lower half-space is $H^-(\xi) = \{p \in \mathbb{R}^d : \xi \cdot p \le t\}$.

## Sources

- D. Ryabogin, A negative answer to Ulam's Problem 19 from the Scottish Book, Annals of Math. 195 (3) 2022, Equation (1).

Formalized by `MathlibExt.Geometry.UlamWanted.Ulam.H_minus`, a definition declared in [WantedExt/Geometry/UlamWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/UlamWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/ulam-s-floating-body-problem/index.html#h-minus).

## Cutting hyperplane at a level

Let $K \subseteq \mathbb{R}^d$, let $\xi \in \mathbb{R}^d$ be
a unit vector and let $\delta \in \mathbb{R}$. A cutting hyperplane of $K$ in direction $\xi$ at
level $\delta$ is a real number $t$, standing for the hyperplane
$\{p \in \mathbb{R}^d : \xi \cdot p = t\}$, such that the volume of
$K \cap \{p \in \mathbb{R}^d : \xi \cdot p \le t\}$ equals $\delta$. Here a set of infinite volume
is assigned volume $0$.

Formalized by `MathlibExt.Geometry.UlamWanted.Ulam.CuttingHyperplaneAtLevel`, a structure declared in [WantedExt/Geometry/UlamWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/UlamWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/ulam-s-floating-body-problem/index.html#cutting-hyperplane-at-level).

## Direction of the line through the centers of mass

Let $d$ be a natural number, let
$K \subseteq \mathbb{R}^d$, let $\xi$ be a unit vector in $\mathbb{R}^d$, let
$\delta \in \mathbb{R}$, and let $H$ be a cutting hyperplane of $K$ in direction $\xi$ at level
$\delta$, with translation $t$, so that
$H^-(\xi) = \{x \in \mathbb{R}^d : \langle x, \xi \rangle \le t\}$. Writing $c(A)$ for the center
of mass of a set $A \subseteq \mathbb{R}^d$, the direction vector of the line $l(\xi)$ through the
center of mass of $K$ and the center of mass of the submerged part $K \cap H^-(\xi)$ is the vector
$c(K) - c(K \cap H^-(\xi))$.

Formalized by `MathlibExt.Geometry.UlamWanted.Ulam.CuttingHyperplaneAtLevel.lineThroughCentersOfMass`, a definition declared in [WantedExt/Geometry/UlamWanted.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/UlamWanted.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/ulam-s-floating-body-problem/index.html#line-through-centers-of-mass).

## Floating in equilibrium in a direction

Let $K \subseteq \mathbb{R}^d$, let
$\xi \in \mathbb{R}^d$ be a unit vector and let $\delta \in \mathbb{R}$. We say that $K$ floats in
equilibrium in direction $\xi$ at level $\delta$ if, for every cutting hyperplane
$\{p : \xi \cdot p = t\}$ of $K$ in direction $\xi$ at level $\delta$, the center of mass of $K$
minus the center of mass of $K \cap \{p : \xi \cdot p \le t\}$ is a real multiple of $\xi$
(possibly zero); that is, the line through the two centers of mass is parallel to $\xi$ when they
differ.

Formalized by `MathlibExt.Geometry.UlamWanted.Ulam.FloatsInEquilibriumInDirectionAtLevel`, a definition declared in [WantedExt/Geometry/UlamWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/UlamWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/ulam-s-floating-body-problem/index.html#floats-in-equilibrium-in-direction-at-le).

## Floating in equilibrium in every orientation

A set $K \subseteq \mathbb{R}^d$ floats in
equilibrium in every orientation at level $\delta \in \mathbb{R}$ if it floats in equilibrium in
direction $\xi$ at level $\delta$ for every unit vector $\xi \in \mathbb{R}^d$.

Formalized by `MathlibExt.Geometry.UlamWanted.Ulam.FloatsInEquilibriumInEveryOrientationAtLevel`, a definition declared in [WantedExt/Geometry/UlamWanted.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/UlamWanted.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/ulam-s-floating-body-problem/index.html#floats-in-equilibrium-in-every-orientati).

## Body of revolution

A body of revolution in $\mathbb{R}^d$ is given by real numbers
$R_1, R_2$ and a function $f : \mathbb{R} \to \mathbb{R}$ that vanishes outside the interval
$[-R_1, R_2]$, is infinitely differentiable on the open interval $(-R_1, R_2)$ and is concave on
$[-R_1, R_2]$. The dimension $d$ is only a parameter; these data do not depend on it.

Formalized by `MathlibExt.Geometry.UlamWanted.Ulam.BodyOfRevolution`, a structure declared in [WantedExt/Geometry/UlamWanted.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/UlamWanted.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/ulam-s-floating-body-problem/index.html#body-of-revolution).

## Solid of revolution

Let $d \ge 1$ and let a body of revolution in $\mathbb{R}^d$ be given
by $R_1$, $R_2$ and $f$. Writing points of $\mathbb{R}^d$ as $x = (x_0, \dots, x_{d-1})$, its solid
is the set of all $x$ with $x_0 \in [-R_1, R_2]$ and $x_1^2 + \dots + x_{d-1}^2 \le f(x_0)^2$.

Formalized by `MathlibExt.Geometry.UlamWanted.Ulam.BodyOfRevolution.body`, a definition declared in [WantedExt/Geometry/UlamWanted.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/UlamWanted.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/ulam-s-floating-body-problem/index.html#body).

## Strictly convex body

A set $K \subseteq \mathbb{R}^d$ is a strictly convex body if it is
strictly convex (for distinct $x, y \in K$, every point of the open segment between $x$ and $y$
lies in the interior of $K$), compact, and has nonempty interior.

Formalized by `MathlibExt.Geometry.UlamWanted.Ulam.IsStrictlyConvexBody`, a definition declared in [WantedExt/Geometry/UlamWanted.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/UlamWanted.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/ulam-s-floating-body-problem/index.html#is-strictly-convex-body).

## Ryabogin's negative answer to Ulam's floating body problem

Let $d \ge 3$. There exists a
body of revolution $K \subset \mathbb{R}^d$ that is a strictly convex body, is not centrally
symmetric, and floats in equilibrium in every orientation at the level $\operatorname{vol}(K)/2$.

## Sources

- D. Ryabogin, `A negative answer to Ulam's Problem 19 from the Scottish Book`, Annals of Math, 195 (3) 2022. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_ulam` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.UlamWanted.Ulam.theorem_1` is written with `theorem_wanted` in [WantedExt/Geometry/UlamWanted.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/UlamWanted.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/ulam-s-floating-body-problem/index.html#theorem-1).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ulam's floating body problem](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/ulam-s-floating-body-problem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Geometry/convex-geometry/ulam-s-floating-body-problem)
