---
declaration: def
origin: cited
lean: TauCeti.hermiteQuotientEquiv
statement: formalized
---

# Chinese remainder theorem for the Hermite modulus

```lean
TauCeti.hermiteQuotientEquiv.{u_1, u_3} {K : Type u_1} [Field K] {ι : Type u_3} [Fintype ι]
  {a : ι → K} (ha : Function.Injective a) (m : ι → ℕ) :
  Polynomial K ⧸ Ideal.span {TauCeti.hermiteModulus a m} ≃+*
    ((i : ι) → Polynomial K ⧸ Ideal.span {(Polynomial.X - Polynomial.C (a i)) ^ m i})
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.hermiteQuotientEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/Polynomial/HermiteInterpolation.html#TauCeti.hermiteQuotientEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.hermiteQuotientEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/Polynomial/HermiteInterpolation.html#TauCeti.hermiteQuotientEquiv)
- [Source of `TauCeti.hermiteQuotientEquiv` in TauCeti/RingTheory/Polynomial/HermiteInterpolation.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Polynomial/HermiteInterpolation.lean#L147)
