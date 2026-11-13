---
declaration: section
origin: cited
lean: Real.LogarithmicIntegralDomain, Real.logarithmicIntegral, Real.logarithmicIntegral_zero, Real.logarithmicIntegral_of_lt_one, Real.logarithmicIntegral_of_one_lt, Real.logarithmicIntegralReal, Real.hasDerivAt_logarithmicIntegralReal
statement: formalized
proof: formalized
---

# Logarithmic integral

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/logarithmic-integral/index.html).

## Domain of the logarithmic integral

The domain of the logarithmic integral is the set of
real numbers $x$ with $x \ge 0$ and $x \ne 1$.

The point $1$ is excluded because $1 / \log t$ is singular at $t = 1$; the classical integral
$\int_0^x dt / \log t$ has no finite real value at $x = 1$ and is understood as a Cauchy
principal value for $x \ne 1$.

## Sources

- arXiv:2306.14073v1 and arXiv:2309.16007v1, classical `li(x) := PV ∫₀ˣ dt/log t` with lower limit `0` and principal value at `t = 1`.

Formalized by `Real.LogarithmicIntegralDomain`, an abbreviation declared in [MathlibExt/Analysis/SpecialFunctions/Log/Integral.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/Log/Integral.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/logarithmic-integral/index.html#logarithmic-integral-domain).

## Logarithmic integral

For a real number $x$ in the domain of the logarithmic integral
(that is, $x \ge 0$ and $x \ne 1$), the logarithmic integral $\mathrm{li}(x)$ is
$\mathrm{li}(x) = \int_0^x \frac{dt}{\log t}$ if $x < 1$, and if $x > 1$ it is

$$
\mathrm{li}(x) = \int_0^1 \Big(\frac{1}{\log(1-u)} + \frac{1}{\log(1+u)}\Big) du +
\int_2^x \frac{dt}{\log t}.
$$

The first integral in the second case is the Cauchy principal value
$\mathrm{PV}\int_0^2 \frac{dt}{\log t}$, rewritten by the substitutions $t = 1 - u$ and
$t = 1 + u$, so that $\mathrm{li}(x)$ is the principal value
$\mathrm{PV}\int_0^x \frac{dt}{\log t}$. In particular $\mathrm{li}(0) = 0$.

## Sources

- arXiv:2306.14073v1 and arXiv:2309.16007v1, normalized lower limit `0` and Cauchy principal value at `t = 1` via symmetric pairing.

Formalized by `Real.logarithmicIntegral`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/Log/Integral.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/Log/Integral.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/logarithmic-integral/index.html#logarithmic-integral).

## The logarithmic integral vanishes at zero

The logarithmic integral $\mathrm{li}$
satisfies $\mathrm{li}(0) = 0$; here $0$ lies in its domain since $0 \ge 0$ and $0 \ne 1$.

## Sources

- `∫₀⁰ = 0` for Lebesgue interval integrals; holds for any domain proof `hx` with `x = 0`.

Formalized by `Real.logarithmicIntegral_zero`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/Log/Integral.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/Log/Integral.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/logarithmic-integral/index.html#logarithmic-integral-zero).

## The logarithmic integral below $1$

For every real number $x$ with $0 \le x < 1$, the
logarithmic integral $\mathrm{li}$ satisfies $\mathrm{li}(x) = \int_0^x \frac{dt}{\log t}$.

## Sources

- Direct unfolding of the `x < 1` branch of the piecewise definition.

Formalized by `Real.logarithmicIntegral_of_lt_one`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/Log/Integral.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/Log/Integral.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/logarithmic-integral/index.html#logarithmic-integral-of-lt-one).

## The logarithmic integral above $1$

For every real number $x > 1$, the logarithmic
integral $\mathrm{li}$ satisfies

$$
\mathrm{li}(x) = \int_0^1 \Big(\frac{1}{\log(1-u)} + \frac{1}{\log(1+u)}\Big) du +
\int_2^x \frac{dt}{\log t}.
$$

The paired integral over $[0, 1]$ is the symmetric principal value
$\mathrm{PV}\int_0^2 \frac{dt}{\log t}$.

## Sources

- Direct unfolding of the `x > 1` branch; `¬ x < 1` from `1 < x`.

Formalized by `Real.logarithmicIntegral_of_one_lt`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/Log/Integral.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/Log/Integral.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/logarithmic-integral/index.html#logarithmic-integral-of-one-lt).

## Real logarithmic integral extended by zero

This is the function $\mathbb{R} \to \mathbb{R}$
whose value at $x$ is the logarithmic integral $\operatorname{li}(x)$ when $0 \le x$ and $x \ne 1$,
and $0$ when $x < 0$ or $x = 1$.

The value $0$ off the domain of $\operatorname{li}$ is a convention. Near every $x > 0$ with
$x \ne 1$ the function agrees with $\operatorname{li}$, so its derivative there does not depend
on this choice.

Formalized by `Real.logarithmicIntegralReal`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/Log/IntegralDerivative.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/Log/IntegralDerivative.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/logarithmic-integral/index.html#logarithmic-integral-real).

## Derivative of the logarithmic integral

For every real $x$ with $0 < x$ and $x \ne 1$,
the real logarithmic integral extended by zero has derivative $1/\log x$ at $x$.

Below $1$ the function agrees near $x$ with $\int_0^x dt/\log t$; above $1$ it agrees near $x$
with the paired principal-value constant plus $\int_2^x dt/\log t$. In both cases the
fundamental theorem of calculus gives the derivative $1/\log x$.

Formalized by `Real.hasDerivAt_logarithmicIntegralReal`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/Log/IntegralDerivative.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/Log/IntegralDerivative.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/logarithmic-integral/index.html#has-deriv-at-logarithmic-integral-real).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Logarithmic integral](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/logarithmic-integral/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/special-functions/elementary-transcendental-functions/logarithmic-integral)
