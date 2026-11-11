---
declaration: structure
origin: cited
lean: TauCeti.ContMDiffAlmostComplexStructure
statement: formalized
---

# TauCeti.ContMDiffAlmostComplexStructure

A `Cⁿ` tangent endomorphism whose square is minus the identity in every fibre.
The ambient manifold is smooth; the structure need only have regularity `n`.

```lean
TauCeti.ContMDiffAlmostComplexStructure.{u_1, u_2, u_4} {E : Type u_1} {H : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H] (I : ModelWithCorners ℝ E H)
  (n : ℕ∞) (M : Type u_4) [TopologicalSpace M] [ChartedSpace H M] [IsManifold I (↑⊤) M] :
  Type (max u_1 u_4)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ContMDiffAlmostComplexStructure`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Manifold/AlmostComplex/ContMDiff.html#TauCeti.ContMDiffAlmostComplexStructure).

## Sources

- [Tau Ceti documentation: `TauCeti.ContMDiffAlmostComplexStructure`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Manifold/AlmostComplex/ContMDiff.html#TauCeti.ContMDiffAlmostComplexStructure)
- [Source of `TauCeti.ContMDiffAlmostComplexStructure` in TauCeti/Geometry/Symplectic/Manifold/AlmostComplex/ContMDiff.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Symplectic/Manifold/AlmostComplex/ContMDiff.lean#L39)
- [Tau Ceti roadmap status: Elliptic analysis of pseudoholomorphic curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PseudoholomorphicCurveAnalysis/STATUS.md)
