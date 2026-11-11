---
declaration: theorem
origin: cited
lean: TauCeti.two_mul_re_inner_le_add_mul_norm_sq
statement: formalized
proof: formalized
---

# Young's inequality for inner products

for every weight `ε > 0`,
`2 re ⟪x, y⟫ ≤ ε ‖x‖² + ε⁻¹ ‖y‖²`.

```lean
TauCeti.two_mul_re_inner_le_add_mul_norm_sq.{u_1, u_2} {𝕜 : Type u_1} {F : Type u_2} [RCLike 𝕜]
  [SeminormedAddCommGroup F] [InnerProductSpace 𝕜 F] (x y : F) {ε : ℝ} (hε : 0 < ε) :
  2 * RCLike.re (inner 𝕜 x y) ≤ ε * ‖x‖ ^ 2 + ε⁻¹ * ‖y‖ ^ 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.two_mul_re_inner_le_add_mul_norm_sq`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Young.html#TauCeti.two_mul_re_inner_le_add_mul_norm_sq).

## Sources

- [Tau Ceti documentation: `TauCeti.two_mul_re_inner_le_add_mul_norm_sq`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Young.html#TauCeti.two_mul_re_inner_le_add_mul_norm_sq)
- [Source of `TauCeti.two_mul_re_inner_le_add_mul_norm_sq` in TauCeti/Analysis/InnerProductSpace/Young.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/InnerProductSpace/Young.lean#L36)
