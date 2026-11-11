---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FunctionalAnalysis.TikhonovRegularization.tikhonovFunctional, MathlibExt.Analysis.FunctionalAnalysis.TikhonovRegularization.tikhonovOperator, MathlibExt.Analysis.FunctionalAnalysis.TikhonovRegularization.tikhonovOperator_inner_self, MathlibExt.Analysis.FunctionalAnalysis.TikhonovRegularization.re_inner_tikhonovOperator_self, MathlibExt.Analysis.FunctionalAnalysis.TikhonovRegularization.isSelfAdjoint_tikhonovOperator, MathlibExt.Analysis.FunctionalAnalysis.TikhonovRegularization.tikhonovOperator_le_norm, MathlibExt.Analysis.FunctionalAnalysis.TikhonovRegularization.ker_tikhonovOperator_eq_bot, MathlibExt.Analysis.FunctionalAnalysis.TikhonovRegularization.isClosed_range_tikhonovOperator
statement: formalized
proof: formalized
---

# Tikhonov regularization

18 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/tikhonov-regularization/index.html).

## Tikhonov functional

The Tikhonov (ridge) functional `J(x) = ‖A x - b‖ ^ 2 + Λ * ‖x‖ ^ 2`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.TikhonovRegularization.tikhonovFunctional`, a definition declared in [MathlibExt/Analysis/FunctionalAnalysis/TikhonovRegularization.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/TikhonovRegularization.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/tikhonov-regularization/index.html#tikhonov-functional).

## Normal operator of the Tikhonov problem

The normal operator `A† ∘L A + Λ • 1` of the Tikhonov problem.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.TikhonovRegularization.tikhonovOperator`, a definition declared in [MathlibExt/Analysis/FunctionalAnalysis/TikhonovRegularization.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/TikhonovRegularization.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/tikhonov-regularization/index.html#tikhonov-operator).

## Inner product of the Tikhonov normal operator with its argument

The inner product of the normal operator applied to `x` with `x` itself.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.TikhonovRegularization.tikhonovOperator_inner_self`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/TikhonovRegularization.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/TikhonovRegularization.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/tikhonov-regularization/index.html#tikhonov-operator-inner-self).

## Real part of the Tikhonov normal operator's quadratic form

The real part of the inner product of the normal operator applied to `x`
with `x` itself.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.TikhonovRegularization.re_inner_tikhonovOperator_self`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/TikhonovRegularization.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/TikhonovRegularization.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/tikhonov-regularization/index.html#re-inner-tikhonov-operator-self).

## Tikhonov normal operator is self-adjoint

The normal operator is self-adjoint, for every real `Λ`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.TikhonovRegularization.isSelfAdjoint_tikhonovOperator`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/TikhonovRegularization.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/TikhonovRegularization.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/tikhonov-regularization/index.html#is-self-adjoint-tikhonov-operator).

## Tikhonov normal operator is bounded below by the regularization parameter

The normal operator is bounded below by `Λ`, for every real `Λ`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.TikhonovRegularization.tikhonovOperator_le_norm`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/TikhonovRegularization.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/TikhonovRegularization.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/tikhonov-regularization/index.html#tikhonov-operator-le-norm).

## Tikhonov normal operator has trivial kernel

The normal operator has trivial kernel when `Λ > 0`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.TikhonovRegularization.ker_tikhonovOperator_eq_bot`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/TikhonovRegularization.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/TikhonovRegularization.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/tikhonov-regularization/index.html#ker-tikhonov-operator-eq-bot).

## Tikhonov normal operator has closed range

The normal operator has closed range when `Λ > 0`, since it is bounded below.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.TikhonovRegularization.isClosed_range_tikhonovOperator`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/TikhonovRegularization.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/TikhonovRegularization.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/tikhonov-regularization/index.html#is-closed-range-tikhonov-operator).

## Tikhonov normal operator is surjective

The normal operator is surjective when `Λ > 0`: its range is closed and
its orthogonal complement is its kernel, which is trivial since the operator
is self-adjoint.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.TikhonovRegularization.range_tikhonovOperator_eq_top`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/TikhonovRegularization.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/TikhonovRegularization.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/tikhonov-regularization/index.html#range-tikhonov-operator-eq-top).

## Tikhonov normal operator is bijective

The normal operator is bijective when `Λ > 0`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.TikhonovRegularization.bijective_tikhonovOperator`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/TikhonovRegularization.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/TikhonovRegularization.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/tikhonov-regularization/index.html#bijective-tikhonov-operator).

## Tikhonov normal operator is invertible

The normal operator is a unit when `Λ > 0`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.TikhonovRegularization.isUnit_tikhonovOperator`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/TikhonovRegularization.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/TikhonovRegularization.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/tikhonov-regularization/index.html#is-unit-tikhonov-operator).

## Solvability of the Tikhonov normal equations

The normal equations are solvable when `Λ > 0`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.TikhonovRegularization.exists_tikhonov_normal_equations`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/TikhonovRegularization.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/TikhonovRegularization.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/tikhonov-regularization/index.html#exists-tikhonov-normal-equations).

## Quadratic identity for the Tikhonov functional at a normal-equation solution

The quadratic identity for the Tikhonov functional around a solution of
the normal equations: the cross term vanishes by the normal equations.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.TikhonovRegularization.tikhonovFunctional_add_of_normal_equations`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/TikhonovRegularization.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/TikhonovRegularization.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/tikhonov-regularization/index.html#tikhonov-functional-add-of-normal-equati).

## Solutions of the normal equations minimize the Tikhonov functional

A solution of the normal equations minimizes the Tikhonov functional.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.TikhonovRegularization.isMinOn_tikhonovFunctional_of_normal_equations`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/TikhonovRegularization.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/TikhonovRegularization.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/tikhonov-regularization/index.html#is-min-on-tikhonov-functional-of-normal).

## Tikhonov minimizers solve the normal equations

A minimizer of the Tikhonov functional equals a solution of the normal
equations, when `Λ > 0`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.TikhonovRegularization.eq_of_isMinOn_tikhonovFunctional`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/TikhonovRegularization.lean, line 265](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/TikhonovRegularization.lean#L265). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/tikhonov-regularization/index.html#eq-of-is-min-on-tikhonov-functional).

## Existence and uniqueness of the Tikhonov minimizer

The Tikhonov functional has a unique minimizer when `Λ > 0`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.TikhonovRegularization.existsUnique_tikhonov_minimizer`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/TikhonovRegularization.lean, line 281](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/TikhonovRegularization.lean#L281). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/tikhonov-regularization/index.html#exists-unique-tikhonov-minimizer).

## Stability bound for Tikhonov regularized solutions

Stability bound for a solution of the normal equations.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.TikhonovRegularization.norm_le_of_tikhonov_normal_equations`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/TikhonovRegularization.lean, line 291](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/TikhonovRegularization.lean#L291). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/tikhonov-regularization/index.html#norm-le-of-tikhonov-normal-equations).

## Tikhonov solutions tend to zero as the parameter grows

Solutions of the Tikhonov normal equations tend to `0` as `Λ → ∞`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.TikhonovRegularization.tendsto_tikhonov_solution_zero`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/TikhonovRegularization.lean, line 322](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/TikhonovRegularization.lean#L322). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/tikhonov-regularization/index.html#tendsto-tikhonov-solution-zero).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Tikhonov regularization](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/tikhonov-regularization/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/convex-analysis-and-variations/tikhonov-regularization)
