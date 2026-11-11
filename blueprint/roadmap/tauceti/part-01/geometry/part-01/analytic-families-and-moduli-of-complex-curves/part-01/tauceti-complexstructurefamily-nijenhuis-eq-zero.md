---
declaration: theorem
origin: cited
lean: TauCeti.ComplexStructureFamily.nijenhuis_eq_zero_iff
statement: formalized
proof: formalized
---

# TauCeti.ComplexStructureFamily.nijenhuis_eq_zero_iff

The full product criterion: the mixed and horizontal equations, together with fibrewise
vanishing, are equivalent to vanishing of the total Nijenhuis tensor. In particular, when the
fibres are integrable, both of the corrected family equations remain necessary.

```lean
TauCeti.ComplexStructureFamily.nijenhuis_eq_zero_iff.{u_1, u_2} {B : Type u_1} {V : Type u_2}
  [NormedAddCommGroup B] [NormedSpace ℝ B] [NormedAddCommGroup V] [NormedSpace ℝ V]
  [FiniteDimensional ℝ B] [FiniteDimensional ℝ V]
  (J : TauCeti.SmoothAlmostComplexStructure (modelWithCornersSelf ℝ (B × V)) (B × V))
  (i : B →L[ℝ] B) (α : B × V → B →L[ℝ] V) (j : B × V → V →L[ℝ] V) {p : B × V}
  (hJ :
    (fun q => J.toEndomorphism q) =ᶠ[nhds p] TauCeti.ComplexStructureFamily.blockEndomorphism i α j)
  (hα : DifferentiableAt ℝ α p) (hj : DifferentiableAt ℝ j p) :
  J.nijenhuis p = 0 ↔
    (∀ (a : B) (v : V), TauCeti.ComplexStructureFamily.mixedTerm i α j p a v = 0) ∧
      (∀ (a b : B), TauCeti.ComplexStructureFamily.horizontalTerm i α j p a b = 0) ∧
        ∀ (v w : V), ((J.nijenhuis p) (0, v)) (0, w) = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ComplexStructureFamily.nijenhuis_eq_zero_iff`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/Family/Nijenhuis.html#TauCeti.ComplexStructureFamily.nijenhuis_eq_zero_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.ComplexStructureFamily.nijenhuis_eq_zero_iff`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/Family/Nijenhuis.html#TauCeti.ComplexStructureFamily.nijenhuis_eq_zero_iff)
- [Source of `TauCeti.ComplexStructureFamily.nijenhuis_eq_zero_iff` in TauCeti/Geometry/Manifold/Complex/Family/Nijenhuis.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Complex/Family/Nijenhuis.lean#L297)
- [Tau Ceti roadmap status: Analytic families and moduli of complex curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ComplexCurveModuli/STATUS.md)
