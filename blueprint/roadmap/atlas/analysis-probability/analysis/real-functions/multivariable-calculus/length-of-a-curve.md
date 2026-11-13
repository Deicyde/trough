---
declaration: section
origin: cited
lean: intervalIntegral.integral_norm_deriv_eq_integral_norm_derivWithin_Icc, ContDiffOn.eVariationOn_Icc_eq_ofReal_integral_norm_derivWithin, MetaMathlibExt.curve_length_eq_integral_norm_deriv
statement: formalized
proof: formalized
---

# Length of a curve

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/length-of-a-curve/index.html).

## Integrating the norm of a derivative within a closed interval

Let $E$ be a real normed
space, let $f : \mathbb{R} \to E$ be any function and let $a \le b$ be real numbers. Then
$\int_a^b \lVert f'(t) \rVert \, dt = \int_a^b \lVert f'_{[a,b]}(t) \rVert \, dt$, where $f'(t)$
is the derivative of $f$ at $t$ and $f'_{[a,b]}(t)$ is its derivative at $t$ within $[a, b]$, each
taken to be $0$ where it does not exist.

Formalized by `intervalIntegral.integral_norm_deriv_eq_integral_norm_derivWithin_Icc`, a theorem declared in [MathlibExt/Analysis/Calculus/CurveLength.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Calculus/CurveLength.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/length-of-a-curve/index.html#integral-norm-deriv-eq-integral-norm-der).

## Length of a $C^1$ curve via its derivative within the interval

Let $E$ be a real Banach
space, let $a \le b$ be real numbers and let $\gamma : \mathbb{R} \to E$ be continuously
differentiable on $[a, b]$. Then the total variation of $\gamma$ on $[a, b]$, a priori a value in
$[0, \infty]$, equals the real number $\int_a^b \lVert \gamma'_{[a,b]}(t) \rVert \, dt$, where
$\gamma'_{[a,b]}(t)$ is the derivative of $\gamma$ at $t$ within $[a, b]$.

Formalized by `ContDiffOn.eVariationOn_Icc_eq_ofReal_integral_norm_derivWithin`, a theorem declared in [MathlibExt/Analysis/Calculus/CurveLength.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Calculus/CurveLength.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/length-of-a-curve/index.html#e-variation-on-icc-eq-of-real-integral-n).

## Length of a $C^1$ curve

Let $E$ be a real Banach space, let $a \le b$ be real numbers,
and let $\gamma : \mathbb{R} \to E$ be continuously differentiable on $[a, b]$. Then the total
variation of $\gamma$ on $[a, b]$ (its length, a priori a value in $[0, \infty]$) equals
$\int_a^b \lVert \gamma'(t) \rVert \, dt$.

Proof: Extend the derivative of $\gamma$ relative to $[a, b]$ by zero outside the interval and
identify the vector measure of its primitive with the corresponding density vector measure. The
variation of that measure is the integral of the norm, and the ordinary derivative agrees with the
derivative relative to $[a, b]$ almost everywhere on the interval.

## Sources

- W. Rudin, Principles of Mathematical Analysis, 3rd ed., Ch. 6; stable ref https://en.wikipedia.org/wiki/Arc_length.

Formalized by `MetaMathlibExt.curve_length_eq_integral_norm_deriv`, a theorem declared in [MathlibExt/Analysis/Calculus/CurveLength.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Calculus/CurveLength.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/length-of-a-curve/index.html#curve-length-eq-integral-norm-deriv).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Length of a curve](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/length-of-a-curve/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/real-functions/multivariable-calculus/length-of-a-curve)
