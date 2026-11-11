---
declaration: section
origin: cited
lean: Matrix.frischWaughLovell, Matrix.frischWaughLovell_residual, Matrix.frischWaughLovell_eq_div
statement: formalized
proof: formalized
---

# Frisch–Waugh–Lovell theorem

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/frisch-waugh-lovell-theorem/index.html).

## Frisch–Waugh–Lovell

**Frisch–Waugh–Lovell** for weighted least squares with a symmetric weight matrix `W`: if
`(b, t)` solves the normal equations of the regression of `y` on `[A | z]` and `z⊥ = z - A u`
is the weighted residual of `z` on `A` (`Aᵀ W z⊥ = 0`), then `t ⟪z⊥, z⊥⟫_W = ⟪z⊥, y⟫_W`, where
`⟪x, y⟫_W = x ⬝ᵥ W y`.

Formalized by `Matrix.frischWaughLovell`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/FrischWaughLovell.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/FrischWaughLovell.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/frisch-waugh-lovell-theorem/index.html#frisch-waugh-lovell).

## Frisch–Waugh–Lovell, residualized form

Under the hypotheses of `frischWaughLovell`, if
also `y⊥ = y - A v` is the weighted residual of `y` on `A` (`Aᵀ W y⊥ = 0`), then
`t ⟪z⊥, z⊥⟫_W = ⟪z⊥, y⊥⟫_W`: the coefficient of `z` in the full regression is the coefficient of
the regression of the residualized response on the residualized regressor.

Formalized by `Matrix.frischWaughLovell_residual`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/FrischWaughLovell.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/FrischWaughLovell.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/frisch-waugh-lovell-theorem/index.html#frisch-waugh-lovell-residual).

## Frisch–Waugh–Lovell, solved form

Under the hypotheses of `frischWaughLovell_residual`, if
`⟪z⊥, z⊥⟫_W ≠ 0` then `t = ⟪z⊥, y⊥⟫_W / ⟪z⊥, z⊥⟫_W`.

Formalized by `Matrix.frischWaughLovell_eq_div`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/FrischWaughLovell.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/FrischWaughLovell.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/frisch-waugh-lovell-theorem/index.html#frisch-waugh-lovell-eq-div).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Frisch–Waugh–Lovell theorem](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/frisch-waugh-lovell-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/linear-models-multivariate/frisch-waugh-lovell-theorem)
