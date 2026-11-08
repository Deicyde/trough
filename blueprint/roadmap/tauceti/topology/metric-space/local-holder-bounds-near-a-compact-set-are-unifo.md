---
declaration: theorem
origin: cited
lean: IsCompact.exists_holderOnWith_thickening_and_norm_le
statement: formalized
proof: formalized
---

# Local Hölder bounds near a compact set are uniform on a thickening

If `f` is `α`-Hölder on
a ball around each point of a compact set `K`, with radii and constants depending on the point, then
on some open thickening of `K` the function `f` is `α`-Hölder with one constant and is bounded.

```lean
IsCompact.exists_holderOnWith_thickening_and_norm_le.{u_3, u_4} {X : Type u_3} {Y : Type u_4}
  [PseudoMetricSpace X] [SeminormedAddCommGroup Y] {K : Set X} (hK : IsCompact K) {α : NNReal}
  {f : X → Y} (hf : ∀ x ∈ K, ∃ r > 0, ∃ L, HolderOnWith L α f (Metric.ball x r)) :
  ∃ δ > 0,
    ∃ L M, HolderOnWith L α f (Metric.thickening δ K) ∧ ∀ y ∈ Metric.thickening δ K, ‖f y‖ ≤ ↑M
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`IsCompact.exists_holderOnWith_thickening_and_norm_le`](https://taucetiproject.org/docs/TauCeti/Topology/MetricSpace/Holder.html#IsCompact.exists_holderOnWith_thickening_and_norm_le).

## Sources

- [Tau Ceti documentation: `IsCompact.exists_holderOnWith_thickening_and_norm_le`](https://taucetiproject.org/docs/TauCeti/Topology/MetricSpace/Holder.html#IsCompact.exists_holderOnWith_thickening_and_norm_le)
- [Source of `IsCompact.exists_holderOnWith_thickening_and_norm_le` in TauCeti/Topology/MetricSpace/Holder.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/MetricSpace/Holder.lean#L232)
