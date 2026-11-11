---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry10Example1SqrtPoissonAsymptotic.ramanujan_part1_ch3_entry10_example1_sqrt_poisson_asymptotic, MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry10Example1SummableEventually.ramanujan_part1_ch3_entry10_example1_summable_eventually, MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry10Example1SumPositiveEventually.ramanujan_part1_ch3_entry10_example1_sum_positive_eventually, MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry10Example2LogPoissonAsymptotic.ramanujan_part1_ch3_entry10_example2_log_poisson_asymptotic, MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry10Example2Summable.ramanujan_part1_ch3_entry10_example2_summable, MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry10Example4Summable.ramanujan_part1_ch3_entry10_example4_summable, MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry10Example4HarmonicPoissonAsymptotic.ramanujan_part1_ch3_entry10_example4_harmonic_poisson_asymptotic, MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry10PoissonAsymptotic.twoAssocStirlingSecond
statement: formalized
proof: formalized
---

# Asymptotic expansion of Poisson averages

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansion-of-poisson-averages/index.html).

## Logarithmic asymptotics of the square-root Poisson series

For real $x$ let
$S(x) = \sum_{k=1}^{\infty} x^k \sqrt{k} / k!$. Then, as $x \to \infty$,

$$\log S(x) = x + \tfrac{1}{2} \log x - \frac{1}{8x} - \frac{1}{16 x^2} + O\left(x^{-3}\right).$$

## Sources

- Berndt, Ramanujan's Notebooks Part I, Chapter 3, Entry 10, Example 1, printed p. 64 / PDF p. 74.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry10Example1SqrtPoissonAsymptotic.ramanujan_part1_ch3_entry10_example1_sqrt_poisson_asymptotic`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry10Example1SqrtPoissonAsymptotic.lean, line 822](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry10Example1SqrtPoissonAsymptotic.lean#L822). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansion-of-poisson-averages/index.html#ramanujan-part1-ch3-entry10-example1-sqr).

## Eventual summability of the square-root Poisson series

For all sufficiently large
real $x$, the series $\sum_{k=1}^{\infty} x^k \sqrt{k} / k!$ is summable.

## Sources

- Berndt, Ramanujan's Notebooks Part I, Chapter 3, Entry 10, Example 1, printed p. 64 / PDF p. 74.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry10Example1SummableEventually.ramanujan_part1_ch3_entry10_example1_summable_eventually`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry10Example1SummableEventually.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry10Example1SummableEventually.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansion-of-poisson-averages/index.html#ramanujan-part1-ch3-entry10-example1-sum-2).

## Eventual positivity of the square-root Poisson series

For all sufficiently large
real $x$, the sum $\sum_{k=1}^{\infty} x^k \sqrt{k} / k!$ is strictly positive.

## Sources

- Berndt, Ramanujan's Notebooks Part I, Chapter 3, Entry 10, Example 1, printed p. 64 / PDF p. 74.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry10Example1SumPositiveEventually.ramanujan_part1_ch3_entry10_example1_sum_positive_eventually`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry10Example1SumPositiveEventually.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry10Example1SumPositiveEventually.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansion-of-poisson-averages/index.html#ramanujan-part1-ch3-entry10-example1-sum).

## Asymptotics of the logarithmic Poisson series

There are real constants $C > 0$ and
$x_0$ such that for every real $x \ge x_0$ the series $\sum_{k=1}^{\infty} x^k \log(k + 1) / k!$
has a sum $S$ satisfying

$$\left| e^{-x} S - \log x - \frac{1}{2x} - \frac{1}{12 x^2} \right| \le \frac{C}{x^3}.$$

## Sources

- Berndt, Ramanujan's Notebooks Part I, Chapter 3, Entry 10, Example 2, printed p. 65 / PDF p. 75.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry10Example2LogPoissonAsymptotic.ramanujan_part1_ch3_entry10_example2_log_poisson_asymptotic`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry10Example2LogPoissonAsymptotic.lean, line 987](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry10Example2LogPoissonAsymptotic.lean#L987). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansion-of-poisson-averages/index.html#ramanujan-part1-ch3-entry10-example2-log).

## Summability of the logarithmic Poisson series

For every real $x$, the series
$\sum_{k=1}^{\infty} e^{-x} x^k \log(k + 1) / k!$ is summable.

## Sources

- Berndt, Ramanujan's Notebooks Part I, Chapter 3, Entry 10, Example 2, printed p. 65 / PDF p. 75.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry10Example2Summable.ramanujan_part1_ch3_entry10_example2_summable`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry10Example2Summable.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry10Example2Summable.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansion-of-poisson-averages/index.html#ramanujan-part1-ch3-entry10-example2-sum).

## Summability of the harmonic Poisson series

Let $H_k = \sum_{j=1}^{k} 1/j$ be the $k$-th
harmonic number (so $H_0 = 0$). For every real $x$, the series
$\sum_{k=0}^{\infty} e^{-x} x^k H_k / k!$ is summable.

## Sources

- Berndt, Ramanujan's Notebooks Part I, Chapter 3, Entry 10, Example 4, printed pp. 65-66 / PDF pp. 75-76.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry10Example4Summable.ramanujan_part1_ch3_entry10_example4_summable`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry10Example4Summable.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry10Example4Summable.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansion-of-poisson-averages/index.html#ramanujan-part1-ch3-entry10-example4-sum).

## Asymptotics of the harmonic Poisson series

Let $H_k = \sum_{j=1}^{k} 1/j$ be the $k$-th
harmonic number (so $H_0 = 0$) and let $\gamma$ be the Euler–Mascheroni constant. Then, as
$x \to \infty$,

$$e^{-x} \sum_{k=0}^{\infty} \frac{x^k H_k}{k!} = \log x + \gamma + O\left(\frac{1}{x}\right).$$

## Sources

- Berndt, Ramanujan's Notebooks Part I, Chapter 3, Entry 10, Example 4, printed pp. 65-66 / PDF pp. 75-76.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry10Example4HarmonicPoissonAsymptotic.ramanujan_part1_ch3_entry10_example4_harmonic_poisson_asymptotic`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry10Example4HarmonicPoissonAsymptotic.lean, line 688](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry10Example4HarmonicPoissonAsymptotic.lean#L688). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansion-of-poisson-averages/index.html#ramanujan-part1-ch3-entry10-example4-har).

## 2-associated Stirling numbers in Ramanujan's Entry 10

For natural numbers $n$ and $k$,
$S_2(n, k)$ is the integer $\sum_{j=0}^{k} (-1)^j \binom{n}{j} S(n - j, k - j)$, where $S$
denotes the Stirling numbers of the second kind.

$S_2(n, k)$ is the number of partitions of an $n$-element set into $k$ blocks, each containing at
least two elements.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry10PoissonAsymptotic.twoAssocStirlingSecond`, a definition declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry10PoissonAsymptotic.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry10PoissonAsymptotic.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansion-of-poisson-averages/index.html#two-assoc-stirling-second).

## The Entry 10 Stirling numbers are the 2-associated Stirling numbers

For all natural
numbers $n$ and $k$, the integer $\sum_{j=0}^{k} (-1)^j \binom{n}{j} S(n - j, k - j)$ used in
Ramanujan's Entry 10, where $S$ denotes the Stirling numbers of the second kind, equals the
2-associated Stirling number of the second kind $S_2(n, k)$.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry10PoissonAsymptotic.twoAssocStirlingSecond_eq_canonical`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry10PoissonAsymptotic.lean, line 762](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry10PoissonAsymptotic.lean#L762). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansion-of-poisson-averages/index.html#two-assoc-stirling-second-eq-canonical).

## Ramanujan's asymptotic expansion of Poisson averages

Let $M \ge 1$ be an integer,
$\varphi : \mathbb{R} \to \mathbb{C}$ and $G : \mathbb{R} \to \mathbb{R}$ functions, $A \ge 1$ a
real number and $F$ a finite set of natural numbers. Write $\varphi^{(n)}$ for the $n$-th
iterated derivative of $\varphi$ and $S_2(n, k)$ for the 2-associated Stirling numbers of the
second kind. Assume that there are $C \ge 0$ and $p \in \mathbb{N}$ such that
$|\varphi(x)| \le C x^p$ and $|G(x)| \le C x^p$ for all sufficiently large $x$; that $G(x) \ge 1$
for all sufficiently large $x$; and that for every integer $m \ge 1$ and all sufficiently large
$x$, the derivatives $\varphi^{(0)}, \dots, \varphi^{(m-1)}$ are differentiable at $x$ and
$|\varphi^{(m)}(x)| / m! \le G(x) (A / x)^m$. Then, as $x \to \infty$,

$$e^{-x} \sum_{j \in \mathbb{N} \setminus F} \frac{x^j}{j!} \varphi(j) - \varphi(x) -
\sum_{k=2}^{M} \sum_{n=k}^{2k-2} S_2(n, n + 1 - k) \, x^{n-k+1} \frac{\varphi^{(n)}(x)}{n!}
= O\left(\frac{G(x)}{x^M}\right).$$

Proof: Taylor expansion on the central Poisson range is combined with the associated-Stirling
central-moment identity from Comtet; Berndt's route and even-moment tails control the remainder.

## Sources

- Berndt, Ramanujan's Notebooks Part I, Chapter 3, Entry 10, printed pp. 57-58 / PDF pp. 67-68.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry10PoissonAsymptotic.ramanujan_part1_ch3_entry10_poisson_asymptotic`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry10PoissonAsymptotic.lean, line 1981](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry10PoissonAsymptotic.lean#L1981). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansion-of-poisson-averages/index.html#ramanujan-part1-ch3-entry10-poisson-asym).

## Eventual summability of the series in Entry 10

Let $\varphi : \mathbb{R} \to \mathbb{C}$
be polynomially bounded at infinity, that is, there are a real number $C \ge 0$ and a natural
number $p$ such that $|\varphi(x)| \le C x^p$ for all sufficiently large real $x$. Let $F$ be a
finite set of natural numbers. Then for all sufficiently large real $x$, the family indexed by
the natural numbers $j$ whose $j$-th term is $0$ for $j \in F$ and $x^j \varphi(j) / j!$ for
$j \notin F$ is summable.

## Sources

- Berndt, Ramanujan's Notebooks Part I, Chapter 3, Entry 10, printed pp. 57-58 / PDF pp. 67-68.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry10PoissonSummable.ramanujan_part1_ch3_entry10_poisson_summable`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry10PoissonSummable.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry10PoissonSummable.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansion-of-poisson-averages/index.html#ramanujan-part1-ch3-entry10-poisson-summ).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Asymptotic expansion of Poisson averages](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansion-of-poisson-averages/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/asymptotic-analysis/asymptotic-expansion-of-poisson-averages)
