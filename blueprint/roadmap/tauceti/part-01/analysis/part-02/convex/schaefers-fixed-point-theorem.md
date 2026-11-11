---
declaration: theorem
origin: cited
lean: TauCeti.schaeferFixedPoint
statement: formalized
proof: formalized
---

# Schaefer's fixed-point theorem

a continuous map `T` of a real normed space that sends
bounded sets to sets with compact closure has a fixed point, provided the solutions `u` of
`u = θ • T u` with `0 < θ < 1` form a bounded set. The classical a priori bound over
`0 ≤ θ ≤ 1` implies this hypothesis.

```lean
TauCeti.schaeferFixedPoint.{u_1} {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] {T : E → E}
  (hT : Continuous T) (hK : ∀ (s : Set E), Bornology.IsBounded s → IsCompact (closure (T '' s)))
  (hbd : Bornology.IsBounded {u | ∃ θ ∈ Set.Ioo 0 1, u = θ • T u}) : ∃ u, Function.IsFixedPt T u
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Leray–Schauder fixed-point theorem on a ball](the-leray-schauder-fixed-point-theorem-on-a-ball.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.schaeferFixedPoint`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/SchauderFixedPoint.html#TauCeti.schaeferFixedPoint).

## Sources

- [Tau Ceti documentation: `TauCeti.schaeferFixedPoint`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/SchauderFixedPoint.html#TauCeti.schaeferFixedPoint)
- [Source of `TauCeti.schaeferFixedPoint` in TauCeti/Analysis/Convex/SchauderFixedPoint.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Convex/SchauderFixedPoint.lean#L188)
