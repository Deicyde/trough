---
declaration: section
origin: cited
lean: MathlibExt.Analysis.OperatorTheory.HilbertIntegralOperatorLpBoundWanted.eLpNorm_hilbertIntegralOperator_le, MathlibExt.Analysis.OperatorTheory.LpKernelIntegralOperatorBoundedWanted.integrable_kernel_mul_and_exists_clm_integral_operator, MathlibExt.Analysis.OperatorTheory.LaplaceTransformLpBoundedIffTwoWanted.laplaceTransform_bounded_on_Lp_iff_eq_two
statement: formalized
---

# Integral, multiplication and diagonal operators: its own results

3 results, 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/index.html).

Volterra and kernel integral operators, Cesàro and Hilbert operators, multiplication operators on C(X) and L², diagonal operators, Schur tests, L^p bounds for integral operators.

## An $L^p$ bound for Hilbert's integral operator

Let $p$ be a real number with
$p > 1$ and let $T$ be the operator on functions $g : \mathbb{R} \to \mathbb{R}$ given by

$$Tg(x) = \int_0^\infty \frac{g(y)}{x+y}\,dy \qquad (x \in \mathbb{R}).$$

Let $f : \mathbb{R} \to \mathbb{R}$ be continuous on $[0,\infty)$, compactly supported and zero
outside $[0,\infty)$, and put

$$C_p = \int_0^\infty \frac{dx}{x^{1/p}(1+x)}.$$

Then

$$\|Tf\|_{L^p([0,\infty))} \le C_p \, \|f\|_{L^p([0,\infty))},$$

where both norms are taken in $[0,\infty]$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Operator theory; Integral, integro-differential, and pseudodifferential operators), problem `ma_proofbench_l2_29`.

Stated but not proved: `MathlibExt.Analysis.OperatorTheory.HilbertIntegralOperatorLpBoundWanted.eLpNorm_hilbertIntegralOperator_le` is written with `theorem_wanted` in [WantedExt/Analysis/OperatorTheory/HilbertIntegralOperatorLpBoundWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/OperatorTheory/HilbertIntegralOperatorLpBoundWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/index.html#e-lp-norm-hilbert-integral-operator-le).

## Integral operators with an $L^p$ kernel map $L^q$ to $L^p$

Let $1 < p < \infty$ and let
$q \ge 1$ be the dual exponent, $p^{-1} + q^{-1} = 1$. Let $K : \mathbb{R}^2 \to \mathbb{R}$ lie
in $L^p((0,1)^2)$, where $L^p((0,1)^2)$, $L^p(0,1)$ and $L^q(0,1)$ are spaces of real functions
for Lebesgue measure. Then for every $f \in L^q(0,1)$ the function $y \mapsto K(x,y)f(y)$ is
integrable on $(0,1)$ for almost every $x \in (0,1)$, and there is a bounded linear operator
$A : L^q(0,1) \to L^p(0,1)$ such that for every $f \in L^q(0,1)$,

$$(Af)(x) = \int_0^1 K(x,y) f(y)\,dy \quad \text{for almost every } x \in (0,1).$$

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Operator theory; Integral, integro-differential, and pseudodifferential operators), problem `ma_proofbench_l2_87`.

Stated but not proved: `MathlibExt.Analysis.OperatorTheory.LpKernelIntegralOperatorBoundedWanted.integrable_kernel_mul_and_exists_clm_integral_operator` is written with `theorem_wanted` in [WantedExt/Analysis/OperatorTheory/LpKernelIntegralOperatorBoundedWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/OperatorTheory/LpKernelIntegralOperatorBoundedWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/index.html#integrable-kernel-mul-and-exists-clm-int).

## The Laplace transform is bounded on $L^p((0,\infty))$ exactly when $p = 2$

For a real
function $f$ on $\mathbb{R}$ let

$$Lf(s) = \int_0^\infty e^{-xs} f(x)\,dx \qquad (s \in \mathbb{R}).$$

Let $p \in [1,\infty]$. Then $p = 2$ if and only if there is a constant $C$ with $0 < C < \infty$
such that every real function $f \in L^p([0,\infty))$ satisfies $Lf \in L^p([0,\infty))$ and
$\|Lf\|_{L^p([0,\infty))} \le C\,\|f\|_{L^p([0,\infty))}$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Operator theory; Integral, integro-differential, and pseudodifferential operators), problem `ma_proofbench_l2_31`.

Stated but not proved: `MathlibExt.Analysis.OperatorTheory.LaplaceTransformLpBoundedIffTwoWanted.laplaceTransform_bounded_on_Lp_iff_eq_two` is written with `theorem_wanted` in [WantedExt/Analysis/OperatorTheory/LaplaceTransformLpBoundedIffTwoWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/OperatorTheory/LaplaceTransformLpBoundedIffTwoWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/index.html#laplace-transform-bounded-on-lp-iff-eq-t).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Integral, multiplication and diagonal operators](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/operator-theory/integral-and-multiplication)
