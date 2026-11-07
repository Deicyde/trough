---
declaration: theorem
origin: cited
lean: TauCeti.holomorphicStructureSheaf.isFractionRing_meromorphicGerms
statement: formalized
proof: formalized
---

# TauCeti.holomorphicStructureSheaf.isFractionRing\_meromorphicGerms

The field of meromorphic germs at `a : ℂ` is the fraction field of the ring of holomorphic
germs at `a`.

```lean
TauCeti.holomorphicStructureSheaf.isFractionRing_meromorphicGerms (a : ℂ) :
  IsFractionRing
    ↑((TauCeti.holomorphicStructureSheaf (modelWithCornersSelf ℂ ℂ) ℂ).presheaf.stalk a)
    ↥(TauCeti.meromorphicGerms ℂ a)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.holomorphicStructureSheaf.isFractionRing_meromorphicGerms`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/StructureSheaf/MeromorphicGerm.html#TauCeti.holomorphicStructureSheaf.isFractionRing_meromorphicGerms).

## Sources

- [Tau Ceti documentation: `TauCeti.holomorphicStructureSheaf.isFractionRing_meromorphicGerms`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/StructureSheaf/MeromorphicGerm.html#TauCeti.holomorphicStructureSheaf.isFractionRing_meromorphicGerms)
- [Source of `TauCeti.holomorphicStructureSheaf.isFractionRing_meromorphicGerms` in TauCeti/Geometry/Manifold/Complex/StructureSheaf/MeromorphicGerm.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Complex/StructureSheaf/MeromorphicGerm.lean#L139)
- [Tau Ceti roadmap status: Complex manifolds, Dolbeault theory, and Kähler geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ComplexKahlerGeometry/STATUS.md)
