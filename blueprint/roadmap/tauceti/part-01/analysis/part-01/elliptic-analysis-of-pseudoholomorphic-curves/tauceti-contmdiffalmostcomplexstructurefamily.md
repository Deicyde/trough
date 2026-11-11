---
declaration: structure
origin: cited
lean: TauCeti.ContMDiffAlmostComplexStructureFamily
statement: formalized
---

# TauCeti.ContMDiffAlmostComplexStructureFamily

A jointly `Cⁿ` vertical tangent endomorphism with square minus the identity at every pair
of a domain point and a target point.

```lean
TauCeti.ContMDiffAlmostComplexStructureFamily.{u_1, u_2, u_4, u_5, u_7, u_8} {E : Type u_1}
  {H : Type u_2} {EP : Type u_4} {HP : Type u_5} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [TopologicalSpace H] [NormedAddCommGroup EP] [NormedSpace ℝ EP] [TopologicalSpace HP]
  (I : ModelWithCorners ℝ E H) (M : Type u_7) [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I (↑⊤) M] (IP : ModelWithCorners ℝ EP HP) (P : Type u_8) [TopologicalSpace P]
  [ChartedSpace HP P] (n : ℕ∞) : Type (max (max u_1 u_7) u_8)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ContMDiffAlmostComplexStructureFamily`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Manifold/AlmostComplex/Family.html#TauCeti.ContMDiffAlmostComplexStructureFamily).

## Sources

- [Tau Ceti documentation: `TauCeti.ContMDiffAlmostComplexStructureFamily`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Manifold/AlmostComplex/Family.html#TauCeti.ContMDiffAlmostComplexStructureFamily)
- [Source of `TauCeti.ContMDiffAlmostComplexStructureFamily` in TauCeti/Geometry/Symplectic/Manifold/AlmostComplex/Family.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Symplectic/Manifold/AlmostComplex/Family.lean#L46)
- [Tau Ceti roadmap status: Elliptic analysis of pseudoholomorphic curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PseudoholomorphicCurveAnalysis/STATUS.md)
