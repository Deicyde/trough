---
declaration: theorem
origin: cited
lean: TauCeti.expReTrivialization_notMem_maximalAtlas
statement: formalized
proof: formalized
---

# TauCeti.expReTrivialization_notMem_maximalAtlas

The gauge transform of the standard trivialization by `exp (re z)` is not a holomorphic
trivialization of the trivial line bundle over `ℂ`, at any positive order of smoothness.

```lean
TauCeti.expReTrivialization_notMem_maximalAtlas {n : WithTop ℕ∞} (hn : n ≠ 0) :
  TauCeti.expReTrivialization.toOpenPartialHomeomorph ∉
    StructureGroupoid.maximalAtlas (Bundle.TotalSpace ℂ (Bundle.Trivial ℂ ℂ))
      (contMDiffFiberwiseLinear ℂ ℂ (modelWithCornersSelf ℂ ℂ) n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Bundle.Trivialization.mem_maximalAtlas_contMDiffFiberwiseLinear_iff](bundle-trivialization-mem-maximalatlas-contmdiff.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.expReTrivialization_notMem_maximalAtlas`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/Holomorphic/ExpReGauge.html#TauCeti.expReTrivialization_notMem_maximalAtlas).

## Sources

- [Tau Ceti documentation: `TauCeti.expReTrivialization_notMem_maximalAtlas`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/Holomorphic/ExpReGauge.html#TauCeti.expReTrivialization_notMem_maximalAtlas)
- [Source of `TauCeti.expReTrivialization_notMem_maximalAtlas` in TauCeti/Geometry/Manifold/VectorBundle/Holomorphic/ExpReGauge.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/VectorBundle/Holomorphic/ExpReGauge.lean#L121)
- [Tau Ceti roadmap status: Complex manifolds: transport, quotients, bundles, and gluing](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ComplexManifolds/STATUS.md)
