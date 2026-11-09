---
declaration: theorem
origin: cited
lean: TauCeti.IsAdicComplete.existsUnique_eval_eq_zero_of_dvd_pow
statement: formalized
proof: formalized
---

# Hensel's lemma with a derivative dividing `π ^ k`

Let `R` be `π`-adically complete with
`π` a non-zero-divisor, and let `f` be a polynomial with `f'(t) ∣ π ^ k` and
`f(t) ≡ 0 mod π ^ (2k + 1)`. Then `f` has exactly one root congruent to `t` modulo `π ^ (k + 1)`.

```lean
TauCeti.IsAdicComplete.existsUnique_eval_eq_zero_of_dvd_pow.{u_1} {R : Type u_1} [CommRing R]
  {π : R} {f : Polynomial R} {k : ℕ} {t : R} [IsAdicComplete (Ideal.span {π}) R]
  (hπ : IsLeftRegular π) (hd : Polynomial.eval t (Polynomial.derivative f) ∣ π ^ k)
  (ht : π ^ (2 * k + 1) ∣ Polynomial.eval t f) : ∃! u, π ^ (k + 1) ∣ u - t ∧ Polynomial.eval u f = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Taylor's estimate](../../../../algebra/polynomial/taylors-estimate.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsAdicComplete.existsUnique_eval_eq_zero_of_dvd_pow`](https://taucetiproject.org/docs/TauCeti/RingTheory/AdicCompletion/Newton.html#TauCeti.IsAdicComplete.existsUnique_eval_eq_zero_of_dvd_pow).

## Sources

- [Tau Ceti documentation: `TauCeti.IsAdicComplete.existsUnique_eval_eq_zero_of_dvd_pow`](https://taucetiproject.org/docs/TauCeti/RingTheory/AdicCompletion/Newton.html#TauCeti.IsAdicComplete.existsUnique_eval_eq_zero_of_dvd_pow)
- [Source of `TauCeti.IsAdicComplete.existsUnique_eval_eq_zero_of_dvd_pow` in TauCeti/RingTheory/AdicCompletion/Newton.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/AdicCompletion/Newton.lean#L336)
