---
declaration: theorem
origin: cited
lean: TauCeti.exists_representsLaplace_of_isContinuousCompletelyMonotoneOnIoi, TauCeti.exists_representsLaplace_of_isDifferenceCompletelyMonotone_of_continuousWithinAt
statement: formalized
proof: formalized
---

# Existence half of the Hausdorff--Bernstein--Widder theorem

a function continuous on
`[0, ∞)` and completely monotone on `(0, ∞)` is the Laplace transform of a finite positive
measure on `ℝ≥0`.

```lean
TauCeti.exists_representsLaplace_of_isContinuousCompletelyMonotoneOnIoi {f : ℝ → ℝ}
  (hf : TauCeti.IsContinuousCompletelyMonotoneOnIoi f) : ∃ μ, TauCeti.RepresentsLaplace μ f
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Bernstein's theorem, existence half](bernsteins-theorem-existence-half.md)
- [Prokhorov's theorem for finite measures](../../../../measure-theory/measure/prokhorovs-theorem-for-finite-measures.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_representsLaplace_of_isContinuousCompletelyMonotoneOnIoi`](https://taucetiproject.org/docs/TauCeti/Analysis/CompletelyMonotone/Bernstein/HausdorffBernsteinWidder.html#TauCeti.exists_representsLaplace_of_isContinuousCompletelyMonotoneOnIoi).

## Other forms

**The existence half of the Hausdorff--Bernstein--Widder theorem in finite-difference form.** Formalized in Tau Ceti as [`TauCeti.exists_representsLaplace_of_isDifferenceCompletelyMonotone_of_continuousWithinAt`](https://taucetiproject.org/docs/TauCeti/Analysis/CompletelyMonotone/FiniteDifference/Laplace.html#TauCeti.exists_representsLaplace_of_isDifferenceCompletelyMonotone_of_continuousWithinAt).

```lean
TauCeti.exists_representsLaplace_of_isDifferenceCompletelyMonotone_of_continuousWithinAt {f : ℝ → ℝ}
  (hf : TauCeti.IsDifferenceCompletelyMonotone f) (hcont : ContinuousWithinAt f (Set.Ici 0) 0) :
  ∃ μ, TauCeti.RepresentsLaplace μ f
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_representsLaplace_of_isContinuousCompletelyMonotoneOnIoi`](https://taucetiproject.org/docs/TauCeti/Analysis/CompletelyMonotone/Bernstein/HausdorffBernsteinWidder.html#TauCeti.exists_representsLaplace_of_isContinuousCompletelyMonotoneOnIoi)
- [Source of `TauCeti.exists_representsLaplace_of_isContinuousCompletelyMonotoneOnIoi` in TauCeti/Analysis/CompletelyMonotone/Bernstein/HausdorffBernsteinWidder.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/CompletelyMonotone/Bernstein/HausdorffBernsteinWidder.lean#L50)
