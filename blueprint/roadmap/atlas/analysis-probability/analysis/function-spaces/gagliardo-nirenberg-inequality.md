---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Calculus.SixthPowerIntegralLeDerivSqWanted.exists_integral_pow_six_le_integral_deriv_sq_of_integral_sq_eq_one, MathlibExt.Analysis.Calculus.WeightedSixthPowerGagliardoNirenbergWanted.exists_integral_pow_six_mul_weight_le
statement: formalized
---

# Gagliardo–Nirenberg inequality

2 results, 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/gagliardo-nirenberg-inequality/index.html).

## Sixth-power integral bounded by the Dirichlet energy under $L^2$ normalization

There is
a constant $C_2 > 0$ such that every infinitely differentiable, compactly supported function
$u : \mathbb{R} \to \mathbb{R}$ with $\int_{\mathbb{R}} u(t)^2 \, dt = 1$ satisfies

$$\int_{\mathbb{R}} u(t)^6 \, dt \le C_2 \int_{\mathbb{R}} u'(t)^2 \, dt.$$

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Real functions; Inequalities in real analysis), problem `ma_proofbench_l2_79`.

Stated but not proved: `MathlibExt.Analysis.Calculus.SixthPowerIntegralLeDerivSqWanted.exists_integral_pow_six_le_integral_deriv_sq_of_integral_sq_eq_one` is written with `theorem_wanted` in [WantedExt/Analysis/Calculus/SixthPowerIntegralLeDerivSqWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Calculus/SixthPowerIntegralLeDerivSqWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/gagliardo-nirenberg-inequality/index.html#exists-integral-pow-six-le-integral-deri).

## A weighted $L^6$ bound with a slowly varying weight

There is a constant $C > 0$ with the
following property. Let $\theta : \mathbb{R} \to \mathbb{R}$ be continuously differentiable, with
$\theta(x) > 0$ for every $x$ and $\|\theta'/\theta\|_{L^\infty(\mathbb{R})} \le 1$, and let
$u : \mathbb{R} \to \mathbb{R}$ be smooth with compact support. Then

$$\int_{\mathbb{R}} u(x)^6\,\theta(x)\,dx \le C\,\|u\|_{L^2(\mathbb{R})}^4
\int_{\mathbb{R}} \left(|u'(x)|^2 + |u(x)|^2\right)\theta(x)\,dx.$$

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Real functions; Inequalities in real analysis), problem `ma_proofbench_l2_67`.

Stated but not proved: `MathlibExt.Analysis.Calculus.WeightedSixthPowerGagliardoNirenbergWanted.exists_integral_pow_six_mul_weight_le` is written with `theorem_wanted` in [WantedExt/Analysis/Calculus/WeightedSixthPowerGagliardoNirenbergWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Calculus/WeightedSixthPowerGagliardoNirenbergWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/gagliardo-nirenberg-inequality/index.html#exists-integral-pow-six-mul-weight-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Gagliardo–Nirenberg inequality](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/gagliardo-nirenberg-inequality/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/function-spaces/gagliardo-nirenberg-inequality)
