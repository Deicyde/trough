---
declaration: theorem
origin: cited
lean: TauCeti.LSeries.landau, TauCeti.LSeries.landau_of_abscissaOfConv, TauCeti.LSeries.abscissaOfAbsConv_le_of_differentiableOn
statement: formalized
proof: formalized
---

# Landau's theorem

If `a` has nonnegative values and its abscissa of absolute convergence
is the real number `σ`, then `LSeries a` has no analytic continuation across `σ`.

```lean
TauCeti.LSeries.landau {a : ℕ → ℂ} (ha : 0 ≤ a) {σ : ℝ} (habs : LSeries.abscissaOfAbsConv a = ↑σ) :
  ¬TauCeti.LSeries.HasAnalyticExtensionAt a σ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.LSeries.landau`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/Landau.html#TauCeti.LSeries.landau).

## Other forms

**Landau's theorem at the abscissa of ordinary convergence.** Formalized in Tau Ceti as [`TauCeti.LSeries.landau_of_abscissaOfConv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/Landau.html#TauCeti.LSeries.landau_of_abscissaOfConv).

```lean
TauCeti.LSeries.landau_of_abscissaOfConv {a : ℕ → ℂ} (ha : ∀ (n : ℕ), n ≠ 0 → 0 ≤ a n) {σ : ℝ}
  (hconv : TauCeti.LSeries.abscissaOfConv a = ↑σ) : ¬TauCeti.LSeries.HasAnalyticExtensionAt a σ
```

**Landau's theorem, half-plane form.** Formalized in Tau Ceti as [`TauCeti.LSeries.abscissaOfAbsConv_le_of_differentiableOn`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/Landau.html#TauCeti.LSeries.abscissaOfAbsConv_le_of_differentiableOn).

```lean
TauCeti.LSeries.abscissaOfAbsConv_le_of_differentiableOn {a : ℕ → ℂ} (ha : 0 ≤ a)
  (hfin : LSeries.abscissaOfAbsConv a ≠ ⊤) {σ₁ : ℝ} {F : ℂ → ℂ}
  (hF : DifferentiableOn ℂ F {s | σ₁ < s.re})
  (hFeq : ∀ (s : ℂ), σ₁ < s.re → LSeries.abscissaOfAbsConv a < ↑s.re → F s = LSeries a s) :
  LSeries.abscissaOfAbsConv a ≤ ↑σ₁
```

## Sources

- [Tau Ceti documentation: `TauCeti.LSeries.landau`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/Landau.html#TauCeti.LSeries.landau)
- [Source of `TauCeti.LSeries.landau` in TauCeti/NumberTheory/LSeries/Landau.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LSeries/Landau.lean#L294)
