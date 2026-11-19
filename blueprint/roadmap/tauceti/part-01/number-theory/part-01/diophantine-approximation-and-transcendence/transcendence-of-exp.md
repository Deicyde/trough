---
declaration: theorem
origin: cited
lean: TauCeti.transcendental_exp_pi_mul
statement: formalized
proof: formalized
---

# Transcendence of `exp (π α)`

If `α` is an algebraic number that is not a rational
multiple of `i`, then `exp (π α)` is transcendental.

```lean
TauCeti.transcendental_exp_pi_mul {α : ℂ} (hα : IsAlgebraic ℚ α)
  (hαI : ∀ (q : ℚ), α ≠ ↑q * Complex.I) : Transcendental ℚ (Complex.exp (↑Real.pi * α))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Gelfond–Schneider theorem (Karatarakis–Wiedijk, §3)](the-gelfond-schneider-theorem-karatarakis-wiedij.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.transcendental_exp_pi_mul`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Transcendental/GelfondSchneider/Corollaries.html#TauCeti.transcendental_exp_pi_mul).

## Sources

- [Tau Ceti documentation: `TauCeti.transcendental_exp_pi_mul`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Transcendental/GelfondSchneider/Corollaries.html#TauCeti.transcendental_exp_pi_mul)
- [Source of `TauCeti.transcendental_exp_pi_mul` in TauCeti/NumberTheory/Transcendental/GelfondSchneider/Corollaries.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/Transcendental/GelfondSchneider/Corollaries.lean#L55)
- [Tau Ceti roadmap status: Diophantine approximation and transcendence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/DiophantineApproximationAndTranscendence/STATUS.md)
