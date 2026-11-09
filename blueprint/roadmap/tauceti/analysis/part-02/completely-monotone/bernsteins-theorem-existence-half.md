---
declaration: theorem
origin: cited
lean: TauCeti.exists_representsLaplace_of_isCompletelyMonotone
statement: formalized
proof: formalized
---

# Bernstein's theorem, existence half

A completely monotone function on `[0, ∞)` is the
Laplace transform of a finite positive measure on `ℝ≥0`.

Uniqueness of that measure is not asserted here; it is `TauCeti.RepresentsLaplace.unique`, and
the two combine in the Hausdorff--Bernstein--Widder theorem.

```lean
TauCeti.exists_representsLaplace_of_isCompletelyMonotone {f : ℝ → ℝ}
  (hcm : TauCeti.IsCompletelyMonotone f) : ∃ μ, TauCeti.RepresentsLaplace μ f
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Prokhorov's theorem for finite measures](../../../measure-theory/measure/prokhorovs-theorem-for-finite-measures.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_representsLaplace_of_isCompletelyMonotone`](https://taucetiproject.org/docs/TauCeti/Analysis/CompletelyMonotone/Bernstein/Theorem.html#TauCeti.exists_representsLaplace_of_isCompletelyMonotone).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_representsLaplace_of_isCompletelyMonotone`](https://taucetiproject.org/docs/TauCeti/Analysis/CompletelyMonotone/Bernstein/Theorem.html#TauCeti.exists_representsLaplace_of_isCompletelyMonotone)
- [Source of `TauCeti.exists_representsLaplace_of_isCompletelyMonotone` in TauCeti/Analysis/CompletelyMonotone/Bernstein/Theorem.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/CompletelyMonotone/Bernstein/Theorem.lean#L123)
