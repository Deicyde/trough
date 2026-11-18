# Hölder continuity

A function `f : X → Y` between two `PseudoEMetricSpace`s is Hölder continuous with constant
`C : ℝ≥0` and exponent `r : ℝ≥0`, if `edist (f x) (f y) ≤ C * edist x y ^ r` for all `x y : X`.

```lean
HolderWith.{u_1, u_2} {X : Type u_1} {Y : Type u_2} [PseudoEMetricSpace X] [PseudoEMetricSpace Y]
  (C r : NNReal) (f : X → Y) : Prop
```

## Depends on

- [Real number](../../general-algebra/numbers/real-number.md)

## Sources

- [Mathlib documentation: `HolderWith`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/MetricSpace/Holder.html#HolderWith)
- [Source of `HolderWith` in Mathlib/Topology/MetricSpace/Holder.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Topology/MetricSpace/Holder.lean#L48)
- [Mathlib overview: Topology › Metric spaces](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/overview.yaml#L265)
