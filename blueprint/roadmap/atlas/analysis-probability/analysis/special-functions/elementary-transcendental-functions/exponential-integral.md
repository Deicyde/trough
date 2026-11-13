---
declaration: section
origin: cited
lean: Complex.einTerm, Complex.ein, Complex.differentiable_ein, Complex.analyticOnNhd_ein, Complex.mul_deriv_ein, Complex.principalExponentialIntegralE1Raw, Complex.principalExponentialIntegralE1, Complex.e1AsymptoticTermRaw
statement: formalized
proof: formalized
---

# Exponential integral

24 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/exponential-integral/index.html).

## Terms of the series for the entire exponential integral

For a natural number $n$ and a
complex number $z$, this is the complex number $\frac{(-1)^n z^{n+1}}{(n+1) \cdot (n+1)!}$,
the term of index $j = n + 1$ in the series
$\operatorname{Ein}(z) = \sum_{j \ge 1} \frac{(-1)^{j+1} z^j}{j \cdot j!}$.

Formalized by `Complex.einTerm`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/EntireExponentialIntegral.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/EntireExponentialIntegral.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/exponential-integral/index.html#ein-term).

## The entire exponential integral Ein

The entire exponential integral is the function
$\operatorname{Ein} : \mathbb{C} \to \mathbb{C}$ defined by
$\operatorname{Ein}(z) = \sum_{j \ge 1} \frac{(-1)^{j+1} z^j}{j \cdot j!}$.

Formalized by `Complex.ein`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/EntireExponentialIntegral.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/EntireExponentialIntegral.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/exponential-integral/index.html#ein).

## Differentiability of the entire exponential integral

The entire exponential integral
$\operatorname{Ein}$ is complex differentiable at every point of $\mathbb{C}$.

Formalized by `Complex.differentiable_ein`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/EntireExponentialIntegral.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/EntireExponentialIntegral.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/exponential-integral/index.html#differentiable-ein).

## Analyticity of the entire exponential integral

The entire exponential integral
$\operatorname{Ein}$ is complex analytic at every point of $\mathbb{C}$.

Formalized by `Complex.analyticOnNhd_ein`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/EntireExponentialIntegral.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/EntireExponentialIntegral.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/exponential-integral/index.html#analytic-on-nhd-ein).

## Derivative of the entire exponential integral

For every complex number $z$, the entire
exponential integral $\operatorname{Ein}$ satisfies $z \operatorname{Ein}'(z) = 1 - e^{-z}$.

This is the identity $\operatorname{Ein}'(z) = (1 - e^{-z})/z$ multiplied through by $z$, a form
that remains valid at $z = 0$.

Formalized by `Complex.mul_deriv_ein`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/EntireExponentialIntegral.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/EntireExponentialIntegral.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/exponential-integral/index.html#mul-deriv-ein).

## Totalized principal exponential integral

For every complex number $z$, this is
$\operatorname{Ein}(z) - \operatorname{Log} z - \gamma$, where
$\operatorname{Ein}(z) = \sum_{j \ge 1} (-1)^{j+1} z^j / (j \cdot j!)$ is the entire exponential
integral, $\operatorname{Log}$ is the principal branch of the complex logarithm (imaginary part
in $(-\pi, \pi]$) extended by $\operatorname{Log} 0 = 0$, and $\gamma$ is the Euler–Mascheroni
constant.

At $z = 0$ the value is therefore $-\gamma$. This is a convention, not a value of the classical
principal $E_1$, which has a logarithmic singularity at $0$.

Formalized by `Complex.principalExponentialIntegralE1Raw`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/ExponentialIntegral/E1.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/ExponentialIntegral/E1.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/exponential-integral/index.html#principal-exponential-integral-e1-raw).

## The principal exponential integral

For a nonzero complex number $z$, the principal
exponential integral is $E_1(z) = \operatorname{Ein}(z) - \operatorname{Log} z - \gamma$, where
$\operatorname{Ein}(z) = \sum_{j \ge 1} (-1)^{j+1} z^j / (j \cdot j!)$ is the entire exponential
integral, $\operatorname{Log}$ is the principal branch of the complex logarithm (imaginary part
in $(-\pi, \pi]$) and $\gamma$ is the Euler–Mascheroni constant.

This is the connection formula DLMF 6.2.4, taken as the definition. On the branch cut, the
negative real axis, the value is the one given by the principal logarithm.

Formalized by `Complex.principalExponentialIntegralE1`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/ExponentialIntegral/E1.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/ExponentialIntegral/E1.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/exponential-integral/index.html#principal-exponential-integral-e1).

## Totalized asymptotic term of $E_1$

For $n \in \mathbb{N}$ and every complex number $z$,
the $n$-th term of the asymptotic expansion of $E_1$ is
$\frac{e^{-z}}{z} \cdot \frac{(-1)^n \, n!}{z^n}$, with division by zero read as $0$.

At $z = 0$ this gives $0$, a value with no classical meaning; the domain-safe term requires
$z \neq 0$.

Formalized by `Complex.e1AsymptoticTermRaw`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/ExponentialIntegral/E1.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/ExponentialIntegral/E1.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/exponential-integral/index.html#e1-asymptotic-term-raw).

## Asymptotic term of $E_1$

For $n \in \mathbb{N}$ and a nonzero complex number $z$, the
$n$-th term of the asymptotic expansion of the exponential integral $E_1$ is
$\frac{e^{-z}}{z} \cdot \frac{(-1)^n \, n!}{z^n}$.

Formalized by `Complex.e1AsymptoticTerm`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/ExponentialIntegral/E1.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/ExponentialIntegral/E1.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/exponential-integral/index.html#e1-asymptotic-term).

## Totalized partial sum of the $E_1$ asymptotic expansion

For $n \in \mathbb{N}$ and every
complex number $z$, this is $\sum_{j < n} t_j(z)$, where
$t_j(z) = \frac{e^{-z}}{z} \cdot \frac{(-1)^j \, j!}{z^j}$ with division by zero read as $0$.

At $z = 0$ every term, hence the sum, is $0$; this value has no classical meaning, and the
domain-safe partial sum requires $z \neq 0$.

Formalized by `Complex.e1AsymptoticPartialRaw`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/ExponentialIntegral/E1.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/ExponentialIntegral/E1.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/exponential-integral/index.html#e1-asymptotic-partial-raw).

## Partial sum of the $E_1$ asymptotic expansion

For $n \in \mathbb{N}$ and a nonzero complex
number $z$, the sum of the first $n$ terms of the asymptotic expansion of the exponential
integral $E_1$ is $\sum_{j < n} \frac{e^{-z}}{z} \cdot \frac{(-1)^j \, j!}{z^j}$.

Formalized by `Complex.e1AsymptoticPartial`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/ExponentialIntegral/E1.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/ExponentialIntegral/E1.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/exponential-integral/index.html#e1-asymptotic-partial).

## Totalized remainder of the $E_1$ asymptotic expansion

For $n \in \mathbb{N}$ and every
complex number $z$, this is $\operatorname{Ein}(z) - \operatorname{Log} z - \gamma - S_n(z)$,
where $\operatorname{Ein}$ is the entire exponential integral, $\operatorname{Log}$ is the
principal logarithm extended by $\operatorname{Log} 0 = 0$, $\gamma$ is the Euler–Mascheroni
constant and $S_n$ is the totalized sum of the first $n$ terms of the asymptotic expansion
of $E_1$.

At $z = 0$ this equals $-\gamma$, a value with no classical meaning; the domain-safe remainder
requires $z \neq 0$.

Formalized by `Complex.e1AsymptoticRemainderRaw`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/ExponentialIntegral/E1.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/ExponentialIntegral/E1.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/exponential-integral/index.html#e1-asymptotic-remainder-raw).

## Remainder of the $E_1$ asymptotic expansion

For $n \in \mathbb{N}$ and a nonzero complex
number $z$, the remainder after $n$ terms is
$E_1(z) - \sum_{j < n} \frac{e^{-z}}{z} \cdot \frac{(-1)^j \, j!}{z^j}$, where $E_1$ is the
principal exponential integral.

Formalized by `Complex.e1AsymptoticRemainder`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/ExponentialIntegral/E1.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/ExponentialIntegral/E1.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/exponential-integral/index.html#e1-asymptotic-remainder).

## Totalized principal $E_1$ kernel at zero

The totalized kernel
$\operatorname{Ein}(z) - \operatorname{Log} z - \gamma$, where $\operatorname{Ein}$ is the entire
exponential integral, $\operatorname{Log}$ is the principal logarithm extended by
$\operatorname{Log} 0 = 0$ and $\gamma$ is the Euler–Mascheroni constant, equals $-\gamma$ at
$z = 0$.

This value comes from $\operatorname{Ein}(0) = 0$ and the convention $\operatorname{Log} 0 = 0$,
not from analysis; the classical $E_1$ is singular at $0$.

Formalized by `Complex.principalExponentialIntegralE1Raw_zero`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/ExponentialIntegral/E1.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/ExponentialIntegral/E1.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/exponential-integral/index.html#principal-exponential-integral-e1-raw-ze).

## Totalized $E_1$ asymptotic terms vanish at zero

For every $n \in \mathbb{N}$, the
totalized $n$-th term $\frac{e^{-z}}{z} \cdot \frac{(-1)^n \, n!}{z^n}$ of the asymptotic
expansion of $E_1$, with division by zero read as $0$, equals $0$ at $z = 0$.

This value comes from the convention that division by zero gives $0$, not from analysis.

Formalized by `Complex.e1AsymptoticTermRaw_zero`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/ExponentialIntegral/E1.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/ExponentialIntegral/E1.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/exponential-integral/index.html#e1-asymptotic-term-raw-zero).

## Totalized partial sums of the $E_1$ expansion vanish at zero

For every
$n \in \mathbb{N}$, the totalized sum of the first $n$ terms of the asymptotic expansion of $E_1$
equals $0$ at $z = 0$.

This value comes from the convention that division by zero gives $0$, not from analysis.

Formalized by `Complex.e1AsymptoticPartialRaw_zero`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/ExponentialIntegral/E1.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/ExponentialIntegral/E1.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/exponential-integral/index.html#e1-asymptotic-partial-raw-zero).

## Totalized $E_1$ remainder at zero

For every $n \in \mathbb{N}$, the totalized remainder
of the asymptotic expansion of $E_1$ after $n$ terms equals $-\gamma$ at $z = 0$, where $\gamma$
is the Euler–Mascheroni constant.

This value comes from the conventions $\operatorname{Log} 0 = 0$ and division by zero giving
$0$, not from analysis; the classical $E_1$ is singular at $0$.

Formalized by `Complex.e1AsymptoticRemainderRaw_zero`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/ExponentialIntegral/E1.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/ExponentialIntegral/E1.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/exponential-integral/index.html#e1-asymptotic-remainder-raw-zero).

## Two-term expansion of $1/(t + z)$

Let $z \ne 0$ be a complex number and $t$ a real
number with $t + z \ne 0$. Then
$\frac{1}{t + z} = \frac{1}{z} - \frac{t}{z^2} + \frac{t^2}{z^2 (t + z)}$.

Formalized by `Complex.two_term_kernel_identity`, a lemma declared in [MathlibExt/Analysis/SpecialFunctions/ExponentialIntegral/E1/Basic.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/ExponentialIntegral/E1/Basic.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/exponential-integral/index.html#two-term-kernel-identity).

## Integrability of $e^{-t} t^n$ on $(0, \infty)$

For every natural number $n$, the
function $t \mapsto e^{-t} t^n$ is Lebesgue integrable on the open interval $(0, \infty)$.

Formalized by `Complex.integrableOn_exp_neg_mul_pow`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/ExponentialIntegral/E1/Basic.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/ExponentialIntegral/E1/Basic.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/exponential-integral/index.html#integrable-on-exp-neg-mul-pow).

## The moments of $e^{-t}$ are factorials

For every natural number $n$, the integral of
$e^{-t} t^n$ over the open interval $(0, \infty)$ equals $n!$.

Formalized by `Complex.integral_exp_neg_mul_pow_Ioi`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/ExponentialIntegral/E1/Basic.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/ExponentialIntegral/E1/Basic.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/exponential-integral/index.html#integral-exp-neg-mul-pow-ioi).

## Positivity of $\sin |\arg z|$ in the outer sector

Let $z \ne 0$ be a complex number with
$\pi/2 \le |\arg z| < \pi$, where $\arg z \in (-\pi, \pi]$ is the principal argument. Then
$\sin |\arg z| > 0$.

Formalized by `Complex.outer_sector_sin_abs_arg_pos`, a lemma declared in [MathlibExt/Analysis/SpecialFunctions/ExponentialIntegral/E1/Basic.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/ExponentialIntegral/E1/Basic.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/exponential-integral/index.html#outer-sector-sin-abs-arg-pos).

## Lower bound for $|t + z|$ in the outer sector

Let $z \ne 0$ be a complex number with
$\pi/2 \le |\arg z| < \pi$, where $\arg z \in (-\pi, \pi]$ is the principal argument, and let
$t \ge 0$ be a real number. Then $|z| \sin |\arg z| \le |t + z|$.

Formalized by `Complex.outer_sector_distance`, a lemma declared in [MathlibExt/Analysis/SpecialFunctions/ExponentialIntegral/E1/Basic.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/ExponentialIntegral/E1/Basic.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/exponential-integral/index.html#outer-sector-distance).

## Outer-sector bound for the quadratic integral remainder

Let $z \ne 0$ be a complex number
with $\pi/2 \le |\arg z| < \pi$, where $\arg z \in (-\pi, \pi]$ is the principal argument, and
let $T_2(z) = \frac{e^{-z}}{z} \cdot \frac{(-1)^2 \, 2!}{z^2}$ be the $n = 2$ term of the
asymptotic expansion of $E_1$. Then

$$\left| \frac{e^{-z}}{z^2} \int_0^\infty \frac{e^{-t} t^2}{t + z} \, dt \right| \le
\frac{|T_2(z)|}{\sin |\arg z|},$$

where the integral is taken over the open interval $(0, \infty)$.

Formalized by `Complex.integral_remainder_bound`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/ExponentialIntegral/E1/Basic.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/ExponentialIntegral/E1/Basic.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/exponential-integral/index.html#integral-remainder-bound).

## Two-term remainder bound for $E_1$ in the outer sector

Let $z \ne 0$ be a complex number
with $\pi/2 \le |\arg z| < \pi$, where $\arg z \in (-\pi, \pi]$ is the principal argument. Let
$E_1(z)$ be the principal exponential integral, let
$T_n(z) = \frac{e^{-z}}{z} \cdot \frac{(-1)^n n!}{z^n}$ be the $n$-th term of its asymptotic
expansion, and let $R_2(z) = E_1(z) - T_0(z) - T_1(z)$ be the remainder after the first two
terms. Then $|R_2(z)| \le \frac{|T_2(z)|}{\sin |\arg z|}$.

## Sources

- DLMF 6.12.1 and the outer-sector remainder bound of DLMF §6.12(i), with $n = 2$.

Formalized by `Complex.principal_exponential_integral_e1_two_term_remainder_dlmf`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/ExponentialIntegral/E1/DLMF.lean, line 22](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/ExponentialIntegral/E1/DLMF.lean#L22). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/exponential-integral/index.html#principal-exponential-integral-e1-two-te).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Exponential integral](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/exponential-integral/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/special-functions/elementary-transcendental-functions/exponential-integral)
