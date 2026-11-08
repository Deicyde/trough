---
declaration: theorem
origin: cited
lean: TauCeti.IsLocallyCollared.isCollared
statement: formalized
proof: formalized
---

# Brown's collaring theorem, for a compact domain

an injective, locally collared map from a
compact space into a Hausdorff space is collared. The local collars are assembled into one by
pushing an external collar inward along each of them in turn (Connelly's proof).

```lean
TauCeti.IsLocallyCollared.isCollared.{u_1, u_2} {M : Type u_1} {N : Type u_2} [TopologicalSpace M]
  [TopologicalSpace N] {f : N → M} [CompactSpace N] [T2Space M] (h : TauCeti.IsLocallyCollared f)
  (hf : Function.Injective f) : TauCeti.IsCollared f
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsLocallyCollared.isCollared`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Boundary/Collar/Brown.html#TauCeti.IsLocallyCollared.isCollared).

## Sources

- [Tau Ceti documentation: `TauCeti.IsLocallyCollared.isCollared`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Boundary/Collar/Brown.html#TauCeti.IsLocallyCollared.isCollared)
- [Source of `TauCeti.IsLocallyCollared.isCollared` in TauCeti/Geometry/Manifold/Boundary/Collar/Brown.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Boundary/Collar/Brown.lean#L456)
