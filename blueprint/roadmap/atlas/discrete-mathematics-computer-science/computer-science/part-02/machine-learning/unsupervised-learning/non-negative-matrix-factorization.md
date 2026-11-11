---
declaration: section
origin: cited
lean: Cslib.MachineLearning.NMF.objective, Cslib.MachineLearning.NMF.objective_nonneg, Cslib.MachineLearning.NMF.objective_transpose, Cslib.MachineLearning.NMF.exists_minimizer, Cslib.MachineLearning.NMF.updateH, Cslib.MachineLearning.NMF.updateW, Cslib.MachineLearning.NMF.sweep, Cslib.MachineLearning.NMF.updateW_eq_transpose
statement: formalized
proof: formalized
---

# Non-negative matrix factorization

34 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/non-negative-matrix-factorization/index.html).

## Objective of nonnegative matrix factorization

The NMF objective: the squared Frobenius distance `‖X - W H‖_F² = ∑ i j, (X i j - (W H) i j)²`
between the data `X` and the product `W * H`.

Formalized by `Cslib.MachineLearning.NMF.objective`, a definition declared in [CSLibExt/MachineLearning/Factorization/NMF.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Factorization/NMF.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/non-negative-matrix-factorization/index.html#objective).

## Nonnegativity of the NMF objective

The objective is nonnegative.

Formalized by `Cslib.MachineLearning.NMF.objective_nonneg`, a theorem declared in [CSLibExt/MachineLearning/Factorization/NMF.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Factorization/NMF.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/non-negative-matrix-factorization/index.html#objective-nonneg).

## The NMF objective is invariant under transposition

Transposing exchanges the roles of `W` and `H`: `‖Xᵀ - Hᵀ Wᵀ‖² = ‖X - W H‖²`.

Formalized by `Cslib.MachineLearning.NMF.objective_transpose`, a theorem declared in [CSLibExt/MachineLearning/Factorization/NMF.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Factorization/NMF.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/non-negative-matrix-factorization/index.html#objective-transpose).

## Existence of a minimizer

For every real matrix `X` and every finite inner index type
`k`, the objective attains its infimum over pairs `W, H ≥ 0` (entrywise).

Formalized by `Cslib.MachineLearning.NMF.exists_minimizer`, a theorem declared in [CSLibExt/MachineLearning/Factorization/NMF.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Factorization/NMF.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/non-negative-matrix-factorization/index.html#exists-minimizer).

## Lee–Seung multiplicative update of H

The Lee–Seung multiplicative update of `H` (Lee and Seung 2001, Theorem 1):
`H a j ← H a j * (Wᵀ X) a j / (Wᵀ W H) a j`. An entry with a zero denominator becomes `0`
(Lean's `x / 0 = 0`).

Formalized by `Cslib.MachineLearning.NMF.updateH`, a definition declared in [CSLibExt/MachineLearning/Factorization/NMF.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Factorization/NMF.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/non-negative-matrix-factorization/index.html#update-h).

## Lee–Seung multiplicative update of W

The Lee–Seung multiplicative update of `W` (Lee and Seung 2001, Theorem 1):
`W i a ← W i a * (X Hᵀ) i a / (W H Hᵀ) i a`. An entry with a zero denominator becomes `0`.

Formalized by `Cslib.MachineLearning.NMF.updateW`, a definition declared in [CSLibExt/MachineLearning/Factorization/NMF.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Factorization/NMF.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/non-negative-matrix-factorization/index.html#update-w).

## One sweep of the Lee–Seung algorithm

One sweep of the Lee–Seung algorithm: update `H`, then update `W` using the new `H`.

Formalized by `Cslib.MachineLearning.NMF.sweep`, a definition declared in [CSLibExt/MachineLearning/Factorization/NMF.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Factorization/NMF.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/non-negative-matrix-factorization/index.html#sweep).

## The W update is the H update of the transposed problem

The `W` update is the `H` update of the transposed problem.

Formalized by `Cslib.MachineLearning.NMF.updateW_eq_transpose`, a theorem declared in [CSLibExt/MachineLearning/Factorization/NMF.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Factorization/NMF.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/non-negative-matrix-factorization/index.html#update-w-eq-transpose).

## The Lee–Seung H update preserves nonnegativity

The `H` update keeps `H` nonnegative when `X`, `W`, `H` are nonnegative.

Formalized by `Cslib.MachineLearning.NMF.updateH_nonneg`, a theorem declared in [CSLibExt/MachineLearning/Factorization/NMF.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Factorization/NMF.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/non-negative-matrix-factorization/index.html#update-h-nonneg).

## The Lee–Seung W update preserves nonnegativity

The `W` update keeps `W` nonnegative when `X`, `W`, `H` are nonnegative.

Formalized by `Cslib.MachineLearning.NMF.updateW_nonneg`, a theorem declared in [CSLibExt/MachineLearning/Factorization/NMF.lean, line 258](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Factorization/NMF.lean#L258). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/non-negative-matrix-factorization/index.html#update-w-nonneg).

## Lee–Seung, `H` step

**Lee–Seung, `H` step** (Lee and Seung 2001, Theorem 1): for `W, H ≥ 0`, the multiplicative
update of `H` does not increase `‖X - W H‖_F²`. The proof is the auxiliary-function argument:
the quadratic term of the exact expansion is bounded by Lee and Seung's diagonal majorant
(here through a weighted Cauchy–Schwarz inequality), and the update minimizes the majorant.
`X` may have any sign.

Formalized by `Cslib.MachineLearning.NMF.objective_updateH_le`, a theorem declared in [CSLibExt/MachineLearning/Factorization/NMF.lean, line 289](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Factorization/NMF.lean#L289). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/non-negative-matrix-factorization/index.html#objective-update-h-le).

## Lee–Seung, `W` step

For `W, H ≥ 0`, the multiplicative update of `W` does not increase
`‖X - W H‖_F²`.

Formalized by `Cslib.MachineLearning.NMF.objective_updateW_le`, a theorem declared in [CSLibExt/MachineLearning/Factorization/NMF.lean, line 388](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Factorization/NMF.lean#L388). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/non-negative-matrix-factorization/index.html#objective-update-w-le).

## A Lee–Seung sweep preserves nonnegativity

One sweep keeps both factors nonnegative when `X ≥ 0`.

Formalized by `Cslib.MachineLearning.NMF.sweep_nonneg`, a theorem declared in [CSLibExt/MachineLearning/Factorization/NMF.lean, line 397](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Factorization/NMF.lean#L397). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/non-negative-matrix-factorization/index.html#sweep-nonneg).

## One Lee–Seung sweep does not increase the objective

**One Lee–Seung sweep does not increase the objective**, for `X, W, H ≥ 0`.

Formalized by `Cslib.MachineLearning.NMF.objective_sweep_le`, a theorem declared in [CSLibExt/MachineLearning/Factorization/NMF.lean, line 405](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Factorization/NMF.lean#L405). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/non-negative-matrix-factorization/index.html#objective-sweep-le).

## The objective is non-increasing along the Lee–Seung iterates

**The objective is non-increasing along the Lee–Seung iterates** started from `W, H ≥ 0`,
for `X ≥ 0`.

Formalized by `Cslib.MachineLearning.NMF.objective_sweep_iterate_antitone`, a theorem declared in [CSLibExt/MachineLearning/Factorization/NMF.lean, line 413](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Factorization/NMF.lean#L413). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/non-negative-matrix-factorization/index.html#objective-sweep-iterate-antitone).

## Gradient of the NMF objective with respect to H

The gradient of the objective with respect to `H`: `2 (Wᵀ W H - Wᵀ X)`.

Formalized by `Cslib.MachineLearning.NMF.gradH`, a definition declared in [CSLibExt/MachineLearning/Factorization/NMF.lean, line 432](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Factorization/NMF.lean#L432). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/non-negative-matrix-factorization/index.html#grad-h).

## Gradient of the NMF objective with respect to W

The gradient of the objective with respect to `W`: `2 (W H Hᵀ - X Hᵀ)`.

Formalized by `Cslib.MachineLearning.NMF.gradW`, a definition declared in [CSLibExt/MachineLearning/Factorization/NMF.lean, line 437](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Factorization/NMF.lean#L437). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/non-negative-matrix-factorization/index.html#grad-w).

## Partial derivative of the NMF objective in an entry of H

`gradH X W H a j` is the partial derivative of the objective in the entry `H a j`.

Formalized by `Cslib.MachineLearning.NMF.hasDerivAt_objective_H`, a theorem declared in [CSLibExt/MachineLearning/Factorization/NMF.lean, line 442](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Factorization/NMF.lean#L442). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/non-negative-matrix-factorization/index.html#has-deriv-at-objective-h).

## Partial derivative of the NMF objective in an entry of W

`gradW X W H i a` is the partial derivative of the objective in the entry `W i a`.

Formalized by `Cslib.MachineLearning.NMF.hasDerivAt_objective_W`, a theorem declared in [CSLibExt/MachineLearning/Factorization/NMF.lean, line 478](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Factorization/NMF.lean#L478). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/non-negative-matrix-factorization/index.html#has-deriv-at-objective-w).

## Complementary slackness at a fixed point of the `H` update

If `updateH X W H = H`,
then `H a j * gradH X W H a j = 0` for every entry.

Formalized by `Cslib.MachineLearning.NMF.mul_gradH_eq_zero_of_updateH_eq`, a theorem declared in [CSLibExt/MachineLearning/Factorization/NMF.lean, line 499](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Factorization/NMF.lean#L499). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/non-negative-matrix-factorization/index.html#mul-grad-h-eq-zero-of-update-h-eq).

## Complementary slackness at a fixed point of the `W` update

**Complementary slackness at a fixed point of the `W` update**.

Formalized by `Cslib.MachineLearning.NMF.mul_gradW_eq_zero_of_updateW_eq`, a theorem declared in [CSLibExt/MachineLearning/Factorization/NMF.lean, line 513](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Factorization/NMF.lean#L513). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/non-negative-matrix-factorization/index.html#mul-grad-w-eq-zero-of-update-w-eq).

## Karush–Kuhn–Tucker point of nonnegative matrix factorization

The Karush–Kuhn–Tucker conditions of `min ‖X - W H‖_F²` subject to `W, H ≥ 0`: primal
feasibility, dual feasibility (nonnegative gradients) and complementary slackness.

Formalized by `Cslib.MachineLearning.NMF.IsKKTPoint`, a structure declared in [CSLibExt/MachineLearning/Factorization/NMF.lean, line 528](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Factorization/NMF.lean#L528). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/non-negative-matrix-factorization/index.html#is-kktpoint).

## Positive fixed points are KKT points

A fixed point of the Lee–Seung sweep with all
entries of `W` and `H` positive has both gradients zero, so it satisfies the KKT conditions.

Formalized by `Cslib.MachineLearning.NMF.isKKTPoint_of_sweep_eq`, a theorem declared in [CSLibExt/MachineLearning/Factorization/NMF.lean, line 545](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Factorization/NMF.lean#L545). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/non-negative-matrix-factorization/index.html#is-kktpoint-of-sweep-eq).

## Separable factor matrix

`H` is separable: every factor `a` has a pure column, a column `j` of `H` equal to a
positive multiple of the unit vector `e_a`. For `X = W * H` this makes column `j` of `X` a
positive multiple of column `a` of `W` (a sample containing only factor `a`). Applied to `Wᵀ`
it says that every factor has a pure row of `W` (an "anchor" feature of factor `a` alone).

Formalized by `Cslib.MachineLearning.NMF.IsSeparable`, a definition declared in [CSLibExt/MachineLearning/Factorization/NMF.lean, line 567](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Factorization/NMF.lean#L567). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/non-negative-matrix-factorization/index.html#is-separable).

## A nonnegative matrix with a nonnegative inverse is monomial

If `G * K = 1` with `G` and
`K` entrywise nonnegative, then there are a permutation `σ` and positive weights `d` with
`G a b = d b` if `a = σ b` and `0` otherwise.

Formalized by `Cslib.MachineLearning.NMF.exists_perm_of_mul_eq_one`, a theorem declared in [CSLibExt/MachineLearning/Factorization/NMF.lean, line 573](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Factorization/NMF.lean#L573). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/non-negative-matrix-factorization/index.html#exists-perm-of-mul-eq-one).

## Essential uniqueness of NMF when both factors are separable

Suppose `X = W * H`, where
`W` has a pure row for every factor (`IsSeparable Wᵀ`: for each `a` a row `i` with
`W i · = e • e_a`, `e > 0`) and `H` has a pure column for every factor (`IsSeparable H`). Then
every factorization `X = W' * H'` with `W', H' ≥ 0` and the same inner dimension agrees with
`(W, H)` up to a permutation `σ` and positive scalings `d` of the factors:
`W' · a = d a • W · (σ a)` and `H' a · = (d a)⁻¹ • H (σ a) ·`. The signs of `W` and `H` are not
used. Proof: the anchor rows and columns of `X` form a positive diagonal block, so the matching
block of `W'` is a nonnegative matrix with a nonnegative inverse, hence monomial
(`exists_perm_of_mul_eq_one`).

Formalized by `Cslib.MachineLearning.NMF.eq_of_isSeparable`, a theorem declared in [CSLibExt/MachineLearning/Factorization/NMF.lean, line 623](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Factorization/NMF.lean#L623). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/non-negative-matrix-factorization/index.html#eq-of-is-separable).

## Nonnegative rank of a matrix

The nonnegative rank of `X`: the least `r` such that `X = W * H` with `W : m × r` and
`H : r × n` entrywise nonnegative (Cohen and Rothblum 1993). If `X` has a negative entry no
such factorization exists and the value is the junk value `sInf ∅ = 0`.

Formalized by `Cslib.MachineLearning.NMF.nonnegRank`, a definition declared in [CSLibExt/MachineLearning/Factorization/NMF.lean, line 698](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Factorization/NMF.lean#L698). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/non-negative-matrix-factorization/index.html#nonneg-rank).

## A nonnegative factorization bounds the nonnegative rank

A nonnegative factorization with inner dimension `r` bounds the nonnegative rank by `r`.

Formalized by `Cslib.MachineLearning.NMF.nonnegRank_le_of_mul_eq`, a theorem declared in [CSLibExt/MachineLearning/Factorization/NMF.lean, line 714](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Factorization/NMF.lean#L714). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/non-negative-matrix-factorization/index.html#nonneg-rank-le-of-mul-eq).

## Existence of a factorization of nonnegative-rank inner dimension

A nonnegative matrix has a nonnegative factorization of inner dimension `nonnegRank X`.

Formalized by `Cslib.MachineLearning.NMF.exists_mul_eq_nonnegRank`, a theorem declared in [CSLibExt/MachineLearning/Factorization/NMF.lean, line 720](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Factorization/NMF.lean#L720). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/non-negative-matrix-factorization/index.html#exists-mul-eq-nonneg-rank).

## Nonnegative rank is at most the number of columns

The nonnegative rank of a nonnegative matrix is at most its number of columns.

Formalized by `Cslib.MachineLearning.NMF.nonnegRank_le_card_width`, a theorem declared in [CSLibExt/MachineLearning/Factorization/NMF.lean, line 730](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Factorization/NMF.lean#L730). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/non-negative-matrix-factorization/index.html#nonneg-rank-le-card-width).

## The nonnegative rank of a nonnegative matrix is at least its rank

**The nonnegative rank of a nonnegative matrix is at least its rank.**

Formalized by `Cslib.MachineLearning.NMF.rank_le_nonnegRank`, a theorem declared in [CSLibExt/MachineLearning/Factorization/NMF.lean, line 736](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Factorization/NMF.lean#L736). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/non-negative-matrix-factorization/index.html#rank-le-nonneg-rank).

## Column sums of a matrix product

Column sums of a product: `∑ i, (W H) i j = ∑ a, (∑ i, W i a) H a j`.

Formalized by `Cslib.MachineLearning.NMF.sum_mul_apply`, a theorem declared in [CSLibExt/MachineLearning/Factorization/NMF.lean, line 745](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Factorization/NMF.lean#L745). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/non-negative-matrix-factorization/index.html#sum-mul-apply).

## Mutational signatures

**Mutational signatures** (Alexandrov et al. 2013). Write the mutation-count matrix
(mutation types × samples) as `W * H`, signatures (columns of `W`) times exposures `H`. If every
signature is a probability vector over mutation types, the total mutation count of sample `j`
equals the sum of its exposures.

Formalized by `Cslib.MachineLearning.NMF.sum_mul_apply_of_sum_eq_one`, a theorem declared in [CSLibExt/MachineLearning/Factorization/NMF.lean, line 755](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Factorization/NMF.lean#L755). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/non-negative-matrix-factorization/index.html#sum-mul-apply-of-sum-eq-one).

## Gene-expression deconvolution

Write the bulk matrix (genes × samples) as `C * P`, the
cell-type profiles `C` times the cell-type proportions `P`. If the proportions of sample `j` are
nonnegative and sum to `1` and every cell type expresses gene `g` at a level in `[lo, hi]`, then
the bulk level of `g` in sample `j` lies in `[lo, hi]`.

Formalized by `Cslib.MachineLearning.NMF.mul_apply_mem_Icc`, a theorem declared in [CSLibExt/MachineLearning/Factorization/NMF.lean, line 764](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Factorization/NMF.lean#L764). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/non-negative-matrix-factorization/index.html#mul-apply-mem-icc).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Non-negative matrix factorization](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/non-negative-matrix-factorization/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/machine-learning/unsupervised-learning/non-negative-matrix-factorization)
