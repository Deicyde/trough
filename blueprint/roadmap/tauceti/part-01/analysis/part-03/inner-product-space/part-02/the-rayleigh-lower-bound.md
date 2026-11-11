---
declaration: theorem
origin: cited
lean: IsCoercive.inv_norm_formSolutionOperator_mul_norm_apply_sq_le
statement: formalized
proof: formalized
---

# The Rayleigh lower bound

`‖S‖⁻¹ ‖J v‖² ≤ B v v` for every `v : V`.  For the Dirichlet
problem this is the Poincaré inequality with the reciprocal solution-operator norm as its
constant.  Beyond coercivity, only symmetry is needed: when `S = 0` the left-hand side vanishes
and the bound is the nonnegativity of the energy.

```lean
IsCoercive.inv_norm_formSolutionOperator_mul_norm_apply_sq_le.{u_1, u_2} {V : Type u_1}
  {H : Type u_2} [NormedAddCommGroup V] [InnerProductSpace ℝ V] [CompleteSpace V]
  [SeminormedAddCommGroup H] [InnerProductSpace ℝ H] {B : V →L[ℝ] V →L[ℝ] ℝ} (hB : IsCoercive B)
  (J : V →L[ℝ] H) (hsymm : ∀ (u v : V), (B u) v = (B v) u) (v : V) :
  ‖hB.formSolutionOperator J‖⁻¹ * ‖J v‖ ^ 2 ≤ (B v) v
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`IsCoercive.inv_norm_formSolutionOperator_mul_norm_apply_sq_le`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Variational/Rayleigh.html#IsCoercive.inv_norm_formSolutionOperator_mul_norm_apply_sq_le).

## Sources

- [Tau Ceti documentation: `IsCoercive.inv_norm_formSolutionOperator_mul_norm_apply_sq_le`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Variational/Rayleigh.html#IsCoercive.inv_norm_formSolutionOperator_mul_norm_apply_sq_le)
- [Source of `IsCoercive.inv_norm_formSolutionOperator_mul_norm_apply_sq_le` in TauCeti/Analysis/InnerProductSpace/Variational/Rayleigh.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/InnerProductSpace/Variational/Rayleigh.lean#L112)
