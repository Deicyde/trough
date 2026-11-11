---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry2Stirlingseries.ramanujan_part1_ch6_entry2_stirlingseries, MathlibExt.Analysis.Ramanujan.Part1Ch8.Entry10Qgammalimit.ramanujan_part1_ch8_entry10_qgammalimit, MathlibExt.Analysis.Ramanujan.Part1Ch8.Entry11Qgammafunctional.chapter8Digamma_eq_digamma, MathlibExt.Analysis.Ramanujan.Part1Ch8.Entry11Qgammafunctional.chapter8PhiTerm_eq_entry12Qgammaintegers, MathlibExt.Analysis.Ramanujan.Part1Ch8.Entry11Qgammafunctional.chapter8Phi_eq_entry12Qgammaintegers, MathlibExt.Analysis.Ramanujan.Part1Ch8.Entry11Qgammafunctional.ramanujan_part1_ch8_entry11_qgammafunctional_digamma, MathlibExt.Analysis.Ramanujan.Part1Ch8.Entry11Qgammafunctional.ramanujan_part1_ch8_entry11_qgammafunctional, MathlibExt.Analysis.Ramanujan.Part1Ch8.Entry12Qgammaintegers.chapter8UnitPow_eq_cpow
statement: formalized
proof: formalized
---

# Series and integrals for the digamma function

17 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/gamma-function/series-and-integrals-for-the-digamma-function/index.html).

## Series for the derivative of $\Gamma'(z+1)/\Gamma(z+1)$

Let $\gamma$ be the
Euler–Mascheroni constant and let $\varphi(w) = \gamma + \Gamma'(w+1)/\Gamma(w+1)$ for complex
$w$. For every complex number $z$ other than $-1, -2, -3, \dots$, the function $\varphi$ is
complex differentiable at $z$, and the series $\sum_{k=1}^{\infty} \frac{1}{(z+k)^2}$ converges
absolutely with sum $\varphi'(z)$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 6.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry2Stirlingseries.ramanujan_part1_ch6_entry2_stirlingseries`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch6Entry2Stirlingseries.lean, line 570](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch6Entry2Stirlingseries.lean#L570). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/gamma-function/series-and-integrals-for-the-digamma-function/index.html#ramanujan-part1-ch6-entry2-stirlingserie).

## Ramanujan's integral for $\psi(1 - 1/x)$ (Chapter 8, Entry 10)

Let $x$ be a complex
number with $\operatorname{Re} x < 0$. For real $u$ put $u^x = e^{x \log |u|}$ when $u \ne 0$,
and define $K_x(0) = 0$, $K_x(1) = -1/x$ and $K_x(u) = \frac{1 - u}{u\,(u^x - 1)}$ for every
other real $u$, the quotient being taken to be $0$ at $u = -1$, where its denominator vanishes.
Then $x \ne 0$ and $\Gamma(1 - 1/x) \ne 0$; for every $u \in (0, 1)$ the denominator
$u\,(u^x - 1)$ is nonzero and $K_x(u) = \frac{1 - u}{u\,(u^x - 1)}$; $K_x$ is integrable on
$[0, 1]$; and

$$\psi\left(1 - \frac{1}{x}\right) + \gamma = -x \int_0^1 K_x(u)\,du,$$

where $\psi$ is the digamma function and $\gamma$ is the Euler–Mascheroni constant.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 8.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch8.Entry10Qgammalimit.ramanujan_part1_ch8_entry10_qgammalimit`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch8Entry10Qgammalimit.lean, line 1037](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch8Entry10Qgammalimit.lean#L1037). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/gamma-function/series-and-integrals-for-the-digamma-function/index.html#ramanujan-part1-ch8-entry10-qgammalimit).

## Digamma as the logarithmic derivative of Gamma (used for Chapter 8, Entry 11)

For every
complex number $z$, $\Gamma'(z)/\Gamma(z) = \psi(z)$, where $\psi$ is the digamma function.

At the poles $z = 0, -1, -2, \dots$ the conventions $\Gamma(z) = 0$ and division by zero giving
$0$ make both sides $0$, so the identity holds for every $z$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch8.Entry11Qgammafunctional.chapter8Digamma_eq_digamma`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch8Entry11Qgammafunctional.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch8Entry11Qgammafunctional.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/gamma-function/series-and-integrals-for-the-digamma-function/index.html#chapter8-digamma-eq-digamma).

## The Entry 11 and Entry 12 series terms agree

For every complex number $x$ and every
natural number $j$, with $k = j + 1$, the term $\frac{2}{(kx)^3 - kx}$ as defined for Entry 11
equals the term given by the same formula for Entry 12.

In both definitions a term with zero denominator is $0$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch8.Entry11Qgammafunctional.chapter8PhiTerm_eq_entry12Qgammaintegers`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch8Entry11Qgammafunctional.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch8Entry11Qgammafunctional.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/gamma-function/series-and-integrals-for-the-digamma-function/index.html#chapter8-phi-term-eq-entry12-qgammainteg).

## The Entry 11 and Entry 12 definitions of $\varphi$ agree

For every complex number $x$,
the function $\varphi(x) = 1 + \sum_{k \ge 1} \frac{2}{(kx)^3 - kx}$ as defined for Entry 11
equals the function given by the same formula for Entry 12.

In both definitions the sum is the unconditional sum, taken to be $0$ when it does not converge,
and a term with zero denominator is $0$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch8.Entry11Qgammafunctional.chapter8Phi_eq_entry12Qgammaintegers`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch8Entry11Qgammafunctional.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch8Entry11Qgammafunctional.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/gamma-function/series-and-integrals-for-the-digamma-function/index.html#chapter8-phi-eq-entry12-qgammaintegers).

## Chapter 8, Entry 11 in terms of the digamma function

Let $x$ be a nonzero complex number
with $x \ne 1/k$ and $x \ne -1/k$ for every positive integer $k$, and put
$\varphi(x) = 1 + \sum_{k \ge 1} \frac{2}{(kx)^3 - kx}$. Then the series
$\sum_{k \ge 1} \frac{2}{(kx)^3 - kx}$ converges unconditionally, $\Gamma(1/x) \ne 0$,
$\Gamma(1 - 1/x) \ne 0$, and

$$\psi(1/x) + \psi(1 - 1/x) = -2\gamma - x\,\varphi(x),$$

where $\psi$ is the digamma function and $\gamma$ is the Euler–Mascheroni constant.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch8.Entry11Qgammafunctional.ramanujan_part1_ch8_entry11_qgammafunctional_digamma`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch8Entry11Qgammafunctional.lean, line 747](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch8Entry11Qgammafunctional.lean#L747). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/gamma-function/series-and-integrals-for-the-digamma-function/index.html#ramanujan-part1-ch8-entry11-qgammafuncti).

## Ramanujan's identity for $\Gamma'/\Gamma$ at $1/x$ and $1 - 1/x$ (Chapter 8, Entry 11)

Let $x$ be a nonzero complex number with $x \ne 1/k$ and $x \ne -1/k$ for every positive integer
$k$, and put $\varphi(x) = 1 + \sum_{k \ge 1} \frac{2}{(kx)^3 - kx}$. Then the series
$\sum_{k \ge 1} \frac{2}{(kx)^3 - kx}$ converges unconditionally, $\Gamma(1/x) \ne 0$,
$\Gamma(1 - 1/x) \ne 0$, and

$$\frac{\Gamma'(1/x)}{\Gamma(1/x)} + \frac{\Gamma'(1 - 1/x)}{\Gamma(1 - 1/x)} =
-2\gamma - x\,\varphi(x),$$

where $\gamma$ is the Euler–Mascheroni constant.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 8.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch8.Entry11Qgammafunctional.ramanujan_part1_ch8_entry11_qgammafunctional`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch8Entry11Qgammafunctional.lean, line 800](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch8Entry11Qgammafunctional.lean#L800). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/gamma-function/series-and-integrals-for-the-digamma-function/index.html#ramanujan-part1-ch8-entry11-qgammafuncti-2).

## Exponential and principal powers agree for positive bases (Chapter 8, Entry 12)

For a
complex number $x$ and a real number $u$, let $P_x(u) = 0$ if $u = 0$ and
$P_x(u) = e^{x \log |u|}$ otherwise. Then for every complex $x$ and every real $u > 0$,
$P_x(u) = u^x$, where $u^x$ is the principal complex power.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch8.Entry12Qgammaintegers.chapter8UnitPow_eq_cpow`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch8Entry12Qgammaintegers.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch8Entry12Qgammaintegers.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/gamma-function/series-and-integrals-for-the-digamma-function/index.html#chapter8-unit-pow-eq-cpow).

## Ramanujan's integral for $\varphi(x) - 1$ with principal powers (Chapter 8, Entry 12)

Let $x$ be a complex number with $\operatorname{Re} x > 1$. For real $u$ and complex $s$ put
$P_s(u) = 0$ if $u = 0$ and $P_s(u) = e^{s \log |u|}$ otherwise, and define $K_x(0) = 0$,
$K_x(1) = 0$ and $K_x(u) = \frac{P_{x-2}(u)\,(1 - u)^2}{1 - P_x(u)}$ for every other real $u$, the
quotient being taken to be $0$ at $u = -1$, where its denominator vanishes. Let
$\varphi(x) = 1 + \sum_{k \ge 1} \frac{2}{(kx)^3 - kx}$. Then $(kx)^3 - kx \ne 0$ for every
positive integer $k$; the series $\sum_{k \ge 1} \frac{2}{(kx)^3 - kx}$ converges
unconditionally; $K_x(0) = 0$ and $K_x(1) = 0$; for every $u \in (0, 1)$, with $u^x$ and
$u^{x-2}$ the principal complex powers, $1 - u^x \ne 0$ and
$K_x(u) = \frac{u^{x-2}\,(1 - u)^2}{1 - u^x}$; $K_x$ is integrable on $[0, 1]$; and

$$\int_0^1 K_x(u)\,du = \varphi(x) - 1.$$

For $u > 0$ the powers $P_s(u)$ and $u^s$ agree, so this is the same statement as the version
written with $P_s$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch8.Entry12Qgammaintegers.ramanujan_part1_ch8_entry12_qgammaintegers_cpow`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch8Entry12Qgammaintegers.lean, line 464](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch8Entry12Qgammaintegers.lean#L464). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/gamma-function/series-and-integrals-for-the-digamma-function/index.html#ramanujan-part1-ch8-entry12-qgammaintege).

## Ramanujan's integral for $\varphi(x) - 1$ (Chapter 8, Entry 12)

Let $x$ be a complex
number with $\operatorname{Re} x > 1$. For real $u$ and complex $s$ put $P_s(u) = 0$ if $u = 0$
and $P_s(u) = e^{s \log |u|}$ otherwise, and define $K_x(0) = 0$, $K_x(1) = 0$ and
$K_x(u) = \frac{P_{x-2}(u)\,(1 - u)^2}{1 - P_x(u)}$ for every other real $u$, the quotient being
taken to be $0$ at $u = -1$, where its denominator vanishes. Let
$\varphi(x) = 1 + \sum_{k \ge 1} \frac{2}{(kx)^3 - kx}$. Then $(kx)^3 - kx \ne 0$ for every
positive integer $k$; the series $\sum_{k \ge 1} \frac{2}{(kx)^3 - kx}$ converges
unconditionally; $K_x(0) = 0$ and $K_x(1) = 0$; for every $u \in (0, 1)$,
$1 - P_x(u) \ne 0$ and $K_x(u) = \frac{P_{x-2}(u)\,(1 - u)^2}{1 - P_x(u)}$; $K_x$ is integrable
on $[0, 1]$; and

$$\int_0^1 K_x(u)\,du = \varphi(x) - 1.$$

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 8.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch8.Entry12Qgammaintegers.ramanujan_part1_ch8_entry12_qgammaintegers`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch8Entry12Qgammaintegers.lean, line 516](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch8Entry12Qgammaintegers.lean#L516). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/gamma-function/series-and-integrals-for-the-digamma-function/index.html#ramanujan-part1-ch8-entry12-qgammaintege-2).

## Digamma as the logarithmic derivative of Gamma (used for Chapter 8, Entry 8)

For every
complex number $z$, $\Gamma'(z)/\Gamma(z) = \psi(z)$, where $\psi$ is the digamma function.

At the poles $z = 0, -1, -2, \dots$ the conventions $\Gamma(z) = 0$ and division by zero giving
$0$ make both sides $0$, so the identity holds for every $z$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch8.Entry8Digammaseries.chapter8Digamma_eq_Complex_digamma`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch8Entry8Digammaseries.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch8Entry8Digammaseries.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/gamma-function/series-and-integrals-for-the-digamma-function/index.html#chapter8-digamma-eq-complex-digamma).

## Alternating series $\sum_{k \ge 1} (-1)^{k-1}/(a + kb)$ via the digamma function

Let $a$
and $b$ be complex numbers with $b \ne 0$ and $a + kb \ne 0$ for every integer $k \ge 1$, and let
$\psi$ be the digamma function, the logarithmic derivative of $\Gamma$. Then the partial sums of
$\sum_{k=1}^{\infty} \frac{(-1)^{k-1}}{a + kb}$ converge to

$$\frac{1}{2b} \left(\psi\left(\frac{a+2b}{2b}\right) - \psi\left(\frac{a+b}{2b}\right)\right).$$

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch8.Entry8Digammaseries.ramanujan_part1_ch8_entry8_digammaseries_complex_digamma`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch8Entry8Digammaseries.lean, line 882](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch8Entry8Digammaseries.lean#L882). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/gamma-function/series-and-integrals-for-the-digamma-function/index.html#ramanujan-part1-ch8-entry8-digammaseries).

## Ramanujan's alternating digamma series (Chapter 8, Entry 8)

Let $a$ and $b$ be complex
numbers with $b \ne 0$ and $a + kb \ne 0$ for every integer $k \ge 1$, suppose that
$\Gamma\left(\frac{a+2b}{2b}\right) \ne 0$ and $\Gamma\left(\frac{a+b}{2b}\right) \ne 0$, and let
$\psi(z) = \Gamma'(z)/\Gamma(z)$. Then the partial sums of
$\sum_{k=1}^{\infty} \frac{(-1)^{k-1}}{a + kb}$ converge to

$$\frac{1}{2b} \left(\psi\left(\frac{a+2b}{2b}\right) - \psi\left(\frac{a+b}{2b}\right)\right).$$

Here $\Gamma$ takes the value $0$ at its poles $0, -1, -2, \dots$, so the two conditions on $\Gamma$
say that these arguments are not poles; they already follow from the condition on $a + kb$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 8.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch8.Entry8Digammaseries.ramanujan_part1_ch8_entry8_digammaseries`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch8Entry8Digammaseries.lean, line 899](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch8Entry8Digammaseries.lean#L899). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/gamma-function/series-and-integrals-for-the-digamma-function/index.html#ramanujan-part1-ch8-entry8-digammaseries-2).

## Digamma as the logarithmic derivative of Gamma (Chapter 8, Entry 9)

For every complex
number $z$, $\Gamma'(z)/\Gamma(z) = \psi(z)$, where $\Gamma'$ is the complex derivative of the
Gamma function and $\psi$ is the digamma function. At the poles of $\Gamma$ both sides are $0$ by
convention.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch8.Entry9Qgamma.chapter8Digamma_eq_digamma`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch8Entry9Qgamma.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch8Entry9Qgamma.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/gamma-function/series-and-integrals-for-the-digamma-function/index.html#chapter8-digamma-eq-digamma-2).

## The Entry 9 power function on positive reals (Chapter 8)

For a complex number $x$ and a
real number $u$, let $p_x(u) = e^{x \log\lvert u\rvert}$ if $u \ne 0$ and $p_x(0) = 0$. If $u > 0$,
then $p_x(u) = u^x$, the principal complex power of $u$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch8.Entry9Qgamma.chapter8UnitPow_eq_cpow`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch8Entry9Qgamma.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch8Entry9Qgamma.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/gamma-function/series-and-integrals-for-the-digamma-function/index.html#chapter8-unit-pow-eq-cpow-2).

## Ramanujan's integral for the digamma function (Chapter 8, Entry 9)

Let $x$ be a complex
number with $\operatorname{Re} x > 0$, and for real $u$ write $u^x = e^{x \log u}$ if $u > 0$ and
$0^x = 0$. Let $\psi$ be the digamma function. Then $x \ne 0$; the function
$u \mapsto u^x/(1 + u^x)$ is integrable on $[0, 1]$; $1 + u^x \ne 0$ for every $u \in [0, 1]$;
$\Gamma(1/(2x) + 1) \ne 0$ and $\Gamma(1/x + 1) \ne 0$; and

$$
\psi\Bigl(\frac{1}{2x} + 1\Bigr) = \psi\Bigl(\frac{1}{x} + 1\Bigr) - \log 2 +
x \int_0^1 \frac{u^x}{1 + u^x}\,du.
$$

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 8.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch8.Entry9Qgamma.ramanujan_part1_ch8_entry9_qgamma_digamma`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch8Entry9Qgamma.lean, line 1804](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch8Entry9Qgamma.lean#L1804). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/gamma-function/series-and-integrals-for-the-digamma-function/index.html#ramanujan-part1-ch8-entry9-qgamma-digamm).

## Ramanujan's integral for $\Gamma'/\Gamma$ (Chapter 8, Entry 9)

Let $x$ be a complex number
with $\operatorname{Re} x > 0$, and for real $u$ write $u^x = e^{x \log u}$ if $u > 0$ and
$0^x = 0$. Write $\Gamma'$ for the complex derivative of the Gamma function. Then $x \ne 0$; the
function $u \mapsto u^x/(1 + u^x)$ is integrable on $[0, 1]$; $1 + u^x \ne 0$ for every
$u \in [0, 1]$; $\Gamma(1/(2x) + 1) \ne 0$ and $\Gamma(1/x + 1) \ne 0$; and

$$
\frac{\Gamma'}{\Gamma}\Bigl(\frac{1}{2x} + 1\Bigr) =
\frac{\Gamma'}{\Gamma}\Bigl(\frac{1}{x} + 1\Bigr) - \log 2 + x \int_0^1 \frac{u^x}{1 + u^x}\,du.
$$

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 8.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch8.Entry9Qgamma.ramanujan_part1_ch8_entry9_qgamma`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch8Entry9Qgamma.lean, line 1835](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch8Entry9Qgamma.lean#L1835). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/gamma-function/series-and-integrals-for-the-digamma-function/index.html#ramanujan-part1-ch8-entry9-qgamma).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Series and integrals for the digamma function](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/gamma-function/series-and-integrals-for-the-digamma-function/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/special-functions/gamma-function/series-and-integrals-for-the-digamma-function)
