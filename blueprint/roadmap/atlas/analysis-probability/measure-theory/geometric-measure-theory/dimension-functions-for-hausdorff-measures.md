---
declaration: section
origin: cited
lean: HausdorffDimensionFunction, HausdorffDimensionFunction.continuous, HausdorffDimensionFunction.monotone, HausdorffDimensionFunction.map_zero, HausdorffDimensionFunction.map_pos, HausdorffDimensionFunction.map_eq_zero_iff, HausdorffDimensionFunction.tendsto_zero
statement: formalized
proof: formalized
---

# Dimension functions for Hausdorff measures

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/dimension-functions-for-hausdorff-measures/index.html).

## Hausdorff dimension function

A Hausdorff dimension function (gauge) is a continuous,
non-decreasing function $\psi : [0,\infty) \to [0,\infty)$ with $\psi(0) = 0$ and $\psi(r) > 0$
for every $r > 0$. In particular $\psi(r) \to 0$ as $r \to 0^+$.

## Sources

- Das and Simmons, arXiv:2305.11829v1, line 211; the source gauge on $(0,\infty)$ is extended by $\psi(0) = 0$, and "increasing" is read as non-decreasing.

Formalized by `HausdorffDimensionFunction`, a structure declared in [MathlibExt/Topology/MetricSpace/HausdorffDimensionFunction.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/MetricSpace/HausdorffDimensionFunction.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/dimension-functions-for-hausdorff-measures/index.html#hausdorff-dimension-function).

## Continuity of a Hausdorff dimension function

Every Hausdorff dimension function
$\psi : [0,\infty) \to [0,\infty)$ is continuous.

Formalized by `HausdorffDimensionFunction.continuous`, a theorem declared in [MathlibExt/Topology/MetricSpace/HausdorffDimensionFunction.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/MetricSpace/HausdorffDimensionFunction.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/dimension-functions-for-hausdorff-measures/index.html#continuous).

## Monotonicity of a Hausdorff dimension function

Every Hausdorff dimension function
$\psi : [0,\infty) \to [0,\infty)$ is non-decreasing: if $r \le s$ then $\psi(r) \le \psi(s)$.

Formalized by `HausdorffDimensionFunction.monotone`, a theorem declared in [MathlibExt/Topology/MetricSpace/HausdorffDimensionFunction.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/MetricSpace/HausdorffDimensionFunction.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/dimension-functions-for-hausdorff-measures/index.html#monotone).

## A Hausdorff dimension function vanishes at zero

Every Hausdorff dimension function
$\psi$ satisfies $\psi(0) = 0$.

Formalized by `HausdorffDimensionFunction.map_zero`, a theorem declared in [MathlibExt/Topology/MetricSpace/HausdorffDimensionFunction.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/MetricSpace/HausdorffDimensionFunction.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/dimension-functions-for-hausdorff-measures/index.html#map-zero).

## A Hausdorff dimension function is positive at positive radii

If $\psi$ is a Hausdorff
dimension function and $r > 0$ is a real number, then $\psi(r) > 0$.

Formalized by `HausdorffDimensionFunction.map_pos`, a theorem declared in [MathlibExt/Topology/MetricSpace/HausdorffDimensionFunction.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/MetricSpace/HausdorffDimensionFunction.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/dimension-functions-for-hausdorff-measures/index.html#map-pos).

## A Hausdorff dimension function vanishes only at zero

If $\psi$ is a Hausdorff dimension
function and $r \ge 0$, then $\psi(r) = 0$ if and only if $r = 0$.

Formalized by `HausdorffDimensionFunction.map_eq_zero_iff`, a theorem declared in [MathlibExt/Topology/MetricSpace/HausdorffDimensionFunction.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/MetricSpace/HausdorffDimensionFunction.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/dimension-functions-for-hausdorff-measures/index.html#map-eq-zero-iff).

## A Hausdorff dimension function tends to zero at zero

Every Hausdorff dimension function
$\psi$ satisfies $\psi(r) \to 0$ as $r \to 0^+$, that is, as $r$ tends to $0$ through positive
values.

Formalized by `HausdorffDimensionFunction.tendsto_zero`, a theorem declared in [MathlibExt/Topology/MetricSpace/HausdorffDimensionFunction.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/MetricSpace/HausdorffDimensionFunction.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/dimension-functions-for-hausdorff-measures/index.html#tendsto-zero).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Dimension functions for Hausdorff measures](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/dimension-functions-for-hausdorff-measures/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/MeasureTheory/geometric-measure-theory/dimension-functions-for-hausdorff-measures)
