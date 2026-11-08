---
declaration: theorem
origin: cited
lean: TauCeti.hausdorff_bernstein_widder, TauCeti.hausdorff_bernstein_widder_difference, TauCeti.hausdorff_bernstein_widder_onIoi
statement: formalized
proof: formalized
---

# Hausdorff--Bernstein--Widder theorem, finite-measure version on `ℝ≥0`

A function is continuous on `[0, ∞)` and completely monotone on `(0, ∞)` if and only if it is
the Laplace transform of a finite positive measure on `ℝ≥0`.

```lean
TauCeti.hausdorff_bernstein_widder (f : ℝ → ℝ) :
  TauCeti.IsContinuousCompletelyMonotoneOnIoi f ↔ ∃ μ, TauCeti.RepresentsLaplace μ f
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Bernstein's theorem, existence half](bernsteins-theorem-existence-half.md)
- [Existence half of the Hausdorff--Bernstein--Widder theorem](existence-half-of-the-hausdorff-bernstein-widder.md)
- [Moment determinacy, exponential-moment form (the roadmap's B1 hypothesis)](../../../../probability/weighted-orthogonal-l2-bases-completeness-hilber/part-01/moment-determinacy-exponential-moment-form-the-r.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.hausdorff_bernstein_widder`](https://taucetiproject.org/docs/TauCeti/Analysis/CompletelyMonotone/Bernstein/HausdorffBernsteinWidder.html#TauCeti.hausdorff_bernstein_widder).

## Other forms

**The Hausdorff--Bernstein--Widder theorem in finite-difference form.** Formalized in Tau Ceti as [`TauCeti.hausdorff_bernstein_widder_difference`](https://taucetiproject.org/docs/TauCeti/Analysis/CompletelyMonotone/FiniteDifference/Laplace.html#TauCeti.hausdorff_bernstein_widder_difference).

```lean
TauCeti.hausdorff_bernstein_widder_difference (f : ℝ → ℝ) :
  TauCeti.IsDifferenceCompletelyMonotone f ∧ ContinuousWithinAt f (Set.Ici 0) 0 ↔
    ∃ μ, TauCeti.RepresentsLaplace μ f
```

**The Hausdorff--Bernstein--Widder theorem on the open half-line.** Formalized in Tau Ceti as [`TauCeti.hausdorff_bernstein_widder_onIoi`](https://taucetiproject.org/docs/TauCeti/Analysis/CompletelyMonotone/Bernstein/OpenHalfLine.html#TauCeti.hausdorff_bernstein_widder_onIoi).

```lean
TauCeti.hausdorff_bernstein_widder_onIoi (f : ℝ → ℝ) :
  TauCeti.IsCompletelyMonotoneOnIoi f ↔ ∃ μ, TauCeti.RepresentsLaplaceOnIoi μ f
```

## Sources

- [Tau Ceti documentation: `TauCeti.hausdorff_bernstein_widder`](https://taucetiproject.org/docs/TauCeti/Analysis/CompletelyMonotone/Bernstein/HausdorffBernsteinWidder.html#TauCeti.hausdorff_bernstein_widder)
- [Source of `TauCeti.hausdorff_bernstein_widder` in TauCeti/Analysis/CompletelyMonotone/Bernstein/HausdorffBernsteinWidder.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/CompletelyMonotone/Bernstein/HausdorffBernsteinWidder.lean#L62)
- [Tau Ceti roadmap status: One-parameter semigroups, completely monotone and positive-definite functions, and Bochner-type representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/OneParameterSemigroups/STATUS.md)
