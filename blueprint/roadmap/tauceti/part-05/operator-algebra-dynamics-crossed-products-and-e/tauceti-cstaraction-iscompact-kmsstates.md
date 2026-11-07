---
declaration: theorem
origin: cited
lean: TauCeti.CStarAction.isCompact_kmsStates
statement: formalized
proof: formalized
---

# TauCeti.CStarAction.isCompact\_kmsStates

**Weak-* compactness of `K_β`.** For unital `B`, the set of β-KMS states is weak-* compact.

```lean
TauCeti.CStarAction.isCompact_kmsStates.{u_2} {B : Type u_2} [CStarAlgebra B] [PartialOrder B]
  [StarOrderedRing B] {α : TauCeti.CStarAction (Multiplicative ℝ) B} {β : ℝ} :
  IsCompact (α.kmsStates β)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Dense analytic KMS criterion](dense-analytic-kms-criterion.md)
- [Density of entire analytic elements](density-of-entire-analytic-elements.md)
- [TauCeti.CStarAction.entireAnalytic](tauceti-cstaraction-entireanalytic.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CStarAction.isCompact_kmsStates`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Action/KMS/StateSpace.html#TauCeti.CStarAction.isCompact_kmsStates).

## Sources

- [Tau Ceti documentation: `TauCeti.CStarAction.isCompact_kmsStates`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Action/KMS/StateSpace.html#TauCeti.CStarAction.isCompact_kmsStates)
- [Source of `TauCeti.CStarAction.isCompact_kmsStates` in TauCeti/Analysis/CStarAlgebra/Action/KMS/StateSpace.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/CStarAlgebra/Action/KMS/StateSpace.lean#L147)
- [Tau Ceti roadmap status: Operator-algebra dynamics, crossed products, and equilibrium](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/OperatorAlgebraDynamics/STATUS.md)
