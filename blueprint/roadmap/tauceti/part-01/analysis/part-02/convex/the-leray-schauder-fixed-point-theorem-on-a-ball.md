---
declaration: theorem
origin: cited
lean: TauCeti.leraySchauderFixedPoint_closedBall
statement: formalized
proof: formalized
---

# The Leray–Schauder fixed-point theorem on a ball

let `T` be continuous on the closed
ball of radius `R > 0` about the origin, with image of compact closure. If no `u` with
`‖u‖ = R` solves `u = θ • T u` for `0 < θ < 1`, then `T` has a fixed point in the ball.

```lean
TauCeti.leraySchauderFixedPoint_closedBall.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] {R : ℝ} (hR : 0 < R) {T : E → E} (hT : ContinuousOn T (Metric.closedBall 0 R))
  (hK : IsCompact (closure (T '' Metric.closedBall 0 R)))
  (hbd : ∀ (u : E), ‖u‖ = R → ∀ θ ∈ Set.Ioo 0 1, u ≠ θ • T u) :
  ∃ u ∈ Metric.closedBall 0 R, Function.IsFixedPt T u
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Schauder's fixed-point theorem](schauders-fixed-point-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.leraySchauderFixedPoint_closedBall`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/SchauderFixedPoint.html#TauCeti.leraySchauderFixedPoint_closedBall).

## Sources

- [Tau Ceti documentation: `TauCeti.leraySchauderFixedPoint_closedBall`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/SchauderFixedPoint.html#TauCeti.leraySchauderFixedPoint_closedBall)
- [Source of `TauCeti.leraySchauderFixedPoint_closedBall` in TauCeti/Analysis/Convex/SchauderFixedPoint.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Convex/SchauderFixedPoint.lean#L156)
