---
declaration: section
origin: cited
lean: Metric.IsGeodesicOnWithSpeed, Metric.IsGeodesicOn, Metric.IsGeodesic, Metric.IsClosedGeodesic, Metric.isGeodesic_const, Metric.not_isClosedGeodesic_const, Metric.isGeodesicOnWithSpeed_lineMap, Metric.isGeodesic_lineMap
statement: formalized
proof: formalized
---

# Geodesics in metric spaces

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/metric-geometry/geodesics-in-metric-spaces/index.html).

## Geodesics of a given speed on a set of times

Let $X$ be a pseudo-extended metric space
with extended distance $d$, let $\gamma : \mathbb{R} \to X$ be a curve, $s \subseteq \mathbb{R}$ a
set of times and $c \ge 0$ a real number. The curve $\gamma$ is a geodesic of speed $c$ on $s$ if
every $t \in s$ has some $\varepsilon > 0$ such that $d(\gamma(t_1), \gamma(t_2)) = c\,|t_1 - t_2|$
for all $t_1, t_2 \in s$ with $|t_1 - t| < \varepsilon$ and $|t_2 - t| < \varepsilon$.

Formalized by `Metric.IsGeodesicOnWithSpeed`, a definition declared in [MathlibExt/Topology/MetricSpace/Geodesic.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/MetricSpace/Geodesic.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/metric-geometry/geodesics-in-metric-spaces/index.html#is-geodesic-on-with-speed).

## Geodesic on a set of times

Let $X$ be a pseudo-extended metric space. A curve
$\gamma : \mathbb{R} \to X$ is a geodesic on a set of times $s \subseteq \mathbb{R}$ if, for some
real number $c \ge 0$, it is a geodesic of speed $c$ on $s$.

On a Riemannian manifold without boundary, with its Riemannian distance, every Riemannian geodesic
is a geodesic in this sense, and the piecewise $C^1$ geodesics in this sense are the Riemannian
geodesics.

Formalized by `Metric.IsGeodesicOn`, a definition declared in [MathlibExt/Topology/MetricSpace/Geodesic.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/MetricSpace/Geodesic.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/metric-geometry/geodesics-in-metric-spaces/index.html#is-geodesic-on).

## Geodesics defined for all times

Let $X$ be a pseudo-extended metric space. A curve
$\gamma : \mathbb{R} \to X$ is a geodesic if it is a geodesic on the set of all times
$\mathbb{R}$.

Formalized by `Metric.IsGeodesic`, a definition declared in [MathlibExt/Topology/MetricSpace/Geodesic.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/MetricSpace/Geodesic.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/metric-geometry/geodesics-in-metric-spaces/index.html#is-geodesic).

## Closed geodesic

Let $X$ be a pseudo-extended metric space. A curve
$\gamma : \mathbb{R} \to X$ is a closed geodesic if it is a geodesic defined on all of $\mathbb{R}$,
it is periodic with some period $T > 0$ (that is, $\gamma(t + T) = \gamma(t)$ for all
$t \in \mathbb{R}$), and it is not constant: $\gamma(t_1) \ne \gamma(t_2)$ for some
$t_1, t_2 \in \mathbb{R}$.

Periodicity of a geodesic defined on all of $\mathbb{R}$ encodes both $\gamma(0) = \gamma(T)$ and
the matching of the velocities at $0$ and $T$. For a closed geodesic of speed $1$, every period
$T > 0$ is the length of $\gamma$ traversed over one period; its smallest positive period is the
length of the underlying prime closed geodesic.

Formalized by `Metric.IsClosedGeodesic`, a definition declared in [MathlibExt/Topology/MetricSpace/Geodesic.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/MetricSpace/Geodesic.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/metric-geometry/geodesics-in-metric-spaces/index.html#is-closed-geodesic).

## Constant curves are geodesics

Let $X$ be a pseudo-extended metric space. For every point
$p \in X$, the constant curve $\mathbb{R} \to X$, $t \mapsto p$, is a geodesic.

Its speed is $0$.

Formalized by `Metric.isGeodesic_const`, a theorem declared in [MathlibExt/Topology/MetricSpace/Geodesic.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/MetricSpace/Geodesic.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/metric-geometry/geodesics-in-metric-spaces/index.html#is-geodesic-const).

## Constant curves are not closed geodesics

Let $X$ be a pseudo-extended metric space. For
every point $p \in X$, the constant curve $\mathbb{R} \to X$, $t \mapsto p$, is not a closed
geodesic.

Formalized by `Metric.not_isClosedGeodesic_const`, a theorem declared in [MathlibExt/Topology/MetricSpace/Geodesic.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/MetricSpace/Geodesic.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/metric-geometry/geodesics-in-metric-spaces/index.html#not-is-closed-geodesic-const).

## Straight lines are geodesics of constant speed

Let $F$ be a real normed space and
$p, v \in F$. For every set of times $s \subseteq \mathbb{R}$, the straight line
$t \mapsto p + t v$ is a geodesic of speed $\|v\|$ on $s$.

Formalized by `Metric.isGeodesicOnWithSpeed_lineMap`, a theorem declared in [MathlibExt/Topology/MetricSpace/Geodesic.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/MetricSpace/Geodesic.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/metric-geometry/geodesics-in-metric-spaces/index.html#is-geodesic-on-with-speed-line-map).

## Straight lines are geodesics

Let $F$ be a real normed space. For all $p, v \in F$, the
straight line $\mathbb{R} \to F$, $t \mapsto p + t v$, is a geodesic.

Formalized by `Metric.isGeodesic_lineMap`, a theorem declared in [MathlibExt/Topology/MetricSpace/Geodesic.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/MetricSpace/Geodesic.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/metric-geometry/geodesics-in-metric-spaces/index.html#is-geodesic-line-map).

## Closed geodesics are not constant

Let $X$ be a pseudo-extended metric space. If
$\gamma : \mathbb{R} \to X$ is a closed geodesic, then for every $p \in X$, $\gamma$ is not the
constant curve $t \mapsto p$.

Formalized by `Metric.IsClosedGeodesic.not_const`, a theorem declared in [MathlibExt/Topology/MetricSpace/Geodesic.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/MetricSpace/Geodesic.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/metric-geometry/geodesics-in-metric-spaces/index.html#not-const).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Geodesics in metric spaces](https://deicyde.github.io/atlas-lean/roadmap/Geometry/metric-geometry/geodesics-in-metric-spaces/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Geometry/metric-geometry/geodesics-in-metric-spaces)
