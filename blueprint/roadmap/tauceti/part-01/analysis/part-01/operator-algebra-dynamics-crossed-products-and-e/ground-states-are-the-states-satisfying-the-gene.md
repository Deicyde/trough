---
declaration: theorem
origin: cited
lean: TauCeti.CStarAction.isGroundState_iff_neg_I_mul_apply_star_mul_generator_nonneg
statement: formalized
proof: formalized
---

# Ground states are the states satisfying the generator inequality

A positive functional
`ω` is a ground state exactly when it has norm one and `-i ω (a⋆ δ(a)) ≥ 0` for every `a` in the
domain of the generator `δ` of the dynamics.

```lean
TauCeti.CStarAction.isGroundState_iff_neg_I_mul_apply_star_mul_generator_nonneg.{u_1} {A : Type u_1}
  [NonUnitalCStarAlgebra A] {α : TauCeti.CStarAction (Multiplicative ℝ) A} [PartialOrder A]
  [StarOrderedRing A] {ω : A →P[ℂ] ℂ} :
  α.IsGroundState ω ↔
    ‖ω.toContinuousLinearMap‖ = 1 ∧
      ∀ (a : ↥α.generator.domain), 0 ≤ -Complex.I * ω (star ↑a * ↑α.generator a)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Analytic characterization of ground states](analytic-characterization-of-ground-states.md)
- [Phragmén–Lindelöf principle on the upper half-plane](../../part-02/complex/part-03/phragmen-lindelof-principle-on-the-upper-half-pl.md)
- [Schwarz reflection principle (real axis)](../../part-02/complex/part-03/schwarz-reflection-principle-real-axis.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CStarAction.isGroundState_iff_neg_I_mul_apply_star_mul_generator_nonneg`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Action/GroundState/Basic.html#TauCeti.CStarAction.isGroundState_iff_neg_I_mul_apply_star_mul_generator_nonneg).

## Sources

- [Tau Ceti documentation: `TauCeti.CStarAction.isGroundState_iff_neg_I_mul_apply_star_mul_generator_nonneg`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Action/GroundState/Basic.html#TauCeti.CStarAction.isGroundState_iff_neg_I_mul_apply_star_mul_generator_nonneg)
- [Source of `TauCeti.CStarAction.isGroundState_iff_neg_I_mul_apply_star_mul_generator_nonneg` in TauCeti/Analysis/CStarAlgebra/Action/GroundState/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/CStarAlgebra/Action/GroundState/Basic.lean#L449)
- [Tau Ceti roadmap status: Operator-algebra dynamics, crossed products, and equilibrium](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/OperatorAlgebraDynamics/STATUS.md)
