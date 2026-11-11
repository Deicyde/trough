---
declaration: section
origin: cited
lean: MoserConvexWormCoverConstant.ArcParameter, MoserConvexWormCoverConstant.UnitArc, MoserConvexWormCoverConstant.move, MoserConvexWormCoverConstant.move_isometry, MoserConvexWormCoverConstant.straightPath, MoserConvexWormCoverConstant.parameter_variation, MoserConvexWormCoverConstant.straightPath_length, MoserConvexWormCoverConstant.straightUnitArc
statement: formalized
---

# Moser's worm problem

76 results, 56 proved and 20 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html).

## Parameter interval of unit arcs

Planar arcs are parametrized by the closed unit interval
$[0, 1]$ of real numbers.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.ArcParameter`, an abbreviation declared in [MathlibExt/Geometry/MoserWormCover.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MoserWormCover.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#arc-parameter).

## Unit arc

A unit arc is a continuous map $\gamma$ from the closed interval $[0, 1]$ to
the complex plane whose length, the total variation of $\gamma$ on $[0, 1]$, equals $1$.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.UnitArc`, a structure declared in [MathlibExt/Geometry/MoserWormCover.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MoserWormCover.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#unit-arc).

## Direct rigid motion of the plane

For a real angle $\theta$ and a complex number
$\tau$, the motion with angle $\theta$ and translation $\tau$ sends $z \in \mathbb{C}$ to
$e^{i\theta} z + \tau$: a rotation about the origin by $\theta$ followed by translation by
$\tau$, with neither reflection nor rescaling.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.move`, a definition declared in [MathlibExt/Geometry/MoserWormCover.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MoserWormCover.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#move).

## Direct rigid motions of the plane are isometries

For every real angle $\theta$ and every
complex number $\tau$, the map $z \mapsto e^{i\theta} z + \tau$ of the complex plane is an
isometry: it preserves the distance $|z - w|$ between any two points $z, w \in \mathbb{C}$.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.move_isometry`, a theorem declared in [MathlibExt/Geometry/MoserWormCover.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MoserWormCover.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#move-isometry).

## Straight path

The straight path is the continuous map from the interval $[0, 1]$ to
the complex plane that sends each $t \in [0, 1]$ to $t$ viewed as a complex number; it traces
the segment from $0$ to $1$.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.straightPath`, a definition declared in [MathlibExt/Geometry/MoserWormCover.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MoserWormCover.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#straight-path).

## The identity on the unit interval has total variation one

The total variation of the
inclusion $[0, 1] \to \mathbb{R}$, $t \mapsto t$, over the whole interval $[0, 1]$ equals $1$.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.parameter_variation`, a theorem declared in [MathlibExt/Geometry/MoserWormCover.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MoserWormCover.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#parameter-variation).

## The straight segment has length one

The path $[0, 1] \to \mathbb{C}$, $t \mapsto t$,
which traces the segment from $0$ to $1$ on the real axis, has total variation (length) exactly
$1$ over $[0, 1]$.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.straightPath_length`, a theorem declared in [MathlibExt/Geometry/MoserWormCover.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MoserWormCover.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#straight-path-length).

## Straight unit arc

The straight unit arc is the unit arc whose curve is the straight
path $t \mapsto t$ from $[0, 1]$ to the complex plane, which traces the segment from $0$ to $1$
and has length $1$.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.straightUnitArc`, a definition declared in [MathlibExt/Geometry/MoserWormCover.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MoserWormCover.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#straight-unit-arc).

## Sets that cover every unit arc

A set $\Omega \subseteq \mathbb{C}$ covers every
unit arc when for every unit arc $\gamma : [0, 1] \to \mathbb{C}$, that is, every continuous map
whose total variation (length) is exactly $1$, there are an angle $\theta \in \mathbb{R}$ and a
translation $\tau \in \mathbb{C}$ such that $e^{i\theta} \gamma(t) + \tau \in \Omega$ for every
$t \in [0, 1]$.

Only rotations followed by translations are allowed; reflections and rescalings are not.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.CoversEveryUnitArc`, a definition declared in [MathlibExt/Geometry/MoserWormCover.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MoserWormCover.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#covers-every-unit-arc).

## Sets covering every unit arc are nonempty

If a set $\Omega \subseteq \mathbb{C}$
covers every unit arc, that is, contains a rotated and translated copy of every continuous curve
$[0, 1] \to \mathbb{C}$ of length exactly one, then $\Omega$ is nonempty.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.CoversEveryUnitArc.nonempty`, a theorem declared in [MathlibExt/Geometry/MoserWormCover.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MoserWormCover.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#nonempty).

## The empty set does not cover every unit arc

The empty set
$\emptyset \subseteq \mathbb{C}$ does not cover every unit arc: not every continuous curve
$\gamma : [0, 1] \to \mathbb{C}$ of length exactly $1$ can be mapped into $\emptyset$ by a
rotation followed by a translation.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.empty_not_covers`, a theorem declared in [MathlibExt/Geometry/MoserWormCover.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MoserWormCover.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#empty-not-covers).

## Convex universal covers

A set $\Omega \subseteq \mathbb{C}$ is a convex universal cover
when it is nonempty, convex (as a subset of the real plane $\mathbb{C} \cong \mathbb{R}^2$), and
covers every unit arc: for every continuous curve $\gamma : [0, 1] \to \mathbb{C}$ of length
exactly $1$ there are $\theta \in \mathbb{R}$ and $\tau \in \mathbb{C}$ with
$e^{i\theta} \gamma(t) + \tau \in \Omega$ for all $t \in [0, 1]$.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.IsConvexUniversalCover`, a definition declared in [MathlibExt/Geometry/MoserWormCover.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MoserWormCover.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#is-convex-universal-cover).

## Universal covers

A set $\Omega \subseteq \mathbb{C}$ is a universal cover when it is
nonempty and covers every unit arc: for every continuous curve $\gamma : [0, 1] \to \mathbb{C}$
of length exactly $1$ there are $\theta \in \mathbb{R}$ and $\tau \in \mathbb{C}$ with
$e^{i\theta} \gamma(t) + \tau \in \Omega$ for all $t \in [0, 1]$. Neither convexity nor
measurability of $\Omega$ is required.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.IsUniversalCover`, a definition declared in [MathlibExt/Geometry/MoserWormCover.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MoserWormCover.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#is-universal-cover).

## Convex universal covers are null-measurable

If $\Omega \subseteq \mathbb{C}$ is a
convex universal cover of unit arcs, then $\Omega$ is a null-measurable set for Lebesgue measure
on $\mathbb{C}$.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.IsConvexUniversalCover.nullMeasurableSet`, a theorem declared in [MathlibExt/Geometry/MoserWormCover.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MoserWormCover.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#null-measurable-set).

## Convex universal covers are universal covers

Every convex universal cover
$\Omega \subseteq \mathbb{C}$ is a universal cover.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.IsConvexUniversalCover.isUniversalCover`, a theorem declared in [MathlibExt/Geometry/MoserWormCover.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MoserWormCover.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#is-universal-cover-2).

## Areas of convex universal covers

The set of convex cover areas is the set of all values
$\operatorname{vol}(\Omega) \in [0, \infty]$, where $\Omega \subseteq \mathbb{C}$ ranges over the
convex universal covers and $\operatorname{vol}$ is Lebesgue measure on
$\mathbb{C} \cong \mathbb{R}^2$.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.convexCoverAreas`, a definition declared in [MathlibExt/Geometry/MoserWormCover.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MoserWormCover.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#convex-cover-areas).

## Areas of universal covers

The set of values $\lambda(\Omega) \in [0, \infty]$, where
$\Omega \subseteq \mathbb{C}$ ranges over the universal covers and $\lambda$ is Lebesgue measure on
$\mathbb{C} \cong \mathbb{R}^2$, applied as an outer measure since $\Omega$ need not be
measurable.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.coverAreas`, a definition declared in [MathlibExt/Geometry/MoserWormCover.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MoserWormCover.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#cover-areas).

## Infimal area of convex universal covers

The convex cover area infimum is the infimum in
$[0, \infty]$ of the set of convex cover areas, that is, the infimum of the Lebesgue areas of all
convex universal covers $\Omega \subseteq \mathbb{C}$.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.convexCoverAreaInfimum`, a definition declared in [MathlibExt/Geometry/MoserWormCover.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MoserWormCover.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#convex-cover-area-infimum).

## Infimal area of a universal cover

The infimum in $[0, \infty]$ of the areas
$\lambda(\Omega)$ of the universal covers $\Omega \subseteq \mathbb{C}$, where $\lambda$ is
Lebesgue measure on $\mathbb{C} \cong \mathbb{R}^2$, applied as an outer measure since $\Omega$
need not be measurable.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.coverAreaInfimum`, a definition declared in [MathlibExt/Geometry/MoserWormCover.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MoserWormCover.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#cover-area-infimum).

## The closed unit disk covers every unit arc

For every continuous curve
$\gamma : [0, 1] \to \mathbb{C}$ of length exactly $1$ there are an angle $\theta \in \mathbb{R}$
and a translation $c \in \mathbb{C}$ such that $|e^{i\theta}\gamma(t) + c| \le 1$ for every
$t \in [0, 1]$; that is, the closed disk of radius $1$ centred at $0$ covers every unit arc.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.closedBall_one_covers`, a theorem declared in [MathlibExt/Geometry/MoserWormCover.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MoserWormCover.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#closed-ball-one-covers).

## The closed unit disk is a convex universal cover

The closed disk
$\{z \in \mathbb{C} : |z| \le 1\}$ is a convex universal cover: it is nonempty, convex, and covers
every unit arc.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.closedBall_one_isConvexUniversalCover`, a theorem declared in [MathlibExt/Geometry/MoserWormCover.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MoserWormCover.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#closed-ball-one-is-convex-universal-cove).

## The set of convex cover areas is nonempty

The set of convex cover areas, the Lebesgue
areas of all convex universal covers in $\mathbb{C}$, is nonempty; that is, some convex universal
cover exists.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.convexCoverAreas_nonempty`, a theorem declared in [MathlibExt/Geometry/MoserWormCover.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MoserWormCover.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#convex-cover-areas-nonempty).

## The set of universal cover areas is nonempty

The set of values
$\lambda(\Omega) \in [0, \infty]$, where $\Omega \subseteq \mathbb{C}$ ranges over the universal
covers and $\lambda$ is Lebesgue outer measure on $\mathbb{C} \cong \mathbb{R}^2$, is nonempty.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.coverAreas_nonempty`, a theorem declared in [MathlibExt/Geometry/MoserWormCover.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MoserWormCover.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#cover-areas-nonempty).

## The infimal area of convex universal covers is finite

The convex cover area infimum, the
infimum in $[0, \infty]$ of the Lebesgue areas of all convex universal covers in $\mathbb{C}$, is
not $\infty$.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.convexCoverAreaInfimum_ne_top`, a theorem declared in [MathlibExt/Geometry/MoserWormCover.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MoserWormCover.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#convex-cover-area-infimum-ne-top).

## The infimal area of universal covers is finite

The cover area infimum, the infimum in
$[0, \infty]$ of the Lebesgue areas of all universal covers in $\mathbb{C}$ (nonempty sets that
cover every unit arc, not necessarily convex), is not $\infty$.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.coverAreaInfimum_ne_top`, a theorem declared in [MathlibExt/Geometry/MoserWormCover.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MoserWormCover.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#cover-area-infimum-ne-top).

## Moser's convex worm cover constant

The convex worm cover constant is the real number
obtained from the convex cover area infimum, the infimum in $[0, \infty]$ of the Lebesgue areas of
all convex universal covers in $\mathbb{C}$, by the conversion $[0, \infty] \to \mathbb{R}$ that
is the identity on finite values and sends $\infty$ to $0$.

That infimum is finite, so the constant equals the infimal area itself.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.convexWormCoverConstant`, a definition declared in [MathlibExt/Geometry/MoserWormCover.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MoserWormCover.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#convex-worm-cover-constant).

## Nonconvex worm cover constant

The nonconvex worm cover constant is the real number
obtained from the cover area infimum, the infimum in $[0, \infty]$ of the Lebesgue outer measures
of all universal covers of unit arcs (nonempty sets $\Omega \subseteq \mathbb{C}$ containing a
rotated and translated copy of every continuous curve of length one), by converting it to a
real number. The conversion would send $\infty$ to $0$, but this infimum is finite.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.nonconvexWormCoverConstant`, a definition declared in [MathlibExt/Geometry/MoserWormCover.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MoserWormCover.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#nonconvex-worm-cover-constant).

## The convex worm cover constant is nonnegative

The convex worm cover constant is at
least $0$.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.convexWormCoverConstant_nonneg`, a theorem declared in [MathlibExt/Geometry/MoserWormCover.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MoserWormCover.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#convex-worm-cover-constant-nonneg).

## Nonnegativity of the nonconvex worm cover constant

The nonconvex worm cover constant
is greater than or equal to $0$.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.nonconvexWormCoverConstant_nonneg`, a theorem declared in [MathlibExt/Geometry/MoserWormCover.lean, line 254](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MoserWormCover.lean#L254). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#nonconvex-worm-cover-constant-nonneg).

## The nonconvex worm cover constant is at most the convex one

The nonconvex worm cover
constant (the infimal area of universal covers of unit arcs) is less than or equal to the convex
worm cover constant (the infimal area of convex universal covers of unit arcs).

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.nonconvex_le_convex`, a theorem declared in [MathlibExt/Geometry/MoserWormCover.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MoserWormCover.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#nonconvex-le-convex).

## Disk of radius one half

The closed disk $\{z \in \mathbb{C} : |z| \le 1/2\}$ of
radius $1/2$ centred at $0$.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.halfDisk`, a definition declared in [MathlibExt/Geometry/MoserWormCover.lean, line 269](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MoserWormCover.lean#L269). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#half-disk).

## Semidisk of radius one half

The closed upper half-disk
$\{z \in \mathbb{C} : |z| \le 1/2,\ \operatorname{Im} z \ge 0\}$ of radius $1/2$ centred at $0$.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.halfSemidisk`, a definition declared in [MathlibExt/Geometry/MoserWormCover.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MoserWormCover.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#half-semidisk).

## Wetzel's sector

This is the closed circular sector of radius $1$ and opening angle
$30^\circ$ with apex at the origin, placed symmetrically about the positive real axis: the set
of complex numbers $z$ with $|z| \le 1$, $\operatorname{Re} z \ge 0$ and
$|\operatorname{Im} z| \le \tan(\pi/12) \operatorname{Re} z$.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.wetzelSector`, a definition declared in [MathlibExt/Geometry/MoserWormCover.lean, line 281](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MoserWormCover.lean#L281). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#wetzel-sector).

## Covers give upper bounds on the nonconvex worm cover constant

Let $r \ge 0$ be a real
number. If some set $\Omega \subseteq \mathbb{C}$ is a universal cover of unit arcs whose
Lebesgue outer measure is at most $r$, then the nonconvex worm cover constant is at most $r$.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.nonconvexUpperBound_of_cover`, a theorem declared in [MathlibExt/Geometry/MoserWormCover.lean, line 287](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MoserWormCover.lean#L287). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#nonconvex-upper-bound-of-cover).

## Proposition: the convex worm cover constant is at most π/4

A unit arc is a
continuous curve $\gamma : [0, 1] \to \mathbb{C}$ of length exactly $1$. The convex worm cover
constant is the infimum of the areas of the nonempty convex sets $\Omega \subseteq \mathbb{C}$
that contain, for every unit arc $\gamma$, the image of $\gamma$ under some rotation followed by
a translation. This proposition states that the convex worm cover constant is at most $\pi/4$.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.upperBoundPiOverFour`, a definition declared in [WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#upper-bound-pi-over-four).

## Proposition: the convex worm cover constant is at most π/8

A unit arc is a
continuous curve $\gamma : [0, 1] \to \mathbb{C}$ of length exactly $1$. The convex worm cover
constant is the infimum of the areas of the nonempty convex sets $\Omega \subseteq \mathbb{C}$
that contain, for every unit arc $\gamma$, the image of $\gamma$ under some rotation followed by
a translation. This proposition states that the convex worm cover constant is at most $\pi/8$.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.upperBoundPiOverEight`, a definition declared in [WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#upper-bound-pi-over-eight).

## Proposition: the convex worm cover constant is at most 0.34501

A unit arc is a
continuous curve $\gamma : [0, 1] \to \mathbb{C}$ of length exactly $1$. The convex worm cover
constant is the infimum of the areas of the nonempty convex sets $\Omega \subseteq \mathbb{C}$
that contain, for every unit arc $\gamma$, the image of $\gamma$ under some rotation followed by
a translation. This proposition states that the convex worm cover constant is at most $0.34501$.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.upperBoundWetzel1973`, a definition declared in [WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#upper-bound-wetzel1973).

## Statement of Gerriets' upper bound $0.3214$ for convex worm covers

The proposition that
Moser's convex worm cover constant, the infimum of the areas of convex planar sets containing a
rotated and translated copy of every planar curve of length $1$, is at most $0.3214$.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.upperBoundGerriets1972`, a definition declared in [WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#upper-bound-gerriets1972).

## Statement of the Gerriets–Poole upper bound $0.2861$ for convex worm covers

The
proposition that Moser's convex worm cover constant, the infimum of the areas of convex planar
sets containing a rotated and translated copy of every planar curve of length $1$, is at most
$0.2861$.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.upperBoundGerrietsPoole1974`, a definition declared in [WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#upper-bound-gerriets-poole1974).

## Statement of the Norwood–Poole–Laidacker upper bound $0.27524$ for convex worm covers

The
proposition that Moser's convex worm cover constant, the infimum of the areas of convex planar
sets containing a rotated and translated copy of every planar curve of length $1$, is at most
$0.27524$.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.upperBoundNorwoodPooleLaidacker1992`, a definition declared in [WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#upper-bound-norwood-poole-laidacker1992).

## Proposition: the convex worm cover constant is at most 0.270911861

A unit arc is a
continuous curve $\gamma : [0, 1] \to \mathbb{C}$ of length exactly $1$. The convex worm cover
constant is the infimum of the areas of the nonempty convex sets $\Omega \subseteq \mathbb{C}$
that contain, for every unit arc $\gamma$, the image of $\gamma$ under some rotation followed by
a translation. This proposition states that the convex worm cover constant is at most
$0.270911861$.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.upperBoundWang2006`, a definition declared in [WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#upper-bound-wang2006).

## Proposition: the convex worm cover constant is at most π/12

A unit arc is a
continuous curve $\gamma : [0, 1] \to \mathbb{C}$ of length exactly $1$. The convex worm cover
constant is the infimum of the areas of the nonempty convex sets $\Omega \subseteq \mathbb{C}$
that contain, for every unit arc $\gamma$, the image of $\gamma$ under some rotation followed by
a translation. This proposition states that the convex worm cover constant is at most $\pi/12$.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.upperBoundPiOverTwelve`, a definition declared in [WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#upper-bound-pi-over-twelve).

## Wetzel's 1973 lower bound for the convex worm cover constant (claim)

This proposition
asserts that $0.2194 \le \mu$, where $\mu$ is the convex worm cover constant: the infimum of the
areas of the nonempty convex sets $\Omega \subseteq \mathbb{C}$ such that every continuous curve
$\gamma : [0, 1] \to \mathbb{C}$ of length exactly $1$ can be moved into $\Omega$ by a rotation
followed by a translation.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.lowerBoundWetzel1973`, a definition declared in [WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#lower-bound-wetzel1973).

## Khandhawit–Sriswasdi 2009 lower bound for the convex worm cover constant (claim)

This
proposition asserts that $0.227498 \le \mu$, where $\mu$ is the convex worm cover constant: the
infimum of the areas of the nonempty convex sets $\Omega \subseteq \mathbb{C}$ such that every
continuous curve $\gamma : [0, 1] \to \mathbb{C}$ of length exactly $1$ can be moved into $\Omega$
by a rotation followed by a translation.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.lowerBoundKhandhawitSriswasdi2009`, a definition declared in [WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#lower-bound-khandhawit-sriswasdi2009).

## Khandhawit–Pagonakis–Sriswasdi 2013 lower bound on the convex worm cover constant (claim)

This proposition asserts that $0.232239 \le \mu$, where $\mu$ is the convex worm cover constant:
the infimum of the areas of the nonempty convex sets $\Omega \subseteq \mathbb{C}$ such that every
continuous curve $\gamma : [0, 1] \to \mathbb{C}$ of length exactly $1$ can be moved into $\Omega$
by a rotation followed by a translation.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.lowerBoundKhandhawitPagonakisSriswasdi2013`, a definition declared in [WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#lower-bound-khandhawit-pagonakis-sriswas).

## The minimal-convex-cover claim

Call a nonempty convex set $\Omega \subseteq \mathbb{C}$ a
convex universal cover if every continuous curve $\gamma : [0, 1] \to \mathbb{C}$ of length
exactly $1$ can be moved into $\Omega$ by some rotation followed by a translation, and let the
convex worm cover constant be the infimum of the areas (Lebesgue measures) of all convex
universal covers, which is a finite real number. This is the proposition that some convex
universal cover has area equal to the convex worm cover constant.

Attainment of the minimum is a claim to be proved; it is not built into the definition of the
constant.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.minimalConvexCoverExists`, a definition declared in [WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#minimal-convex-cover-exists).

## The Norwood–Poole cover claim

Call a nonempty set $\Omega \subseteq \mathbb{C}$ a
universal cover if every continuous curve $\gamma : [0, 1] \to \mathbb{C}$ of length exactly $1$
can be moved into $\Omega$ by some rotation followed by a translation. This is the proposition
that some universal cover has area (Lebesgue outer measure) at most $0.260437$.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.nonconvexCoverNorwoodPoole2003`, a definition declared in [WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#nonconvex-cover-norwood-poole2003).

## The Ploymaklam–Wichiramala cover claim

Call a nonempty set $\Omega \subseteq \mathbb{C}$
a universal cover if every continuous curve $\gamma : [0, 1] \to \mathbb{C}$ of length exactly
$1$ can be moved into $\Omega$ by some rotation followed by a translation. This is the
proposition that some universal cover has area (Lebesgue outer measure) at most $0.26007$.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.nonconvexCoverPloymaklamWichiramala2018`, a definition declared in [WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#nonconvex-cover-ploymaklam-wichiramala20).

## Statement of the Norwood–Poole upper bound $0.260437$ for worm covers

The proposition
that the nonconvex worm cover constant, the infimum of the areas (Lebesgue outer measures) of
planar sets containing a rotated and translated copy of every planar curve of length $1$, is at
most $0.260437$.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.nonconvexUpperBoundNorwoodPoole2003`, a definition declared in [WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#nonconvex-upper-bound-norwood-poole2003).

## Statement of the Ploymaklam–Wichiramala upper bound $0.26007$ for worm covers

The
proposition that the nonconvex worm cover constant, the infimum of the areas (Lebesgue outer
measures) of planar sets containing a rotated and translated copy of every planar curve of length
$1$, is at most $0.26007$.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.nonconvexUpperBoundPloymaklamWichiramala2018`, a definition declared in [WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#nonconvex-upper-bound-ploymaklam-wichira).

## The positivity claim for the nonconvex worm cover constant

Call a nonempty set
$\Omega \subseteq \mathbb{C}$ a universal cover if every continuous curve
$\gamma : [0, 1] \to \mathbb{C}$ of length exactly $1$ can be moved into $\Omega$ by some rotation
followed by a translation, and let the nonconvex worm cover constant be the infimum of the areas
(Lebesgue outer measures) of all universal covers, which is a finite real number. This is the
proposition that the nonconvex worm cover constant is strictly positive.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.nonconvexStrictPositivity`, a definition declared in [WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#nonconvex-strict-positivity).

## The disk of diameter one covers every unit arc (claim)

This proposition asserts that
the closed disk $D = \{z \in \mathbb{C} : |z| \le 1/2\}$ covers every unit arc: for every
continuous curve $\gamma : [0, 1] \to \mathbb{C}$ of length exactly $1$ there are an angle
$\theta \in \mathbb{R}$ and a translation $c \in \mathbb{C}$ such that
$e^{i\theta}\gamma(t) + c \in D$ for every $t \in [0, 1]$.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.halfDiskCovers`, a definition declared in [WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#half-disk-covers).

## The half-disk of diameter one covers every unit arc (claim)

This proposition asserts
that the closed half-disk $H = \{z \in \mathbb{C} : |z| \le 1/2,\ \operatorname{Im} z \ge 0\}$
covers every unit arc: for every continuous curve $\gamma : [0, 1] \to \mathbb{C}$ of length
exactly $1$ there are an angle $\theta \in \mathbb{R}$ and a translation $c \in \mathbb{C}$ such
that $e^{i\theta}\gamma(t) + c \in H$ for every $t \in [0, 1]$.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.halfSemidiskCovers`, a definition declared in [WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#half-semidisk-covers).

## Wetzel's sector covering claim

The proposition that the closed circular sector $S$ of
radius $1$ and angle $30^\circ$ with apex $0$ and symmetric about the positive real axis, that is,
the set of complex numbers $z$ with $|z| \le 1$, $\operatorname{Re} z \ge 0$ and
$|\operatorname{Im} z| \le \tan(\pi/12)\operatorname{Re} z$, covers every unit arc: for every
continuous curve $\gamma : [0,1] \to \mathbb{C}$ of length (total variation) exactly $1$ there are
an angle $\theta \in \mathbb{R}$ and a point $c \in \mathbb{C}$ such that
$e^{i\theta}\gamma(t) + c \in S$ for all $t \in [0,1]$.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.wetzelSectorCovers`, a definition declared in [WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#wetzel-sector-covers).

## A Norwood–Poole cover bounds the nonconvex worm cover constant

Call a nonempty set
$\Omega \subseteq \mathbb{C}$ a universal cover if every continuous curve
$\gamma : [0, 1] \to \mathbb{C}$ of length exactly $1$ can be moved into $\Omega$ by some rotation
followed by a translation, and let the nonconvex worm cover constant be the infimum of the areas
(Lebesgue outer measures) of all universal covers, which is a finite real number. If some
universal cover has area at most $0.260437$, then the nonconvex worm cover constant is at most
$0.260437$.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.nonconvexUpperBoundNorwoodPoole2003_of_cover`, a theorem declared in [WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#nonconvex-upper-bound-norwood-poole2003-2).

## Covers of area at most $0.26007$ bound the nonconvex worm cover constant

If some
nonempty planar set of area (Lebesgue outer measure) at most $0.26007$ contains a rotated and
translated copy of every planar curve of length $1$, then the nonconvex worm cover constant is at
most $0.26007$.

## Sources

- Optimization Problems, constant 13a; source-specific interval-arc adaptation.

Formalized by `MoserConvexWormCoverConstant.nonconvexUpperBoundPloymaklamWichiramala2018_of_cover`, a theorem declared in [WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#nonconvex-upper-bound-ploymaklam-wichira-2).

## The convex worm cover constant is at most π/4

A unit arc is a continuous
curve $\gamma : [0, 1] \to \mathbb{C}$ of length exactly $1$. The convex worm cover constant,
the infimum of the areas of the nonempty convex sets $\Omega \subseteq \mathbb{C}$ that contain,
for every unit arc $\gamma$, the image of $\gamma$ under some rotation followed by a translation,
is at most $\pi/4$.

## Sources

- Optimization Problems, constant 13a, closed claim `upperBoundPiOverFour`.

Stated but not proved: `MoserConvexWormCoverConstant.upperBoundPiOverFour_holds` is written with `theorem_wanted` in [WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#upper-bound-pi-over-four-holds).

## The convex worm cover constant is at most π/8

A unit arc is a continuous
curve $\gamma : [0, 1] \to \mathbb{C}$ of length exactly $1$. The convex worm cover constant,
the infimum of the areas of the nonempty convex sets $\Omega \subseteq \mathbb{C}$ that contain,
for every unit arc $\gamma$, the image of $\gamma$ under some rotation followed by a translation,
is at most $\pi/8$.

## Sources

- Optimization Problems, constant 13a, closed claim `upperBoundPiOverEight`.

Stated but not proved: `MoserConvexWormCoverConstant.upperBoundPiOverEight_holds` is written with `theorem_wanted` in [WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#upper-bound-pi-over-eight-holds).

## The convex worm cover constant is at most 0.34501

A unit arc is a continuous
curve $\gamma : [0, 1] \to \mathbb{C}$ of length exactly $1$. The convex worm cover constant,
the infimum of the areas of the nonempty convex sets $\Omega \subseteq \mathbb{C}$ that contain,
for every unit arc $\gamma$, the image of $\gamma$ under some rotation followed by a translation,
is at most $0.34501$.

## Sources

- Optimization Problems, constant 13a, closed claim `upperBoundWetzel1973`.

Stated but not proved: `MoserConvexWormCoverConstant.upperBoundWetzel1973_holds` is written with `theorem_wanted` in [WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#upper-bound-wetzel1973-holds).

## Gerriets' upper bound for the convex worm cover constant

Moser's convex worm cover
constant, the infimum of the areas of convex planar sets containing a rotated and translated copy
of every planar curve of length $1$, is at most $0.3214$.

## Sources

- Optimization Problems, constant 13a, closed claim `upperBoundGerriets1972`.

Stated but not proved: `MoserConvexWormCoverConstant.upperBoundGerriets1972_holds` is written with `theorem_wanted` in [WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#upper-bound-gerriets1972-holds).

## Gerriets–Poole upper bound for the convex worm cover constant

Moser's convex worm cover
constant, the infimum of the areas of convex planar sets containing a rotated and translated copy
of every planar curve of length $1$, is at most $0.2861$.

## Sources

- Optimization Problems, constant 13a, closed claim `upperBoundGerrietsPoole1974`.

Stated but not proved: `MoserConvexWormCoverConstant.upperBoundGerrietsPoole1974_holds` is written with `theorem_wanted` in [WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#upper-bound-gerriets-poole1974-holds).

## Norwood–Poole–Laidacker upper bound for the convex worm cover constant

Moser's convex
worm cover constant, the infimum of the areas of convex planar sets containing a rotated and
translated copy of every planar curve of length $1$, is at most $0.27524$.

## Sources

- Optimization Problems, constant 13a, closed claim `upperBoundNorwoodPooleLaidacker1992`.

Stated but not proved: `MoserConvexWormCoverConstant.upperBoundNorwoodPooleLaidacker1992_holds` is written with `theorem_wanted` in [WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#upper-bound-norwood-poole-laidacker1992-2).

## The convex worm cover constant is at most 0.270911861

A unit arc is a continuous
curve $\gamma : [0, 1] \to \mathbb{C}$ of length exactly $1$. The convex worm cover constant,
the infimum of the areas of the nonempty convex sets $\Omega \subseteq \mathbb{C}$ that contain,
for every unit arc $\gamma$, the image of $\gamma$ under some rotation followed by a translation,
is at most $0.270911861$.

## Sources

- Optimization Problems, constant 13a, closed claim `upperBoundWang2006`.

Stated but not proved: `MoserConvexWormCoverConstant.upperBoundWang2006_holds` is written with `theorem_wanted` in [WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#upper-bound-wang2006-holds).

## The convex worm cover constant is at most π/12

A unit arc is a continuous
curve $\gamma : [0, 1] \to \mathbb{C}$ of length exactly $1$. The convex worm cover constant,
the infimum of the areas of the nonempty convex sets $\Omega \subseteq \mathbb{C}$ that contain,
for every unit arc $\gamma$, the image of $\gamma$ under some rotation followed by a translation,
is at most $\pi/12$.

## Sources

- Optimization Problems, constant 13a, closed claim `upperBoundPiOverTwelve`.

Stated but not proved: `MoserConvexWormCoverConstant.upperBoundPiOverTwelve_holds` is written with `theorem_wanted` in [WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#upper-bound-pi-over-twelve-holds).

## Wetzel's 1973 lower bound for the convex worm cover constant

Let $\mu$ be the convex
worm cover constant, the infimum of the areas of the nonempty convex sets
$\Omega \subseteq \mathbb{C}$ such that every continuous curve $\gamma : [0, 1] \to \mathbb{C}$ of
length exactly $1$ can be moved into $\Omega$ by a rotation followed by a translation. Then
$0.2194 \le \mu$.

## Sources

- Optimization Problems, constant 13a, closed claim `lowerBoundWetzel1973`.

Stated but not proved: `MoserConvexWormCoverConstant.lowerBoundWetzel1973_holds` is written with `theorem_wanted` in [WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#lower-bound-wetzel1973-holds).

## Khandhawit–Sriswasdi 2009 lower bound for the convex worm cover constant

Let $\mu$ be
the convex worm cover constant, the infimum of the areas of the nonempty convex sets
$\Omega \subseteq \mathbb{C}$ such that every continuous curve $\gamma : [0, 1] \to \mathbb{C}$ of
length exactly $1$ can be moved into $\Omega$ by a rotation followed by a translation. Then
$0.227498 \le \mu$.

## Sources

- Optimization Problems, constant 13a, closed claim `lowerBoundKhandhawitSriswasdi2009`.

Stated but not proved: `MoserConvexWormCoverConstant.lowerBoundKhandhawitSriswasdi2009_holds` is written with `theorem_wanted` in [WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#lower-bound-khandhawit-sriswasdi2009-hol).

## Khandhawit–Pagonakis–Sriswasdi 2013 lower bound on the convex worm cover constant

Let
$\mu$ be the convex worm cover constant, the infimum of the areas of the nonempty convex sets
$\Omega \subseteq \mathbb{C}$ such that every continuous curve $\gamma : [0, 1] \to \mathbb{C}$ of
length exactly $1$ can be moved into $\Omega$ by a rotation followed by a translation. Then
$0.232239 \le \mu$.

## Sources

- Optimization Problems, constant 13a, closed claim `lowerBoundKhandhawitPagonakisSriswasdi2013`.

Stated but not proved: `MoserConvexWormCoverConstant.lowerBoundKhandhawitPagonakisSriswasdi2013_holds` is written with `theorem_wanted` in [WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#lower-bound-khandhawit-pagonakis-sriswas-2).

## A minimal convex cover for unit arcs exists

Call a nonempty convex set
$\Omega \subseteq \mathbb{C}$ a convex universal cover if every continuous curve
$\gamma : [0, 1] \to \mathbb{C}$ of length exactly $1$ can be moved into $\Omega$ by some rotation
followed by a translation, and let the convex worm cover constant be the infimum of the areas
(Lebesgue measures) of all convex universal covers, which is a finite real number. Then some
convex universal cover has area equal to the convex worm cover constant.

## Sources

- Optimization Problems, constant 13a, closed claim `minimalConvexCoverExists`.

Stated but not proved: `MoserConvexWormCoverConstant.minimalConvexCoverExists_holds` is written with `theorem_wanted` in [WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#minimal-convex-cover-exists-holds).

## Norwood–Poole universal cover for unit arcs

There is a nonempty set
$\Omega \subseteq \mathbb{C}$ of area (Lebesgue outer measure) at most $0.260437$ such that every
continuous curve $\gamma : [0, 1] \to \mathbb{C}$ of length exactly $1$ can be moved into $\Omega$
by some rotation followed by a translation.

## Sources

- Optimization Problems, constant 13a, closed claim `nonconvexCoverNorwoodPoole2003`.

Stated but not proved: `MoserConvexWormCoverConstant.nonconvexCoverNorwoodPoole2003_holds` is written with `theorem_wanted` in [WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#nonconvex-cover-norwood-poole2003-holds).

## Ploymaklam–Wichiramala universal cover for unit arcs

There is a nonempty set
$\Omega \subseteq \mathbb{C}$ of area (Lebesgue outer measure) at most $0.26007$ such that every
continuous curve $\gamma : [0, 1] \to \mathbb{C}$ of length exactly $1$ can be moved into $\Omega$
by some rotation followed by a translation.

## Sources

- Optimization Problems, constant 13a, closed claim `nonconvexCoverPloymaklamWichiramala2018`.

Stated but not proved: `MoserConvexWormCoverConstant.nonconvexCoverPloymaklamWichiramala2018_holds` is written with `theorem_wanted` in [WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#nonconvex-cover-ploymaklam-wichiramala20-2).

## Norwood–Poole upper bound for the nonconvex worm cover constant

Call a nonempty set
$\Omega \subseteq \mathbb{C}$ a universal cover if every continuous curve
$\gamma : [0, 1] \to \mathbb{C}$ of length exactly $1$ can be moved into $\Omega$ by some rotation
followed by a translation, and let the nonconvex worm cover constant be the infimum of the areas
(Lebesgue outer measures) of all universal covers, which is a finite real number. Then the
nonconvex worm cover constant is at most $0.260437$.

## Sources

- Optimization Problems, constant 13a, closed claim `nonconvexUpperBoundNorwoodPoole2003`.

Stated but not proved: `MoserConvexWormCoverConstant.nonconvexUpperBoundNorwoodPoole2003_holds` is written with `theorem_wanted` in [WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#nonconvex-upper-bound-norwood-poole2003-3).

## Ploymaklam–Wichiramala upper bound for the nonconvex worm cover constant

The nonconvex
worm cover constant, the infimum of the areas (Lebesgue outer measures) of planar sets containing
a rotated and translated copy of every planar curve of length $1$, is at most $0.26007$.

## Sources

- Optimization Problems, constant 13a, closed claim `nonconvexUpperBoundPloymaklamWichiramala2018`.

Stated but not proved: `MoserConvexWormCoverConstant.nonconvexUpperBoundPloymaklamWichiramala2018_holds` is written with `theorem_wanted` in [WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#nonconvex-upper-bound-ploymaklam-wichira-3).

## The nonconvex worm cover constant is positive

Call a nonempty set
$\Omega \subseteq \mathbb{C}$ a universal cover if every continuous curve
$\gamma : [0, 1] \to \mathbb{C}$ of length exactly $1$ can be moved into $\Omega$ by some rotation
followed by a translation, and let the nonconvex worm cover constant be the infimum of the areas
(Lebesgue outer measures) of all universal covers, which is a finite real number. Then the
nonconvex worm cover constant is strictly positive.

## Sources

- Optimization Problems, constant 13a, closed claim `nonconvexStrictPositivity`.

Stated but not proved: `MoserConvexWormCoverConstant.nonconvexStrictPositivity_holds` is written with `theorem_wanted` in [WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#nonconvex-strict-positivity-holds).

## The disk of diameter one covers every unit arc

For every continuous curve
$\gamma : [0, 1] \to \mathbb{C}$ of length exactly $1$ there are an angle $\theta \in \mathbb{R}$
and a translation $c \in \mathbb{C}$ such that $|e^{i\theta}\gamma(t) + c| \le 1/2$ for every
$t \in [0, 1]$.

## Sources

- Optimization Problems, constant 13a, closed claim `halfDiskCovers`.

Stated but not proved: `MoserConvexWormCoverConstant.halfDiskCovers_holds` is written with `theorem_wanted` in [WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#half-disk-covers-holds).

## The half-disk of diameter one covers every unit arc

Let
$H = \{z \in \mathbb{C} : |z| \le 1/2,\ \operatorname{Im} z \ge 0\}$. For every continuous curve
$\gamma : [0, 1] \to \mathbb{C}$ of length exactly $1$ there are an angle $\theta \in \mathbb{R}$
and a translation $c \in \mathbb{C}$ such that $e^{i\theta}\gamma(t) + c \in H$ for every
$t \in [0, 1]$.

## Sources

- Optimization Problems, constant 13a, closed claim `halfSemidiskCovers`.

Stated but not proved: `MoserConvexWormCoverConstant.halfSemidiskCovers_holds` is written with `theorem_wanted` in [WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#half-semidisk-covers-holds).

## Wetzel's sector covers every unit arc

Let $S$ be the closed circular sector of radius $1$
and angle $30^\circ$ with apex $0$ and symmetric about the positive real axis, that is, the set of
complex numbers $z$ with $|z| \le 1$, $\operatorname{Re} z \ge 0$ and
$|\operatorname{Im} z| \le \tan(\pi/12)\operatorname{Re} z$. Then for every continuous curve
$\gamma : [0,1] \to \mathbb{C}$ of length (total variation) exactly $1$ there are an angle
$\theta \in \mathbb{R}$ and a point $c \in \mathbb{C}$ such that $e^{i\theta}\gamma(t) + c \in S$
for all $t \in [0,1]$.

## Sources

- Optimization Problems, constant 13a, closed claim `wetzelSectorCovers`.

Stated but not proved: `MoserConvexWormCoverConstant.wetzelSectorCovers_holds` is written with `theorem_wanted` in [WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/MoserConvexWormCoverConstantWanted.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html#wetzel-sector-covers-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Moser's worm problem](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Geometry/packings-and-coverings/moser-s-worm-problem)
