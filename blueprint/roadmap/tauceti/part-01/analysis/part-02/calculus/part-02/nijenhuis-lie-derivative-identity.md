---
declaration: theorem
origin: cited
lean: TauCeti.lieDerivEndomorphism_apply_sub_apply
statement: formalized
proof: formalized
---

# Nijenhuis–Lie-derivative identity

if `A x` squares to `-1`, then for every differentiable
vector field `X`, the derivative `DX(x)` cancels out of `(L_{A X} A)(x) w - A x ((L_X A)(x) w)`,
leaving the pointwise Nijenhuis expression of `A` on `(X x, w)`.

```lean
TauCeti.lieDerivEndomorphism_apply_sub_apply.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2}
  [NontriviallyNormedField 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E] {A : E → E →L[𝕜] E} {x : E}
  {X : E → E} (hA : DifferentiableAt 𝕜 A x) (hX : DifferentiableAt 𝕜 X x)
  (hsq : ∀ (u : E), (A x) ((A x) u) = -u) (w : E) :
  (TauCeti.lieDerivEndomorphism (fun y => (A y) (X y)) A x) w -
      (A x) ((TauCeti.lieDerivEndomorphism X A x) w) =
    ((fderiv 𝕜 A x) ((A x) (X x))) w - ((fderiv 𝕜 A x) ((A x) w)) (X x) +
        (A x) (((fderiv 𝕜 A x) w) (X x)) -
      (A x) (((fderiv 𝕜 A x) (X x)) w)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.lieDerivEndomorphism_apply_sub_apply`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/EndomorphismLieDeriv.html#TauCeti.lieDerivEndomorphism_apply_sub_apply).

## Sources

- [Tau Ceti documentation: `TauCeti.lieDerivEndomorphism_apply_sub_apply`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/EndomorphismLieDeriv.html#TauCeti.lieDerivEndomorphism_apply_sub_apply)
- [Source of `TauCeti.lieDerivEndomorphism_apply_sub_apply` in TauCeti/Analysis/Calculus/EndomorphismLieDeriv.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Calculus/EndomorphismLieDeriv.lean#L385)
