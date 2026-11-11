---
declaration: theorem
origin: cited
lean: TauCeti.IsLocallyBoundedOn.equicontinuousOn
statement: formalized
proof: formalized
---

# The equicontinuity half of Montel's theorem

A locally bounded family of holomorphic
functions on an open set `U ⊆ ℂ` is equicontinuous on `U`.

Around a point `z₀ ∈ U` pick `r > 0` with `closedBall z₀ (2 * r) ⊆ U`; local boundedness supplies
one constant `C` bounding the whole family on that compact ball, and
`dist_le_of_forall_mem_closedBall_two_mul_norm_le` then makes every member of the family
`C / r`-Lipschitz on `ball z₀ r`.  A single Lipschitz constant is a common continuity modulus.

```lean
TauCeti.IsLocallyBoundedOn.equicontinuousOn.{u_1, u_2} {ι : Type u_1} {E : Type u_2} {U : Set ℂ}
  [NormedAddCommGroup E] [NormedSpace ℂ E] {F : ι → ℂ → E} (hb : TauCeti.IsLocallyBoundedOn F U)
  (hU : IsOpen U) (hF : ∀ (i : ι), DifferentiableOn ℂ (F i) U) : EquicontinuousOn F U
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cauchy estimate](cauchy-estimate.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsLocallyBoundedOn.equicontinuousOn`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/NormalFamilies.html#TauCeti.IsLocallyBoundedOn.equicontinuousOn).

## Sources

- [Tau Ceti documentation: `TauCeti.IsLocallyBoundedOn.equicontinuousOn`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/NormalFamilies.html#TauCeti.IsLocallyBoundedOn.equicontinuousOn)
- [Source of `TauCeti.IsLocallyBoundedOn.equicontinuousOn` in TauCeti/Analysis/Complex/Conformal/NormalFamilies.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/Conformal/NormalFamilies.lean#L147)
