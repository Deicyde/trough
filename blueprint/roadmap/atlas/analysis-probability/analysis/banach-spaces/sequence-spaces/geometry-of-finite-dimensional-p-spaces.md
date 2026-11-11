---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FunctionalAnalysis.LpGeometry.lpTwoPlus, MathlibExt.Analysis.FunctionalAnalysis.LpGeometry.lpTwoMinus, MathlibExt.Analysis.FunctionalAnalysis.LpGeometry.lpTwoPlus_add_lpTwoMinus, MathlibExt.Analysis.FunctionalAnalysis.LpGeometry.lpTwoPlus_sub_lpTwoMinus, MathlibExt.Analysis.FunctionalAnalysis.LpGeometry.norm_add_lpTwo, MathlibExt.Analysis.FunctionalAnalysis.LpGeometry.norm_sub_lpTwo, MathlibExt.Analysis.FunctionalAnalysis.LpGeometry.norm_lpTwoPlus_of_ne_top, MathlibExt.Analysis.FunctionalAnalysis.LpGeometry.norm_lpTwoMinus_of_ne_top
statement: formalized
proof: formalized
---

# Geometry of finite-dimensional ℓ^p spaces

20 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/geometry-of-finite-dimensional-p-spaces/index.html).

## The vector $(1, 1)$ in $\ell^p_2$

For $p \in [0, \infty]$, write $\ell^p_2$ for the
space $\mathbb{R}^2$ regarded as the $\ell^p$ product of two copies of $\mathbb{R}$ (normed by the
$\ell^p$ norm when $p \ge 1$). The vector $u_p \in \ell^p_2$ is $(1, 1)$, that is, $e_0 + e_1$,
where $e_0 = (1, 0)$ and $e_1 = (0, 1)$ are the standard basis vectors.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.LpGeometry.lpTwoPlus`, a definition declared in [MathlibExt/Analysis/FunctionalAnalysis/LpGeometry.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/LpGeometry.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/geometry-of-finite-dimensional-p-spaces/index.html#lp-two-plus).

## The vector $(1, -1)$ in $\ell^p_2$

For $p \in [0, \infty]$, write $\ell^p_2$ for the
space $\mathbb{R}^2$ regarded as the $\ell^p$ product of two copies of $\mathbb{R}$ (normed by the
$\ell^p$ norm when $p \ge 1$). The vector $v_p \in \ell^p_2$ is $(1, -1)$, that is, $e_0 - e_1$,
where $e_0 = (1, 0)$ and $e_1 = (0, 1)$ are the standard basis vectors.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.LpGeometry.lpTwoMinus`, a definition declared in [MathlibExt/Analysis/FunctionalAnalysis/LpGeometry.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/LpGeometry.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/geometry-of-finite-dimensional-p-spaces/index.html#lp-two-minus).

## Sum of $(1, 1)$ and $(1, -1)$ in $\ell^p_2$

For every $p \in [0, \infty]$, write $\ell^p_2$
for the space $\mathbb{R}^2$ regarded as the $\ell^p$ product of two copies of $\mathbb{R}$. The
vectors $u_p = (1, 1)$ and $v_p = (1, -1)$ of $\ell^p_2$ satisfy $u_p + v_p = 2 e_0$, where
$e_0 = (1, 0)$ is the first standard basis vector.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.LpGeometry.lpTwoPlus_add_lpTwoMinus`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/LpGeometry.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/LpGeometry.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/geometry-of-finite-dimensional-p-spaces/index.html#lp-two-plus-add-lp-two-minus).

## Difference of $(1, 1)$ and $(1, -1)$ in $\ell^p_2$

For every $p \in [0, \infty]$, write
$\ell^p_2$ for the space $\mathbb{R}^2$ regarded as the $\ell^p$ product of two copies of
$\mathbb{R}$. The vectors $u_p = (1, 1)$ and $v_p = (1, -1)$ of $\ell^p_2$ satisfy
$u_p - v_p = 2 e_1$, where $e_1 = (0, 1)$ is the second standard basis vector.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.LpGeometry.lpTwoPlus_sub_lpTwoMinus`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/LpGeometry.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/LpGeometry.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/geometry-of-finite-dimensional-p-spaces/index.html#lp-two-plus-sub-lp-two-minus).

## Norm of $(1, 1) + (1, -1)$ in $\ell^p_2$

For every $p \in [1, \infty]$, let $\ell^p_2$ be
$\mathbb{R}^2$ with the $\ell^p$ norm, and let $u_p = (1, 1)$ and $v_p = (1, -1)$. Then
$\|u_p + v_p\| = 2$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.LpGeometry.norm_add_lpTwo`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/LpGeometry.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/LpGeometry.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/geometry-of-finite-dimensional-p-spaces/index.html#norm-add-lp-two).

## The difference of the parallelogram witnesses has norm two

For every extended real
$p \in [1, \infty]$, in $\mathbb{R}^2$ with the $\ell^p$ norm the vectors $u = (1, 1)$ and
$v = (1, -1)$ satisfy $\|u - v\| = 2$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.LpGeometry.norm_sub_lpTwo`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/LpGeometry.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/LpGeometry.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/geometry-of-finite-dimensional-p-spaces/index.html#norm-sub-lp-two).

## The $\ell^p$ norm of $(1, 1)$ for finite $p$

For every real $p$ with $1 \le p < \infty$,
the vector $(1, 1)$ of $\mathbb{R}^2$ has $\ell^p$ norm $\|(1, 1)\|_p = 2^{1/p}$, where
$\|(x, y)\|_p = (|x|^p + |y|^p)^{1/p}$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.LpGeometry.norm_lpTwoPlus_of_ne_top`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/LpGeometry.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/LpGeometry.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/geometry-of-finite-dimensional-p-spaces/index.html#norm-lp-two-plus-of-ne-top).

## The $\ell^p$ norm of $(1, -1)$ for finite $p$

For every real $p$ with $1 \le p < \infty$,
the vector $(1, -1)$ of $\mathbb{R}^2$ has $\ell^p$ norm $\|(1, -1)\|_p = 2^{1/p}$, where
$\|(x, y)\|_p = (|x|^p + |y|^p)^{1/p}$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.LpGeometry.norm_lpTwoMinus_of_ne_top`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/LpGeometry.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/LpGeometry.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/geometry-of-finite-dimensional-p-spaces/index.html#norm-lp-two-minus-of-ne-top).

## The $\ell^\infty$ norm of $(1, 1)$

In $\mathbb{R}^2$ with the $\ell^\infty$ norm
$\|(x, y)\|_\infty = \max(|x|, |y|)$, the vector $(1, 1)$ has norm $\|(1, 1)\|_\infty = 1$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.LpGeometry.norm_lpTwoPlus_top`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/LpGeometry.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/LpGeometry.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/geometry-of-finite-dimensional-p-spaces/index.html#norm-lp-two-plus-top).

## The $\ell^\infty$ norm of $(1, -1)$

In $\mathbb{R}^2$ with the $\ell^\infty$ norm
$\|(x, y)\|_\infty = \max(|x|, |y|)$, the vector $(1, -1)$ has norm $\|(1, -1)\|_\infty = 1$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.LpGeometry.norm_lpTwoMinus_top`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/LpGeometry.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/LpGeometry.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/geometry-of-finite-dimensional-p-spaces/index.html#norm-lp-two-minus-top).

## The squared $\ell^p$ norm of $(1, 1)$ for finite $p$

For every real $p$ with
$1 \le p < \infty$, the vector $(1, 1)$ of $\mathbb{R}^2$ satisfies $\|(1, 1)\|_p^2 = 2^{2/p}$,
where $\|(x, y)\|_p = (|x|^p + |y|^p)^{1/p}$ is the $\ell^p$ norm.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.LpGeometry.norm_sq_lpTwoPlus_of_ne_top`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/LpGeometry.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/LpGeometry.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/geometry-of-finite-dimensional-p-spaces/index.html#norm-sq-lp-two-plus-of-ne-top).

## The parallelogram law for $(1, 1)$ and $(1, -1)$ holds only for the $\ell^2$ norm

Let
$p \in [1, \infty]$ and equip $\mathbb{R}^2$ with the $\ell^p$ norm. The vectors $u = (1, 1)$ and
$v = (1, -1)$ satisfy $\|u + v\|^2 + \|u - v\|^2 = 2 (\|u\|^2 + \|v\|^2)$ if and only if
$p = 2$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.LpGeometry.parallelogram_eq_iff_piLp_two`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/LpGeometry.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/LpGeometry.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/geometry-of-finite-dimensional-p-spaces/index.html#parallelogram-eq-iff-pi-lp-two).

## The parallelogram law fails on $\mathbb{R}^2$ with the $\ell^p$ norm for $p \neq 2$

Let
$p \in [1, \infty]$ with $p \neq 2$ and equip $\mathbb{R}^2$ with the $\ell^p$ norm. Then the
vectors $u = (1, 1)$ and $v = (1, -1)$ satisfy
$\|u + v\|^2 + \|u - v\|^2 \neq 2 (\|u\|^2 + \|v\|^2)$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.LpGeometry.parallelogram_fails_piLp_two`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/LpGeometry.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/LpGeometry.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/geometry-of-finite-dimensional-p-spaces/index.html#parallelogram-fails-pi-lp-two).

## The $\ell^p$ norm on $\mathbb{R}^2$ comes from no inner product unless $p = 2$

Let
$p \in [1, \infty]$ with $p \neq 2$. Then the normed space $\mathbb{R}^2$ with the $\ell^p$ norm
carries no real inner product space structure, that is, there is no real inner product with
$\langle x, x \rangle = \|x\|^2$ for every $x$.

Any such inner product would satisfy the parallelogram law, which fails for $(1, 1)$ and
$(1, -1)$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.LpGeometry.not_innerProductSpace_piLp_two`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/LpGeometry.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/LpGeometry.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/geometry-of-finite-dimensional-p-spaces/index.html#not-inner-product-space-pi-lp-two).

## Midpoints of distinct $\ell^p$ unit vectors in $\mathbb{R}^2$ have norm less than one

Let $1 < p < \infty$ and equip $\mathbb{R}^2$ with the $\ell^p$ norm. If $x \neq y$ are vectors
with $\|x\| = \|y\| = 1$, then $\|\tfrac{1}{2} (x + y)\| < 1$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.LpGeometry.piLp_two_strictConvex`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/LpGeometry.lean, line 293](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/LpGeometry.lean#L293). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/geometry-of-finite-dimensional-p-spaces/index.html#pi-lp-two-strict-convex).

## $\mathbb{R}^2$ with the $\ell^p$ norm is strictly convex for $1 < p < \infty$

For
$1 < p < \infty$, the real normed space $\mathbb{R}^2$ with the $\ell^p$ norm is a strictly
convex space: every closed ball of positive radius centred at the origin is a strictly convex
set.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.LpGeometry.strictConvexSpace_piLp_two`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/LpGeometry.lean, line 337](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/LpGeometry.lean#L337). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/geometry-of-finite-dimensional-p-spaces/index.html#strict-convex-space-pi-lp-two).

## Two distinct $\ell^1$ unit vectors in $\mathbb{R}^2$ with a unit midpoint

In
$\mathbb{R}^2$ with the $\ell^1$ norm there exist vectors $x \neq y$ with $\|x\| = \|y\| = 1$
and $\|\tfrac{1}{2} (x + y)\| = 1$.

For example, the unit vectors $(1, 0)$ and $(0, 1)$ have midpoint $(1/2, 1/2)$ of norm $1$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.LpGeometry.not_strictConvex_piLp_two_one`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/LpGeometry.lean, line 346](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/LpGeometry.lean#L346). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/geometry-of-finite-dimensional-p-spaces/index.html#not-strict-convex-pi-lp-two-one).

## $\mathbb{R}^2$ with the $\ell^1$ norm is not strictly convex

The real normed space
$\mathbb{R}^2$ with the $\ell^1$ norm is not a strictly convex space: not every closed ball of
positive radius centred at the origin is a strictly convex set.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.LpGeometry.not_strictConvexSpace_piLp_two_one`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/LpGeometry.lean, line 363](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/LpGeometry.lean#L363). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/geometry-of-finite-dimensional-p-spaces/index.html#not-strict-convex-space-pi-lp-two-one).

## Two distinct $\ell^\infty$ unit vectors in $\mathbb{R}^2$ with a unit midpoint

In
$\mathbb{R}^2$ with the $\ell^\infty$ norm there exist vectors $x \neq y$ with
$\|x\| = \|y\| = 1$ and $\|\tfrac{1}{2} (x + y)\| = 1$.

For example, the unit vectors $(1, 1)$ and $(1, -1)$ have midpoint $(1, 0)$ of norm $1$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.LpGeometry.not_strictConvex_piLp_two_top`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/LpGeometry.lean, line 373](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/LpGeometry.lean#L373). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/geometry-of-finite-dimensional-p-spaces/index.html#not-strict-convex-pi-lp-two-top).

## $\mathbb{R}^2$ with the $\ell^\infty$ norm is not strictly convex

The real normed space
$\mathbb{R}^2$ with the $\ell^\infty$ norm is not a strictly convex space: not every closed ball
of positive radius centred at the origin is a strictly convex set.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.LpGeometry.not_strictConvexSpace_piLp_two_top`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/LpGeometry.lean, line 390](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/LpGeometry.lean#L390). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/geometry-of-finite-dimensional-p-spaces/index.html#not-strict-convex-space-pi-lp-two-top).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Geometry of finite-dimensional ℓ^p spaces](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/geometry-of-finite-dimensional-p-spaces/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/banach-spaces/sequence-spaces/geometry-of-finite-dimensional-p-spaces)
