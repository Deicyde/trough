---
declaration: def
origin: cited
lean: TauCeti.ManifoldTotalSpace
statement: formalized
---

# TauCeti.ManifoldTotalSpace

A copy of the total space of a fibre bundle whose model fibre `F` is a manifold modelled on
`HF`. It carries the topology of `Bundle.TotalSpace F E` and the charts obtained by following the
trivializations of the atlas with product charts of `B × F`, modelled on `ModelProd HB HF`.

```lean
TauCeti.ManifoldTotalSpace.{u_2, u_3, u_5} {B : Type u_2} (F : Type u_3) (E : B → Type u_5) :
  Type (max u_2 u_5)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ManifoldTotalSpace`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/FiberBundle/Basic.html#TauCeti.ManifoldTotalSpace).

## Sources

- [Tau Ceti documentation: `TauCeti.ManifoldTotalSpace`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/FiberBundle/Basic.html#TauCeti.ManifoldTotalSpace)
- [Source of `TauCeti.ManifoldTotalSpace` in TauCeti/Geometry/Manifold/FiberBundle/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/FiberBundle/Basic.lean#L203)
- [Tau Ceti roadmap status: Smooth principal bundles, connections, and holonomy](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SmoothBundlesConnections/STATUS.md)
