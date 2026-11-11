---
declaration: theorem
origin: cited
lean: TauCeti.transcendental_rpow, TauCeti.transcendental_exp_mul, TauCeti.transcendental_cpow
statement: formalized
proof: formalized
---

# The Gelfond–Schneider theorem for real numbers (Evertse, Theorem 4.21)

If `α > 0` and `β`
are real algebraic numbers with `α ≠ 1` and `β` irrational, then `α ^ β` is transcendental.

```lean
TauCeti.transcendental_rpow {α β : ℝ} (hα : IsAlgebraic ℚ α) (hβ : IsAlgebraic ℚ β) (h0 : 0 < α)
  (h1 : α ≠ 1) (hirr : Irrational β) : Transcendental ℚ (α ^ β)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Iterated Rolle's theorem](../../../analysis/part-02/calculus/part-01/iterated-rolles-theorem.md)
- [Liouville's inequality in exponential form](../../part-02/height/liouvilles-inequality-in-exponential-form.md)
- [Liouville's lower bound for Gelfond's values (Karatarakis–Wiedijk, §3)](../../part-02/transcendental/liouvilles-lower-bound-for-gelfonds-values-karat.md)
- [Schwarz's lemma for Schneider's auxiliary function](../../part-02/transcendental/schwarzs-lemma-for-schneiders-auxiliary-function.md)
- [Schwarz's lemma with prescribed zeros](../../../analysis/part-02/complex/part-03/schwarzs-lemma-with-prescribed-zeros.md)
- [Siegel's lemma over a number field, with rational integer unknowns (Evertse, Theorem 3.20)](../../part-02/number-field/siegels-lemma-over-a-number-field-with-rational.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.transcendental_rpow`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Transcendental/GelfondSchneider/Theorem.html#TauCeti.transcendental_rpow).

## Other forms

**The Gelfond–Schneider theorem (Karatarakis–Wiedijk, §3).** Formalized in Tau Ceti as [`TauCeti.transcendental_exp_mul`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Transcendental/GelfondSchneider/Gelfond/Theorem.html#TauCeti.transcendental_exp_mul).

```lean
TauCeti.transcendental_exp_mul {l β : ℂ} (hl : l ≠ 0) (hα : IsAlgebraic ℚ (Complex.exp l))
  (hβ : IsAlgebraic ℚ β) (hirr : ∀ (q : ℚ), β ≠ ↑q) : Transcendental ℚ (Complex.exp (β * l))
```

**The Gelfond–Schneider theorem for `Complex.cpow`.** Formalized in Tau Ceti as [`TauCeti.transcendental_cpow`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Transcendental/GelfondSchneider/Gelfond/Theorem.html#TauCeti.transcendental_cpow).

```lean
TauCeti.transcendental_cpow {α β : ℂ} (hα : IsAlgebraic ℚ α) (h0 : α ≠ 0) (h1 : α ≠ 1)
  (hβ : IsAlgebraic ℚ β) (hirr : ∀ (q : ℚ), β ≠ ↑q) : Transcendental ℚ (α ^ β)
```

## Sources

- [Tau Ceti documentation: `TauCeti.transcendental_rpow`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Transcendental/GelfondSchneider/Theorem.html#TauCeti.transcendental_rpow)
- [Source of `TauCeti.transcendental_rpow` in TauCeti/NumberTheory/Transcendental/GelfondSchneider/Theorem.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/Transcendental/GelfondSchneider/Theorem.lean#L208)
- [Tau Ceti roadmap status: Diophantine approximation and transcendence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/DiophantineApproximationAndTranscendence/STATUS.md)
