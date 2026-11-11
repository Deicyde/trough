---
declaration: theorem
origin: cited
lean: TauCeti.CStarAction.isGroundState_iff_norm_apply_mul_entireExtension_le
statement: formalized
proof: formalized
---

# Analytic characterization of ground states

A positive functional `ω` is a ground state
exactly when it has norm one and `‖ω (a α_z(b))‖ ≤ ‖a‖ ‖b‖` for every `a`, every entire analytic
`b` and every `z` in the closed upper half-plane.

```lean
TauCeti.CStarAction.isGroundState_iff_norm_apply_mul_entireExtension_le.{u_1} {A : Type u_1}
  [NonUnitalCStarAlgebra A] {α : TauCeti.CStarAction (Multiplicative ℝ) A} [PartialOrder A]
  [StarOrderedRing A] {ω : A →P[ℂ] ℂ} :
  α.IsGroundState ω ↔
    ‖ω.toContinuousLinearMap‖ = 1 ∧
      ∀ (a b : A),
        α.IsEntireAnalytic b → ∀ (z : ℂ), 0 ≤ z.im → ‖ω (a * α.entireExtension b z)‖ ≤ ‖a‖ * ‖b‖
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Phragmén–Lindelöf principle on the upper half-plane](../../part-02/complex/part-03/phragmen-lindelof-principle-on-the-upper-half-pl.md)
- [Schwarz reflection principle (real axis)](../../part-02/complex/part-03/schwarz-reflection-principle-real-axis.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CStarAction.isGroundState_iff_norm_apply_mul_entireExtension_le`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Action/GroundState/Basic.html#TauCeti.CStarAction.isGroundState_iff_norm_apply_mul_entireExtension_le).

## Sources

- [Tau Ceti documentation: `TauCeti.CStarAction.isGroundState_iff_norm_apply_mul_entireExtension_le`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Action/GroundState/Basic.html#TauCeti.CStarAction.isGroundState_iff_norm_apply_mul_entireExtension_le)
- [Source of `TauCeti.CStarAction.isGroundState_iff_norm_apply_mul_entireExtension_le` in TauCeti/Analysis/CStarAlgebra/Action/GroundState/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/CStarAlgebra/Action/GroundState/Basic.lean#L236)
- [Tau Ceti roadmap status: Operator-algebra dynamics, crossed products, and equilibrium](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/OperatorAlgebraDynamics/STATUS.md)
