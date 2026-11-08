---
declaration: theorem
origin: cited
lean: PowerSeries.IsRestricted.norm_evalAt_le_gaussNorm_mul_norm_prod, PowerSeries.IsRestricted.norm_evalAt_le_gaussNorm_mul_norm_factorial, PowerSeries.IsRestricted.norm_evalAt_le_gaussNorm_mul_norm_factorial_pow, TauCeti.norm_schneider_auxiliary_le
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

- [The Schwarz lemma for restricted series](../../../ring-theory/p-adic-measures-completed-group-algebras-and-cha/part-01/the-schwarz-lemma-for-restricted-series.md)
- [Schwarz's lemma with prescribed zeros](../../../analysis/part-02/complex/part-02/schwarzs-lemma-with-prescribed-zeros.md)

## Lean

Formalized in Tau Ceti as [`PowerSeries.IsRestricted.norm_evalAt_le_gaussNorm_mul_norm_prod`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/IntegerGrid.html#PowerSeries.IsRestricted.norm_evalAt_le_gaussNorm_mul_norm_prod).

## Other forms

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

**Schwarz's lemma for Schneider's auxiliary function.** Formalized in Tau Ceti as [`TauCeti.norm_schneider_auxiliary_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Transcendental/GelfondSchneider/AnalyticBound.html#TauCeti.norm_schneider_auxiliary_le).

```lean
TauCeti.norm_schneider_auxiliary_le {β : ℂ} (hβ : ∀ (q : ℚ), ↑q ≠ β) {l : ℂ} {L D₁ D₂ : ℕ}
  {a : Fin D₁ → Fin D₂ → ℂ} {A R T : ℝ} (ha : ∀ (i : Fin D₁) (j : Fin D₂), ‖a i j‖ ≤ A)
  (hzero :
    ∀ (u v : ℕ),
      1 ≤ u →
        u ≤ L →
          1 ≤ v →
            v ≤ L →
              ∑ i, ∑ j, a i j * (↑u + ↑v * β) ^ ↑i * Complex.exp (↑↑j * l * (↑u + ↑v * β)) = 0)
  (hR : ↑L * (1 + ‖β‖) ≤ R) (hRT : 3 * R ≤ T) (hT : 1 ≤ T) {z : ℂ} (hz : ‖z‖ ≤ R) :
  ‖∑ i, ∑ j, a i j * z ^ ↑i * Complex.exp (↑↑j * l * z)‖ ≤
    ↑D₁ * ↑D₂ * A * T ^ D₁ * Real.exp (↑D₂ * ‖l‖ * T) * (3 * R / T) ^ L ^ 2
```

## Sources

- [Tau Ceti documentation: `PowerSeries.IsRestricted.norm_evalAt_le_gaussNorm_mul_norm_prod`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/IntegerGrid.html#PowerSeries.IsRestricted.norm_evalAt_le_gaussNorm_mul_norm_prod)
- [Source of `PowerSeries.IsRestricted.norm_evalAt_le_gaussNorm_mul_norm_prod` in TauCeti/NumberTheory/Padics/IntegerGrid.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/Padics/IntegerGrid.lean#L123)
