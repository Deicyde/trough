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
- [Source of `TauCeti.LaurentSeries.coeff_neg_one_substAlgHom_mul_derivative_eq_nsmul` in TauCeti/RingTheory/LaurentSeries/Substitution/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/LaurentSeries/Substitution/Basic.lean#L205)
- [Tau Ceti roadmap status: Formal Laurent fields, Puiseux expansions and continuous differential calculus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FormalLaurentPuiseux/STATUS.md)
