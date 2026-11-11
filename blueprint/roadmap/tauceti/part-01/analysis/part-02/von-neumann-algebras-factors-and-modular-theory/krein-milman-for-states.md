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

Formalized in Tau Ceti as [`TauCeti.closure_convexHull_extremePoints_stateSpace`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/StateSpace.html#TauCeti.closure_convexHull_extremePoints_stateSpace).

## Sources

- [Tau Ceti documentation: `TauCeti.closure_convexHull_extremePoints_stateSpace`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/StateSpace.html#TauCeti.closure_convexHull_extremePoints_stateSpace)
- [Source of `TauCeti.closure_convexHull_extremePoints_stateSpace` in TauCeti/Analysis/CStarAlgebra/StateSpace.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/CStarAlgebra/StateSpace.lean#L223)
- [Tau Ceti roadmap status: Von Neumann algebras, factors, and modular theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/VonNeumannAlgebras/STATUS.md)
