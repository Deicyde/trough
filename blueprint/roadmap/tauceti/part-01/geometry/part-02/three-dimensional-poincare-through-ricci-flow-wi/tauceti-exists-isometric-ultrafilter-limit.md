---
declaration: theorem
origin: cited
lean: TauCeti.exists_isometric_ultrafilter_limit
statement: formalized
proof: formalized
---

# TauCeti.exists_isometric_ultrafilter_limit

Compactness constructs one simultaneous isometric limit from actual
pairwise distance convergence, without a supplied embedding.

```lean
TauCeti.exists_isometric_ultrafilter_limit.{u_1, u_2, u_3} {A : Type u_1} {B : Type u_2}
  {ι : Type u_3} [PseudoMetricSpace A] [MetricSpace B] [CompactSpace B] {l : Filter ι} [l.NeBot]
  (f : ι → A → B)
  (hdist : ∀ (x y : A), Filter.Tendsto (fun k => dist (f k x) (f k y)) l (nhds (dist x y))) :
  ∃ U, ↑U ≤ l ∧ ∃ e, Isometry e ∧ ∀ (x : A), Filter.Tendsto (fun k => f k x) (↑U) (nhds (e x))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_isometric_ultrafilter_limit`](https://taucetiproject.org/docs/TauCeti/Topology/MetricSpace/Isometry/CompactLimit.html#TauCeti.exists_isometric_ultrafilter_limit).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_isometric_ultrafilter_limit`](https://taucetiproject.org/docs/TauCeti/Topology/MetricSpace/Isometry/CompactLimit.html#TauCeti.exists_isometric_ultrafilter_limit)
- [Source of `TauCeti.exists_isometric_ultrafilter_limit` in TauCeti/Topology/MetricSpace/Isometry/CompactLimit.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/MetricSpace/Isometry/CompactLimit.lean#L68)
- [Tau Ceti roadmap status: Three-dimensional Poincaré through Ricci flow with surgery](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/Poincare3D/STATUS.md)
