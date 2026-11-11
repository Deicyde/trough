---
declaration: section
origin: cited
lean: MathlibExt.Geometry.SpherePackingDensityFourWanted.Space, MathlibExt.Geometry.SpherePackingDensityFourWanted.PositiveRadius, MathlibExt.Geometry.SpherePackingDensityFourWanted.Packing, MathlibExt.Geometry.SpherePackingDensityFourWanted.packedBall, MathlibExt.Geometry.SpherePackingDensityFourWanted.packingRegion, MathlibExt.Geometry.SpherePackingDensityFourWanted.finiteRadiusDensity, MathlibExt.Geometry.SpherePackingDensityFourWanted.centeredRadiusDensity, MathlibExt.Geometry.SpherePackingDensityFourWanted.upperDensity
statement: formalized
---

# Sphere packing in four dimensions

37 results, 32 proved and 5 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/sphere-packing-in-four-dimensions/index.html).

## Four-dimensional Euclidean space

The ambient space is $\mathbb{R}^4$, the space of real
$4$-tuples with the standard Euclidean inner product and the distance it induces.

## Sources

- CE2003, the ambient Euclidean space `ℝ⁴`.

Formalized by `MathlibExt.Geometry.SpherePackingDensityFourWanted.Space`, an abbreviation declared in [MathlibExt/Geometry/SpherePackingDensityFour.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/SpherePackingDensityFour.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/sphere-packing-in-four-dimensions/index.html#space).

## Positive radii

A positive radius is a real number $R$ with $R > 0$; the positive radii
form the set $\{R \in \mathbb{R} : R > 0\}$.

## Sources

- CE2003 Appendix A, positive observation radii tending to infinity.

Formalized by `MathlibExt.Geometry.SpherePackingDensityFourWanted.PositiveRadius`, an abbreviation declared in [MathlibExt/Geometry/SpherePackingDensityFour.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/SpherePackingDensityFour.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/sphere-packing-in-four-dimensions/index.html#positive-radius).

## Packings of congruent balls in $\mathbb{R}^4$

A packing in $\mathbb{R}^4$ consists of a
real radius $r > 0$ and a set $C \subseteq \mathbb{R}^4$ of centres such that for any two distinct
centres $c, c' \in C$ the open balls of radius $r$ about $c$ and $c'$ are disjoint.

## Sources

- CE2003 introduction, congruent positive-radius balls with disjoint interiors.

Formalized by `MathlibExt.Geometry.SpherePackingDensityFourWanted.Packing`, a structure declared in [MathlibExt/Geometry/SpherePackingDensityFour.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/SpherePackingDensityFour.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/sphere-packing-in-four-dimensions/index.html#packing).

## Packed ball

For a packing $P$ in $\mathbb{R}^4$ with radius $r$ and a point
$c \in \mathbb{R}^4$, the packed ball of $P$ at $c$ is the closed ball
$\{x \in \mathbb{R}^4 : \|x - c\| \le r\}$, boundary included.

## Sources

- CE2003, the packed closed ball at a center, including its boundary.

Formalized by `MathlibExt.Geometry.SpherePackingDensityFourWanted.packedBall`, a definition declared in [MathlibExt/Geometry/SpherePackingDensityFour.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/SpherePackingDensityFour.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/sphere-packing-in-four-dimensions/index.html#packed-ball).

## Region covered by a packing

For a packing $P$ in $\mathbb{R}^4$ with radius $r$ and set
of centres $C$, the region covered by $P$ is the union, over all centres $c \in C$, of the packed
closed balls $\{x \in \mathbb{R}^4 : \|x - c\| \le r\}$.

## Sources

- CE2003 Appendix A, the union `P` of all packed balls.

Formalized by `MathlibExt.Geometry.SpherePackingDensityFourWanted.packingRegion`, a definition declared in [MathlibExt/Geometry/SpherePackingDensityFour.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/SpherePackingDensityFour.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/sphere-packing-in-four-dimensions/index.html#packing-region).

## Density of a packing in a ball

For a packing $P$ of congruent balls in $\mathbb{R}^4$, a
point $p \in \mathbb{R}^4$ and a radius $R > 0$, the density of $P$ in the open ball $B(p, R)$ of
radius $R$ about $p$ is $\operatorname{vol}(U \cap B(p, R)) / \operatorname{vol}(B(p, R))$, where
$U$ is the union of the closed balls of $P$ and $\operatorname{vol}$ is Lebesgue measure; the
quotient is taken in $[0, \infty]$.

## Sources

- CE2003 Appendix A, `vol(P ∩ B(p,R)) / vol(B(p,R))`.

Formalized by `MathlibExt.Geometry.SpherePackingDensityFourWanted.finiteRadiusDensity`, a definition declared in [MathlibExt/Geometry/SpherePackingDensityFour.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/SpherePackingDensityFour.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/sphere-packing-in-four-dimensions/index.html#finite-radius-density).

## Density of a packing at a fixed radius

For a packing $P$ of congruent balls in
$\mathbb{R}^4$ and a radius $R > 0$, the density of $P$ at radius $R$ is the supremum, over all
centers $p \in \mathbb{R}^4$, of the density of $P$ in the open ball of radius $R$ about $p$;
it is a value in $[0, \infty]$.

## Sources

- CE2003 Appendix A, supremum over all observation centers at fixed radius.

Formalized by `MathlibExt.Geometry.SpherePackingDensityFourWanted.centeredRadiusDensity`, a definition declared in [MathlibExt/Geometry/SpherePackingDensityFour.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/SpherePackingDensityFour.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/sphere-packing-in-four-dimensions/index.html#centered-radius-density).

## Upper density of a packing

For a packing $P$ of congruent balls in $\mathbb{R}^4$, let
$U_P$ be the union of the closed balls of the packing, and for $p \in \mathbb{R}^4$ and $R > 0$ let
$B(p, R)$ be the open ball of radius $R$ about $p$. The upper density of $P$ is the extended
nonnegative real number

$$\limsup_{R \to \infty} \sup_{p \in \mathbb{R}^4}
\frac{\operatorname{vol}(U_P \cap B(p, R))}{\operatorname{vol}(B(p, R))},$$

where $\operatorname{vol}$ is Lebesgue measure and the limit superior is taken as the positive
radius $R$ tends to infinity.

## Sources

- CE2003 Appendix A, limsup as positive radii tend to infinity.

Formalized by `MathlibExt.Geometry.SpherePackingDensityFourWanted.upperDensity`, a definition declared in [MathlibExt/Geometry/SpherePackingDensityFour.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/SpherePackingDensityFour.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/sphere-packing-in-four-dimensions/index.html#upper-density).

## Sphere-packing density of $\mathbb{R}^4$

The sphere-packing density
$\Delta_4 \in [0, \infty]$ is the supremum, over all packings $P$ of congruent balls in
$\mathbb{R}^4$, of the upper density of $P$. Here the upper density of $P$ is the limit superior,
as the real radius $R > 0$ tends to infinity, of the supremum over all points
$p \in \mathbb{R}^4$ of the ratio of the volume of the part of the open ball $B(p, R)$ covered
by $P$ to the volume of $B(p, R)$.

## Sources

- catalogue C36, supremum over all congruent-ball packings in `ℝ⁴`.

Formalized by `MathlibExt.Geometry.SpherePackingDensityFourWanted.spherePackingDensity4`, a definition declared in [MathlibExt/Geometry/SpherePackingDensityFour.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/SpherePackingDensityFour.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/sphere-packing-in-four-dimensions/index.html#sphere-packing-density4).

## Volume of the unit ball in $\mathbb{R}^4$

The volume of the unit ball in $\mathbb{R}^4$ is
the Lebesgue measure, as an extended nonnegative real number, of the open ball of radius $1$ about
the origin in four-dimensional Euclidean space $\mathbb{R}^4$.

## Sources

- dLOV2014 Section 1.4, volume of a unit ball in `ℝ⁴`.

Formalized by `MathlibExt.Geometry.SpherePackingDensityFourWanted.unitBallVolume4`, a definition declared in [MathlibExt/Geometry/SpherePackingDensityFour.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/SpherePackingDensityFour.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/sphere-packing-in-four-dimensions/index.html#unit-ball-volume4).

## Center density in four dimensions

The center density of sphere packings in
$\mathbb{R}^4$ is $\delta_4 = \Delta_4 / \operatorname{vol}(B)$, where $\Delta_4$ is the
sphere-packing density of $\mathbb{R}^4$ and $B$ is the open unit ball of $\mathbb{R}^4$ centered
at the origin; the quotient is taken in $[0, \infty]$.

## Sources

- dLOV2014 Section 1.4, `δ₄ = Δ₄ / vol(B)` for unit spheres.

Formalized by `MathlibExt.Geometry.SpherePackingDensityFourWanted.centerDensity4`, a definition declared in [MathlibExt/Geometry/SpherePackingDensityFour.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/SpherePackingDensityFour.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/sphere-packing-in-four-dimensions/index.html#center-density4).

## Periodic packings

A packing $P$ of congruent balls in $\mathbb{R}^4$ is periodic if there
are a basis $b_1, b_2, b_3, b_4$ of $\mathbb{R}^4$ and a finite set $F \subseteq \mathbb{R}^4$ such
that the set of centers of $P$ equals $\{c + w : c \in F, w \in \Lambda\}$, where $\Lambda$ is the
set of integer linear combinations of $b_1, b_2, b_3, b_4$.

## Sources

- CE2003 introduction, finite union of translates of a full-rank lattice. The lattice is the integer span of a real basis, not an arbitrary periodicity oracle.

Formalized by `MathlibExt.Geometry.SpherePackingDensityFourWanted.Packing.IsPeriodic`, a definition declared in [MathlibExt/Geometry/SpherePackingDensityFour.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/SpherePackingDensityFour.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/sphere-packing-in-four-dimensions/index.html#is-periodic).

## Trivial upper bound for the sphere-packing density of $\mathbb{R}^4$

The trivial upper
bound is the statement that the sphere-packing density of $\mathbb{R}^4$ is at most $1$.

## Sources

- catalogue C36, trivial upper-bound row.

Formalized by `MathlibExt.Geometry.SpherePackingDensityFourWanted.upperBound_trivial`, a definition declared in [MathlibExt/Geometry/SpherePackingDensityFour.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/SpherePackingDensityFour.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/sphere-packing-in-four-dimensions/index.html#upper-bound-trivial).

## The trivial lower bound for the four-dimensional packing density

This is the statement
that the sphere-packing density $\Delta_4$ of $\mathbb{R}^4$ satisfies $0 \le \Delta_4$.

## Sources

- catalogue C36, trivial nonnegative lower-bound row.

Formalized by `MathlibExt.Geometry.SpherePackingDensityFourWanted.lowerBound_trivial`, a definition declared in [MathlibExt/Geometry/SpherePackingDensityFour.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/SpherePackingDensityFour.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/sphere-packing-in-four-dimensions/index.html#lower-bound-trivial).

## A packing has countably many centers

For every packing of congruent balls in
$\mathbb{R}^4$, the set of centers of its balls is countable.

## Sources

- packing admission conditions; disjoint nonempty open balls have countably many centers.

Formalized by `MathlibExt.Geometry.SpherePackingDensityFourWanted.centers_countable`, a theorem declared in [MathlibExt/Geometry/SpherePackingDensityFour.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/SpherePackingDensityFour.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/sphere-packing-in-four-dimensions/index.html#centers-countable).

## The region covered by a packing is measurable

For every packing $P$ in $\mathbb{R}^4$,
the region covered by $P$, the union of its packed closed balls, is a Borel set; in
particular it is Lebesgue measurable.

## Sources

- the covered region is Lebesgue measurable, without an extra packing restriction.

Formalized by `MathlibExt.Geometry.SpherePackingDensityFourWanted.packingRegion_measurable`, a theorem declared in [MathlibExt/Geometry/SpherePackingDensityFour.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/SpherePackingDensityFour.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/sphere-packing-in-four-dimensions/index.html#packing-region-measurable).

## Balls of positive radius in $\mathbb{R}^4$ have nonzero volume

For every point
$p \in \mathbb{R}^4$ and every real $R > 0$, the open ball of radius $R$ centred at $p$ has nonzero
Lebesgue measure.

## Sources

- positive observation radii give nonzero volume denominators.

Formalized by `MathlibExt.Geometry.SpherePackingDensityFourWanted.observationVolume_ne_zero`, a theorem declared in [MathlibExt/Geometry/SpherePackingDensityFour.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/SpherePackingDensityFour.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/sphere-packing-in-four-dimensions/index.html#observation-volume-ne-zero).

## Balls of positive radius in $\mathbb{R}^4$ have finite volume

For every point
$p \in \mathbb{R}^4$ and every real $R > 0$, the open ball of radius $R$ centred at $p$ has finite
Lebesgue measure.

## Sources

- every finite-radius observation ball has finite volume.

Formalized by `MathlibExt.Geometry.SpherePackingDensityFourWanted.observationVolume_ne_top`, a theorem declared in [MathlibExt/Geometry/SpherePackingDensityFour.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/SpherePackingDensityFour.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/sphere-packing-in-four-dimensions/index.html#observation-volume-ne-top).

## The density in a ball is at most one

For every packing $P$ of congruent balls in
$\mathbb{R}^4$, every point $p \in \mathbb{R}^4$ and every radius $R > 0$, the density of $P$ in
the open ball of radius $R$ about $p$ is at most $1$.

## Sources

- a covered-volume fraction cannot exceed one.

Formalized by `MathlibExt.Geometry.SpherePackingDensityFourWanted.finiteRadiusDensity_le_one`, a theorem declared in [MathlibExt/Geometry/SpherePackingDensityFour.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/SpherePackingDensityFour.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/sphere-packing-in-four-dimensions/index.html#finite-radius-density-le-one).

## The density at a fixed radius is at most one

For every packing $P$ of congruent balls
in $\mathbb{R}^4$ and every radius $R > 0$, the density of $P$ at radius $R$ (the supremum over
all centers $p \in \mathbb{R}^4$ of the density of $P$ in the open ball of radius $R$ about $p$)
is at most $1$.

## Sources

- taking the observation-center supremum preserves the bound by one.

Formalized by `MathlibExt.Geometry.SpherePackingDensityFourWanted.centeredRadiusDensity_le_one`, a theorem declared in [MathlibExt/Geometry/SpherePackingDensityFour.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/SpherePackingDensityFour.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/sphere-packing-in-four-dimensions/index.html#centered-radius-density-le-one).

## The upper density of a packing is at most one

For every packing $P$ of congruent balls in
$\mathbb{R}^4$, the upper density of $P$ is at most $1$.

## Sources

- taking the radius limsup preserves the bound by one.

Formalized by `MathlibExt.Geometry.SpherePackingDensityFourWanted.upperDensity_le_one`, a theorem declared in [MathlibExt/Geometry/SpherePackingDensityFour.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/SpherePackingDensityFour.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/sphere-packing-in-four-dimensions/index.html#upper-density-le-one).

## The sphere-packing density of $\mathbb{R}^4$ is at most one

The trivial upper bound holds:
the sphere-packing density of $\mathbb{R}^4$ is at most $1$.

## Sources

- catalogue C36 trivial upper bound, proved for the actual optimized constant.

Formalized by `MathlibExt.Geometry.SpherePackingDensityFourWanted.upperBound_trivial_proved`, a theorem declared in [MathlibExt/Geometry/SpherePackingDensityFour.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/SpherePackingDensityFour.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/sphere-packing-in-four-dimensions/index.html#upper-bound-trivial-proved).

## The four-dimensional packing density is nonnegative

The trivial lower bound holds: the
sphere-packing density $\Delta_4$ of $\mathbb{R}^4$ satisfies $0 \le \Delta_4$.

## Sources

- catalogue C36 trivial lower bound, proved in the measure codomain.

Formalized by `MathlibExt.Geometry.SpherePackingDensityFourWanted.lowerBound_trivial_proved`, a theorem declared in [MathlibExt/Geometry/SpherePackingDensityFour.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/SpherePackingDensityFour.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/sphere-packing-in-four-dimensions/index.html#lower-bound-trivial-proved).

## The unit ball in $\mathbb{R}^4$ has volume $\pi^2/2$

The Lebesgue measure of the open unit
ball centred at the origin of $\mathbb{R}^4$ equals $\pi^2/2$.

## Sources

- the standard four-dimensional unit-ball volume `π²/2`.

Formalized by `MathlibExt.Geometry.SpherePackingDensityFourWanted.unitBallVolume4_eq`, a theorem declared in [MathlibExt/Geometry/SpherePackingDensityFour.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/SpherePackingDensityFour.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/sphere-packing-in-four-dimensions/index.html#unit-ball-volume4-eq).

## The unit ball in $\mathbb{R}^4$ has nonzero volume

The Lebesgue volume of the open unit
ball of radius $1$ about the origin in $\mathbb{R}^4$ is not $0$.

## Sources

- the center-density divisor is nonzero.

Formalized by `MathlibExt.Geometry.SpherePackingDensityFourWanted.unitBallVolume4_ne_zero`, a theorem declared in [MathlibExt/Geometry/SpherePackingDensityFour.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/SpherePackingDensityFour.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/sphere-packing-in-four-dimensions/index.html#unit-ball-volume4-ne-zero).

## The unit ball in $\mathbb{R}^4$ has finite volume

The Lebesgue volume of the open unit
ball of radius $1$ about the origin in $\mathbb{R}^4$ is not $\infty$.

## Sources

- the center-density divisor is finite.

Formalized by `MathlibExt.Geometry.SpherePackingDensityFourWanted.unitBallVolume4_ne_top`, a theorem declared in [MathlibExt/Geometry/SpherePackingDensityFour.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/SpherePackingDensityFour.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/sphere-packing-in-four-dimensions/index.html#unit-ball-volume4-ne-top).

## Center-density upper bounds as packing-density upper bounds

For every real number
$a \ge 0$, the center density $\delta_4$ of sphere packings in $\mathbb{R}^4$ is at most $a$ if
and only if the sphere-packing density $\Delta_4$ of $\mathbb{R}^4$ is at most $\pi^2 a / 2$.

## Sources

- exact conversion between a nonnegative center-density upper bound and its `π²/2`-scaled volume-density bound.

Formalized by `MathlibExt.Geometry.SpherePackingDensityFourWanted.centerDensity_upper_iff`, a theorem declared in [MathlibExt/Geometry/SpherePackingDensityFour.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/SpherePackingDensityFour.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/sphere-packing-in-four-dimensions/index.html#center-density-upper-iff).

## Statement that periodic packings approach the optimal density in dimension four

For a
packing $Q$ of congruent balls in $\mathbb{R}^4$, let its upper density $\overline{\delta}(Q)$ be
the limit superior, as $R \to \infty$, of the supremum over all points $p$ of the fraction of the
volume of the open ball $B(p, R)$ covered by the closed balls of $Q$, and let the sphere packing
density $\Delta_4$ of $\mathbb{R}^4$ be the supremum of $\overline{\delta}(Q)$ over all such
packings $Q$. This is the proposition that for every real $\varepsilon > 0$ there is a periodic
packing $P$ of congruent balls in $\mathbb{R}^4$, meaning that its set of centers is a finite
union of translates of the lattice $\mathbb{Z}b_1 + \mathbb{Z}b_2 + \mathbb{Z}b_3 + \mathbb{Z}b_4$
for some basis $b_1, \dots, b_4$ of $\mathbb{R}^4$, such that
$\Delta_4 \le \overline{\delta}(P) + \varepsilon$.

## Sources

- CE2003 introduction and Appendix A, periodic packings come arbitrarily close to the greatest density. Positive error does not assert attainment.

Formalized by `MathlibExt.Geometry.SpherePackingDensityFourWanted.periodicApproximation`, a definition declared in [WantedExt/Geometry/SpherePackingDensityFourWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/SpherePackingDensityFourWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/sphere-packing-in-four-dimensions/index.html#periodic-approximation).

## Statement of the Rogers upper bound in dimension four

The proposition that the sphere
packing density $\Delta_4$ of $\mathbb{R}^4$, the supremum of the upper densities of all packings
of congruent balls in $\mathbb{R}^4$, satisfies
$\Delta_4 \le \frac{\pi^2}{2} \cdot \frac{13127}{100000}$.

## Sources

- CE2003 Table 3, Rogers center-density upper bound `0.13127`, converted exactly; displayed `0.647791…` is only an approximation.

Formalized by `MathlibExt.Geometry.SpherePackingDensityFourWanted.upperBound_CE2003_Rogers`, a definition declared in [WantedExt/Geometry/SpherePackingDensityFourWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/SpherePackingDensityFourWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/sphere-packing-in-four-dimensions/index.html#upper-bound-ce2003-rogers).

## Statement of the Cohn–Elkies upper bound in dimension four

The proposition that the
sphere packing density $\Delta_4$ of $\mathbb{R}^4$, the supremum of the upper densities of all
packings of congruent balls in $\mathbb{R}^4$, satisfies
$\Delta_4 \le \frac{\pi^2}{2} \cdot \frac{13126}{100000}$.

## Sources

- CE2003 Table 3, new center-density upper bound `0.13126`, converted exactly; displayed `0.647742…` is only an approximation.

Formalized by `MathlibExt.Geometry.SpherePackingDensityFourWanted.upperBound_CE2003_new`, a definition declared in [WantedExt/Geometry/SpherePackingDensityFourWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/SpherePackingDensityFourWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/sphere-packing-in-four-dimensions/index.html#upper-bound-ce2003-new).

## Statement of the de Laat–Oliveira–Vallentin upper bound in dimension four

The
proposition that the sphere packing density $\Delta_4$ of $\mathbb{R}^4$, the supremum of the
upper densities of all packings of congruent balls in $\mathbb{R}^4$, satisfies
$\Delta_4 \le \frac{\pi^2}{2} \cdot \frac{130587}{1000000}$.

## Sources

- dLOV2014 Table 1, center-density upper bound `0.130587`, converted exactly; displayed `0.644421…` is only an approximation.

Formalized by `MathlibExt.Geometry.SpherePackingDensityFourWanted.upperBound_dLOV2014`, a definition declared in [WantedExt/Geometry/SpherePackingDensityFourWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/SpherePackingDensityFourWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/sphere-packing-in-four-dimensions/index.html#upper-bound-d-lov2014).

## Statement of the lower bound for sphere packing in dimension four

The proposition that
the sphere packing density $\Delta_4$ of $\mathbb{R}^4$, the supremum of the upper densities of
all packings of congruent balls in $\mathbb{R}^4$, satisfies $\frac{\pi^2}{16} \le \Delta_4$.

## Sources

- dLOV2014 Table 1, center-density lower bound `0.12500 = 1/8`, converted exactly to `π²/16`; `0.616850` is only an approximation.

Formalized by `MathlibExt.Geometry.SpherePackingDensityFourWanted.lowerBound_dLOV2014`, a definition declared in [WantedExt/Geometry/SpherePackingDensityFourWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/SpherePackingDensityFourWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/sphere-packing-in-four-dimensions/index.html#lower-bound-d-lov2014).

## Rogers upper bound for sphere packing in dimension four

The sphere packing density
$\Delta_4$ of $\mathbb{R}^4$, the supremum of the upper densities of all packings of congruent
balls in $\mathbb{R}^4$, satisfies $\Delta_4 \le \frac{\pi^2}{2} \cdot \frac{13127}{100000}$.

## Sources

- CE2003 Table 3. Known literature bound; no Lean proof supplied.

Stated but not proved: `MathlibExt.Geometry.SpherePackingDensityFourWanted.upperBound_CE2003_Rogers_wanted` is written with `theorem_wanted` in [WantedExt/Geometry/SpherePackingDensityFourWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/SpherePackingDensityFourWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/sphere-packing-in-four-dimensions/index.html#upper-bound-ce2003-rogers-wanted).

## Cohn–Elkies upper bound for sphere packing in dimension four

The sphere packing density
$\Delta_4$ of $\mathbb{R}^4$, the supremum of the upper densities of all packings of congruent
balls in $\mathbb{R}^4$, satisfies $\Delta_4 \le \frac{\pi^2}{2} \cdot \frac{13126}{100000}$.

## Sources

- CE2003 Table 3. Known literature bound; no Lean proof supplied.

Stated but not proved: `MathlibExt.Geometry.SpherePackingDensityFourWanted.upperBound_CE2003_new_wanted` is written with `theorem_wanted` in [WantedExt/Geometry/SpherePackingDensityFourWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/SpherePackingDensityFourWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/sphere-packing-in-four-dimensions/index.html#upper-bound-ce2003-new-wanted).

## de Laat–Oliveira–Vallentin upper bound for sphere packing in dimension four

The sphere
packing density $\Delta_4$ of $\mathbb{R}^4$, the supremum of the upper densities of all packings
of congruent balls in $\mathbb{R}^4$, satisfies
$\Delta_4 \le \frac{\pi^2}{2} \cdot \frac{130587}{1000000}$.

## Sources

- dLOV2014 Table 1. Known literature bound; no Lean proof supplied.

Stated but not proved: `MathlibExt.Geometry.SpherePackingDensityFourWanted.upperBound_dLOV2014_wanted` is written with `theorem_wanted` in [WantedExt/Geometry/SpherePackingDensityFourWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/SpherePackingDensityFourWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/sphere-packing-in-four-dimensions/index.html#upper-bound-d-lov2014-wanted).

## Lower bound for sphere packing in dimension four

The sphere packing density $\Delta_4$
of $\mathbb{R}^4$, the supremum of the upper densities of all packings of congruent balls in
$\mathbb{R}^4$, satisfies $\frac{\pi^2}{16} \le \Delta_4$.

## Sources

- dLOV2014 Table 1. Known literature bound; no Lean proof supplied.

Stated but not proved: `MathlibExt.Geometry.SpherePackingDensityFourWanted.lowerBound_dLOV2014_wanted` is written with `theorem_wanted` in [WantedExt/Geometry/SpherePackingDensityFourWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/SpherePackingDensityFourWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/sphere-packing-in-four-dimensions/index.html#lower-bound-d-lov2014-wanted).

## Periodic packings approach the optimal density in dimension four

For a packing $Q$ of
congruent balls in $\mathbb{R}^4$, let its upper density $\overline{\delta}(Q)$ be the limit
superior, as $R \to \infty$, of the supremum over all points $p$ of the fraction of the volume of
the open ball $B(p, R)$ covered by the closed balls of $Q$, and let the sphere packing density
$\Delta_4$ of $\mathbb{R}^4$ be the supremum of $\overline{\delta}(Q)$ over all such packings $Q$.
Then for every real $\varepsilon > 0$ there is a periodic packing $P$ of congruent balls in
$\mathbb{R}^4$, meaning that its set of centers is a finite union of translates of the lattice
$\mathbb{Z}b_1 + \mathbb{Z}b_2 + \mathbb{Z}b_3 + \mathbb{Z}b_4$ for some basis $b_1, \dots, b_4$ of
$\mathbb{R}^4$, such that $\Delta_4 \le \overline{\delta}(P) + \varepsilon$.

## Sources

- CE2003 introduction and Appendix A. Known periodic approximation; no Lean proof supplied and no exact optimum-attainment claim.

Stated but not proved: `MathlibExt.Geometry.SpherePackingDensityFourWanted.periodicApproximation_wanted` is written with `theorem_wanted` in [WantedExt/Geometry/SpherePackingDensityFourWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/SpherePackingDensityFourWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/sphere-packing-in-four-dimensions/index.html#periodic-approximation-wanted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sphere packing in four dimensions](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/sphere-packing-in-four-dimensions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Geometry/packings-and-coverings/sphere-packing-in-four-dimensions)
