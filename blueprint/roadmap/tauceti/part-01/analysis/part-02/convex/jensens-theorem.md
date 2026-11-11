---
declaration: theorem
origin: cited
lean: TauCeti.convexOn_of_midpoint
statement: formalized
proof: formalized
---

# Jensen's theorem

On a convex subset of a real topological vector space, an upper
semicontinuous function that is midpoint convex is convex. In particular, so is a continuous one.

```lean
TauCeti.convexOn_of_midpoint.{u_1} {E : Type u_1} [AddCommGroup E] [_root_.Module ℝ E]
  [TopologicalSpace E] [IsTopologicalAddGroup E] [ContinuousSMul ℝ E] {s : Set E} {f : E → ℝ}
  (hs : Convex ℝ s) (hf : UpperSemicontinuousOn f s)
  (h : ∀ x ∈ s, ∀ y ∈ s, f (midpoint ℝ x y) ≤ (f x + f y) / 2) : ConvexOn ℝ s f
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.convexOn_of_midpoint`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/Midpoint.html#TauCeti.convexOn_of_midpoint).

## Sources

- [Tau Ceti documentation: `TauCeti.convexOn_of_midpoint`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/Midpoint.html#TauCeti.convexOn_of_midpoint)
- [Source of `TauCeti.convexOn_of_midpoint` in TauCeti/Analysis/Convex/Midpoint.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Convex/Midpoint.lean#L84)
