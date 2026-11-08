---
declaration: theorem
origin: cited
lean: TauCeti.RiemannSurface.apply_eq_of_eventuallyConst
statement: formalized
proof: formalized
---

# The identity theorem for Riemann surfaces

A holomorphic map on a connected Riemann
surface which is constant near one point is constant.

```lean
TauCeti.RiemannSurface.apply_eq_of_eventuallyConst.{u_1, u_2} {X : Type u_1} {Y : Type u_2}
  [TopologicalSpace X] [ChartedSpace ℂ X] [TopologicalSpace Y] [ChartedSpace ℂ Y]
  [IsManifold (modelWithCornersSelf ℂ ℂ) 1 X] [IsManifold (modelWithCornersSelf ℂ ℂ) 1 Y]
  {f : X → Y} [PreconnectedSpace X] (hf : MDiff f) {x : X} (hx : Filter.EventuallyConst f (nhds x))
  (x' : X) : f x' = f x
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.RiemannSurface.apply_eq_of_eventuallyConst`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/RiemannSurface/IdentityTheorem.html#TauCeti.RiemannSurface.apply_eq_of_eventuallyConst).

## Sources

- [Tau Ceti documentation: `TauCeti.RiemannSurface.apply_eq_of_eventuallyConst`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/RiemannSurface/IdentityTheorem.html#TauCeti.RiemannSurface.apply_eq_of_eventuallyConst)
- [Source of `TauCeti.RiemannSurface.apply_eq_of_eventuallyConst` in TauCeti/Analysis/Complex/RiemannSurface/IdentityTheorem.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/RiemannSurface/IdentityTheorem.lean#L86)
