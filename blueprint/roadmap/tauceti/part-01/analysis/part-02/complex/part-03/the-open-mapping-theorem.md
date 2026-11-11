---
declaration: theorem
origin: cited
lean: TauCeti.RiemannSurface.isOpenMap_of_forall_not_eventuallyConst, TauCeti.RiemannSurface.nhds_le_map_nhds_of_not_eventuallyConst
statement: formalized
proof: formalized
---

# The open mapping theorem

A holomorphic map between Riemann surfaces which is constant
near no point is an open map.

```lean
TauCeti.RiemannSurface.isOpenMap_of_forall_not_eventuallyConst.{u_1, u_2} {X : Type u_1}
  {Y : Type u_2} [TopologicalSpace X] [ChartedSpace ℂ X] [TopologicalSpace Y] [ChartedSpace ℂ Y]
  [IsManifold (modelWithCornersSelf ℂ ℂ) 1 X] [IsManifold (modelWithCornersSelf ℂ ℂ) 1 Y]
  {f : X → Y} (hf : MDiff f) (hne : ∀ (x : X), ¬Filter.EventuallyConst f (nhds x)) : IsOpenMap f
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Rouché's theorem for a disc, classical form](rouches-theorem-for-a-disc-classical-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.RiemannSurface.isOpenMap_of_forall_not_eventuallyConst`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/RiemannSurface/OpenMapping.html#TauCeti.RiemannSurface.isOpenMap_of_forall_not_eventuallyConst).

## Other forms

**The open mapping theorem, at a point.** Formalized in Tau Ceti as [`TauCeti.RiemannSurface.nhds_le_map_nhds_of_not_eventuallyConst`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/RiemannSurface/OpenMapping.html#TauCeti.RiemannSurface.nhds_le_map_nhds_of_not_eventuallyConst).

```lean
TauCeti.RiemannSurface.nhds_le_map_nhds_of_not_eventuallyConst.{u_1, u_2} {X : Type u_1}
  {Y : Type u_2} [TopologicalSpace X] [ChartedSpace ℂ X] [TopologicalSpace Y] [ChartedSpace ℂ Y]
  [IsManifold (modelWithCornersSelf ℂ ℂ) 1 X] [IsManifold (modelWithCornersSelf ℂ ℂ) 1 Y]
  {f : X → Y} {x : X} (hf : ∀ᶠ (y : X) in nhds x, MDiffAt f y)
  (hne : ¬Filter.EventuallyConst f (nhds x)) : nhds (f x) ≤ Filter.map f (nhds x)
```

## Sources

- [Tau Ceti documentation: `TauCeti.RiemannSurface.isOpenMap_of_forall_not_eventuallyConst`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/RiemannSurface/OpenMapping.html#TauCeti.RiemannSurface.isOpenMap_of_forall_not_eventuallyConst)
- [Source of `TauCeti.RiemannSurface.isOpenMap_of_forall_not_eventuallyConst` in TauCeti/Analysis/Complex/RiemannSurface/OpenMapping.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/RiemannSurface/OpenMapping.lean#L67)
