---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Convex.Straszewicz.IsCompact.convexHull_of_compact, MathlibExt.Analysis.Convex.Straszewicz.dirQuot, MathlibExt.Analysis.Convex.Straszewicz.dirDeriv, MathlibExt.Analysis.Convex.Straszewicz.convexOn_line, MathlibExt.Analysis.Convex.Straszewicz.dirQuot_bddBelow, MathlibExt.Analysis.Convex.Straszewicz.dirDeriv_subadd, MathlibExt.Analysis.Convex.Straszewicz.dirDeriv_zero, MathlibExt.Analysis.Convex.Straszewicz.dirDeriv_add_neg_nonneg
statement: formalized
proof: formalized
---

# Straszewicz's theorem

22 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/straszewicz-s-theorem/index.html).

## Convex hull of a compact set is compact

Let $E$ be a finite-dimensional real normed
space. If $K \subseteq E$ is compact, then the convex hull of $K$ is compact.

Formalized by `MathlibExt.Analysis.Convex.Straszewicz.IsCompact.convexHull_of_compact`, a theorem declared in [MathlibExt/Analysis/Convex/Straszewicz.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Convex/Straszewicz.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/straszewicz-s-theorem/index.html#convex-hull-of-compact).

## Difference quotients

Let $E$ be a real normed space and $E^*$ its continuous dual. For
$h : E^* \to \mathbb{R}$ and $x, v \in E^*$, the difference quotients of $h$ at $x$ in direction
$v$ form the set $\{(h(x + t v) - h(x))/t : t > 0\}$.

When $h$ is convex this set is bounded below, and its infimum is the one-sided directional
derivative of $h$ at $x$ in direction $v$.

Formalized by `MathlibExt.Analysis.Convex.Straszewicz.dirQuot`, a definition declared in [MathlibExt/Analysis/Convex/Straszewicz.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Convex/Straszewicz.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/straszewicz-s-theorem/index.html#dir-quot).

## Directional derivative

Let $E$ be a real normed space with continuous dual $E^*$. For
$h : E^* \to \mathbb{R}$ and $x, v \in E^*$, the directional derivative of $h$ at $x$ in
direction $v$ is the infimum of the difference quotients,
$h'(x; v) = \inf_{t > 0} \frac{h(x + t v) - h(x)}{t}$, which is taken to be $0$ when these
quotients are not bounded below.

For convex $h$ the quotients are bounded below, so this is the usual one-sided directional
derivative.

Formalized by `MathlibExt.Analysis.Convex.Straszewicz.dirDeriv`, a definition declared in [MathlibExt/Analysis/Convex/Straszewicz.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Convex/Straszewicz.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/straszewicz-s-theorem/index.html#dir-deriv).

## Restriction of a convex function to a line

Let $E$ be a real normed space with
continuous dual $E^*$, and let $h : E^* \to \mathbb{R}$ be convex. For all $x, v \in E^*$, the
function $s \mapsto h(x + s v)$ is convex on $\mathbb{R}$.

Formalized by `MathlibExt.Analysis.Convex.Straszewicz.convexOn_line`, a theorem declared in [MathlibExt/Analysis/Convex/Straszewicz.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Convex/Straszewicz.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/straszewicz-s-theorem/index.html#convex-on-line).

## Difference quotients of a convex function are bounded below

Let $E$ be a real normed
space, $E^*$ its continuous dual, and $h : E^* \to \mathbb{R}$ a convex function. For all
$x, v \in E^*$, the set of difference quotients $\{(h(x + t v) - h(x))/t : t > 0\}$ is bounded
below.

The bound comes from comparing slopes of $h$ on the line through $x$ in direction $v$.

Formalized by `MathlibExt.Analysis.Convex.Straszewicz.dirQuot_bddBelow`, a theorem declared in [MathlibExt/Analysis/Convex/Straszewicz.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Convex/Straszewicz.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/straszewicz-s-theorem/index.html#dir-quot-bdd-below).

## Subadditivity of the directional derivative

Let $E$ be a real normed space with
continuous dual $E^*$, let $h : E^* \to \mathbb{R}$ be convex, and write $h'(x; v)$ for the
directional derivative of $h$ at $x$ in direction $v$. For all $x, v, w \in E^*$,
$h'(x; v + w) \le h'(x; v) + h'(x; w)$.

Formalized by `MathlibExt.Analysis.Convex.Straszewicz.dirDeriv_subadd`, a theorem declared in [MathlibExt/Analysis/Convex/Straszewicz.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Convex/Straszewicz.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/straszewicz-s-theorem/index.html#dir-deriv-subadd).

## Directional derivative in direction zero

Let $E$ be a real normed space with continuous
dual $E^*$ and let $h : E^* \to \mathbb{R}$ be any function. For every $x \in E^*$, the directional
derivative of $h$ at $x$ in direction $0$ is $0$.

Formalized by `MathlibExt.Analysis.Convex.Straszewicz.dirDeriv_zero`, a theorem declared in [MathlibExt/Analysis/Convex/Straszewicz.lean, line 327](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Convex/Straszewicz.lean#L327). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/straszewicz-s-theorem/index.html#dir-deriv-zero).

## Opposite directional derivatives have nonnegative sum

Let $E$ be a real normed space
with continuous dual $E^*$, let $h : E^* \to \mathbb{R}$ be convex, and write $h'(x; v)$ for the
directional derivative of $h$ at $x$ in direction $v$. For all $x, v \in E^*$,
$h'(x; v) + h'(x; -v) \ge 0$.

Formalized by `MathlibExt.Analysis.Convex.Straszewicz.dirDeriv_add_neg_nonneg`, a theorem declared in [MathlibExt/Analysis/Convex/Straszewicz.lean, line 348](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Convex/Straszewicz.lean#L348). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/straszewicz-s-theorem/index.html#dir-deriv-add-neg-nonneg).

## Support function

For a set $K$ in a real normed space $E$, the support function of $K$
sends a continuous linear functional $\ell$ on $E$ to the supremum $\sup_{x \in K} \ell(x)$ of the
values of $\ell$ on $K$.

The supremum is taken in $\mathbb{R}$, so it is $0$ when $K$ is empty or $\ell$ is unbounded
above on $K$; for nonempty compact $K$ it is attained.

Formalized by `MathlibExt.Analysis.Convex.Straszewicz.suppFunc`, a definition declared in [MathlibExt/Analysis/Convex/Straszewicz.lean, line 361](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Convex/Straszewicz.lean#L361). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/straszewicz-s-theorem/index.html#supp-func).

## The support function of a compact set is attained

Let $K$ be a nonempty compact subset
of a real normed space $E$, and let $h_K(l) = \sup_{x \in K} l(x)$ be its support function on the
continuous dual $E^*$. For every $l \in E^*$ there is $x \in K$ with $l(x) = h_K(l)$.

Formalized by `MathlibExt.Analysis.Convex.Straszewicz.suppFunc_attain`, a theorem declared in [MathlibExt/Analysis/Convex/Straszewicz.lean, line 366](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Convex/Straszewicz.lean#L366). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/straszewicz-s-theorem/index.html#supp-func-attain).

## The support function of a compact set is convex

Let $K$ be a nonempty compact subset of
a real normed space $E$. Its support function $h_K(l) = \sup_{x \in K} l(x)$ is a convex function
on the whole continuous dual $E^*$.

Formalized by `MathlibExt.Analysis.Convex.Straszewicz.suppFunc_convex`, a theorem declared in [MathlibExt/Analysis/Convex/Straszewicz.lean, line 376](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Convex/Straszewicz.lean#L376). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/straszewicz-s-theorem/index.html#supp-func-convex).

## The support function of a compact set is Lipschitz

Let $K$ be a nonempty compact subset
of a real normed space $E$, and let $h_K(l) = \sup_{x \in K} l(x)$ be its support function on the
continuous dual $E^*$. There is a constant $C \ge 0$ such that
$h_K(l_1) - h_K(l_2) \le C \|l_1 - l_2\|$ for all $l_1, l_2 \in E^*$, where $\|\cdot\|$ is the
operator norm.

Formalized by `MathlibExt.Analysis.Convex.Straszewicz.suppFunc_lipschitz`, a theorem declared in [MathlibExt/Analysis/Convex/Straszewicz.lean, line 398](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Convex/Straszewicz.lean#L398). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/straszewicz-s-theorem/index.html#supp-func-lipschitz).

## The support function of a compact set is continuous

Let $K$ be a nonempty compact
subset of a real normed space $E$. Its support function $h_K(l) = \sup_{x \in K} l(x)$ is
continuous on the continuous dual $E^*$ with the operator norm.

Formalized by `MathlibExt.Analysis.Convex.Straszewicz.suppFunc_continuous`, a theorem declared in [MathlibExt/Analysis/Convex/Straszewicz.lean, line 420](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Convex/Straszewicz.lean#L420). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/straszewicz-s-theorem/index.html#supp-func-continuous).

## Gateaux points

Let $E$ be a real normed space, $E^*$ its continuous dual, and
$h : E^* \to \mathbb{R}$. For $x, v \in E^*$ let $h'(x; v)$ be the infimum of the difference
quotients $(h(x + t v) - h(x))/t$ over $t > 0$, taken to be $0$ when they are unbounded below.
A point $x \in E^*$ is a Gateaux point of $h$ when $h'(x; v) + h'(x; -v) \le 0$ for every
$v \in E^*$.

Formalized by `MathlibExt.Analysis.Convex.Straszewicz.GateauxPt`, a definition declared in [MathlibExt/Analysis/Convex/Straszewicz.lean, line 453](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Convex/Straszewicz.lean#L453). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/straszewicz-s-theorem/index.html#gateaux-pt).

## Strict sublevel sets of the symmetrized directional derivative are open

Let $E$ be a
real normed space with continuous dual $E^*$, let $K \subseteq E$ be a nonempty compact set with
support function $h_K$, and write $h_K'(x; v)$ for the directional derivative of $h_K$ at $x$ in
direction $v$. For every $v \in E^*$ and every real $c$, the set of $x \in E^*$ with
$h_K'(x; v) + h_K'(x; -v) < c$ is open.

Formalized by `MathlibExt.Analysis.Convex.Straszewicz.dirDeriv_sublevel_open`, a theorem declared in [MathlibExt/Analysis/Convex/Straszewicz.lean, line 458](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Convex/Straszewicz.lean#L458). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/straszewicz-s-theorem/index.html#dir-deriv-sublevel-open).

## Continuity of the directional derivative of a support function in the direction

Let
$E$ be a real normed space with continuous dual $E^*$, let $K \subseteq E$ be a nonempty compact
set with support function $h_K$, and write $h_K'(x; w)$ for the directional derivative of $h_K$
at $x$ in direction $w$. For every $x \in E^*$, the map $w \mapsto h_K'(x; w)$ is continuous on
$E^*$.

Formalized by `MathlibExt.Analysis.Convex.Straszewicz.dirDeriv_continuous_in_v`, a theorem declared in [MathlibExt/Analysis/Convex/Straszewicz.lean, line 525](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Convex/Straszewicz.lean#L525). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/straszewicz-s-theorem/index.html#dir-deriv-continuous-in-v).

## Lipschitz bound on directional derivatives of a support function

Let $E$ be a real
normed space with continuous dual $E^*$, let $K \subseteq E$ be a nonempty compact set with
support function $h_K$, and write $h_K'(x; w)$ for the directional derivative of $h_K$ at $x$ in
direction $w$. If $C$ is a real number with $h_K(\ell_1) - h_K(\ell_2) \le C \|\ell_1 - \ell_2\|$
for all $\ell_1, \ell_2 \in E^*$, then $h_K'(x; w) \le C \|w\|$ for all $x, w \in E^*$.

Formalized by `MathlibExt.Analysis.Convex.Straszewicz.dirDeriv_suppFunc_bound`, a theorem declared in [MathlibExt/Analysis/Convex/Straszewicz.lean, line 582](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Convex/Straszewicz.lean#L582). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/straszewicz-s-theorem/index.html#dir-deriv-supp-func-bound).

## Mazur's theorem for support functions

Let $E$ be a finite-dimensional real normed space
with continuous dual $E^*$, let $K \subseteq E$ be a nonempty compact set with support function
$h_K$, and write $h_K'(\ell; v)$ for the directional derivative of $h_K$ at $\ell$ in direction
$v$. Then the Gateaux points of $h_K$, that is, the functionals $\ell \in E^*$ with
$h_K'(\ell; v) + h_K'(\ell; -v) \le 0$ for every $v \in E^*$, form a dense subset of $E^*$.

Formalized by `MathlibExt.Analysis.Convex.Straszewicz.dense_gateaux`, a theorem declared in [MathlibExt/Analysis/Convex/Straszewicz.lean, line 597](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Convex/Straszewicz.lean#L597). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/straszewicz-s-theorem/index.html#dense-gateaux).

## A maximizer bounds the directional derivative of the support function from below

Let
$K$ be a nonempty compact subset of a real normed space $E$, let $h_K(l) = \sup_{y \in K} l(y)$
be its support function on the continuous dual $E^*$, and write $h_K'(u; v)$ for the
directional derivative of $h_K$ at $u$ in direction $v$. If $u \in E^*$ and $z \in K$ satisfy
$u(z) = h_K(u)$, then $v(z) \le h_K'(u; v)$ for every $v \in E^*$.

Formalized by `MathlibExt.Analysis.Convex.Straszewicz.maximizer_dirDeriv_ge`, a theorem declared in [MathlibExt/Analysis/Convex/Straszewicz.lean, line 992](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Convex/Straszewicz.lean#L992). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/straszewicz-s-theorem/index.html#maximizer-dir-deriv-ge).

## Maximizers at a Gateaux point of the support function are unique

Let $K$ be a
nonempty compact subset of a real normed space $E$, and let $h_K(l) = \sup_{y \in K} l(y)$ be its
support function on the continuous dual $E^*$. If $l \in E^*$ is a Gateaux point of $h_K$ and
$z_1, z_2 \in K$ satisfy $l(z_1) = h_K(l)$ and $l(z_2) = h_K(l)$, then $z_1 = z_2$.

Formalized by `MathlibExt.Analysis.Convex.Straszewicz.gateaux_unique_maximizer`, a theorem declared in [MathlibExt/Analysis/Convex/Straszewicz.lean, line 1014](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Convex/Straszewicz.lean#L1014). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/straszewicz-s-theorem/index.html#gateaux-unique-maximizer).

## A unique maximizer of a linear functional is an exposed point

Let $K$ be a nonempty
compact set in a real normed space $E$, let $\ell$ be a continuous linear functional on $E$, and
let $h_K$ be the support function of $K$. If $z \in K$ satisfies $\ell(z) = h_K(\ell)$ and every
$y \in K$ with $\ell(y) = h_K(\ell)$ equals $z$, then $z$ is an exposed point of $K$.

Formalized by `MathlibExt.Analysis.Convex.Straszewicz.unique_maximizer_exposed`, a theorem declared in [MathlibExt/Analysis/Convex/Straszewicz.lean, line 1037](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Convex/Straszewicz.lean#L1037). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/straszewicz-s-theorem/index.html#unique-maximizer-exposed).

## Straszewicz's theorem

Let $E$ be a finite-dimensional real normed space and let
$A \subseteq E$ be a compact convex set. Then every extreme point of $A$ lies in the closure of
the set of exposed points of $A$.

Formalized by `MathlibExt.Analysis.Convex.Straszewicz.straszewicz_theorem`, a theorem declared in [MathlibExt/Analysis/Convex/Straszewicz.lean, line 1057](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Convex/Straszewicz.lean#L1057). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/straszewicz-s-theorem/index.html#straszewicz-theorem).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Straszewicz's theorem](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/straszewicz-s-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/convex-geometry/straszewicz-s-theorem)
