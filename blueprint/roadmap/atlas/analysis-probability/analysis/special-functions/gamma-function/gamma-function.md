---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Ramanujan.Part1Ch8.Entry15Doublegamma.ramanujan_part1_ch8_entry15_doublegamma, MathlibExt.Analysis.Ramanujan.Part1Ch8.Entry17Loggammaintegral.ramanujan_part1_ch8_entry17_loggammaintegral
statement: formalized
proof: formalized
---

# Gamma and digamma functions: its own results

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/gamma-function/index.html).

The gamma, digamma and trigamma functions: series and integral representations, factorial series, growth bounds against exponentials, and Ramanujan's digamma identities.

## Ramanujan's asymptotic expansion of $((x + 1/2)/e^{\psi(x+1)})^{4n}$

For real $x$ let
$\psi(x) = \Gamma'(x)/\Gamma(x)$ and $a(x) = e^{\psi(x+1)}$. Then $a(x) \to \infty$ as
$x \to \infty$, and for every complex number $n$,

$$\left(\frac{x + 1/2}{a(x)}\right)^{4n} = 1 - \frac{n}{6 a(x)^2} +
\frac{10 n^2 + 11 n}{720 a(x)^4} - \frac{70 n^3 + 231 n^2 + 891 n}{90720 a(x)^6} +
O\left(\frac{1}{a(x)^8}\right)$$

as $x \to \infty$ through the real numbers, where the power is the principal complex power.

Proof: Convexity of `log Γ` gives crude digamma bounds. A telescoped centered expansion and
Taylor's formula for the complex exponential then give the stated coefficients and remainder.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 8.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch8.Entry15Doublegamma.ramanujan_part1_ch8_entry15_doublegamma`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch8Entry15Doublegamma.lean, line 959](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch8Entry15Doublegamma.lean#L959). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/gamma-function/index.html#ramanujan-part1-ch8-entry15-doublegamma).

## Ramanujan's multiplication formula for the series $\sum_k (\log k/k - \log(k+x)/(k+x))$

For real $x$ let

$$\varphi(x) = \sum_{k=1}^{\infty} \left(\frac{\log k}{k} - \frac{\log(k+x)}{k+x}\right),$$

and let $\psi(x) = \Gamma'(x)/\Gamma(x)$. Let $x > -1$ be real and let $n \ge 1$ be an integer.
Then $k + x > 0$ and $k + (x - j)/n > 0$ for all integers $k \ge 1$ and $0 \le j < n$; the series
defining $\varphi(x)$ and $\varphi((x - j)/n)$ for $0 \le j < n$ converge absolutely;
$\Gamma(x + 1) > 0$; and

$$n \varphi(x) - \sum_{j=0}^{n-1} \varphi\left(\frac{x - j}{n}\right) =
n \log n \, \psi(x + 1) - \frac{n (\log n)^2}{2}.$$

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 8.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch8.Entry17Loggammaintegral.ramanujan_part1_ch8_entry17_loggammaintegral`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch8Entry17Loggammaintegral.lean, line 1407](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch8Entry17Loggammaintegral.lean#L1407). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/gamma-function/index.html#ramanujan-part1-ch8-entry17-loggammainte).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Gamma and digamma functions](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/gamma-function/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/special-functions/gamma-function)
