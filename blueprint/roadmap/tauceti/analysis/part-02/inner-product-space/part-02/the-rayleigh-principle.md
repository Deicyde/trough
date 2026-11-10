---
declaration: theorem
origin: cited
lean: IsCoercive.isLeast_rayleighQuotient
statement: formalized
proof: formalized
---

# The Rayleigh principle

the least variational eigenvalue `‖S‖⁻¹` is the *minimum* of the
Rayleigh quotient `B v v / ‖J v‖²` over the vectors with `J v ≠ 0`.  The minimum is attained at
an eigenfunction, which is why compactness of `J` is assumed.

```lean
IsCoercive.isLeast_rayleighQuotient.{u_3, u_4} {V : Type u_3} {H : Type u_4} [NormedAddCommGroup V]
  [InnerProductSpace ℝ V] [CompleteSpace V] [NormedAddCommGroup H] [InnerProductSpace ℝ H]
  {B : V →L[ℝ] V →L[ℝ] ℝ} (hB : IsCoercive B) {J : V →L[ℝ] H} (hJ : IsCompactOperator ⇑J)
  (hsymm : ∀ (u v : V), (B u) v = (B v) u) (hJne : J ≠ 0) :
  IsLeast {r | ∃ v, J v ≠ 0 ∧ (B v) v / ‖J v‖ ^ 2 = r} ‖hB.formSolutionOperator J‖⁻¹
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Rayleigh lower bound](the-rayleigh-lower-bound.md)

## Lean

Formalized in Tau Ceti as [`IsCoercive.isLeast_rayleighQuotient`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Variational/Rayleigh.html#IsCoercive.isLeast_rayleighQuotient).

## Sources

- [Tau Ceti documentation: `IsCoercive.isLeast_rayleighQuotient`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Variational/Rayleigh.html#IsCoercive.isLeast_rayleighQuotient)
- [Source of `IsCoercive.isLeast_rayleighQuotient` in TauCeti/Analysis/InnerProductSpace/Variational/Rayleigh.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/InnerProductSpace/Variational/Rayleigh.lean#L131)
