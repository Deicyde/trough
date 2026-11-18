---
declaration: theorem
origin: cited
lean: TauCeti.closure_convexHull_extremePoints_stateSpace
statement: formalized
proof: formalized
---

# Krein–Milman for states

For unital `A`, the state space is the weak-* closed convex hull
of its extreme points, the pure states.

```lean
TauCeti.closure_convexHull_extremePoints_stateSpace.{u_1} {A : Type u_1} [CStarAlgebra A]
  [PartialOrder A] [StarOrderedRing A] :
  closure ((convexHull ℝ) (Set.extremePoints ℝ (TauCeti.stateSpace A))) = TauCeti.stateSpace A
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Weak-* compactness of the state space](weak-compactness-of-the-state-space.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.closure_convexHull_extremePoints_stateSpace`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/State/Space.html#TauCeti.closure_convexHull_extremePoints_stateSpace).

## Sources

- [Tau Ceti documentation: `TauCeti.closure_convexHull_extremePoints_stateSpace`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/State/Space.html#TauCeti.closure_convexHull_extremePoints_stateSpace)
- [Source of `TauCeti.closure_convexHull_extremePoints_stateSpace` in TauCeti/Analysis/CStarAlgebra/State/Space.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/CStarAlgebra/State/Space.lean#L223)
- [Tau Ceti roadmap status: Von Neumann algebras, factors, and modular theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/VonNeumannAlgebras/STATUS.md)
