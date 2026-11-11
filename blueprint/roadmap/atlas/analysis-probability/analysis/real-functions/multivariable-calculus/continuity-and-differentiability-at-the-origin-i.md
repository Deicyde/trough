---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Calculus.CubicOverSumSquaresPartialsBoundedWanted.bounded_partialDerivs_cube_div_sq_add_sq, MathlibExt.Analysis.Calculus.SignedRadialNotDifferentiableWanted.not_differentiableAt_signed_norm_zero, MathlibExt.Analysis.Calculus.XYOverNormSqDiscontinuityWanted.continuousOn_compl_and_not_continuousAt_mul_div_sq_add_sq
statement: formalized
---

# Continuity and differentiability at the origin in the plane

3 results, 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/continuity-and-differentiability-at-the-origin-i/index.html).

## The partial derivatives of $x^3/(x^2+y^2)$ are bounded

Let
$f : \mathbb{R}^2 \to \mathbb{R}$ satisfy $f(0,0)=0$ and $f(x,y)=x^3/(x^2+y^2)$ for $(x,y)\ne(0,0)$.
Then the partial derivatives $D_1 f$ and $D_2 f$ are bounded on $\mathbb{R}^2$: there is a real $M$
with $|D_1 f(x,y)| \le M$ for all $x,y\in\mathbb{R}$, and a real $M'$ with $|D_2 f(x,y)| \le M'$ for
all $x,y\in\mathbb{R}$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Real functions; Functions of several variables), problem `ma_proofbench_l1_56`.

Stated but not proved: `MathlibExt.Analysis.Calculus.CubicOverSumSquaresPartialsBoundedWanted.bounded_partialDerivs_cube_div_sq_add_sq` is written with `theorem_wanted` in [WantedExt/Analysis/Calculus/CubicOverSumSquaresPartialsBoundedWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Calculus/CubicOverSumSquaresPartialsBoundedWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/continuity-and-differentiability-at-the-origin-i/index.html#bounded-partial-derivs-cube-div-sq-add-s).

## The signed radial function is not differentiable at the origin

Let
$f : \mathbb{R}^2 \to \mathbb{R}$ be the function

$$
f(x,y)=
\begin{cases}
\sqrt{x^{2}+y^{2}}, & y>0,\\
x, & y=0,\\
-\sqrt{x^{2}+y^{2}}, & y<0.
\end{cases}
$$

Then $f$ is not differentiable at $(0, 0)$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Real functions; Functions of several variables), problem `ma_proofbench_l1_06`.

Stated but not proved: `MathlibExt.Analysis.Calculus.SignedRadialNotDifferentiableWanted.not_differentiableAt_signed_norm_zero` is written with `theorem_wanted` in [WantedExt/Analysis/Calculus/SignedRadialNotDifferentiableWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Calculus/SignedRadialNotDifferentiableWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/continuity-and-differentiability-at-the-origin-i/index.html#not-differentiable-at-signed-norm-zero).

## The function $xy/(x^2+y^2)$ is discontinuous only at the origin

Let
$f : \mathbb{R}^2 \to \mathbb{R}$ be given by $f(x,y) = \frac{xy}{x^2+y^2}$ for
$(x,y) \neq (0,0)$ and $f(0,0) = 0$. Then $f$ is continuous on $\mathbb{R}^2 \setminus \{(0,0)\}$
and is not continuous at $(0,0)$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Real functions; Functions of several variables), problem `ma_proofbench_l1_93`.

Stated but not proved: `MathlibExt.Analysis.Calculus.XYOverNormSqDiscontinuityWanted.continuousOn_compl_and_not_continuousAt_mul_div_sq_add_sq` is written with `theorem_wanted` in [WantedExt/Analysis/Calculus/XYOverNormSqDiscontinuityWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Calculus/XYOverNormSqDiscontinuityWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/continuity-and-differentiability-at-the-origin-i/index.html#continuous-on-compl-and-not-continuous-a).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Continuity and differentiability at the origin in the plane](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/continuity-and-differentiability-at-the-origin-i/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/real-functions/multivariable-calculus/continuity-and-differentiability-at-the-origin-i)
