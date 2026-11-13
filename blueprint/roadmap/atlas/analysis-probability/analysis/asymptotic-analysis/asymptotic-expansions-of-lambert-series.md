---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry10Centralbinomialfull.summable_chapter6Entry14MinusTerm, MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry10Centralbinomialfull.chapter6Entry14MinusSum_error_le, MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry10Centralbinomialfull.ramanujan_part1_ch6_entry10_centralbinomialfull, MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry10Centralbinomialexpansion.summable_chapter6Entry14PlusTerm, MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry10Centralbinomialexpansion.ramanujan_part1_ch6_entry10_centralbinomialexpansion
statement: formalized
proof: formalized
---

# Asymptotic expansions of Lambert series

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansions-of-lambert-series/index.html).

## Entry10 Centralbinomialfull

## Summability of the Lambert series $\sum_k 1/(e^{kx}-1)$

For every real $x > 0$, the
series $\sum_{k=1}^{\infty} \frac{1}{e^{kx} - 1}$ is summable.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry10Centralbinomialfull.summable_chapter6Entry14MinusTerm`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch6Entry14LambertSeries.lean, line 1653](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch6Entry14LambertSeries.lean#L1653). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansions-of-lambert-series/index.html#summable-chapter6-entry14-minus-term).

## Remainder bound for the Lambert series $\sum_k 1/(e^{kx}-1)$

Let $x > 0$ be real and
let $n \ge 1$ be an integer. Let $S(x) = \sum_{k=1}^{\infty} \frac{1}{e^{kx} - 1}$, let $B_m$ be
the $m$-th Bernoulli number, let $\gamma$ be the Euler–Mascheroni constant, and let
$C_n(x) = \sum_{k=1}^{n} \frac{B_{2k}^2 \, x^{2k-1}}{2k \, (2k)!}$. Then
$\left| S(x) - \left( \frac{\gamma}{x} - \frac{\log x}{x} + \frac14 - C_n(x) \right) \right|
\le \frac{|B_{2n} B_{2n+2}| \, x^{2n}}{(2n)!}
\left( \frac{x^2}{4\pi^2} + \frac{\pi^2}{6} \right)$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry10Centralbinomialfull.chapter6Entry14MinusSum_error_le`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch6Entry14LambertSeries.lean, line 1659](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch6Entry14LambertSeries.lean#L1659). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansions-of-lambert-series/index.html#chapter6-entry14-minus-sum-error-le).

## Asymptotic expansion of the Lambert series $\sum_k 1/(e^{kx}-1)$

Let $x > 0$ be real
and let $n \ge 1$ be an integer. Let $B_m$ be the $m$-th Bernoulli number, let $\gamma$ be the
Euler–Mascheroni constant, and let
$C_n(x) = \sum_{k=1}^{n} \frac{B_{2k}^2 \, x^{2k-1}}{2k \, (2k)!}$. Then the series
$\sum_{k=1}^{\infty} \frac{1}{e^{kx} - 1}$ is summable, and its sum $S(x)$ satisfies
$\left| S(x) - \left( \frac{\gamma}{x} - \frac{\log x}{x} + \frac14 - C_n(x) \right) \right|
\le \frac{|B_{2n} B_{2n+2}| \, x^{2n}}{(2n)!} \left( \frac{x^2}{4\pi^2} + \frac{\pi^2}{6} \right)$.

The proof applies the Euler–Maclaurin formula to the smooth Mittag-Leffler kernel and bounds
the periodic Bernoulli remainder by its Fourier series.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 6.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry10Centralbinomialfull.ramanujan_part1_ch6_entry10_centralbinomialfull`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch6Entry14LambertSeries.lean, line 1679](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch6Entry14LambertSeries.lean#L1679). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansions-of-lambert-series/index.html#ramanujan-part1-ch6-entry10-centralbinom).

## Summability of the Lambert series $\sum_k 1/(e^{kx}+1)$

For every real $x > 0$, the
series $\sum_{k=1}^{\infty} \frac{1}{e^{kx} + 1}$ is summable.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry10Centralbinomialexpansion.summable_chapter6Entry14PlusTerm`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch6Entry14LambertSeries.lean, line 1761](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch6Entry14LambertSeries.lean#L1761). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansions-of-lambert-series/index.html#summable-chapter6-entry14-plus-term).

## Asymptotic expansion of the Lambert series $\sum_k 1/(e^{kx}+1)$

Let $x > 0$ be real
and let $n \ge 1$ be an integer. Let $B_m$ be the $m$-th Bernoulli number and let
$D_n(x) = \sum_{k=1}^{n} \frac{(2^{2k} - 1) \, B_{2k}^2 \, x^{2k-1}}{2k \, (2k)!}$. Then the
series $\sum_{k=1}^{\infty} \frac{1}{e^{kx} + 1}$ is summable, and its sum $T(x)$ satisfies
$\left| T(x) - \left( \frac{\log 2}{x} - \frac14 + D_n(x) \right) \right|
\le \frac{|B_{2n} B_{2n+2}| \, x^{2n}}{(2n)!} \left( \frac{x^2}{4\pi^2} + \frac{\pi^2}{6} +
2^{2n+1} \left( \frac{x^2}{\pi^2} + \frac{\pi^2}{6} \right) \right)$.

The proof writes this series as the series $\sum_k 1/(e^{kx}-1)$ minus twice the same series
at $2x$, and applies the remainder bound for $\sum_k 1/(e^{kx}-1)$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 6.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry10Centralbinomialexpansion.ramanujan_part1_ch6_entry10_centralbinomialexpansion`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch6Entry14LambertSeries.lean, line 1826](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch6Entry14LambertSeries.lean#L1826). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansions-of-lambert-series/index.html#ramanujan-part1-ch6-entry10-centralbinom-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Asymptotic expansions of Lambert series](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansions-of-lambert-series/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/asymptotic-analysis/asymptotic-expansions-of-lambert-series)
