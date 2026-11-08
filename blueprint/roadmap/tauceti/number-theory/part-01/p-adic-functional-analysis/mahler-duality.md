---
declaration: def
origin: cited
lean: AbstractMeasure.mahlerMomentsEquiv
statement: formalized
---

# Mahler duality

Over a ring with a multiplicative pseudo-uniformiser, a measure on `ℤ_p`
is determined by its moments `μ (x ↦ x choose n)`, the coefficients of its Amice transform, and
every bounded sequence is the moment sequence of a measure. The inverse sends a bounded sequence
`b` to the measure `f ↦ ∑ n, Δ^n f (0) * b n`.

```lean
AbstractMeasure.mahlerMomentsEquiv.{u_1} (p : ℕ) [Fact (Nat.Prime p)] (R : Type u_1)
  [NormedCommRing R] [TauCeti.NormedRing.IsTate R] [Algebra ℤ_[p] R] [IsBoundedSMul ℤ_[p] R]
  [IsUltrametricDist R] [CompleteSpace R] : AbstractMeasure ℤ_[p] R R ≃ₗ[R] ↥(lp (fun x => R) ⊤)
```

## Depends on

- [Mahler's theorem, scalar-linear form](../../part-02/padics/mahlers-theorem-scalar-linear-form.md)
- [The universal property of `C₀(I, R)`](the-universal-property-of-c0-i-r.md)

## Lean

Formalized in Tau Ceti as [`AbstractMeasure.mahlerMomentsEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Measure/MahlerDuality.html#AbstractMeasure.mahlerMomentsEquiv).

## Sources

- [Tau Ceti documentation: `AbstractMeasure.mahlerMomentsEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Measure/MahlerDuality.html#AbstractMeasure.mahlerMomentsEquiv)
- [Source of `AbstractMeasure.mahlerMomentsEquiv` in TauCeti/NumberTheory/Padics/Measure/MahlerDuality.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/Padics/Measure/MahlerDuality.lean#L139)
- [Tau Ceti roadmap status: P-adic functional analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/PadicFunctionalAnalysis/STATUS.md)
