---
declaration: section
origin: cited
lean: Metric.IsDeltaHyperbolic, Metric.IsGromovHyperbolic, Metric.IsDeltaHyperbolic.four_point, Metric.IsDeltaHyperbolic.mono, Metric.IsDeltaHyperbolic.nonneg, Metric.isDeltaHyperbolic_zero_of_subsingleton
statement: formalized
proof: formalized
---

# Gromov-hyperbolic spaces

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/metric-geometry/gromov-hyperbolic-spaces/index.html).

## Gromov $\delta$-hyperbolic space

A pseudometric space `X` is `δ`-hyperbolic (in the sense of Gromov) if `0 ≤ δ` and the
Gromov product satisfies the four-point inequality
`(x ∣ z)_w ≥ min (x ∣ y)_w (y ∣ z)_w - δ` for all points `w x y z`, where
`(x ∣ y)_w = Metric.gromovProduct w x y` (basepoint first, as in Mathlib).

Formalized by `Metric.IsDeltaHyperbolic`, a definition declared in [MathlibExt/Topology/MetricSpace/GromovHyperbolic.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/MetricSpace/GromovHyperbolic.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/metric-geometry/gromov-hyperbolic-spaces/index.html#is-delta-hyperbolic).

## Gromov-hyperbolic spaces

A pseudometric space $X$ is Gromov-hyperbolic if there is a
real number $\delta$ such that $X$ is $\delta$-hyperbolic.

Formalized by `Metric.IsGromovHyperbolic`, a definition declared in [MathlibExt/Topology/MetricSpace/GromovHyperbolic.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/MetricSpace/GromovHyperbolic.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/metric-geometry/gromov-hyperbolic-spaces/index.html#is-gromov-hyperbolic).

## Four-point inequality of a $\delta$-hyperbolic space

The defining four-point inequality of a `δ`-hyperbolic space.

Formalized by `Metric.IsDeltaHyperbolic.four_point`, a theorem declared in [MathlibExt/Topology/MetricSpace/GromovHyperbolic.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/MetricSpace/GromovHyperbolic.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/metric-geometry/gromov-hyperbolic-spaces/index.html#four-point).

## Hyperbolicity is monotone in the constant

If a pseudometric space $X$ is
$\delta$-hyperbolic and $\delta \le \delta'$, then $X$ is $\delta'$-hyperbolic.

Formalized by `Metric.IsDeltaHyperbolic.mono`, a theorem declared in [MathlibExt/Topology/MetricSpace/GromovHyperbolic.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/MetricSpace/GromovHyperbolic.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/metric-geometry/gromov-hyperbolic-spaces/index.html#mono).

## The hyperbolicity constant is nonnegative

If a pseudometric space $X$ is
$\delta$-hyperbolic, then $\delta \ge 0$.

Formalized by `Metric.IsDeltaHyperbolic.nonneg`, a theorem declared in [MathlibExt/Topology/MetricSpace/GromovHyperbolic.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/MetricSpace/GromovHyperbolic.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/metric-geometry/gromov-hyperbolic-spaces/index.html#nonneg).

## A space with at most one point is $0$-hyperbolic

Every pseudometric space $X$ with at
most one point is $0$-hyperbolic.

Formalized by `Metric.isDeltaHyperbolic_zero_of_subsingleton`, a theorem declared in [MathlibExt/Topology/MetricSpace/GromovHyperbolic.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/MetricSpace/GromovHyperbolic.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/metric-geometry/gromov-hyperbolic-spaces/index.html#is-delta-hyperbolic-zero-of-subsingleton).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Gromov-hyperbolic spaces](https://deicyde.github.io/atlas-lean/roadmap/Geometry/metric-geometry/gromov-hyperbolic-spaces/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Geometry/metric-geometry/gromov-hyperbolic-spaces)
