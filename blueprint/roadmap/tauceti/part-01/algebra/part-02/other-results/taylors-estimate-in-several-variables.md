---
declaration: theorem
origin: cited
lean: MvPolynomial.mul_dvd_eval_sub_eval_sub_sum_pderiv
statement: formalized
proof: formalized
---

# Taylor's estimate in several variables

If `d ∣ xᵢ - tᵢ`, `d ∣ e` and `e ∣ x'ᵢ - xᵢ` for
every `i`, then the gradient at `t` linearises `p` from `x` to `x'` up to an error divisible by
`d * e`.

```lean
MvPolynomial.mul_dvd_eval_sub_eval_sub_sum_pderiv.{u_1, u_2} {R : Type u_1} {σ : Type u_2}
  [CommRing R] [Fintype σ] (p : MvPolynomial σ R) {d e : R} {t x x' : σ → R}
  (hx : ∀ (i : σ), d ∣ x i - t i) (hde : d ∣ e) (hxx' : ∀ (i : σ), e ∣ x' i - x i) :
  d * e ∣
    (MvPolynomial.eval x') p - (MvPolynomial.eval x) p -
      ∑ j, (MvPolynomial.eval t) ((MvPolynomial.pderiv j) p) * (x' j - x j)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MvPolynomial.mul_dvd_eval_sub_eval_sub_sum_pderiv`](https://taucetiproject.org/docs/TauCeti/Algebra/MvPolynomial/PDeriv.html#MvPolynomial.mul_dvd_eval_sub_eval_sub_sum_pderiv).

## Sources

- [Tau Ceti documentation: `MvPolynomial.mul_dvd_eval_sub_eval_sub_sum_pderiv`](https://taucetiproject.org/docs/TauCeti/Algebra/MvPolynomial/PDeriv.html#MvPolynomial.mul_dvd_eval_sub_eval_sub_sum_pderiv)
- [Source of `MvPolynomial.mul_dvd_eval_sub_eval_sub_sum_pderiv` in TauCeti/Algebra/MvPolynomial/PDeriv.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/MvPolynomial/PDeriv.lean#L192)
