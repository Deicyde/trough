---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: lineDeriv
mathlib_file: Mathlib/Analysis/Calculus/LineDeriv/Basic.lean
---

# Directional derivative

Line derivative of `f` at the point `x` in the direction `v`, if it exists.  Zero otherwise.

If the line derivative exists (i.e., `∃ f', HasLineDerivAt 𝕜 f f' x v`), then
`f (x + t v) = f x + t lineDeriv 𝕜 f x v + o (t)` when `t` tends to `0`.

```lean
lineDeriv.{u_1, u_2, u_3} (𝕜 : Type u_1) [NontriviallyNormedField 𝕜] {F : Type u_2}
  [NormedAddCommGroup F] [NormedSpace 𝕜 F] {E : Type u_3} [AddCommGroup E] [_root_.Module 𝕜 E]
  (f : E → F) (x v : E) : F
```

## Depends on

- [Differentials (linear tangent functions)](differentials-linear-tangent-functions.md)
- [Normed vector space over a normed field](../../../overview/analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)

## Sources

- [Mathlib documentation: `lineDeriv`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/LineDeriv/Basic.html#lineDeriv)
- [Source of `lineDeriv` in Mathlib/Analysis/Calculus/LineDeriv/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/LineDeriv/Basic.lean#L104)
- [Mathlib undergraduate list: Multivariable calculus › Differential calculus](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L457)
