---
declaration: section
origin: cited
lean: FalconerDistanceSet.distanceSet, FalconerDistanceSet.planarThresholdProperty, FalconerDistanceSet.admissiblePlanarThreshold, FalconerDistanceSet.planarDistanceThreshold, FalconerDistanceSet.distanceSet_subset_nonnegative, FalconerDistanceSet.distanceSet_empty, FalconerDistanceSet.distanceSet_singleton, FalconerDistanceSet.distanceSet_isCompact
statement: formalized
---

# Falconer distance set problem

42 results, 34 proved and 8 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/falconer-distance-set-problem/index.html).

## Euclidean distance set

For a set $E \subseteq \mathbb{R}^d$, the distance set of $E$ is
$\Delta(E) = \{\lvert x - y \rvert : x, y \in E\}$, the set of Euclidean distances between pairs
of points of $E$.

## Sources

- Guth, Iosevich, Ou, and Wang, arXiv:1808.09346v1, introduction.

Formalized by `FalconerDistanceSet.distanceSet`, a definition declared in [MathlibExt/Geometry/FalconerDistanceSet.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/FalconerDistanceSet.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/falconer-distance-set-problem/index.html#distance-set).

## Planar Falconer threshold property

An element $s \in [0, \infty]$ has the planar
threshold property when every compact set $E \subseteq \mathbb{R}^2$ with Hausdorff dimension
$\dim_H E > s$ has a distance set $\{|x - y| : x, y \in E\}$ of positive one-dimensional
Lebesgue measure.

## Sources

- the planar Falconer threshold in optimization catalogue C34a.

Formalized by `FalconerDistanceSet.planarThresholdProperty`, a definition declared in [MathlibExt/Geometry/FalconerDistanceSet.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/FalconerDistanceSet.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/falconer-distance-set-problem/index.html#planar-threshold-property).

## Admissible planar threshold

An extended nonnegative real $s$ is an admissible planar
threshold when $0 \le s \le 2$ and $s$ has the planar threshold property: every compact set
$E \subseteq \mathbb{R}^2$ with Hausdorff dimension $\dim_H E > s$ has a distance set of
positive one-dimensional Lebesgue measure.

## Sources

- the defining infimum in optimization catalogue C34a.

Formalized by `FalconerDistanceSet.admissiblePlanarThreshold`, a definition declared in [MathlibExt/Geometry/FalconerDistanceSet.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/FalconerDistanceSet.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/falconer-distance-set-problem/index.html#admissible-planar-threshold).

## Planar distance threshold

The planar distance threshold is the infimum, taken in
$[0, \infty]$, of the admissible planar thresholds, that is, of all $s \in [0, 2]$ such that
every compact subset $E$ of the Euclidean plane $\mathbb{R}^2$ with Hausdorff dimension greater
than $s$ has a distance set of positive Lebesgue measure.

## Sources

- optimization catalogue C34a. The finite ENNReal representation retains the source's order and measure; finiteness and the real roundtrip are proved below.

Formalized by `FalconerDistanceSet.planarDistanceThreshold`, a definition declared in [MathlibExt/Geometry/FalconerDistanceSet.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/FalconerDistanceSet.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/falconer-distance-set-problem/index.html#planar-distance-threshold).

## Distances are nonnegative

For every set $E \subseteq \mathbb{R}^d$, the distance set of
$E$ is contained in $[0, \infty)$.

Formalized by `FalconerDistanceSet.distanceSet_subset_nonnegative`, a theorem declared in [MathlibExt/Geometry/FalconerDistanceSet.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/FalconerDistanceSet.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/falconer-distance-set-problem/index.html#distance-set-subset-nonnegative).

## Distance set of the empty set

For every $d$, the distance set of the empty subset of
$\mathbb{R}^d$ is empty.

Formalized by `FalconerDistanceSet.distanceSet_empty`, a theorem declared in [MathlibExt/Geometry/FalconerDistanceSet.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/FalconerDistanceSet.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/falconer-distance-set-problem/index.html#distance-set-empty).

## Distance set of a singleton

For every point $x \in \mathbb{R}^d$, the distance set of
$\{x\}$ is $\{0\}$.

Formalized by `FalconerDistanceSet.distanceSet_singleton`, a theorem declared in [MathlibExt/Geometry/FalconerDistanceSet.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/FalconerDistanceSet.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/falconer-distance-set-problem/index.html#distance-set-singleton).

## Distance sets of compact sets are compact

If $E \subseteq \mathbb{R}^d$ is compact,
then the distance set of $E$ is a compact subset of $\mathbb{R}$.

Formalized by `FalconerDistanceSet.distanceSet_isCompact`, a theorem declared in [MathlibExt/Geometry/FalconerDistanceSet.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/FalconerDistanceSet.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/falconer-distance-set-problem/index.html#distance-set-is-compact).

## Distance sets of compact sets are Borel

If $E \subseteq \mathbb{R}^d$ is compact, then
the distance set of $E$ is a Borel measurable subset of $\mathbb{R}$.

Formalized by `FalconerDistanceSet.distanceSet_measurableSet`, a theorem declared in [MathlibExt/Geometry/FalconerDistanceSet.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/FalconerDistanceSet.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/falconer-distance-set-problem/index.html#distance-set-measurable-set).

## The planar threshold property is upward closed

Let $s \le t$ be elements of
$[0, \infty]$. If $s$ has the planar threshold property, that is, every compact set
$E \subseteq \mathbb{R}^2$ with Hausdorff dimension $\dim_H E > s$ has a distance set of
positive one-dimensional Lebesgue measure, then $t$ has the planar threshold property.

Formalized by `FalconerDistanceSet.planarThresholdProperty_mono`, a theorem declared in [MathlibExt/Geometry/FalconerDistanceSet.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/FalconerDistanceSet.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/falconer-distance-set-problem/index.html#planar-threshold-property-mono).

## Subsets of the plane have Hausdorff dimension at most two

Every subset $E$ of the
Euclidean plane $\mathbb{R}^2$ satisfies $\dim_H E \le 2$.

Formalized by `FalconerDistanceSet.dimH_plane_le_two`, a theorem declared in [MathlibExt/Geometry/FalconerDistanceSet.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/FalconerDistanceSet.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/falconer-distance-set-problem/index.html#dim-h-plane-le-two).

## Two is an admissible planar threshold

The number $2$ is an admissible planar threshold:
$2 \in [0, 2]$, and every compact set $E \subseteq \mathbb{R}^2$ with Hausdorff dimension
$\dim_H E > 2$ has a distance set of positive Lebesgue measure. This holds vacuously, since no
subset of the plane has Hausdorff dimension greater than $2$.

Formalized by `FalconerDistanceSet.two_admissiblePlanarThreshold`, a theorem declared in [MathlibExt/Geometry/FalconerDistanceSet.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/FalconerDistanceSet.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/falconer-distance-set-problem/index.html#two-admissible-planar-threshold).

## Admissible planar thresholds exist

There is an admissible planar threshold, that is, the
set of admissible planar thresholds is nonempty.

Formalized by `FalconerDistanceSet.admissiblePlanarThresholds_nonempty`, a theorem declared in [MathlibExt/Geometry/FalconerDistanceSet.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/FalconerDistanceSet.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/falconer-distance-set-problem/index.html#admissible-planar-thresholds-nonempty).

## Admissible thresholds bound the planar distance threshold

For every $s \in [0, \infty]$
that is an admissible planar threshold, the planar distance threshold is at most $s$.

Formalized by `FalconerDistanceSet.planarDistanceThreshold_le_of_admissible`, a theorem declared in [MathlibExt/Geometry/FalconerDistanceSet.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/FalconerDistanceSet.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/falconer-distance-set-problem/index.html#planar-distance-threshold-le-of-admissib).

## The planar distance threshold is at most two

The planar distance threshold is at most
$2$.

Formalized by `FalconerDistanceSet.planarDistanceThreshold_le_two`, a theorem declared in [MathlibExt/Geometry/FalconerDistanceSet.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/FalconerDistanceSet.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/falconer-distance-set-problem/index.html#planar-distance-threshold-le-two).

## The planar distance threshold is finite

The planar distance threshold, an element of
$[0, \infty]$, is not $\infty$.

Formalized by `FalconerDistanceSet.planarDistanceThreshold_ne_top`, a theorem declared in [MathlibExt/Geometry/FalconerDistanceSet.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/FalconerDistanceSet.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/falconer-distance-set-problem/index.html#planar-distance-threshold-ne-top).

## Real round trip of the planar distance threshold

Let $\tau \in [0, \infty]$ be the planar
distance threshold and let $\tau_{\mathbb{R}}$ be its value as a real number (with the convention
that $\infty$ goes to $0$). Viewing $\tau_{\mathbb{R}}$ again as an element of $[0, \infty]$
gives back $\tau$.

Formalized by `FalconerDistanceSet.planarDistanceThreshold_ofReal_toReal`, a theorem declared in [MathlibExt/Geometry/FalconerDistanceSet.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/FalconerDistanceSet.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/falconer-distance-set-problem/index.html#planar-distance-threshold-of-real-to-rea).

## Trivial lower bound for the planar distance threshold

The planar distance threshold is
at least $0$.

Formalized by `FalconerDistanceSet.trivialLowerBound`, a theorem declared in [MathlibExt/Geometry/FalconerDistanceSet.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/FalconerDistanceSet.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/falconer-distance-set-problem/index.html#trivial-lower-bound).

## Thresholds up to two with the planar threshold property bound the planar distance threshold

**Thresholds up to two with the planar threshold property bound the planar distance
threshold.** For every $s \in [0, \infty]$ with $s \le 2$ that has the planar threshold
property, the planar distance threshold is at most $s$.

Formalized by `FalconerDistanceSet.planarDistanceThreshold_le_of_property`, a theorem declared in [MathlibExt/Geometry/FalconerDistanceSet.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/FalconerDistanceSet.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/falconer-distance-set-problem/index.html#planar-distance-threshold-le-of-property).

## Zero-measure distance sets give lower bounds for the planar distance threshold

Let
$t \in [0, \infty]$. If $E$ is a compact subset of the Euclidean plane $\mathbb{R}^2$ whose
Hausdorff dimension $\dim_H E$ satisfies $t \le \dim_H E$ and whose distance set has Lebesgue
measure zero, then $t$ is at most the planar distance threshold.

Formalized by `FalconerDistanceSet.le_planarDistanceThreshold_of_zeroMeasureWitness`, a theorem declared in [MathlibExt/Geometry/FalconerDistanceSet.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/FalconerDistanceSet.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/falconer-distance-set-problem/index.html#le-planar-distance-threshold-of-zero-mea).

## Real form of admissible planar thresholds

For every real number $s \ge 0$, $s$ is an
admissible planar threshold (as an element of $[0, \infty]$) if and only if $s \in [0, 2]$ and
$s$ has the planar threshold property.

Formalized by `FalconerDistanceSet.ofReal_admissiblePlanarThreshold_iff`, a theorem declared in [MathlibExt/Geometry/FalconerDistanceSet.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/FalconerDistanceSet.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/falconer-distance-set-problem/index.html#of-real-admissible-planar-threshold-iff).

## The planar distance threshold is itself a threshold

Let $s_0 \in [0, \infty]$ be the
planar distance threshold, the infimum of the admissible planar thresholds. Every compact set
$E \subseteq \mathbb{R}^2$ with Hausdorff dimension $\dim_H E > s_0$ has a distance set of
positive one-dimensional Lebesgue measure.

Formalized by `FalconerDistanceSet.planarThresholdProperty_planarDistanceThreshold`, a theorem declared in [MathlibExt/Geometry/FalconerDistanceSet.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/FalconerDistanceSet.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/falconer-distance-set-problem/index.html#planar-threshold-property-planar-distanc).

## The planar distance threshold is admissible

The planar distance threshold is an
admissible planar threshold: it lies in $[0, 2]$ and has the planar threshold property.

Formalized by `FalconerDistanceSet.planarDistanceThreshold_admissible`, a theorem declared in [MathlibExt/Geometry/FalconerDistanceSet.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/FalconerDistanceSet.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/falconer-distance-set-problem/index.html#planar-distance-threshold-admissible).

## The planar distance threshold is attained

The planar distance threshold is the least
admissible planar threshold: it is itself an admissible planar threshold, and it is at most every
admissible planar threshold.

Formalized by `FalconerDistanceSet.isLeast_admissiblePlanarThresholds`, a theorem declared in [MathlibExt/Geometry/FalconerDistanceSet.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/FalconerDistanceSet.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/falconer-distance-set-problem/index.html#is-least-admissible-planar-thresholds).

## Real form of the admissible threshold family

The set of real numbers $r \in [0, 2]$
such that $r$, viewed as an element of $[0, \infty]$, has the planar threshold property equals
the image of the set of admissible planar thresholds under the map $[0, \infty] \to \mathbb{R}$
that is the identity on finite values and sends $\infty$ to $0$.

Formalized by `FalconerDistanceSet.realThresholdFamily_eq_toReal_image`, a theorem declared in [MathlibExt/Geometry/FalconerDistanceSet.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/FalconerDistanceSet.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/falconer-distance-set-problem/index.html#real-threshold-family-eq-to-real-image).

## The planar distance threshold as a real infimum

The value of the planar distance
threshold as a real number (with the convention that $\infty$ goes to $0$) equals the infimum
in $\mathbb{R}$ of the set of real numbers $r \in [0, 2]$ that, as elements of $[0, \infty]$,
have the planar threshold property.

Formalized by `FalconerDistanceSet.planarDistanceThreshold_toReal_eq_real_sInf`, a theorem declared in [MathlibExt/Geometry/FalconerDistanceSet.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/FalconerDistanceSet.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/falconer-distance-set-problem/index.html#planar-distance-threshold-to-real-eq-rea).

## Statement of Falconer's distance set theorem

This is the proposition that for every
integer $d \ge 2$ and every compact set $E \subseteq \mathbb{R}^d$ whose Hausdorff dimension is
strictly greater than $(d+1)/2$, the distance set $\{\|x - y\| : x, y \in E\}$ has positive
one-dimensional Lebesgue measure.

## Sources

- GIOW, arXiv:1808.09346v1, introduction line 76, reporting Falconer (1985).

Formalized by `FalconerDistanceSetWanted.falconer1985GeneralSufficiency`, a definition declared in [WantedExt/Geometry/FalconerDistanceSetWanted.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/FalconerDistanceSetWanted.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/falconer-distance-set-problem/index.html#falconer1985-general-sufficiency).

## Wolff's planar distance set condition, as a proposition

The proposition that every
compact set $E \subseteq \mathbb{R}^2$ with Hausdorff dimension greater than $4/3$ has a distance
set $\{|x - y| : x, y \in E\}$ of positive Lebesgue measure.

## Sources

- GIOW, arXiv:1808.09346v1, introduction line 78, reporting Wolff (1999).

Formalized by `FalconerDistanceSetWanted.wolff1999PlanarSufficiency`, a definition declared in [WantedExt/Geometry/FalconerDistanceSetWanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/FalconerDistanceSetWanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/falconer-distance-set-problem/index.html#wolff1999-planar-sufficiency).

## Statement of the Guth–Iosevich–Ou–Wang planar distance set theorem

This is the
proposition that $5/4$ has the planar threshold property: every compact set
$E \subseteq \mathbb{R}^2$ whose Hausdorff dimension is strictly greater than $5/4$ has a
distance set $\{\|x - y\| : x, y \in E\}$ of positive one-dimensional Lebesgue measure.

## Sources

- Guth, Iosevich, Ou, and Wang, arXiv:1808.09346v1, Theorem 1.1, lines 80-81.

Formalized by `FalconerDistanceSetWanted.guthIosevichOuWang2018PlanarSufficiency`, a definition declared in [WantedExt/Geometry/FalconerDistanceSetWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/FalconerDistanceSetWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/falconer-distance-set-problem/index.html#guth-iosevich-ou-wang2018-planar-suffici).

## Statement of Falconer's measure-zero distance set examples

This is the proposition
that for every integer $d \ge 2$ and every $s$ with $0 \le s \le d/2$, there is a compact set
$E \subseteq \mathbb{R}^d$ of Hausdorff dimension exactly $s$ whose distance set
$\{\|x - y\| : x, y \in E\}$ has one-dimensional Lebesgue measure zero.

## Sources

- GIOW, arXiv:1808.09346v1, introduction line 76. Dimensions use actual Hausdorff dimension and distance sets use actual one-dimensional Lebesgue measure.

Formalized by `FalconerDistanceSetWanted.falconer1985LatticeExamples`, a definition declared in [WantedExt/Geometry/FalconerDistanceSetWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/FalconerDistanceSetWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/falconer-distance-set-problem/index.html#falconer1985-lattice-examples).

## Statement of the upper bound $3/2$ for the planar distance threshold

This is the
proposition that the planar distance threshold, the infimum of all $s \in [0, 2]$ such that
every compact set $E \subseteq \mathbb{R}^2$ of Hausdorff dimension strictly greater than $s$
has a distance set $\{\|x - y\| : x, y \in E\}$ of positive one-dimensional Lebesgue measure,
is at most $3/2$.

## Sources

- optimization catalogue C34a, Falconer (1985) upper row.

Formalized by `FalconerDistanceSetWanted.upperBound_Falconer1985`, a definition declared in [WantedExt/Geometry/FalconerDistanceSetWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/FalconerDistanceSetWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/falconer-distance-set-problem/index.html#upper-bound-falconer1985).

## The Wolff bound, as a proposition

The proposition that the planar Falconer distance
threshold is at most $4/3$. Here the planar Falconer distance threshold is the infimum of the
$s \in [0, 2]$ such that every compact set $E \subseteq \mathbb{R}^2$ with Hausdorff dimension
greater than $s$ has a distance set $\{|x - y| : x, y \in E\}$ of positive Lebesgue measure.

## Sources

- optimization catalogue C34a, Wolff (1999) upper row.

Formalized by `FalconerDistanceSetWanted.upperBound_Wolff1999`, a definition declared in [WantedExt/Geometry/FalconerDistanceSetWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/FalconerDistanceSetWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/falconer-distance-set-problem/index.html#upper-bound-wolff1999).

## The Guth–Iosevich–Ou–Wang bound, as a proposition

The proposition that the planar
Falconer distance threshold is at most $5/4$. Here the planar Falconer distance threshold is the
infimum of the $s \in [0, 2]$ such that every compact set $E \subseteq \mathbb{R}^2$ with
Hausdorff dimension greater than $s$ has a distance set $\{|x - y| : x, y \in E\}$ of positive
Lebesgue measure.

## Sources

- optimization catalogue C34a, GIOW (2018) upper row.

Formalized by `FalconerDistanceSetWanted.upperBound_GIOW2018`, a definition declared in [WantedExt/Geometry/FalconerDistanceSetWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/FalconerDistanceSetWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/falconer-distance-set-problem/index.html#upper-bound-giow2018).

## Statement of the lower bound $1$ for the planar distance threshold

This is the
proposition that the planar distance threshold, the infimum of all $s \in [0, 2]$ such that
every compact set $E \subseteq \mathbb{R}^2$ of Hausdorff dimension strictly greater than $s$
has a distance set $\{\|x - y\| : x, y \in E\}$ of positive one-dimensional Lebesgue measure,
is at least $1$.

## Sources

- optimization catalogue C34a and GIOW's endpoint lattice examples, line 76.

Formalized by `FalconerDistanceSetWanted.lowerBound_Falconer1985`, a definition declared in [WantedExt/Geometry/FalconerDistanceSetWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/FalconerDistanceSetWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/falconer-distance-set-problem/index.html#lower-bound-falconer1985).

## Falconer's distance set theorem

For every integer $d \ge 2$ and every compact set
$E \subseteq \mathbb{R}^d$ whose Hausdorff dimension is strictly greater than $(d+1)/2$, the
distance set $\{\|x - y\| : x, y \in E\}$ has positive one-dimensional Lebesgue measure.

## Sources

- GIOW, arXiv:1808.09346v1, line 76, reporting Falconer (1985).

Stated but not proved: `FalconerDistanceSetWanted.falconer1985GeneralSufficiency_holds` is written with `theorem_wanted` in [WantedExt/Geometry/FalconerDistanceSetWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/FalconerDistanceSetWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/falconer-distance-set-problem/index.html#falconer1985-general-sufficiency-holds).

## Wolff's planar distance set theorem

Every compact set $E \subseteq \mathbb{R}^2$ with
Hausdorff dimension greater than $4/3$ has a distance set $\{|x - y| : x, y \in E\}$ of positive
Lebesgue measure.

## Sources

- GIOW, arXiv:1808.09346v1, line 78, reporting Wolff (1999).

Stated but not proved: `FalconerDistanceSetWanted.wolff1999PlanarSufficiency_holds` is written with `theorem_wanted` in [WantedExt/Geometry/FalconerDistanceSetWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/FalconerDistanceSetWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/falconer-distance-set-problem/index.html#wolff1999-planar-sufficiency-holds).

## Guth–Iosevich–Ou–Wang planar distance set theorem

Every compact set
$E \subseteq \mathbb{R}^2$ whose Hausdorff dimension is strictly greater than $5/4$ has a
distance set $\{\|x - y\| : x, y \in E\}$ of positive one-dimensional Lebesgue measure.

## Sources

- GIOW, arXiv:1808.09346v1, Theorem 1.1, lines 80-81.

Stated but not proved: `FalconerDistanceSetWanted.guthIosevichOuWang2018PlanarSufficiency_holds` is written with `theorem_wanted` in [WantedExt/Geometry/FalconerDistanceSetWanted.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/FalconerDistanceSetWanted.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/falconer-distance-set-problem/index.html#guth-iosevich-ou-wang2018-planar-suffici-2).

## Falconer's measure-zero distance set examples

For every integer $d \ge 2$ and every
$s$ with $0 \le s \le d/2$, there is a compact set $E \subseteq \mathbb{R}^d$ of Hausdorff
dimension exactly $s$ whose distance set $\{\|x - y\| : x, y \in E\}$ has one-dimensional
Lebesgue measure zero.

## Sources

- GIOW, arXiv:1808.09346v1, endpoint-inclusive lattice report, line 76.

Stated but not proved: `FalconerDistanceSetWanted.falconer1985LatticeExamples_holds` is written with `theorem_wanted` in [WantedExt/Geometry/FalconerDistanceSetWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/FalconerDistanceSetWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/falconer-distance-set-problem/index.html#falconer1985-lattice-examples-holds).

## Falconer's upper bound for the planar distance threshold

The planar distance
threshold, the infimum of all $s \in [0, 2]$ such that every compact set
$E \subseteq \mathbb{R}^2$ of Hausdorff dimension strictly greater than $s$ has a distance set
$\{\|x - y\| : x, y \in E\}$ of positive one-dimensional Lebesgue measure, is at most $3/2$.

## Sources

- optimization catalogue C34a, Falconer (1985) upper row.

Stated but not proved: `FalconerDistanceSetWanted.upperBound_Falconer1985_holds` is written with `theorem_wanted` in [WantedExt/Geometry/FalconerDistanceSetWanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/FalconerDistanceSetWanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/falconer-distance-set-problem/index.html#upper-bound-falconer1985-holds).

## Wolff's upper bound for the planar Falconer threshold

The planar Falconer distance
threshold, the infimum of the $s \in [0, 2]$ such that every compact set
$E \subseteq \mathbb{R}^2$ with Hausdorff dimension greater than $s$ has a distance set
$\{|x - y| : x, y \in E\}$ of positive Lebesgue measure, is at most $4/3$.

## Sources

- optimization catalogue C34a, Wolff (1999) upper row.

Stated but not proved: `FalconerDistanceSetWanted.upperBound_Wolff1999_holds` is written with `theorem_wanted` in [WantedExt/Geometry/FalconerDistanceSetWanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/FalconerDistanceSetWanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/falconer-distance-set-problem/index.html#upper-bound-wolff1999-holds).

## Guth–Iosevich–Ou–Wang upper bound for the planar Falconer threshold

The planar Falconer
distance threshold, the infimum of the $s \in [0, 2]$ such that every compact set
$E \subseteq \mathbb{R}^2$ with Hausdorff dimension greater than $s$ has a distance set
$\{|x - y| : x, y \in E\}$ of positive Lebesgue measure, is at most $5/4$.

## Sources

- optimization catalogue C34a, GIOW (2018) upper row.

Stated but not proved: `FalconerDistanceSetWanted.upperBound_GIOW2018_holds` is written with `theorem_wanted` in [WantedExt/Geometry/FalconerDistanceSetWanted.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/FalconerDistanceSetWanted.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/falconer-distance-set-problem/index.html#upper-bound-giow2018-holds).

## Falconer's lower bound for the planar distance threshold

The planar distance
threshold, the infimum of all $s \in [0, 2]$ such that every compact set
$E \subseteq \mathbb{R}^2$ of Hausdorff dimension strictly greater than $s$ has a distance set
$\{\|x - y\| : x, y \in E\}$ of positive one-dimensional Lebesgue measure, is at least $1$.

## Sources

- optimization catalogue C34a and GIOW, arXiv:1808.09346v1, line 76.

Stated but not proved: `FalconerDistanceSetWanted.lowerBound_Falconer1985_holds` is written with `theorem_wanted` in [WantedExt/Geometry/FalconerDistanceSetWanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/FalconerDistanceSetWanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/falconer-distance-set-problem/index.html#lower-bound-falconer1985-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Falconer distance set problem](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/falconer-distance-set-problem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/MeasureTheory/geometric-measure-theory/falconer-distance-set-problem)
