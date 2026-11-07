---
declaration: def
origin: cited
lean: TauCeti.holomorphicStructureSheaf.quotientSheaf
statement: formalized
---

# TauCeti.holomorphicStructureSheaf.quotientSheaf

The sheaf of holomorphic functions on the normalization which have matching values on each
fibre of the quotient map. For paired node flags this is the normalization construction of the
structure sheaf of a nodal curve.

```lean
TauCeti.holomorphicStructureSheaf.quotientSheaf.{u_1, u_2} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℂ E] {H : Type u_2} [TopologicalSpace H] (I : ModelWithCorners ℂ E H) {X : Type}
  [TopologicalSpace X] [ChartedSpace H X] (s : Setoid X) : TopCat.Sheaf CommRingCat ↧(Quotient s)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.holomorphicStructureSheaf.quotientSheaf`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/StructureSheaf/Quotient.html#TauCeti.holomorphicStructureSheaf.quotientSheaf).

## Sources

- [Tau Ceti documentation: `TauCeti.holomorphicStructureSheaf.quotientSheaf`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/StructureSheaf/Quotient.html#TauCeti.holomorphicStructureSheaf.quotientSheaf)
- [Source of `TauCeti.holomorphicStructureSheaf.quotientSheaf` in TauCeti/Geometry/Manifold/Complex/StructureSheaf/Quotient.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Complex/StructureSheaf/Quotient.lean#L146)
- [Tau Ceti roadmap status: Analytic families and moduli of complex curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ComplexCurveModuli/STATUS.md)
