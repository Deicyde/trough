---
declaration: theorem
origin: cited
lean: TauCeti.HasLaurentSeriesOnAnnulus.circleLaurentCoeff_eq
statement: formalized
proof: formalized
---

# Cauchy-Laurent coefficient formula

For any convergent Laurent series on
`Metric.eball c R \ Metric.closedBall c r` and any interior circle radius `ρ ∈ (r, R)`, the
`n`-th Laurent coefficient is `circleLaurentCoeff f c ρ n`.

```lean
TauCeti.HasLaurentSeriesOnAnnulus.circleLaurentCoeff_eq.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℂ E] [CompleteSpace E] {f : ℂ → E} {a : ℤ → E} {c : ℂ} {r ρ : ℝ} {R : ENNReal}
  (h : TauCeti.HasLaurentSeriesOnAnnulus f a c r R) (hrρ : r < ρ) (hρR : ENNReal.ofReal ρ < R)
  (n : ℤ) : TauCeti.circleLaurentCoeff f c ρ n = a n
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.HasLaurentSeriesOnAnnulus.circleLaurentCoeff_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Laurent/Expansion.html#TauCeti.HasLaurentSeriesOnAnnulus.circleLaurentCoeff_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.HasLaurentSeriesOnAnnulus.circleLaurentCoeff_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Laurent/Expansion.html#TauCeti.HasLaurentSeriesOnAnnulus.circleLaurentCoeff_eq)
- [Source of `TauCeti.HasLaurentSeriesOnAnnulus.circleLaurentCoeff_eq` in TauCeti/Analysis/Complex/Laurent/Expansion.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/Laurent/Expansion.lean#L220)
