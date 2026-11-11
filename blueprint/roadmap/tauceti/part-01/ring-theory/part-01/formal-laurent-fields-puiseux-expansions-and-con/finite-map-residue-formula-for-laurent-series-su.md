---
declaration: theorem
origin: cited
lean: TauCeti.LaurentSeries.coeff_neg_one_substAlgHom_mul_derivative_eq_nsmul
statement: formalized
proof: formalized
---

# Finite-map residue formula for Laurent series substitution

Substituting a nonzero power
series `φ` of zero constant coefficient multiplies the residue of `f dX` by `φ.order.toNat`, in all
characteristics: `Res(f(φ) Dφ dX) = φ.order.toNat • Res(f dX)`.

```lean
TauCeti.LaurentSeries.coeff_neg_one_substAlgHom_mul_derivative_eq_nsmul.{u_1} {K : Type u_1}
  [Field K] {φ : PowerSeries K} (hφ : PowerSeries.constantCoeff φ = 0) (hφ₀ : φ ≠ 0)
  (f : LaurentSeries K) :
  ((TauCeti.LaurentSeries.substAlgHom hφ hφ₀) f *
          (LaurentSeries.derivative K) ((HahnSeries.ofPowerSeries ℤ K) φ)).coeff
      (-1) =
    φ.order.toNat • f.coeff (-1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.LaurentSeries.coeff_neg_one_substAlgHom_mul_derivative_eq_nsmul`](https://taucetiproject.org/docs/TauCeti/RingTheory/LaurentSeries/Substitution/Basic.html#TauCeti.LaurentSeries.coeff_neg_one_substAlgHom_mul_derivative_eq_nsmul).

## Sources

- [Tau Ceti documentation: `TauCeti.LaurentSeries.coeff_neg_one_substAlgHom_mul_derivative_eq_nsmul`](https://taucetiproject.org/docs/TauCeti/RingTheory/LaurentSeries/Substitution/Basic.html#TauCeti.LaurentSeries.coeff_neg_one_substAlgHom_mul_derivative_eq_nsmul)
- [Source of `TauCeti.LaurentSeries.coeff_neg_one_substAlgHom_mul_derivative_eq_nsmul` in TauCeti/RingTheory/LaurentSeries/Substitution/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/LaurentSeries/Substitution/Basic.lean#L205)
- [Tau Ceti roadmap status: Formal Laurent fields, Puiseux expansions and continuous differential calculus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FormalLaurentPuiseux/STATUS.md)
