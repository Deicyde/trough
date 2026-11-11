---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Calculus.VanishingMomentsImpliesZeroWanted.eqOn_zero_of_integral_mul_pow_eq_zero, MetaMathlibExt.arcsin_div_sin_integral, MathlibExt.Analysis.Calculus.IteratedIntegralCauchyFormulaWanted.intervalIntegral_intervalIntegral_eq_integral_sub_smul, MathlibExt.Analysis.SpecialFunctions.IntegralInvAddMulCosWanted.integral_one_div_add_mul_cos_eq, MathlibExt.Analysis.SpecialFunctions.IntegralSincSqHalfLineWanted.integral_sin_div_sq_Ioi_eq_pi_div_two, MathlibExt.Analysis.SpecialFunctions.IntegralLogOnePlusOverOnePlusSqWanted.integral_log_one_add_div_one_add_sq, MathlibExt.Analysis.Calculus.IntegralXFDerivFWanted.integral_mul_mul_deriv_eq_neg_half, MathlibExt.Analysis.Calculus.UniformlyContinuousIntegrableTendstoZeroWanted.UniformContinuous.tendsto_cocompact_zero_of_integrable
statement: formalized
---

# Riemann integration and definite integrals: its own results

9 results, 1 proved and 8 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/index.html).

The Riemann integral via tagged partitions, iterated-integral formulas, moments, and closed-form evaluations of specific definite integrals (Serret's integral, integrals of 1/(1+u^n), areas between cosine powers, sinc squared); integrals defining a named special function go to Special functions.

## A function continuous on $(0,1)$ with vanishing moments is zero on $(0,1)$

Let
$f : \mathbb{R} \to \mathbb{R}$ be continuous on $[0,1]$, and suppose that
$\int_0^1 f(x)\,x^n\,dx = 0$ for every natural number $n = 0, 1, 2, \dots$. Then $f(x) = 0$ for
every $x \in [0,1]$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Real functions; Functions of one variable), problem `ma_proofbench_l1_51`.

Stated but not proved: `MathlibExt.Analysis.Calculus.VanishingMomentsImpliesZeroWanted.eqOn_zero_of_integral_mul_pow_eq_zero` is written with `theorem_wanted` in [WantedExt/Analysis/Calculus/VanishingMomentsImpliesZeroWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Calculus/VanishingMomentsImpliesZeroWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/index.html#eq-on-zero-of-integral-mul-pow-eq-zero).

## Bhandari's arcsine-over-sine integral

Let $G = \sum_{n \ge 0} (-1)^n/(2n+1)^2$ be
Catalan's constant, and for $s > 0$ let $S_s = \sum_{n \ge 0} 1/(n + s)^2$. Then the integral
$\int_0^{\pi/2} \frac{\arcsin(\sin^2 x)}{\sin x}\,dx$ equals
$-2G - \frac{\pi^2}{2\sqrt 2} + \frac{S_{1/8} + S_{3/8}}{8\sqrt 2}$.

The series $S_{1/8}$ and $S_{3/8}$ are the trigamma values $\psi_1(1/8)$ and $\psi_1(3/8)$;
Catalan's constant and these trigamma values are written out as their defining series.

Proof: The route follows Bhandari's reduction to log-tangent integrals, followed by an
Abel-regularized Fourier expansion and residue-class evaluation.

## Sources

- Narendra Bhandari, "Infinite Series Associated with the Ratio and Product of Central Binomial Coefficients", Journal of Integer Sequences 25 (2022), equation (36), lines 307--309, <https://cs.uwaterloo.ca/journals/JIS/VOL25/Bhandari/bhan8.tex>.

Formalized by `MetaMathlibExt.arcsin_div_sin_integral`, a theorem declared in [MathlibExt/Analysis/Calculus/ArcsinDivSinIntegral.lean, line 1571](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Calculus/ArcsinDivSinIntegral.lean#L1571). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/index.html#arcsin-div-sin-integral).

## Cauchy's formula for the twice-iterated integral

Let $E$ be a real Banach space, let
$\alpha \le \beta$ be real numbers and let $f : \mathbb{R} \to E$ be continuous on
$[\alpha, \beta]$. Then for every $s \in [\alpha, \beta]$,

$$\int_\alpha^s \Bigl(\int_\alpha^t f(\tau)\,d\tau\Bigr)\,dt = \int_\alpha^s (s - t)\, f(t)\,dt.$$

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Real functions; Functions of one variable), problem `ma_proofbench_l1_44`.

Stated but not proved: `MathlibExt.Analysis.Calculus.IteratedIntegralCauchyFormulaWanted.intervalIntegral_intervalIntegral_eq_integral_sub_smul` is written with `theorem_wanted` in [WantedExt/Analysis/Calculus/IteratedIntegralCauchyFormulaWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Calculus/IteratedIntegralCauchyFormulaWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/index.html#interval-integral-interval-integral-eq-i).

## Integral of $1/(a + b\cos\theta)$ over a period

Let $a$ and $b$ be real numbers with
$a > |b|$. Then

$$\int_0^{2\pi} \frac{d\theta}{a + b\cos\theta} = \frac{2\pi}{\sqrt{a^2 - b^2}}.$$

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Functions of a complex variable; General properties of functions of one complex variable), problem `ma_proofbench_l1_89`.

Stated but not proved: `MathlibExt.Analysis.SpecialFunctions.IntegralInvAddMulCosWanted.integral_one_div_add_mul_cos_eq` is written with `theorem_wanted` in [WantedExt/Analysis/SpecialFunctions/IntegralInvAddMulCosWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/SpecialFunctions/IntegralInvAddMulCosWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/index.html#integral-one-div-add-mul-cos-eq).

## Integral of the squared sinc function over the half-line

The integral of
$(\sin x / x)^2$ over $(0, \infty)$ is $\pi/2$:

$$\int_0^\infty \left(\frac{\sin x}{x}\right)^2 dx = \frac{\pi}{2}.$$

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Real functions; Functions of one variable), problem `ma_proofbench_l1_35`.

Stated but not proved: `MathlibExt.Analysis.SpecialFunctions.IntegralSincSqHalfLineWanted.integral_sin_div_sq_Ioi_eq_pi_div_two` is written with `theorem_wanted` in [WantedExt/Analysis/SpecialFunctions/IntegralSincSqHalfLineWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/SpecialFunctions/IntegralSincSqHalfLineWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/index.html#integral-sin-div-sq-ioi-eq-pi-div-two).

## Serret's integral

With $\log$ the natural logarithm,

$$\int_0^1 \frac{\log(1+x)}{1+x^2}\,dx = \frac{\pi}{8}\log 2.$$

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Real functions; Functions of one variable), problem `ma_proofbench_l1_58`.

Stated but not proved: `MathlibExt.Analysis.SpecialFunctions.IntegralLogOnePlusOverOnePlusSqWanted.integral_log_one_add_div_one_add_sq` is written with `theorem_wanted` in [WantedExt/Analysis/SpecialFunctions/IntegralLogOnePlusOverOnePlusSqWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/SpecialFunctions/IntegralLogOnePlusOverOnePlusSqWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/index.html#integral-log-one-add-div-one-add-sq).

## The integral of $x f(x) f'(x)$ equals $-1/2$

Let $a\lt b$ and let
$f : \mathbb{R} \to \mathbb{R}$ be continuously differentiable on $[a,b]$ with $f(a)=f(b)=0$ and

$$
\int_a^b f(x)^2\,dx=1.
$$

Then

$$
\int_a^b x\,f(x)\,f'(x)\,dx=-\frac12.
$$

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Real functions; Functions of one variable), problem `ma_proofbench_l1_16`.

Stated but not proved: `MathlibExt.Analysis.Calculus.IntegralXFDerivFWanted.integral_mul_mul_deriv_eq_neg_half` is written with `theorem_wanted` in [WantedExt/Analysis/Calculus/IntegralXFDerivFWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Calculus/IntegralXFDerivFWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/index.html#integral-mul-mul-deriv-eq-neg-half).

## Uniformly continuous integrable functions vanish at infinity

Let
$f : \mathbb{R} \to \mathbb{R}$ be uniformly continuous and Lebesgue integrable on $\mathbb{R}$.
Then $f(x) \to 0$ as $|x| \to \infty$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Real functions; Functions of one variable), problem `ma_proofbench_l1_48`.

Stated but not proved: `MathlibExt.Analysis.Calculus.UniformlyContinuousIntegrableTendstoZeroWanted.UniformContinuous.tendsto_cocompact_zero_of_integrable` is written with `theorem_wanted` in [WantedExt/Analysis/Calculus/UniformlyContinuousIntegrableTendstoZeroWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Calculus/UniformlyContinuousIntegrableTendstoZeroWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/index.html#tendsto-cocompact-zero-of-integrable).

## Unit-window bound for the integral of $\sin(t^2)$

Let $f : \mathbb{R} \to \mathbb{R}$ be
given by $f(x) = \int_x^{x+1} \sin(t^2)\,dt$. Then $|f(x)| < 1/x$ for every real $x > 0$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Real functions; Functions of one variable), problem `ma_proofbench_l1_29`.

Stated but not proved: `MathlibExt.Analysis.Calculus.IntegralSinSqUnitWindowBoundWanted.abs_integral_sin_sq_lt_inv` is written with `theorem_wanted` in [WantedExt/Analysis/Calculus/IntegralSinSqUnitWindowBoundWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Calculus/IntegralSinSqUnitWindowBoundWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/index.html#abs-integral-sin-sq-lt-inv).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Riemann integration and definite integrals](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/real-functions/integration)
