---
declaration: theorem
origin: cited
lean: TauCeti.two_mul_real_inner_le_add_mul_norm_sq
statement: formalized
proof: formalized
---

# Young's inequality for real inner products

for every weight `ε > 0`,
`2 ⟪x, y⟫ ≤ ε ‖x‖² + ε⁻¹ ‖y‖²`.

```lean
TauCeti.two_mul_real_inner_le_add_mul_norm_sq.{u_1} {F : Type u_1} [SeminormedAddCommGroup F]
  [InnerProductSpace ℝ F] (x y : F) {ε : ℝ} (hε : 0 < ε) :
  2 * inner ℝ x y ≤ ε * ‖x‖ ^ 2 + ε⁻¹ * ‖y‖ ^ 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.two_mul_real_inner_le_add_mul_norm_sq`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Young.html#TauCeti.two_mul_real_inner_le_add_mul_norm_sq).

## Sources

- [Tau Ceti documentation: `TauCeti.two_mul_real_inner_le_add_mul_norm_sq`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Young.html#TauCeti.two_mul_real_inner_le_add_mul_norm_sq)
- [Source of `TauCeti.two_mul_real_inner_le_add_mul_norm_sq` in TauCeti/Analysis/InnerProductSpace/Young.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/InnerProductSpace/Young.lean#L35)
