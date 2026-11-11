---
declaration: theorem
origin: cited
lean: StrongDual.bipolar_eq_closedAbsConvexHull
statement: formalized
proof: formalized
---

# The bipolar theorem for an arbitrary set

Its bipolar is the closed absolutely
convex hull of the set together with zero, including when the set is empty.

```lean
StrongDual.bipolar_eq_closedAbsConvexHull.{u_1, u_2} (𝕜 : Type u_1) {E : Type u_2} [RCLike 𝕜]
  [AddCommGroup E] [_root_.Module 𝕜 E] [TopologicalSpace E] [_root_.Module ℝ E]
  [IsScalarTower ℝ 𝕜 E] [IsTopologicalAddGroup E] [ContinuousSMul 𝕜 E] [LocallyConvexSpace ℝ E]
  (s : Set E) :
  (topDualPairing 𝕜 E).polar (StrongDual.polar 𝕜 s) = (closedAbsConvexHull 𝕜) (insert 0 s)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The bipolar theorem](the-bipolar-theorem.md)

## Lean

Formalized in Tau Ceti as [`StrongDual.bipolar_eq_closedAbsConvexHull`](https://taucetiproject.org/docs/TauCeti/Analysis/LocallyConvex/Bipolar.html#StrongDual.bipolar_eq_closedAbsConvexHull).

## Sources

- [Tau Ceti documentation: `StrongDual.bipolar_eq_closedAbsConvexHull`](https://taucetiproject.org/docs/TauCeti/Analysis/LocallyConvex/Bipolar.html#StrongDual.bipolar_eq_closedAbsConvexHull)
- [Source of `StrongDual.bipolar_eq_closedAbsConvexHull` in TauCeti/Analysis/LocallyConvex/Bipolar.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/LocallyConvex/Bipolar.lean#L85)
