---
declaration: section
origin: cited
lean: MathlibExt.Analysis.InnerProductSpace.NormDerivative.reInnerSL, MathlibExt.Analysis.InnerProductSpace.NormDerivative.hasStrictFDerivAt_norm_sq, MathlibExt.Analysis.InnerProductSpace.NormDerivative.hasStrictFDerivAt_norm, MathlibExt.Analysis.InnerProductSpace.NormDerivative.hasFDerivAt_norm, MathlibExt.Analysis.InnerProductSpace.NormDerivative.fderiv_norm, MathlibExt.Analysis.InnerProductSpace.NormDerivative.fderiv_norm_apply, MathlibExt.Analysis.InnerProductSpace.NormDerivative.norm_reInnerSL, MathlibExt.Analysis.InnerProductSpace.NormDerivative.norm_fderiv_norm
statement: formalized
proof: formalized
---

# Derivatives of the norm

21 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/derivatives-of-the-norm/index.html).

## Real part of the inner product as a real-linear functional

The real-linear functional `y ↦ re ⟪x, y⟫`, the unnormalized gradient of
the norm at `x`. The scalar field `K` is an explicit argument because the
type `E →L[ℝ] ℝ` does not determine it.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NormDerivative.reInnerSL`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/NormDerivative.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NormDerivative.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/derivatives-of-the-norm/index.html#re-inner-sl).

## Strict derivative of the squared norm

The derivative of the squared norm is twice the real inner product with `x`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NormDerivative.hasStrictFDerivAt_norm_sq`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NormDerivative.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NormDerivative.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/derivatives-of-the-norm/index.html#has-strict-fderiv-at-norm-sq).

## Strict Fréchet derivative of the norm at a nonzero point

The Fréchet derivative of the norm at a nonzero point `x` is the norming
functional `y ↦ re ⟪x, y⟫ / ‖x‖`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NormDerivative.hasStrictFDerivAt_norm`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NormDerivative.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NormDerivative.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/derivatives-of-the-norm/index.html#has-strict-fderiv-at-norm).

## Fréchet derivative of the norm at a nonzero point

The non-strict form of `hasStrictFDerivAt_norm`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NormDerivative.hasFDerivAt_norm`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NormDerivative.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NormDerivative.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/derivatives-of-the-norm/index.html#has-fderiv-at-norm).

## Formula for the derivative of the norm

The `fderiv` of the norm at a nonzero point.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NormDerivative.fderiv_norm`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NormDerivative.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NormDerivative.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/derivatives-of-the-norm/index.html#fderiv-norm).

## Derivative of the norm applied to a vector

The `fderiv` of the norm at a nonzero point, applied to a vector.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NormDerivative.fderiv_norm_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NormDerivative.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NormDerivative.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/derivatives-of-the-norm/index.html#fderiv-norm-apply).

## Operator norm of the real inner product functional

The norming functional `reInnerSL K x` has operator norm `‖x‖` (it attains
`‖x‖` at `‖x‖⁻¹ • x`).

Formalized by `MathlibExt.Analysis.InnerProductSpace.NormDerivative.norm_reInnerSL`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NormDerivative.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NormDerivative.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/derivatives-of-the-norm/index.html#norm-re-inner-sl).

## Derivative of the norm has operator norm one

The Fréchet derivative of the norm at a nonzero point has operator norm `1`:
the norming functional is a norming functional. This statement needs the inner
product structure, so `K` is an explicit argument.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NormDerivative.norm_fderiv_norm`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NormDerivative.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NormDerivative.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/derivatives-of-the-norm/index.html#norm-fderiv-norm).

## Over the reals the norming functional is the inner product

Over `ℝ`, the norming functional is just `innerSL ℝ x`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NormDerivative.reInnerSL_real`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NormDerivative.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NormDerivative.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/derivatives-of-the-norm/index.html#re-inner-sl-real).

## Strict derivative of the norm in a real inner product space

The Fréchet derivative of the norm in a real inner product space.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NormDerivative.hasStrictFDerivAt_norm_real`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NormDerivative.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NormDerivative.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/derivatives-of-the-norm/index.html#has-strict-fderiv-at-norm-real).

## Derivative of the norm in a real space applied to a vector

The `fderiv` of the norm in a real inner product space, applied to a vector.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NormDerivative.fderiv_norm_apply_real`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NormDerivative.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NormDerivative.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/derivatives-of-the-norm/index.html#fderiv-norm-apply-real).

## Chain rule for the strict derivative of a norm

Chain rule: the derivative of the norm of a differentiable map.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NormDerivative.HasStrictFDerivAt.norm`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NormDerivative.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NormDerivative.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/derivatives-of-the-norm/index.html#norm).

## Chain rule for the Fréchet derivative of a norm

Chain rule: the non-strict derivative of the norm of a differentiable map.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NormDerivative.HasFDerivAt.norm`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NormDerivative.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NormDerivative.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/derivatives-of-the-norm/index.html#norm-2).

## Derivative of the norm along a curve

The derivative of the norm along a curve is the normalized real inner product
of the position with the velocity.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NormDerivative.HasDerivAt.norm`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NormDerivative.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NormDerivative.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/derivatives-of-the-norm/index.html#norm-3).

## Curves on the unit sphere have velocity orthogonal to position

A differentiable curve lying on the unit sphere has velocity orthogonal to
its position (in the real-inner-product sense).

Formalized by `MathlibExt.Analysis.InnerProductSpace.NormDerivative.re_inner_self_deriv_eq_zero_of_forall_norm_eq_one`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NormDerivative.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NormDerivative.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/derivatives-of-the-norm/index.html#re-inner-self-deriv-eq-zero-of-forall-no).

## Strict derivative of the squared distance to a point

The gradient of the squared distance to a point `a` is `2 • reInnerSL K (x - a)`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NormDerivative.hasStrictFDerivAt_dist_sq`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NormDerivative.lean, line 219](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NormDerivative.lean#L219). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/derivatives-of-the-norm/index.html#has-strict-fderiv-at-dist-sq).

## Derivative of the squared distance to a point applied to a vector

The `fderiv` of the squared distance to a point, applied to a vector.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NormDerivative.fderiv_dist_sq_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NormDerivative.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NormDerivative.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/derivatives-of-the-norm/index.html#fderiv-dist-sq-apply).

## Distance to a subspace as the norm of the projection residual

The distance from `y` to a subspace with an orthogonal projection is the
norm of the residual `y - S.starProjection y`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NormDerivative.infDist_eq_norm_sub_starProjection`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NormDerivative.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NormDerivative.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/derivatives-of-the-norm/index.html#inf-dist-eq-norm-sub-star-projection).

## Strict derivative of the squared projection residual

The gradient of the squared residual `‖y - S.starProjection y‖ ^ 2` is
`2 • reInnerSL K (x - S.starProjection x)`, using that the residual operator
`1 - S.starProjection` is self-adjoint and idempotent.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NormDerivative.hasStrictFDerivAt_residual_sq`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NormDerivative.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NormDerivative.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/derivatives-of-the-norm/index.html#has-strict-fderiv-at-residual-sq).

## Strict derivative of the squared distance to a subspace

The gradient of the squared distance to a subspace `S` is twice the real
inner product with the residual `x - S.starProjection x`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NormDerivative.hasStrictFDerivAt_infDist_sq`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NormDerivative.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NormDerivative.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/derivatives-of-the-norm/index.html#has-strict-fderiv-at-inf-dist-sq).

## Second derivative of the squared norm

Let $E$ be a real inner product space.
For all $p, u, v \in E$, the second Fréchet derivative of $x \mapsto \|x\|^2$ at $p$,
applied to $u$ and then to $v$, equals $2 \langle u, v \rangle$.

Formalized by `fderiv_fderiv_norm_sq_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NormSqHessian.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NormSqHessian.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/derivatives-of-the-norm/index.html#fderiv-fderiv-norm-sq-apply).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Derivatives of the norm](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/derivatives-of-the-norm/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/hilbert-spaces/derivatives-of-the-norm)
