---
declaration: theorem
origin: cited
lean: Polynomial.mul_dvd_eval_sub_eval_sub_mul
statement: formalized
proof: formalized
---

# Taylor's estimate

If `d ∣ x - t`, `d ∣ e` and `e ∣ x' - x`, then the derivative at `t`
linearises the polynomial `f` from `x` to `x'` up to an error divisible by `d * e`.

```lean
Polynomial.mul_dvd_eval_sub_eval_sub_mul.{u_1} {R : Type u_1} [CommRing R] (f : Polynomial R)
  {d e t x x' : R} (hx : d ∣ x - t) (hde : d ∣ e) (hxx' : e ∣ x' - x) :
  d * e ∣
    Polynomial.eval x' f - Polynomial.eval x f -
      Polynomial.eval t (Polynomial.derivative f) * (x' - x)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Polynomial.mul_dvd_eval_sub_eval_sub_mul`](https://taucetiproject.org/docs/TauCeti/Algebra/Polynomial/Identities.html#Polynomial.mul_dvd_eval_sub_eval_sub_mul).

## Sources

- [Tau Ceti documentation: `Polynomial.mul_dvd_eval_sub_eval_sub_mul`](https://taucetiproject.org/docs/TauCeti/Algebra/Polynomial/Identities.html#Polynomial.mul_dvd_eval_sub_eval_sub_mul)
- [Source of `Polynomial.mul_dvd_eval_sub_eval_sub_mul` in TauCeti/Algebra/Polynomial/Identities.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Polynomial/Identities.lean#L32)
