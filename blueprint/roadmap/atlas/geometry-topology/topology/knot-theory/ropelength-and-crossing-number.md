---
declaration: section
origin: cited
lean: MathlibExt.Geometry.Euclidean.Ropelength.R3, MathlibExt.Geometry.Euclidean.Ropelength.triplePoints, MathlibExt.Geometry.Euclidean.Ropelength.triangleOf, MathlibExt.Geometry.Euclidean.Ropelength.circumradiusENN, MathlibExt.Geometry.Euclidean.Ropelength.circumradiusENN_eq_ofReal_circumradius, MathlibExt.Geometry.Euclidean.Ropelength.circumradiusENN_eq_top_of_collinear, MathlibExt.Geometry.Euclidean.Ropelength.circumradiusENN_eq_top_of_eq_left, MathlibExt.Geometry.Euclidean.Ropelength.circumradiusENN_swap_left
statement: formalized
proof: formalized
---

# Ropelength and crossing number

35 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/ropelength-and-crossing-number/index.html).

## Euclidean 3-space

The space $\mathbb{R}^3$ with its Euclidean inner product and norm.

Formalized by `MathlibExt.Geometry.Euclidean.Ropelength.R3`, an abbreviation declared in [MathlibExt/Geometry/Euclidean/Ropelength.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/Ropelength.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/ropelength-and-crossing-number/index.html#r3).

## Ordered triple of points

For points $p, q, r$ of Euclidean 3-space, the family indexed by
$\{0, 1, 2\}$ that sends $0 \mapsto p$, $1 \mapsto q$ and $2 \mapsto r$.

Formalized by `MathlibExt.Geometry.Euclidean.Ropelength.triplePoints`, a definition declared in [MathlibExt/Geometry/Euclidean/Ropelength.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/Ropelength.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/ropelength-and-crossing-number/index.html#triple-points).

## Triangle on three affinely independent points

For points $p, q, r$ of Euclidean 3-space
whose ordered triple $(p, q, r)$ is affinely independent, the triangle in Euclidean 3-space with
vertices $p$, $q$, $r$, in that order.

Formalized by `MathlibExt.Geometry.Euclidean.Ropelength.triangleOf`, a definition declared in [MathlibExt/Geometry/Euclidean/Ropelength.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/Ropelength.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/ropelength-and-crossing-number/index.html#triangle-of).

## Extended circumradius of three points

For points $p, q, r$ of Euclidean 3-space, the
extended circumradius of $(p, q, r)$ is the following value in $[0, \infty]$. If $p, q, r$ are
affinely independent, it is the circumradius of the triangle with vertices $p$, $q$ and $r$.
Otherwise, that is, when the three points are collinear (in particular when two of them
coincide), it is $\infty$.

This matches the convention that collinear points determine a circle of infinite radius.

Formalized by `MathlibExt.Geometry.Euclidean.Ropelength.circumradiusENN`, a definition declared in [MathlibExt/Geometry/Euclidean/Ropelength.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/Ropelength.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/ropelength-and-crossing-number/index.html#circumradius-enn).

## Extended circumradius of a triangle

Let $p, q, r$ be points of Euclidean 3-space and
let $T$ be a triangle in Euclidean 3-space whose vertices, in order, are $p$, $q$ and $r$. Then
the extended circumradius of $(p, q, r)$ equals the circumradius of $T$.

Formalized by `MathlibExt.Geometry.Euclidean.Ropelength.circumradiusENN_eq_ofReal_circumradius`, a theorem declared in [MathlibExt/Geometry/Euclidean/Ropelength.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/Ropelength.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/ropelength-and-crossing-number/index.html#circumradius-enn-eq-of-real-circumradius).

## Collinear points have infinite extended circumradius

If $p, q, r$ are points of
Euclidean 3-space and the set $\{p, q, r\}$ is collinear, then the extended circumradius of
$(p, q, r)$ is $\infty$.

Formalized by `MathlibExt.Geometry.Euclidean.Ropelength.circumradiusENN_eq_top_of_collinear`, a theorem declared in [MathlibExt/Geometry/Euclidean/Ropelength.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/Ropelength.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/ropelength-and-crossing-number/index.html#circumradius-enn-eq-top-of-collinear).

## Equal first two points give infinite extended circumradius

If $p, q, r$ are points of
Euclidean 3-space with $p = q$, then the extended circumradius of $(p, q, r)$ is $\infty$.

A triple with coincident points is treated as degenerate, not as having radius zero.

Formalized by `MathlibExt.Geometry.Euclidean.Ropelength.circumradiusENN_eq_top_of_eq_left`, a theorem declared in [MathlibExt/Geometry/Euclidean/Ropelength.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/Ropelength.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/ropelength-and-crossing-number/index.html#circumradius-enn-eq-top-of-eq-left).

## Extended circumradius is symmetric in the first two points

For all points $p, q, r$ of
Euclidean 3-space, the extended circumradius of $(q, p, r)$ equals the extended circumradius of
$(p, q, r)$.

Formalized by `MathlibExt.Geometry.Euclidean.Ropelength.circumradiusENN_swap_left`, a theorem declared in [MathlibExt/Geometry/Euclidean/Ropelength.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/Ropelength.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/ropelength-and-crossing-number/index.html#circumradius-enn-swap-left).

## Extended circumradius is symmetric in the last two points

For all points $p, q, r$ of
Euclidean 3-space, the extended circumradius of $(p, r, q)$ equals the extended circumradius of
$(p, q, r)$.

Formalized by `MathlibExt.Geometry.Euclidean.Ropelength.circumradiusENN_swap_right`, a theorem declared in [MathlibExt/Geometry/Euclidean/Ropelength.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/Ropelength.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/ropelength-and-crossing-number/index.html#circumradius-enn-swap-right).

## Extended circumradius is invariant under reversal

For all points $p, q, r$ of Euclidean
3-space, the extended circumradius of $(r, q, p)$ equals the extended circumradius of
$(p, q, r)$.

Formalized by `MathlibExt.Geometry.Euclidean.Ropelength.circumradiusENN_reverse`, a theorem declared in [MathlibExt/Geometry/Euclidean/Ropelength.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/Ropelength.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/ropelength-and-crossing-number/index.html#circumradius-enn-reverse).

## Translation invariance of the extended circumradius

For every vector $v$ and all points
$p, q, r$ of Euclidean 3-space, the extended circumradius of $(v + p, v + q, v + r)$ equals the
extended circumradius of $(p, q, r)$.

Formalized by `MathlibExt.Geometry.Euclidean.Ropelength.circumradiusENN_vadd`, a theorem declared in [MathlibExt/Geometry/Euclidean/Ropelength.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/Ropelength.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/ropelength-and-crossing-number/index.html#circumradius-enn-vadd).

## Thickness

The thickness of a set $s$ in Euclidean 3-space is the infimum, in
$[0, \infty]$, of the extended circumradii of $(p, q, r)$ over all points $p, q, r \in s$.
Since the extended circumradius of three collinear points (in particular of three points two of
which coincide) is $\infty$, this is also the infimum over the triples of pairwise distinct
points of $s$.

Formalized by `MathlibExt.Geometry.Euclidean.Ropelength.thickness`, a definition declared in [MathlibExt/Geometry/Euclidean/Ropelength.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/Ropelength.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/ropelength-and-crossing-number/index.html#thickness).

## Thickness is at most every circumradius

For every set $s$ in Euclidean 3-space and all
points $p, q, r \in s$, the thickness of $s$ is at most the extended circumradius of
$p, q, r$.

Formalized by `MathlibExt.Geometry.Euclidean.Ropelength.thickness_le`, a theorem declared in [MathlibExt/Geometry/Euclidean/Ropelength.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/Ropelength.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/ropelength-and-crossing-number/index.html#thickness-le).

## Thickness is antitone

If $s \subseteq t$ are sets in Euclidean 3-space, then the
thickness of $t$ is at most the thickness of $s$: enlarging a set can only add triples and
hence can only decrease the infimum.

Formalized by `MathlibExt.Geometry.Euclidean.Ropelength.thickness_anti`, a theorem declared in [MathlibExt/Geometry/Euclidean/Ropelength.lean, line 251](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/Ropelength.lean#L251). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/ropelength-and-crossing-number/index.html#thickness-anti).

## Thickness of the empty set

The empty subset of Euclidean 3-space has thickness
$\infty$, as an empty infimum in $[0, \infty]$.

Formalized by `MathlibExt.Geometry.Euclidean.Ropelength.thickness_empty`, a theorem declared in [MathlibExt/Geometry/Euclidean/Ropelength.lean, line 266](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/Ropelength.lean#L266). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/ropelength-and-crossing-number/index.html#thickness-empty).

## Thickness of a single point

For every point $p$ of Euclidean 3-space, the set $\{p\}$
has thickness $\infty$: its only triple $(p, p, p)$ is degenerate.

Formalized by `MathlibExt.Geometry.Euclidean.Ropelength.thickness_singleton`, a theorem declared in [MathlibExt/Geometry/Euclidean/Ropelength.lean, line 270](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/Ropelength.lean#L270). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/ropelength-and-crossing-number/index.html#thickness-singleton).

## Contour length

Let $\gamma$ be a map from $\mathbb{R}$ to Euclidean 3-space and let
$a, b$ be real numbers. The contour length of $\gamma$ on $[a, b]$ is the total variation of
$\gamma$ on $[a, b]$: the supremum, over all finite sequences $t_0 \le t_1 \le \dots \le t_n$
of points of $[a, b]$, of $\sum_{i < n} \lVert \gamma(t_{i+1}) - \gamma(t_i) \rVert$. It is a
value in $[0, \infty]$.

For continuously differentiable curves it equals the integral of the speed.

Formalized by `MathlibExt.Geometry.Euclidean.Ropelength.contourLength`, a definition declared in [MathlibExt/Geometry/Euclidean/Ropelength.lean, line 285](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/Ropelength.lean#L285). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/ropelength-and-crossing-number/index.html#contour-length).

## Contour length of a $C^1$ curve

Let $a \le b$ be real numbers and let $\gamma$ be a
map from $\mathbb{R}$ to Euclidean 3-space that is continuously differentiable on $[a, b]$.
Then the contour length of $\gamma$ on $[a, b]$ equals
$\int_a^b \lVert \gamma'(t) \rVert \, dt$.

Formalized by `MathlibExt.Geometry.Euclidean.Ropelength.contourLength_eq_ofReal_integral_norm_deriv`, a theorem declared in [MathlibExt/Geometry/Euclidean/Ropelength.lean, line 289](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/Ropelength.lean#L289). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/ropelength-and-crossing-number/index.html#contour-length-eq-of-real-integral-norm).

## Ropelength ratio

For a curve $\gamma : \mathbb{R} \to \mathbb{R}^3$ and reals $a, b$, the
ropelength ratio of $\gamma$ on $[a, b]$ is the contour length of $\gamma$ on $[a, b]$ divided by
the thickness of the trace $\gamma([a, b])$. The quotient is taken in $[0, \infty]$, where
$c / 0 = \infty$ for $c \ne 0$, $0 / 0 = 0$ and $c / \infty = 0$.

The ropelength of a knot or link type is a further infimum of this ratio over the curves
representing the type.

Formalized by `MathlibExt.Geometry.Euclidean.Ropelength.ropelengthRatio`, a definition declared in [MathlibExt/Geometry/Euclidean/Ropelength.lean, line 299](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/Ropelength.lean#L299). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/ropelength-and-crossing-number/index.html#ropelength-ratio).

## Admissible constants for the tight alternating knot inequality

A real number $c$ is admissible when $c \ge 0$ and, for every $n$ and
every oriented labeled link type with $n$ components that admits an
alternating diagram and whose crossing number is a natural number $k$,
the ropelength of the type is at least $c k$.

The restriction to finite crossing number excludes no such type: the
alternating representative is itself a regular projection, so every
link type admitting an alternating diagram has finite crossing
number.

Formalized by `MathlibExt.Topology.Knot.TightAlternatingKnot.IsAdmissibleAlternating`, a definition declared in [MathlibExt/Topology/Knot/TightAlternatingKnotConstant.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/TightAlternatingKnotConstant.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/ropelength-and-crossing-number/index.html#is-admissible-alternating).

## Tight alternating knot constant

The tight alternating knot
constant $C_{22b} = b_0$ is the supremum, taken in the extended reals,
of the set of real numbers $c$ admissible for the tight alternating
knot inequality: those $c \ge 0$ such that every link type $K$ that
admits an alternating diagram and has finite crossing number
$\mathrm{Cr}(K)$ has ropelength $\mathrm{L}(K) \ge c\,\mathrm{Cr}(K)$.
The supremum is not assumed to be attained.

Formalized by `MathlibExt.Topology.Knot.TightAlternatingKnot.tightAlternatingKnotConstant`, a definition declared in [MathlibExt/Topology/Knot/TightAlternatingKnotConstant.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/TightAlternatingKnotConstant.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/ropelength-and-crossing-number/index.html#tight-alternating-knot-constant).

## Zero is an admissible alternating constant

The constant
$c = 0$ is admissible for the tight alternating knot inequality.

Formalized by `MathlibExt.Topology.Knot.TightAlternatingKnot.isAdmissibleAlternating_zero`, a theorem declared in [MathlibExt/Topology/Knot/TightAlternatingKnotConstant.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/TightAlternatingKnotConstant.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/ropelength-and-crossing-number/index.html#is-admissible-alternating-zero).

## Admissible alternating constants are downward closed among nonnegative reals

**Admissible alternating constants are downward closed among
nonnegative reals.** If a real number $c$ is admissible for the tight
alternating knot inequality and $c'$ is a real number with
$0 \le c' \le c$, then $c'$ is admissible as well.

Formalized by `MathlibExt.Topology.Knot.TightAlternatingKnot.IsAdmissibleAlternating.of_le`, a theorem declared in [MathlibExt/Topology/Knot/TightAlternatingKnotConstant.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/TightAlternatingKnotConstant.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/ropelength-and-crossing-number/index.html#of-le).

## Admissible constants are at most the tight alternating knot constant

**Admissible constants are at most the tight alternating knot
constant.** Every real number $c$ that is admissible for the tight
alternating knot inequality is at most the tight alternating knot
constant.

Formalized by `MathlibExt.Topology.Knot.TightAlternatingKnot.le_tightAlternatingKnotConstant`, a theorem declared in [MathlibExt/Topology/Knot/TightAlternatingKnotConstant.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/TightAlternatingKnotConstant.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/ropelength-and-crossing-number/index.html#le-tight-alternating-knot-constant).

## The tight alternating knot constant is nonnegative

The tight
alternating knot constant, an extended real number, is at least $0$.

Formalized by `MathlibExt.Topology.Knot.TightAlternatingKnot.zero_le_tightAlternatingKnotConstant`, a theorem declared in [MathlibExt/Topology/Knot/TightAlternatingKnotConstant.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/TightAlternatingKnotConstant.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/ropelength-and-crossing-number/index.html#zero-le-tight-alternating-knot-constant).

## Upper bounds for the tight alternating knot constant

For every
extended real number $b$, the tight alternating knot constant is at
most $b$ if and only if every real number $c$ that is admissible for
the tight alternating knot inequality satisfies $c \le b$.

Formalized by `MathlibExt.Topology.Knot.TightAlternatingKnot.tightAlternatingKnotConstant_le_iff`, a theorem declared in [MathlibExt/Topology/Knot/TightAlternatingKnotConstant.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/TightAlternatingKnotConstant.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/ropelength-and-crossing-number/index.html#tight-alternating-knot-constant-le-iff).

## Alternating link types have finite crossing number

If an
oriented labeled link type with $n$ components admits an alternating
diagram, then its crossing number is finite: the alternating
representative is itself a regular projection.

Formalized by `MathlibExt.Topology.Knot.TightAlternatingKnot.crossingNumber_lt_top_of_admitsAlternatingDiagram`, a theorem declared in [MathlibExt/Topology/Knot/TightAlternatingKnotConstant.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/TightAlternatingKnotConstant.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/ropelength-and-crossing-number/index.html#crossing-number-lt-top-of-admits-alterna).

## Alternating link types have a natural-number crossing number

If an oriented labeled link type with $n$ components admits an
alternating diagram, then its crossing number equals some natural
number $k$.

Formalized by `MathlibExt.Topology.Knot.TightAlternatingKnot.exists_crossingNumber_eq_natCast_of_admitsAlternatingDiagram`, a theorem declared in [MathlibExt/Topology/Knot/TightAlternatingKnotConstant.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/TightAlternatingKnotConstant.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/ropelength-and-crossing-number/index.html#exists-crossing-number-eq-nat-cast-of-ad).

## Admissible constants for the tight-knot inequality

A real number $c$ is admissible for
the tight-knot inequality when $c \ge 0$ and, for every $n \in \mathbb{N}$, every parametrized
link $L$ with $n$ components and every $k \in \mathbb{N}$ such that the crossing number of $L$
equals $k$, the ropelength of $L$ is at least $c \, k^{3/4}$, the inequality being read in
$[0, \infty]$. Here the crossing number and the ropelength of $L$ are those of its oriented
labeled ambient-isotopy type.

Link types of infinite crossing number, that is, types none of whose representatives admits a
regular projection, impose no constraint.

Formalized by `MathlibExt.Topology.Knot.TightKnot.IsAdmissible`, a definition declared in [MathlibExt/Topology/Knot/TightKnotConstant.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/TightKnotConstant.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/ropelength-and-crossing-number/index.html#is-admissible).

## Tight knot constant

The tight knot constant $C_{22a}$ is the supremum, taken in the
extended reals $[-\infty, \infty]$, of the set of real numbers $c$ that are admissible for the
tight-knot inequality $\mathrm{ropelength} \ge c \cdot (\text{crossing number})^{3/4}$ on link
types. The supremum is not assumed to be attained.

Formalized by `MathlibExt.Topology.Knot.TightKnot.tightKnotConstant`, a definition declared in [MathlibExt/Topology/Knot/TightKnotConstant.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/TightKnotConstant.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/ropelength-and-crossing-number/index.html#tight-knot-constant).

## Zero is an admissible tight-knot constant

The real number $0$ is admissible for the
tight-knot inequality between the ropelength and the crossing number of link types.

Formalized by `MathlibExt.Topology.Knot.TightKnot.isAdmissible_zero`, a theorem declared in [MathlibExt/Topology/Knot/TightKnotConstant.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/TightKnotConstant.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/ropelength-and-crossing-number/index.html#is-admissible-zero).

## Admissibility passes to smaller nonnegative constants

If a real number $c$ is admissible
for the tight-knot inequality and $c'$ is a real number with $0 \le c' \le c$, then $c'$ is
admissible for the tight-knot inequality as well.

Formalized by `MathlibExt.Topology.Knot.TightKnot.IsAdmissible.of_le`, a theorem declared in [MathlibExt/Topology/Knot/TightKnotConstant.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/TightKnotConstant.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/ropelength-and-crossing-number/index.html#of-le-2).

## Admissible constants are bounded by the tight knot constant

Let $C_{22a}$ be the tight
knot constant. Every real number $c$ that is admissible for the tight-knot inequality satisfies
$c \le C_{22a}$ in the extended reals.

Formalized by `MathlibExt.Topology.Knot.TightKnot.le_tightKnotConstant`, a theorem declared in [MathlibExt/Topology/Knot/TightKnotConstant.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/TightKnotConstant.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/ropelength-and-crossing-number/index.html#le-tight-knot-constant).

## The tight knot constant is nonnegative

The tight knot constant $C_{22a}$ satisfies
$0 \le C_{22a}$ in the extended reals.

Formalized by `MathlibExt.Topology.Knot.TightKnot.zero_le_tightKnotConstant`, a theorem declared in [MathlibExt/Topology/Knot/TightKnotConstant.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/TightKnotConstant.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/ropelength-and-crossing-number/index.html#zero-le-tight-knot-constant).

## Upper bounds for the tight knot constant

For every extended real number $b$, the tight
knot constant $C_{22a}$ satisfies $C_{22a} \le b$ if and only if every real number $c$ that is
admissible for the tight-knot inequality satisfies $c \le b$.

This is the characteristic rule for proving upper bounds on the tight knot constant without
unfolding its definition as a supremum.

Formalized by `MathlibExt.Topology.Knot.TightKnot.tightKnotConstant_le_iff`, a theorem declared in [MathlibExt/Topology/Knot/TightKnotConstant.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/TightKnotConstant.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/ropelength-and-crossing-number/index.html#tight-knot-constant-le-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ropelength and crossing number](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/ropelength-and-crossing-number/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Topology/knot-theory/ropelength-and-crossing-number)
