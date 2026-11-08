---
declaration: def
origin: cited
lean: PadicInt.mahlerLinearIsometryEquiv
statement: formalized
---

# Mahler's theorem, scalar-linear form

Mathlib's Mahler isometry
`mahlerEquiv E : C(ℤ_[p], E) ≃ₗᵢ[ℤ_[p]] C₀(ℕ, E)` is linear over any semiring `S` acting on the
coefficient module `E`.

```lean
PadicInt.mahlerLinearIsometryEquiv.{u_1, u_2} {p : ℕ} [Fact (Nat.Prime p)] (S : Type u_1)
  (E : Type u_2) [Semiring S] [NormedAddCommGroup E] [_root_.Module ℤ_[p] E] [IsBoundedSMul ℤ_[p] E]
  [IsUltrametricDist E] [CompleteSpace E] [_root_.Module S E] [ContinuousConstSMul S E] :
  C(ℤ_[p], E) ≃ₗᵢ[S] ZeroAtInftyContinuousMap ℕ E
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`PadicInt.mahlerLinearIsometryEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/MahlerBasis/Basic.html#PadicInt.mahlerLinearIsometryEquiv).

## Sources

- [Tau Ceti documentation: `PadicInt.mahlerLinearIsometryEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/MahlerBasis/Basic.html#PadicInt.mahlerLinearIsometryEquiv)
- [Source of `PadicInt.mahlerLinearIsometryEquiv` in TauCeti/NumberTheory/Padics/MahlerBasis/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/Padics/MahlerBasis/Basic.lean#L94)
