---
declaration: theorem
origin: cited
lean: TauCeti.subsingleton_deRhamCohomology_normedSpace
statement: formalized
proof: formalized
---

# The de Rham cohomology of a normed space vanishes in positive degrees

```lean
TauCeti.subsingleton_deRhamCohomology_normedSpace.{u_1} (E : Type u_1) [NormedAddCommGroup E]
  [NormedSpace ℝ E] (k : ℕ) :
  Subsingleton (TauCeti.deRhamCohomology (modelWithCornersSelf ℝ E) E (k + 1))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.subsingleton_deRhamCohomology_normedSpace`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/NormedSpace.html#TauCeti.subsingleton_deRhamCohomology_normedSpace).

## Sources

- [Tau Ceti documentation: `TauCeti.subsingleton_deRhamCohomology_normedSpace`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/NormedSpace.html#TauCeti.subsingleton_deRhamCohomology_normedSpace)
- [Source of `TauCeti.subsingleton_deRhamCohomology_normedSpace` in TauCeti/Geometry/Manifold/DeRham/NormedSpace.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/DeRham/NormedSpace.lean#L63)
- [Tau Ceti roadmap status: Differential geometry — forms, de Rham cohomology, flows, and degree](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DifferentialGeometry/STATUS.md)
