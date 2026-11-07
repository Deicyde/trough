---
declaration: theorem
origin: cited
lean: TauCeti.continuous_and_isPositiveDefiniteSub_iff_existsUnique_innerRegular_pontryaginMeasureTransform_eq
statement: formalized
proof: formalized
---

# Bochner's characterization without countability assumptions

A function on a locally
compact abelian group is continuous and positive definite if and only if it is the
Fourier–Stieltjes transform of a unique finite inner regular measure on the Pontryagin dual.

```lean
TauCeti.continuous_and_isPositiveDefiniteSub_iff_existsUnique_innerRegular_pontryaginMeasureTransform_eq.{u_1}
  {G : Type u_1} [AddCommGroup G] [TopologicalSpace G] [IsTopologicalAddGroup G]
  [LocallyCompactSpace G] [MeasurableSpace (PontryaginDual (Multiplicative G))]
  [BorelSpace (PontryaginDual (Multiplicative G))] (φ : G → ℂ) :
  Continuous φ ∧ TauCeti.IsPositiveDefiniteSub φ ↔
    ∃! μ, (↑μ).InnerRegular ∧ μ.pontryaginMeasureTransform = φ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.continuous_and_isPositiveDefiniteSub_iff_existsUnique_innerRegular_pontryaginMeasureTransform_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Bochner/LocallyCompactGroup.html#TauCeti.continuous_and_isPositiveDefiniteSub_iff_existsUnique_innerRegular_pontryaginMeasureTransform_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.continuous_and_isPositiveDefiniteSub_iff_existsUnique_innerRegular_pontryaginMeasureTransform_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Bochner/LocallyCompactGroup.html#TauCeti.continuous_and_isPositiveDefiniteSub_iff_existsUnique_innerRegular_pontryaginMeasureTransform_eq)
- [Source of `TauCeti.continuous_and_isPositiveDefiniteSub_iff_existsUnique_innerRegular_pontryaginMeasureTransform_eq` in TauCeti/Analysis/Bochner/LocallyCompactGroup.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Bochner/LocallyCompactGroup.lean#L105)
- [Tau Ceti roadmap status: One-parameter semigroups, completely monotone and positive-definite functions, and Bochner-type representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/OneParameterSemigroups/STATUS.md)
