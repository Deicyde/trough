---
declaration: theorem
origin: cited
lean: TauCeti.LSeries.differentiableOn_stepCorrection
statement: formalized
proof: formalized
---

# Holomorphy of the step correction

For coefficients bounded from `n = 1` on, the step
correction is holomorphic on the half-plane `-1 < re z`: near `z₀`, the terms are bounded
uniformly by a multiple of the summable `n ^ (-1 - ε)` for `ε = (re z₀ + 1) / 2`.

```lean
TauCeti.LSeries.differentiableOn_stepCorrection {a : ℕ → ℂ} {M : ℝ}
  (hbound : ∀ (n : ℕ), 1 ≤ n → ‖a n‖ ≤ M) :
  DifferentiableOn ℂ (TauCeti.LSeries.stepCorrection a) {z | -1 < z.re}
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Substitution `x = exp t`](substitution-x-exp-t.md)
- [Truncated Laplace transforms are entire](truncated-laplace-transforms-are-entire.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LSeries.differentiableOn_stepCorrection`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/BoundaryConvergence/StepCorrection.html#TauCeti.LSeries.differentiableOn_stepCorrection).

## Sources

- [Tau Ceti documentation: `TauCeti.LSeries.differentiableOn_stepCorrection`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/BoundaryConvergence/StepCorrection.html#TauCeti.LSeries.differentiableOn_stepCorrection)
- [Source of `TauCeti.LSeries.differentiableOn_stepCorrection` in TauCeti/NumberTheory/LSeries/BoundaryConvergence/StepCorrection.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LSeries/BoundaryConvergence/StepCorrection.lean#L183)
- [Tau Ceti roadmap status: Bounded Laplace and ordered Dirichlet boundary convergence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/TauberianBoundaryConvergence/STATUS.md)
