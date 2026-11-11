---
declaration: theorem
origin: cited
lean: TauCeti.RegularFormClass.scharlauTransfer_mul_baseChange
statement: formalized
proof: formalized
---

# Frobenius reciprocity on regular-form classes

Transfer of a class over `L` multiplied
by a scalar-extended class from `K` is the transfer multiplied by the original base class.

```lean
TauCeti.RegularFormClass.scharlauTransfer_mul_baseChange.{u, v} {K : Type u} {L : Type v} [Field K]
  [Field L] [Algebra K L] [FiniteDimensional K L] [Invertible 2] (s : L →ₗ[K] K) (hs : s ≠ 0)
  (x : TauCeti.RegularFormClass L) (y : TauCeti.RegularFormClass K) :
  (TauCeti.RegularFormClass.scharlauTransfer s hs) (x * TauCeti.RegularFormClass.baseChange L y) =
    (TauCeti.RegularFormClass.scharlauTransfer s hs) x * y
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.RegularFormClass.scharlauTransfer_mul_baseChange`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/QuadraticForm/Transfer/Class/Frobenius.html#TauCeti.RegularFormClass.scharlauTransfer_mul_baseChange).

## Sources

- [Tau Ceti documentation: `TauCeti.RegularFormClass.scharlauTransfer_mul_baseChange`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/QuadraticForm/Transfer/Class/Frobenius.html#TauCeti.RegularFormClass.scharlauTransfer_mul_baseChange)
- [Source of `TauCeti.RegularFormClass.scharlauTransfer_mul_baseChange` in TauCeti/LinearAlgebra/QuadraticForm/Transfer/Class/Frobenius.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/QuadraticForm/Transfer/Class/Frobenius.lean#L50)
