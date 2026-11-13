---
declaration: section
origin: cited
lean: MathlibExt.Topology.PardonDistortionWanted.KnotTheory.PardonDistortion.speed, MathlibExt.Topology.PardonDistortionWanted.KnotTheory.PardonDistortion.parameterArcLength, MathlibExt.Topology.PardonDistortionWanted.KnotTheory.PardonDistortion.totalArcLength, MathlibExt.Topology.PardonDistortionWanted.KnotTheory.PardonDistortion.intrinsicDistance, MathlibExt.Topology.PardonDistortionWanted.KnotTheory.PardonDistortion.distortionRatio, MathlibExt.Topology.PardonDistortionWanted.KnotTheory.PardonDistortion.distortion, MathlibExt.Topology.PardonDistortionWanted.KnotTheory.PardonDistortion.standardTorusCurve, MathlibExt.Topology.PardonDistortionWanted.KnotTheory.PardonDistortion.pardon_torus_knot_distortion
statement: formalized
---

# Distortion of knots

8 results, 7 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/distortion-of-knots/index.html).

## Speed of a knot

For a knot $K$ with parametrization $\gamma$ and a real number $t$,
the speed of $K$ at $t$ is the Euclidean norm $\lVert \gamma'(t) \rVert$ of the derivative of
$\gamma$ at $t$.

Formalized by `MathlibExt.Topology.PardonDistortionWanted.KnotTheory.PardonDistortion.speed`, a definition declared in [WantedExt/Topology/PardonDistortionWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/PardonDistortionWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/distortion-of-knots/index.html#speed).

## Arc length between two parameters

For a knot $K$ with parametrization $\gamma$ and real
numbers $s$ and $t$, the arc length of $K$ between $s$ and $t$ is
$\left| \int_s^t \lVert \gamma'(u) \rVert \, du \right|$, the length of the arc that $\gamma$ traces
between the parameters $s$ and $t$. It does not depend on the order of $s$ and $t$.

Formalized by `MathlibExt.Topology.PardonDistortionWanted.KnotTheory.PardonDistortion.parameterArcLength`, a definition declared in [WantedExt/Topology/PardonDistortionWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/PardonDistortionWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/distortion-of-knots/index.html#parameter-arc-length).

## Total arc length of a knot

For a knot $K$ with parametrization $\gamma$, the total arc
length of $K$ is the arc length of $K$ between the parameters $0$ and $2\pi$, namely
$\left| \int_0^{2\pi} \lVert \gamma'(u) \rVert \, du \right|$.

Formalized by `MathlibExt.Topology.PardonDistortionWanted.KnotTheory.PardonDistortion.totalArcLength`, a definition declared in [WantedExt/Topology/PardonDistortionWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/PardonDistortionWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/distortion-of-knots/index.html#total-arc-length).

## Intrinsic distance on a knot

For a knot $K$ and real numbers $s$ and $t$, let $\ell$ be the
arc length of $K$ between the parameters $s$ and $t$, and let $L$ be the total arc length of $K$.
The intrinsic distance between $s$ and $t$ is $\min(\ell, L - \ell)$. When $s$ and $t$ lie in one
closed interval of length $2\pi$, this is the length of the shorter of the two arcs of $K$ joining
the points with parameters $s$ and $t$.

Formalized by `MathlibExt.Topology.PardonDistortionWanted.KnotTheory.PardonDistortion.intrinsicDistance`, a definition declared in [WantedExt/Topology/PardonDistortionWanted.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/PardonDistortionWanted.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/distortion-of-knots/index.html#intrinsic-distance).

## Distortion ratio

For a knot $K$ with parametrization $\gamma$ and real numbers $s$ and $t$,
the distortion ratio of $K$ at $s$ and $t$ is the intrinsic distance between $s$ and $t$ along $K$
divided by the Euclidean distance $\lVert \gamma(s) - \gamma(t) \rVert$ in $\mathbb{R}^3$, where
division by $0$ gives $0$.

Formalized by `MathlibExt.Topology.PardonDistortionWanted.KnotTheory.PardonDistortion.distortionRatio`, a definition declared in [WantedExt/Topology/PardonDistortionWanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/PardonDistortionWanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/distortion-of-knots/index.html#distortion-ratio).

## Distortion of a knot

For a knot $K$, the distortion of $K$ is the supremum in the
extended nonnegative reals $[0, \infty]$ of the distortion ratios of $K$ at $s$ and $t$, taken
over all distinct parameters $s \ne t$ in the half-open interval $[0, 2\pi)$.

Formalized by `MathlibExt.Topology.PardonDistortionWanted.KnotTheory.PardonDistortion.distortion`, a definition declared in [WantedExt/Topology/PardonDistortionWanted.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/PardonDistortionWanted.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/distortion-of-knots/index.html#distortion).

## Standard torus curve

For natural numbers $p$ and $q$, the standard $(p, q)$-torus curve is
the map $\mathbb{R} \to \mathbb{R}^3$ sending $t$ to
$((2 + \cos qt) \cos pt,\ (2 + \cos qt) \sin pt,\ \sin qt)$. It lies on the torus of revolution
about the $z$-axis with major radius $2$ and minor radius $1$, and as $t$ runs over $[0, 2\pi]$ it
winds $p$ times around the $z$-axis and $q$ times around the core circle of the torus.

Formalized by `MathlibExt.Topology.PardonDistortionWanted.KnotTheory.PardonDistortion.standardTorusCurve`, a definition declared in [WantedExt/Topology/PardonDistortionWanted.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/PardonDistortionWanted.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/distortion-of-knots/index.html#standard-torus-curve).

## Pardon's lower bound for the distortion of torus knots

Let $p$ and $q$ be coprime positive
integers, let $T_{p,q}$ be the standard $(p, q)$-torus curve, and let $K$ be a knot with
parametrization $\gamma$. Suppose there are an ambient isotopy $H$ of $\mathbb{R}^3$, with
time-one map $H_1$, and a strictly increasing diffeomorphism $\sigma$ of $\mathbb{R}$ with
$\sigma(t + 2\pi) = \sigma(t) + 2\pi$ for all real $t$, such that
$H_1(\gamma(t)) = T_{p,q}(\sigma(t))$ for every real $t$. Then the distortion of $K$ is at least
$\min(p, q)/160$.

This is the smooth, oriented specialization of Pardon's theorem, which bounds the distortion of
every rectifiable curve in the knot type of the $(p, q)$-torus knot.

## Sources

- John Pardon, 'On the distortion of knots on embedded surfaces', Annals of Mathematics (2) 174 (2011), no. 1, 637-646, Theorem 1.1. https://doi.org/10.4007/annals.2011.174.1.21. Problem `pardon_torus_knot_distortion` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Topology.PardonDistortionWanted.KnotTheory.PardonDistortion.pardon_torus_knot_distortion` is written with `theorem_wanted` in [WantedExt/Topology/PardonDistortionWanted.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/PardonDistortionWanted.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/distortion-of-knots/index.html#pardon-torus-knot-distortion).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Distortion of knots](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/distortion-of-knots/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Topology/knot-theory/distortion-of-knots)
