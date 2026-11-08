---
declaration: theorem
origin: cited
lean: RootPairing.coeff_eq_kostantMultiplicity_of_mul_weylDenominator_eq_weylNumerator
statement: formalized
proof: formalized
---

# Kostant's multiplicity formula, stated before any module is named

an element of `ℤ[M]`
whose product with the Weyl denominator is the Weyl numerator of `λ` has `μ`-th coefficient
`∑_{w ∈ W} sgn(w) P(w ⬝ λ - μ)`.

The hypothesis is exactly the Weyl character formula, so this turns that formula into a closed
expression for one weight multiplicity at a time.

```lean
RootPairing.coeff_eq_kostantMultiplicity_of_mul_weylDenominator_eq_weylNumerator.{u, v, w, x}
  {ι : Type u} {R : Type v} {M : Type w} {N : Type x} [CommRing R] [AddCommGroup M]
  [_root_.Module R M] [AddCommGroup N] [_root_.Module R N] [CharZero R] (P : RootPairing ι R M N)
  [Finite ι] (b : P.Base) [IsDomain R] [Invertible 2] [P.IsCrystallographic] [P.IsReduced]
  [Fintype ↥P.weylGroup] {f : AddMonoidAlgebra ℤ M} {lam : M}
  (hf : f * TauCeti.weylDenominator P b = TauCeti.weylNumerator P b lam) (mu : M) :
  f.coeff mu = P.kostantMultiplicity b lam mu
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`RootPairing.coeff_eq_kostantMultiplicity_of_mul_weylDenominator_eq_weylNumerator`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/KostantPartition/Multiplicity.html#RootPairing.coeff_eq_kostantMultiplicity_of_mul_weylDenominator_eq_weylNumerator).

## Sources

- [Tau Ceti documentation: `RootPairing.coeff_eq_kostantMultiplicity_of_mul_weylDenominator_eq_weylNumerator`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/KostantPartition/Multiplicity.html#RootPairing.coeff_eq_kostantMultiplicity_of_mul_weylDenominator_eq_weylNumerator)
- [Source of `RootPairing.coeff_eq_kostantMultiplicity_of_mul_weylDenominator_eq_weylNumerator` in TauCeti/LinearAlgebra/RootSystem/KostantPartition/Multiplicity.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/RootSystem/KostantPartition/Multiplicity.lean#L185)
