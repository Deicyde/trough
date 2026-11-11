---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Calculus.SupNormEpsDerivPlusIntegralWanted.exists_const_sSup_norm_le_mul_sSup_norm_deriv_add_mul_integral, MathlibExt.Analysis.Calculus.SupNormSqLeHalfH1NormWanted.sSup_norm_sq_le_half_integral_sq_add_deriv_sq
statement: formalized
---

# Sup-norm bounds by derivatives on an interval

2 results, 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/sup-norm-bounds-by-derivatives-on-an-interval/index.html).

## Sup norm on $(0,1)$ bounded by the derivative and the $L^1$ norm

For every
$\varepsilon > 0$ there is a constant $C_\varepsilon > 0$ such that every function
$f : \mathbb{R} \to \mathbb{R}$ that is continuously differentiable on $[0,1]$ satisfies

$$\sup_{x \in [0,1]} |f(x)| \le
\varepsilon \sup_{x \in [0,1]} |f'(x)| + C_\varepsilon \int_0^1 |f(x)|\,dx.$$

At $x = 0$ and $x = 1$, $f'(x)$ is the two-sided derivative of $f$ on $\mathbb{R}$, taken to be $0$
where it does not exist; this does not change the supremum.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Real functions; Inequalities in real analysis), problem `ma_proofbench_l2_49`.

Stated but not proved: `MathlibExt.Analysis.Calculus.SupNormEpsDerivPlusIntegralWanted.exists_const_sSup_norm_le_mul_sSup_norm_deriv_add_mul_integral` is written with `theorem_wanted` in [WantedExt/Analysis/Calculus/SupNormEpsDerivPlusIntegralWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Calculus/SupNormEpsDerivPlusIntegralWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/sup-norm-bounds-by-derivatives-on-an-interval/index.html#exists-const-s-sup-norm-le-mul-s-sup-nor).

## Sup-norm bound by the $H^1$ energy for functions vanishing at both ends

Let
$\alpha \le \beta$ be real numbers and let $f : \mathbb{R} \to \mathbb{R}$ be continuously
differentiable on $[\alpha, \beta]$ with $f(\alpha) = f(\beta) = 0$. Then

$$\Bigl(\sup_{x \in [\alpha, \beta]} |f(x)|\Bigr)^2 \le
\frac{1}{2} \int_\alpha^\beta \bigl(f(x)^2 + f'(x)^2\bigr)\,dx.$$

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Real functions; Inequalities in real analysis), problem `ma_proofbench_l1_54`.

Stated but not proved: `MathlibExt.Analysis.Calculus.SupNormSqLeHalfH1NormWanted.sSup_norm_sq_le_half_integral_sq_add_deriv_sq` is written with `theorem_wanted` in [WantedExt/Analysis/Calculus/SupNormSqLeHalfH1NormWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Calculus/SupNormSqLeHalfH1NormWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/sup-norm-bounds-by-derivatives-on-an-interval/index.html#s-sup-norm-sq-le-half-integral-sq-add-de).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sup-norm bounds by derivatives on an interval](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/sup-norm-bounds-by-derivatives-on-an-interval/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/function-spaces/sup-norm-bounds-by-derivatives-on-an-interval)
