---
declaration: theorem
origin: cited
lean: TauCeti.transcendental_exp_mul, TauCeti.transcendental_cpow, TauCeti.transcendental_rpow
statement: formalized
proof: formalized
---

# The Gelfond–Schneider theorem (Karatarakis–Wiedijk, §3)

Let `λ ≠ 0` be a complex number
such that `exp λ` is algebraic, and let `β` be an algebraic number that is not rational. Then
`exp (β λ)` is transcendental.

```lean
TauCeti.transcendental_exp_mul {l β : ℂ} (hl : l ≠ 0) (hα : IsAlgebraic ℚ (Complex.exp l))
  (hβ : IsAlgebraic ℚ β) (hirr : ∀ (q : ℚ), β ≠ ↑q) : Transcendental ℚ (Complex.exp (β * l))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Iterated Rolle's theorem](../../../analysis/part-03/calculus/part-01/iterated-rolles-theorem.md)
- [Liouville's inequality in exponential form](../../part-02/height/liouvilles-inequality-in-exponential-form.md)
- [Liouville's lower bound for Gelfond's values (Karatarakis–Wiedijk, §3)](../../part-03/transcendental/liouvilles-lower-bound-for-gelfonds-values-karat.md)
- [Schwarz's lemma for Schneider's auxiliary function](schwarzs-lemma-for-schneiders-auxiliary-function.md)
- [Schwarz's lemma with prescribed zeros](../../../analysis/part-03/complex/part-04/schwarzs-lemma-with-prescribed-zeros.md)
- [Siegel's lemma over a number field, with rational integer unknowns (Evertse, Theorem 3.20)](../../part-03/number-field/siegels-lemma-over-a-number-field-with-rational.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.transcendental_exp_mul`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Transcendental/GelfondSchneider/Gelfond/Theorem.html#TauCeti.transcendental_exp_mul).

## Other forms

**The Gelfond–Schneider theorem for `Complex.cpow`.** Formalized in Tau Ceti as [`TauCeti.transcendental_cpow`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Transcendental/GelfondSchneider/Gelfond/Theorem.html#TauCeti.transcendental_cpow).

```lean
TauCeti.transcendental_cpow {α β : ℂ} (hα : IsAlgebraic ℚ α) (h0 : α ≠ 0) (h1 : α ≠ 1)
  (hβ : IsAlgebraic ℚ β) (hirr : ∀ (q : ℚ), β ≠ ↑q) : Transcendental ℚ (α ^ β)
```

**The Gelfond–Schneider theorem for real numbers (Evertse, Theorem 4.21).** Formalized in Tau Ceti as [`TauCeti.transcendental_rpow`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Transcendental/GelfondSchneider/Theorem.html#TauCeti.transcendental_rpow).

```lean
TauCeti.transcendental_rpow {α β : ℝ} (hα : IsAlgebraic ℚ α) (hβ : IsAlgebraic ℚ β) (h0 : 0 < α)
  (h1 : α ≠ 1) (hirr : Irrational β) : Transcendental ℚ (α ^ β)
```

## Sources

- [Tau Ceti documentation: `TauCeti.transcendental_exp_mul`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Transcendental/GelfondSchneider/Gelfond/Theorem.html#TauCeti.transcendental_exp_mul)
- [Source of `TauCeti.transcendental_exp_mul` in TauCeti/NumberTheory/Transcendental/GelfondSchneider/Gelfond/Theorem.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/Transcendental/GelfondSchneider/Gelfond/Theorem.lean#L114)
- [Tau Ceti roadmap status: Diophantine approximation and transcendence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/DiophantineApproximationAndTranscendence/STATUS.md)
