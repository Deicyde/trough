---
declaration: theorem
origin: cited
lean: TauCeti.LSeries.stepCorrection_zero
statement: formalized
proof: formalized
---

# The step correction at `0`

`stepCorrection a 0 = ∑' n, a n (log (1 + 1 / n) - 1 / n)`.

```lean
TauCeti.LSeries.stepCorrection_zero (a : ℕ → ℂ) :
  TauCeti.LSeries.stepCorrection a 0 = ∑' (n : ℕ), a n * ↑(Real.log (1 + 1 / ↑n) - 1 / ↑n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Substitution `x = exp t`](substitution-x-exp-t.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LSeries.stepCorrection_zero`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/BoundaryConvergence/StepCorrection.html#TauCeti.LSeries.stepCorrection_zero).

## Sources

- [Tau Ceti documentation: `TauCeti.LSeries.stepCorrection_zero`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/BoundaryConvergence/StepCorrection.html#TauCeti.LSeries.stepCorrection_zero)
- [Source of `TauCeti.LSeries.stepCorrection_zero` in TauCeti/NumberTheory/LSeries/BoundaryConvergence/StepCorrection.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LSeries/BoundaryConvergence/StepCorrection.lean#L241)
- [Tau Ceti roadmap status: Bounded Laplace and ordered Dirichlet boundary convergence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/TauberianBoundaryConvergence/STATUS.md)
