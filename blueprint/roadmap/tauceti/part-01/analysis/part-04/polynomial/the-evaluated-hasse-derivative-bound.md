---
declaration: theorem
origin: cited
lean: Polynomial.norm_eval_hasseDeriv_le
statement: formalized
proof: formalized
---

# The evaluated Hasse derivative bound

for `natDegree f ≤ d`, coefficients of norm at most
`H` and `‖a‖ ≤ A`, `‖D^[k] f (a)‖ ≤ H ∑_{j = k}^{d} choose j k · A ^ (j - k)`. For `k > d` the
sum is empty and the left side is `0`.

```lean
Polynomial.norm_eval_hasseDeriv_le.{u_1} {R : Type u_1} [SeminormedRing R] {f : Polynomial R}
  {d : ℕ} (hd : f.natDegree ≤ d) {H : ℝ} (hcoeff : ∀ j ≤ d, ‖f.coeff j‖ ≤ H) {a : R} {A : ℝ}
  (ha : ‖a‖ ≤ A) (k : ℕ) :
  ‖Polynomial.eval a ((Polynomial.hasseDeriv k) f)‖ ≤
    H * ∑ j ∈ Finset.Icc k d, ↑(j.choose k) * A ^ (j - k)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Polynomial.norm_eval_hasseDeriv_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Polynomial/HasseDerivBound.html#Polynomial.norm_eval_hasseDeriv_le).

## Sources

- [Tau Ceti documentation: `Polynomial.norm_eval_hasseDeriv_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Polynomial/HasseDerivBound.html#Polynomial.norm_eval_hasseDeriv_le)
- [Source of `Polynomial.norm_eval_hasseDeriv_le` in TauCeti/Analysis/Polynomial/HasseDerivBound.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Polynomial/HasseDerivBound.lean#L95)
