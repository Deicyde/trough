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

## Proof depends on

- [Bochner's theorem](bochners-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.continuous_and_isPositiveDefiniteSub_iff_existsUnique_innerRegular_pontryaginMeasureTransform_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Bochner/LocallyCompactGroup.html#TauCeti.continuous_and_isPositiveDefiniteSub_iff_existsUnique_innerRegular_pontryaginMeasureTransform_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.continuous_and_isPositiveDefiniteSub_iff_existsUnique_innerRegular_pontryaginMeasureTransform_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Bochner/LocallyCompactGroup.html#TauCeti.continuous_and_isPositiveDefiniteSub_iff_existsUnique_innerRegular_pontryaginMeasureTransform_eq)
- [Source of `TauCeti.continuous_and_isPositiveDefiniteSub_iff_existsUnique_innerRegular_pontryaginMeasureTransform_eq` in TauCeti/Analysis/Bochner/LocallyCompactGroup.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Bochner/LocallyCompactGroup.lean#L105)
- [Tau Ceti roadmap status: One-parameter semigroups, completely monotone and positive-definite functions, and Bochner-type representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/OneParameterSemigroups/STATUS.md)
