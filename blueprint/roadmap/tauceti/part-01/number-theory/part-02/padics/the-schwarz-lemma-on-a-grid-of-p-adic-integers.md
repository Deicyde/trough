---
declaration: theorem
origin: cited
lean: PowerSeries.IsRestricted.norm_evalAt_le_gaussNorm_mul_norm_prod, PowerSeries.IsRestricted.norm_evalAt_hasseDeriv_le_gaussNorm_mul_norm_prod, PowerSeries.IsRestricted.norm_evalAt_hasseDeriv_le_gaussNorm_mul_norm_factorial, PowerSeries.IsRestricted.norm_evalAt_hasseDeriv_le_gaussNorm_mul_norm_factorial_pow, PowerSeries.IsRestricted.norm_evalAt_le_gaussNorm_mul_norm_factorial, PowerSeries.IsRestricted.norm_evalAt_le_gaussNorm_mul_norm_factorial_pow
statement: formalized
proof: formalized
---

# The Schwarz lemma on a grid of `p`-adic integers

Let `K` be a complete normed field
extension of `ℚ_p` and `f` a power series over `K` restricted at a radius `c ≥ 1`. If the Hasse
derivatives `(D⁽ᵗ⁾ f)(b)` vanish for `t < T` at every point `b` of a finite set `s` of `p`-adic
integers, then at every `p`-adic integer `x`

```text
‖f(x)‖ ≤ ‖f‖_c * (‖∏_{b ∈ s} (x - b)‖ / c ^ #s) ^ T.
```

```lean
PowerSeries.IsRestricted.norm_evalAt_le_gaussNorm_mul_norm_prod.{u_1} {p : ℕ} [Fact (Nat.Prime p)]
  {K : Type u_1} [NormedField K] [NormedAlgebra ℚ_[p] K] [CompleteSpace K] {c : ℝ}
  {f : PowerSeries K} (hf : PowerSeries.IsRestricted c f) (hc : 1 ≤ c) {s : Finset ℤ_[p]} {T : ℕ}
  (hzero : ∀ b ∈ s, ∀ t < T, ((PowerSeries.hasseDeriv t) f).evalAt ((algebraMap ℚ_[p] K) ↑b) = 0)
  (x : ℤ_[p]) :
  ‖f.evalAt ((algebraMap ℚ_[p] K) ↑x)‖ ≤
    PowerSeries.gaussNorm norm c f * (‖∏ b ∈ s, (x - b)‖ / c ^ s.card) ^ T
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Schwarz lemma for Hasse derivatives](../../../ring-theory/part-01/power-series/the-schwarz-lemma-for-hasse-derivatives.md)

## Lean

Formalized in Tau Ceti as [`PowerSeries.IsRestricted.norm_evalAt_le_gaussNorm_mul_norm_prod`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/IntegerGrid.html#PowerSeries.IsRestricted.norm_evalAt_le_gaussNorm_mul_norm_prod).

## Other forms

**The Schwarz lemma for Hasse derivatives on a grid of `p`-adic integers.** Formalized in Tau Ceti as [`PowerSeries.IsRestricted.norm_evalAt_hasseDeriv_le_gaussNorm_mul_norm_prod`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/IntegerGrid.html#PowerSeries.IsRestricted.norm_evalAt_hasseDeriv_le_gaussNorm_mul_norm_prod).

```lean
PowerSeries.IsRestricted.norm_evalAt_hasseDeriv_le_gaussNorm_mul_norm_prod.{u_1} {p : ℕ}
  [Fact (Nat.Prime p)] {K : Type u_1} [NormedField K] [NormedAlgebra ℚ_[p] K] [CompleteSpace K]
  {c : ℝ} {f : PowerSeries K} (hf : PowerSeries.IsRestricted c f) (hc : 1 ≤ c) {s : Finset ℤ_[p]}
  {T : ℕ}
  (hzero : ∀ b ∈ s, ∀ t < T, ((PowerSeries.hasseDeriv t) f).evalAt ((algebraMap ℚ_[p] K) ↑b) = 0)
  (k : ℕ) (x : ℤ_[p]) :
  ‖((PowerSeries.hasseDeriv k) f).evalAt ((algebraMap ℚ_[p] K) ↑x)‖ ≤
    c⁻¹ ^ k * PowerSeries.gaussNorm norm c f * (‖∏ b ∈ s, (x - b)‖ / c ^ s.card) ^ (T - k)
```

**The Schwarz lemma for Hasse derivatives on a progression of `p`-adic integers.** Formalized in Tau Ceti as [`PowerSeries.IsRestricted.norm_evalAt_hasseDeriv_le_gaussNorm_mul_norm_factorial`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/IntegerGrid.html#PowerSeries.IsRestricted.norm_evalAt_hasseDeriv_le_gaussNorm_mul_norm_factorial).

```lean
PowerSeries.IsRestricted.norm_evalAt_hasseDeriv_le_gaussNorm_mul_norm_factorial.{u_1} {p : ℕ}
  [Fact (Nat.Prime p)] {K : Type u_1} [NormedField K] [NormedAlgebra ℚ_[p] K] [CompleteSpace K]
  {c : ℝ} {f : PowerSeries K} (hf : PowerSeries.IsRestricted c f) (hc : 1 ≤ c) (a : ℤ_[p])
  {d : ℤ_[p]} (hd : IsUnit d) {n T : ℕ}
  (hzero :
    ∀ j < n,
      ∀ t < T, ((PowerSeries.hasseDeriv t) f).evalAt ((algebraMap ℚ_[p] K) ↑(a + ↑j * d)) = 0)
  (k : ℕ) (x : ℤ_[p]) :
  ‖((PowerSeries.hasseDeriv k) f).evalAt ((algebraMap ℚ_[p] K) ↑x)‖ ≤
    c⁻¹ ^ k * PowerSeries.gaussNorm norm c f * (‖↑n.factorial‖ / c ^ n) ^ (T - k)
```

**The Schwarz lemma for Hasse derivatives on the integers not divisible by `q`.** Formalized in Tau Ceti as [`PowerSeries.IsRestricted.norm_evalAt_hasseDeriv_le_gaussNorm_mul_norm_factorial_pow`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/IntegerGrid.html#PowerSeries.IsRestricted.norm_evalAt_hasseDeriv_le_gaussNorm_mul_norm_factorial_pow).

```lean
PowerSeries.IsRestricted.norm_evalAt_hasseDeriv_le_gaussNorm_mul_norm_factorial_pow.{u_1} {p : ℕ}
  [Fact (Nat.Prime p)] {K : Type u_1} [NormedField K] [NormedAlgebra ℚ_[p] K] [CompleteSpace K]
  {c : ℝ} {f : PowerSeries K} (hf : PowerSeries.IsRestricted c f) (hc : 1 ≤ c) {q : ℕ}
  (hq : p.Coprime q) {N T : ℕ}
  (hzero : ∀ j < N, ¬q ∣ j → ∀ t < T, ((PowerSeries.hasseDeriv t) f).evalAt ↑j = 0) (k : ℕ)
  (x : ℤ_[p]) :
  ‖((PowerSeries.hasseDeriv k) f).evalAt ((algebraMap ℚ_[p] K) ↑x)‖ ≤
    c⁻¹ ^ k * PowerSeries.gaussNorm norm c f *
      (‖↑(N / q).factorial‖ ^ (q - 1) / c ^ {x ∈ Finset.range N | ¬q ∣ x}.card) ^ (T - k)
```

**The Schwarz lemma on a progression of `p`-adic integers.** Formalized in Tau Ceti as [`PowerSeries.IsRestricted.norm_evalAt_le_gaussNorm_mul_norm_factorial`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/IntegerGrid.html#PowerSeries.IsRestricted.norm_evalAt_le_gaussNorm_mul_norm_factorial).

```lean
PowerSeries.IsRestricted.norm_evalAt_le_gaussNorm_mul_norm_factorial.{u_1} {p : ℕ}
  [Fact (Nat.Prime p)] {K : Type u_1} [NormedField K] [NormedAlgebra ℚ_[p] K] [CompleteSpace K]
  {c : ℝ} {f : PowerSeries K} (hf : PowerSeries.IsRestricted c f) (hc : 1 ≤ c) (a : ℤ_[p])
  {d : ℤ_[p]} (hd : IsUnit d) {n T : ℕ}
  (hzero :
    ∀ j < n,
      ∀ t < T, ((PowerSeries.hasseDeriv t) f).evalAt ((algebraMap ℚ_[p] K) ↑(a + ↑j * d)) = 0)
  (x : ℤ_[p]) :
  ‖f.evalAt ((algebraMap ℚ_[p] K) ↑x)‖ ≤
    PowerSeries.gaussNorm norm c f * (‖↑n.factorial‖ / c ^ n) ^ T
```

**The Schwarz lemma on the integers not divisible by `q`.** Formalized in Tau Ceti as [`PowerSeries.IsRestricted.norm_evalAt_le_gaussNorm_mul_norm_factorial_pow`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/IntegerGrid.html#PowerSeries.IsRestricted.norm_evalAt_le_gaussNorm_mul_norm_factorial_pow).

```lean
PowerSeries.IsRestricted.norm_evalAt_le_gaussNorm_mul_norm_factorial_pow.{u_1} {p : ℕ}
  [Fact (Nat.Prime p)] {K : Type u_1} [NormedField K] [NormedAlgebra ℚ_[p] K] [CompleteSpace K]
  {c : ℝ} {f : PowerSeries K} (hf : PowerSeries.IsRestricted c f) (hc : 1 ≤ c) {q : ℕ}
  (hq : p.Coprime q) {N T : ℕ}
  (hzero : ∀ j < N, ¬q ∣ j → ∀ t < T, ((PowerSeries.hasseDeriv t) f).evalAt ↑j = 0) (x : ℤ_[p]) :
  ‖f.evalAt ((algebraMap ℚ_[p] K) ↑x)‖ ≤
    PowerSeries.gaussNorm norm c f *
      (‖↑(N / q).factorial‖ ^ (q - 1) / c ^ {x ∈ Finset.range N | ¬q ∣ x}.card) ^ T
```

## Sources

- [Tau Ceti documentation: `PowerSeries.IsRestricted.norm_evalAt_le_gaussNorm_mul_norm_prod`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/IntegerGrid.html#PowerSeries.IsRestricted.norm_evalAt_le_gaussNorm_mul_norm_prod)
- [Source of `PowerSeries.IsRestricted.norm_evalAt_le_gaussNorm_mul_norm_prod` in TauCeti/NumberTheory/Padics/IntegerGrid.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/Padics/IntegerGrid.lean#L136)
