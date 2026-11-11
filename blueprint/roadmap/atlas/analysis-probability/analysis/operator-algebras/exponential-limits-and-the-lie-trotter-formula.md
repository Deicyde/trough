---
declaration: section
origin: cited
lean: NormedSpace.norm_pow_sub_pow_le, NormedSpace.tendsto_one_add_inv_smul_pow, MathlibExt.Analysis.Normed.Algebra.TrotterProductFormula.norm_exp_le_exp_norm, MathlibExt.Analysis.Normed.Algebra.TrotterProductFormula.norm_exp_sub_one_sub_id_le, MathlibExt.Analysis.Normed.Algebra.TrotterProductFormula.norm_exp_mul_exp_sub_exp_add_le, MathlibExt.Analysis.Normed.Algebra.TrotterProductFormula.norm_pow_sub_pow_le, MathlibExt.Analysis.Normed.Algebra.TrotterProductFormula.tendsto_trotter_product, MathlibExt.Analysis.Normed.Algebra.TrotterProductFormula.trotter_product_of_commute
statement: formalized
proof: formalized
---

# Exponential limits and the Lie–Trotter formula

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/exponential-limits-and-the-lie-trotter-formula/index.html).

## Telescoping estimate for differences of powers in a normed ring

Telescoping estimate for powers in a normed ring with `‖1‖ = 1`:
`‖a ^ m - b ^ m‖ ≤ m ‖a - b‖ max(‖a‖, ‖b‖) ^ (m - 1)`.

Formalized by `NormedSpace.norm_pow_sub_pow_le`, a theorem declared in [MathlibExt/Analysis/Normed/Algebra/ExponentialLimit.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Normed/Algebra/ExponentialLimit.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/exponential-limits-and-the-lie-trotter-formula/index.html#norm-pow-sub-pow-le).

## Compound-interest limit in a Banach algebra

If `Y M → X` and `m M / M → t`, then
`(1 + M⁻¹ • Y M) ^ m M → exp (t • X)` as `M → ∞`.

Formalized by `NormedSpace.tendsto_one_add_inv_smul_pow`, a theorem declared in [MathlibExt/Analysis/Normed/Algebra/ExponentialLimit.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Normed/Algebra/ExponentialLimit.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/exponential-limits-and-the-lie-trotter-formula/index.html#tendsto-one-add-inv-smul-pow).

## Norm of the exponential is bounded by the exponential of the norm

The exponential is bounded by the real exponential of the norm.

Formalized by `MathlibExt.Analysis.Normed.Algebra.TrotterProductFormula.norm_exp_le_exp_norm`, a theorem declared in [MathlibExt/Analysis/Normed/Algebra/TrotterProductFormula.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Normed/Algebra/TrotterProductFormula.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/exponential-limits-and-the-lie-trotter-formula/index.html#norm-exp-le-exp-norm).

## First-order Taylor remainder bound for the exponential

The Taylor remainder of `exp` at order one.

Formalized by `MathlibExt.Analysis.Normed.Algebra.TrotterProductFormula.norm_exp_sub_one_sub_id_le`, a theorem declared in [MathlibExt/Analysis/Normed/Algebra/TrotterProductFormula.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Normed/Algebra/TrotterProductFormula.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/exponential-limits-and-the-lie-trotter-formula/index.html#norm-exp-sub-one-sub-id-le).

## One-step Trotter estimate

The one-step Trotter estimate: `exp x * exp y` differs from
`exp (x + y)` by at most a quadratic expression in `‖x‖` and `‖y‖`.

Formalized by `MathlibExt.Analysis.Normed.Algebra.TrotterProductFormula.norm_exp_mul_exp_sub_exp_add_le`, a theorem declared in [MathlibExt/Analysis/Normed/Algebra/TrotterProductFormula.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Normed/Algebra/TrotterProductFormula.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/exponential-limits-and-the-lie-trotter-formula/index.html#norm-exp-mul-exp-sub-exp-add-le).

## Linear bound on differences of powers for the Trotter formula

Powers differ at most linearly in the difference of the bases. The
`1` in the maximum is needed: without it the bound fails when the norms are
`< 1`.

Formalized by `MathlibExt.Analysis.Normed.Algebra.TrotterProductFormula.norm_pow_sub_pow_le`, a theorem declared in [MathlibExt/Analysis/Normed/Algebra/TrotterProductFormula.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Normed/Algebra/TrotterProductFormula.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/exponential-limits-and-the-lie-trotter-formula/index.html#norm-pow-sub-pow-le-2).

## Trotter product formula

The **Trotter product formula** for bounded elements of a complete normed
algebra: `(exp (a / n) * exp (b / n)) ^ n → exp (a + b)` in norm.

Formalized by `MathlibExt.Analysis.Normed.Algebra.TrotterProductFormula.tendsto_trotter_product`, a theorem declared in [MathlibExt/Analysis/Normed/Algebra/TrotterProductFormula.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Normed/Algebra/TrotterProductFormula.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/exponential-limits-and-the-lie-trotter-formula/index.html#tendsto-trotter-product).

## Trotter product formula for commuting elements

If `a` and `b` commute, the Trotter approximants are exactly
`exp (a + b)` for every positive `n`.

Formalized by `MathlibExt.Analysis.Normed.Algebra.TrotterProductFormula.trotter_product_of_commute`, a theorem declared in [MathlibExt/Analysis/Normed/Algebra/TrotterProductFormula.lean, line 444](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Normed/Algebra/TrotterProductFormula.lean#L444). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/exponential-limits-and-the-lie-trotter-formula/index.html#trotter-product-of-commute).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Exponential limits and the Lie–Trotter formula](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/exponential-limits-and-the-lie-trotter-formula/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/operator-algebras/exponential-limits-and-the-lie-trotter-formula)
