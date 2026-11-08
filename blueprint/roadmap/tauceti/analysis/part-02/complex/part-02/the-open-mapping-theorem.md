---
declaration: theorem
origin: cited
lean: TauCeti.RiemannSurface.isOpenMap_of_forall_not_eventuallyConst, LinearMap.isOpenMap_of_isTate, TauCeti.RiemannSurface.nhds_le_map_nhds_of_not_eventuallyConst
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

- [Henkel's open mapping theorem](../../../../topology/algebra/part-01/henkels-open-mapping-theorem.md)
- [Rouché's theorem for a disc, classical form](../../../part-01/conformal-mapping-and-the-geometric-theory-of-ho/part-02/rouches-theorem-for-a-disc-classical-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.RiemannSurface.isOpenMap_of_forall_not_eventuallyConst`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/RiemannSurface/OpenMapping.html#TauCeti.RiemannSurface.isOpenMap_of_forall_not_eventuallyConst).

## Other forms

**Open Mapping Theorem for normed modules over a Tate ring.** Formalized in Tau Ceti as [`LinearMap.isOpenMap_of_isTate`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/RingOpNorm/OpenMapping.html#LinearMap.isOpenMap_of_isTate).

```lean
LinearMap.isOpenMap_of_isTate.{u_1, u_2, u_3} {R : Type u_1} {M : Type u_2} {N : Type u_3}
  [SeminormedRing R] [TauCeti.NormedRing.IsTate R] [SeminormedAddCommGroup M] [IsUltrametricDist M]
  [CompleteSpace M] [_root_.Module R M] [IsBoundedSMul R M] [NormedAddCommGroup N] [CompleteSpace N]
  [_root_.Module R N] [IsBoundedSMul R N] (f : M →ₗ[R] N) (hf : Continuous ⇑f)
  (hsurj : Function.Surjective ⇑f) : IsOpenMap ⇑f
```

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
- [Source of `TauCeti.RiemannSurface.isOpenMap_of_forall_not_eventuallyConst` in TauCeti/Analysis/Complex/RiemannSurface/OpenMapping.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/RiemannSurface/OpenMapping.lean#L63)
