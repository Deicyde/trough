---
declaration: theorem
origin: cited
lean: TauCeti.hausdorff_bernstein_widder
statement: formalized
proof: formalized
---

# Hausdorff--Bernstein--Widder theorem

, finite-measure version on `ℝ≥0`.

A function is continuous on `[0, ∞)` and completely monotone on `(0, ∞)` if and only if it is
the Laplace transform of a finite positive measure on `ℝ≥0`.

```lean
TauCeti.hausdorff_bernstein_widder (f : ℝ → ℝ) :
  TauCeti.IsContinuousCompletelyMonotoneOnIoi f ↔ ∃ μ, TauCeti.RepresentsLaplace μ f
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.hausdorff_bernstein_widder`](https://taucetiproject.org/docs/TauCeti/Analysis/CompletelyMonotone/Bernstein/HausdorffBernsteinWidder.html#TauCeti.hausdorff_bernstein_widder).

## Sources

- [Tau Ceti documentation: `TauCeti.hausdorff_bernstein_widder`](https://taucetiproject.org/docs/TauCeti/Analysis/CompletelyMonotone/Bernstein/HausdorffBernsteinWidder.html#TauCeti.hausdorff_bernstein_widder)
- [Source of `TauCeti.hausdorff_bernstein_widder` in TauCeti/Analysis/CompletelyMonotone/Bernstein/HausdorffBernsteinWidder.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/CompletelyMonotone/Bernstein/HausdorffBernsteinWidder.lean#L62)
- [Tau Ceti roadmap status: One-parameter semigroups, completely monotone and positive-definite functions, and Bochner-type representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/OneParameterSemigroups/STATUS.md)
