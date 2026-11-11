---
declaration: theorem
origin: cited
lean: TotallyBounded.exists_tendsto_zero_subset_closure_convexHull
statement: formalized
proof: formalized
---

# Grothendieck's compactness lemma

A totally bounded subset of a real seminormed space lies
in the closed convex hull of the range of a sequence tending to `0`.

```lean
TotallyBounded.exists_tendsto_zero_subset_closure_convexHull.{u_1} {E : Type u_1}
  [SeminormedAddCommGroup E] [NormedSpace ℝ E] {s : Set E} (hs : TotallyBounded s) :
  ∃ x, Filter.Tendsto x Filter.atTop (nhds 0) ∧ s ⊆ closure ((convexHull ℝ) (Set.range x))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TotallyBounded.exists_tendsto_zero_subset_closure_convexHull`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/TotallyBounded.html#TotallyBounded.exists_tendsto_zero_subset_closure_convexHull).

## Sources

- [Tau Ceti documentation: `TotallyBounded.exists_tendsto_zero_subset_closure_convexHull`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/TotallyBounded.html#TotallyBounded.exists_tendsto_zero_subset_closure_convexHull)
- [Source of `TotallyBounded.exists_tendsto_zero_subset_closure_convexHull` in TauCeti/Analysis/Convex/TotallyBounded.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Convex/TotallyBounded.lean#L101)
