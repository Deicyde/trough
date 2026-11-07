---
declaration: theorem
origin: cited
lean: TauCeti.CStarAction.convex_kmsStates
statement: formalized
proof: formalized
---

# Convexity of `K_β`

Convex combinations of β-KMS states are β-KMS states.

```lean
TauCeti.CStarAction.convex_kmsStates.{u_1} {A : Type u_1} [NonUnitalCStarAlgebra A] [PartialOrder A]
  [StarOrderedRing A] {α : TauCeti.CStarAction (Multiplicative ℝ) A} {β : ℝ} :
  Convex ℝ (α.kmsStates β)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Dense analytic KMS criterion](dense-analytic-kms-criterion.md)
- [Density of entire analytic elements](density-of-entire-analytic-elements.md)
- [TauCeti.CStarAction.entireAnalytic](tauceti-cstaraction-entireanalytic.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CStarAction.convex_kmsStates`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Action/KMS/StateSpace.html#TauCeti.CStarAction.convex_kmsStates).

## Sources

- [Tau Ceti documentation: `TauCeti.CStarAction.convex_kmsStates`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Action/KMS/StateSpace.html#TauCeti.CStarAction.convex_kmsStates)
- [Source of `TauCeti.CStarAction.convex_kmsStates` in TauCeti/Analysis/CStarAlgebra/Action/KMS/StateSpace.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/CStarAlgebra/Action/KMS/StateSpace.lean#L118)
- [Tau Ceti roadmap status: Operator-algebra dynamics, crossed products, and equilibrium](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/OperatorAlgebraDynamics/STATUS.md)
