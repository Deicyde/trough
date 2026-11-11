---
declaration: theorem
origin: cited
lean: TauCeti.norm_le_mul_prod_div_pow, TauCeti.norm_iteratedDeriv_le_mul_prod_div_pow, TauCeti.norm_le_mul_three_mul_div_pow
statement: formalized
proof: formalized
---

# Schwarz's lemma with prescribed zeros

If `f` is analytic on a neighbourhood of
`closedBall c T`, bounded by `M` on `sphere c T`, and vanishes to order at least `k x` at each
point `x` of a finite set `s ⊆ ball c T`, then on `closedBall c T`
`‖f z‖ ≤ M * ∏ x ∈ s, (‖z - x‖ / (T - ‖x - c‖)) ^ k x`.

```lean
TauCeti.norm_le_mul_prod_div_pow.{u_1} {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℂ E]
  {f : ℂ → E} {c : ℂ} {T M : ℝ} {s : Finset ℂ} {k : ℂ → ℕ}
  (hf : AnalyticOnNhd ℂ f (Metric.closedBall c T)) (hk : ∀ x ∈ s, ↑(k x) ≤ analyticOrderAt f x)
  (hs : ↑s ⊆ Metric.ball c T) (hM : ∀ w ∈ Metric.sphere c T, ‖f w‖ ≤ M) {z : ℂ}
  (hz : z ∈ Metric.closedBall c T) : ‖f z‖ ≤ M * ∏ x ∈ s, (‖z - x‖ / (T - ‖x - c‖)) ^ k x
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.norm_le_mul_prod_div_pow`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Schwarz.html#TauCeti.norm_le_mul_prod_div_pow).

## Other forms

**Schwarz's lemma for the first nonvanishing derivative.** Formalized in Tau Ceti as [`TauCeti.norm_iteratedDeriv_le_mul_prod_div_pow`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Schwarz.html#TauCeti.norm_iteratedDeriv_le_mul_prod_div_pow).

```lean
TauCeti.norm_iteratedDeriv_le_mul_prod_div_pow.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℂ E] {f : ℂ → E} {c : ℂ} {T M : ℝ} {s : Finset ℂ} {k : ℂ → ℕ}
  (hf : AnalyticOnNhd ℂ f (Metric.closedBall c T)) (hk : ∀ x ∈ s, ↑(k x) ≤ analyticOrderAt f x)
  (hs : ↑s ⊆ Metric.ball c T) (hM : ∀ w ∈ Metric.sphere c T, ‖f w‖ ≤ M) {a : ℂ} (ha : a ∈ s) :
  ‖iteratedDeriv (k a) f a‖ ≤
    ↑(k a).factorial * M / (T - ‖a - c‖) ^ k a * ∏ x ∈ s.erase a, (‖a - x‖ / (T - ‖x - c‖)) ^ k x
```

**Schwarz's lemma with prescribed zeros, in the form `M * (3 * R / T) ^ ∑ x ∈ s, k x`.** Formalized in Tau Ceti as [`TauCeti.norm_le_mul_three_mul_div_pow`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Schwarz.html#TauCeti.norm_le_mul_three_mul_div_pow).

```lean
TauCeti.norm_le_mul_three_mul_div_pow.{u_1} {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℂ E]
  {f : ℂ → E} {c : ℂ} {T M : ℝ} {s : Finset ℂ} {k : ℂ → ℕ} {R : ℝ}
  (hf : AnalyticOnNhd ℂ f (Metric.closedBall c T)) (hk : ∀ x ∈ s, ↑(k x) ≤ analyticOrderAt f x)
  (hs : ↑s ⊆ Metric.closedBall c R) (hRT : 3 * R ≤ T) (hM : ∀ w ∈ Metric.sphere c T, ‖f w‖ ≤ M)
  {z : ℂ} (hz : z ∈ Metric.closedBall c R) : ‖f z‖ ≤ M * (3 * R / T) ^ ∑ x ∈ s, k x
```

## Sources

- [Tau Ceti documentation: `TauCeti.norm_le_mul_prod_div_pow`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Schwarz.html#TauCeti.norm_le_mul_prod_div_pow)
- [Source of `TauCeti.norm_le_mul_prod_div_pow` in TauCeti/Analysis/Complex/Schwarz.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/Schwarz.lean#L86)
