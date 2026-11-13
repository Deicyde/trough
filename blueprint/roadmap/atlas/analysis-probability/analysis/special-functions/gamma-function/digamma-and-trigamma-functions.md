---
declaration: section
origin: cited
lean: Real.summable_one_div_add_nat_succ_sq, Real.hasSum_digamma_series, Real.hasDerivAt_tsum_digamma_series, Real.deriv_deriv_log_Gamma_add_one, Real.deriv_log_Gamma, Complex.analyticAt_Gamma, Complex.analyticAt_digamma, Complex.deriv_Gamma_ofReal
statement: formalized
proof: formalized
---

# Digamma and trigamma functions

13 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/gamma-function/digamma-and-trigamma-functions/index.html).

## Digamma and trigamma series on the reals

## Summability of the Basel series

The series of real numbers
$\sum_{j \ge 0} \frac{1}{(j+1)^2}$ is summable.

Formalized by `Real.summable_one_div_add_nat_succ_sq`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/Gamma/Digamma.lean, line 333](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/Gamma/Digamma.lean#L333). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/gamma-function/digamma-and-trigamma-functions/index.html#summable-one-div-add-nat-succ-sq).

## Digamma series on the positive reals

For every real $x > 0$, the series
$\sum_{j=0}^{\infty} \left(\frac{1}{j+1} - \frac{1}{x+j+1}\right)$ has sum $\psi(x+1) + \gamma$,
where $\psi = (\log \Gamma)'$ with $\Gamma$ the real Gamma function, and $\gamma$ is the
Euler–Mascheroni constant.

Formalized by `Real.hasSum_digamma_series`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/Gamma/Digamma.lean, line 399](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/Gamma/Digamma.lean#L399). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/gamma-function/digamma-and-trigamma-functions/index.html#has-sum-digamma-series).

## Derivative of the digamma series

For every real $y > 0$, the real function
$z \mapsto \sum_{j=0}^{\infty} \left(\frac{1}{j+1} - \frac{1}{z+j+1}\right)$ is differentiable
at $y$ with derivative $\sum_{j=0}^{\infty} \frac{1}{(y+j+1)^2}$.

Formalized by `Real.hasDerivAt_tsum_digamma_series`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/Gamma/Digamma.lean, line 466](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/Gamma/Digamma.lean#L466). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/gamma-function/digamma-and-trigamma-functions/index.html#has-deriv-at-tsum-digamma-series).

## Trigamma series

For every real $y > 0$, the second derivative of $\log \Gamma$ at
$y + 1$ equals $\sum_{j=0}^{\infty} \frac{1}{(y + j + 1)^2}$, where $\Gamma$ is the real Gamma
function.

Formalized by `Real.deriv_deriv_log_Gamma_add_one`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/Gamma/Digamma.lean, line 503](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/Gamma/Digamma.lean#L503). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/gamma-function/digamma-and-trigamma-functions/index.html#deriv-deriv-log-gamma-add-one).

## Logarithmic derivative of the real Gamma function

For every real $u > 0$, the
derivative of $\log \Gamma$ at $u$ equals $\Gamma'(u) / \Gamma(u)$, where $\Gamma$ is the real
Gamma function.

Formalized by `Real.deriv_log_Gamma`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/Gamma/Digamma.lean, line 555](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/Gamma/Digamma.lean#L555). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/gamma-function/digamma-and-trigamma-functions/index.html#deriv-log-gamma).

## Analyticity of the Gamma function

The complex Gamma function is analytic at every
$w \in \mathbb{C}$ that is not a nonpositive integer.

Formalized by `Complex.analyticAt_Gamma`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/Gamma/Digamma.lean, line 572](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/Gamma/Digamma.lean#L572). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/gamma-function/digamma-and-trigamma-functions/index.html#analytic-at-gamma).

## Analyticity of the digamma function

The digamma function $\psi = \Gamma'/\Gamma$, where
$\Gamma$ is the complex Gamma function, is complex analytic at every $w \in \mathbb{C}$ that is
not a nonpositive integer.

Formalized by `Complex.analyticAt_digamma`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/Gamma/Digamma.lean, line 646](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/Gamma/Digamma.lean#L646). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/gamma-function/digamma-and-trigamma-functions/index.html#analytic-at-digamma).

## Complex and real derivatives of Gamma agree on the positive reals

For every real
$t > 0$, the derivative of the complex Gamma function at $t$ equals the derivative of the real
Gamma function at $t$.

Formalized by `Complex.deriv_Gamma_ofReal`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/Gamma/Digamma.lean, line 652](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/Gamma/Digamma.lean#L652). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/gamma-function/digamma-and-trigamma-functions/index.html#deriv-gamma-of-real).

## Absolute convergence of the trigamma series

For every complex number $z$, the series
$\sum_{k \ge 0} \frac{1}{(z + k + 1)^2}$ converges absolutely, that is, the series of absolute
values $\sum_{k \ge 0} \left|\frac{1}{(z + k + 1)^2}\right|$ is summable, where a term whose
denominator vanishes is read as $0$.

Because of this convention no hypothesis excluding the poles $z = -(k + 1)$ is needed.

Formalized by `Complex.summable_norm_one_div_add_nat_succ_sq`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/Gamma/Digamma.lean, line 681](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/Gamma/Digamma.lean#L681). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/gamma-function/digamma-and-trigamma-functions/index.html#summable-norm-one-div-add-nat-succ-sq).

## Terms of the complex digamma series

For $j \in \mathbb{N}$ and $s \in \mathbb{C}$, the
$j$-th term of the complex digamma series at $s$ is $\frac{1}{j+1} - \frac{1}{j+s}$, where
$1/0$ is read as $0$.

Formalized by `Complex.digammaSeriesTerm`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/Gamma/Digamma.lean, line 738](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/Gamma/Digamma.lean#L738). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/gamma-function/digamma-and-trigamma-functions/index.html#digamma-series-term).

## Complex digamma series

For $s \in \mathbb{C}$, the digamma series function at $s$ is
$\sum_{j=0}^{\infty} \left(\frac{1}{j+1} - \frac{1}{j+s}\right)$, the sum of the terms of the
complex digamma series at $s$.

The value is taken to be $0$ when the series is not summable, and a term with $j + s = 0$ uses
$1/0 = 0$.

Formalized by `Complex.digammaSeriesFun`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/Gamma/Digamma.lean, line 742](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/Gamma/Digamma.lean#L742). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/gamma-function/digamma-and-trigamma-functions/index.html#digamma-series-fun).

## Summability of the digamma series terms

For every complex number $s$ with
$\operatorname{Re} s > 1$, the sequence of digamma series terms
$\frac{1}{j+1} - \frac{1}{j+s}$, for $j = 0, 1, 2, \dots$, is summable.

Formalized by `Complex.summable_digammaSeriesTerm`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/Gamma/Digamma.lean, line 953](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/Gamma/Digamma.lean#L953). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/gamma-function/digamma-and-trigamma-functions/index.html#summable-digamma-series-term).

## Series expansion of the complex digamma function

For every complex number $s$ with
$\operatorname{Re} s > 1$, the series
$\sum_{j=0}^{\infty} \left(\frac{1}{j+1} - \frac{1}{j+s}\right)$ of the terms of the complex
digamma series at $s$ has sum $\psi(s) + \gamma$, where $\psi = \Gamma'/\Gamma$ is the complex
digamma function, the logarithmic derivative of the complex Gamma function, and $\gamma$ is the
Euler–Mascheroni constant.

Formalized by `Complex.hasSum_digamma_series`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/Gamma/Digamma.lean, line 999](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/Gamma/Digamma.lean#L999). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/gamma-function/digamma-and-trigamma-functions/index.html#has-sum-digamma-series-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Digamma and trigamma functions](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/gamma-function/digamma-and-trigamma-functions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/special-functions/gamma-function/digamma-and-trigamma-functions)
