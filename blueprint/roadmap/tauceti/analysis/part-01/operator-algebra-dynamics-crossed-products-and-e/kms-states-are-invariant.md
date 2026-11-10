---
declaration: theorem
origin: cited
lean: TauCeti.CStarAction.IsKMSState.apply_action
statement: formalized
proof: formalized
---

# KMS states are invariant

For `β ≠ 0`, every β-KMS state `ω` is invariant under the
dynamics: `ω (α_t(a)) = ω a`. At `β = 0` the KMS states are the tracial states, which need not
be invariant.

```lean
TauCeti.CStarAction.IsKMSState.apply_action.{u_1} {A : Type u_1} [NonUnitalCStarAlgebra A]
  {α : TauCeti.CStarAction (Multiplicative ℝ) A} {β : ℝ} [PartialOrder A] [StarOrderedRing A]
  {ω : A →P[ℂ] ℂ} (hω : α.IsKMSState β ω) (hβ : β ≠ 0) (t : Multiplicative ℝ) (a : A) :
  ω ((α t) a) = ω a
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Density of entire analytic elements](density-of-entire-analytic-elements.md)
- [Schwarz reflection principle (real axis)](../conformal-mapping-and-the-geometric-theory-of-ho/part-01/schwarz-reflection-principle-real-axis.md)
- [TauCeti.CStarAction.entireAnalytic](tauceti-cstaraction-entireanalytic.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CStarAction.IsKMSState.apply_action`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Action/KMS/Basic.html#TauCeti.CStarAction.IsKMSState.apply_action).

## Sources

- [Tau Ceti documentation: `TauCeti.CStarAction.IsKMSState.apply_action`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Action/KMS/Basic.html#TauCeti.CStarAction.IsKMSState.apply_action)
- [Source of `TauCeti.CStarAction.IsKMSState.apply_action` in TauCeti/Analysis/CStarAlgebra/Action/KMS/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/CStarAlgebra/Action/KMS/Basic.lean#L294)
- [Tau Ceti roadmap status: Operator-algebra dynamics, crossed products, and equilibrium](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/OperatorAlgebraDynamics/STATUS.md)
