---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry13Bernoullipolyadd.ramanujan_part1_ch7_entry13_bernoullipolyadd, MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry13Bernoullirecurrence.ramanujan_part1_ch7_entry13_bernoullirecurrence, MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry14Bernoulliasymptotic.ramanujan_part1_ch7_entry14_bernoulliasymptotic, MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry14Bernoullipolymult.chapter7StieltjesA_eq_entry14Bernoulliasymptotic, MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry14Bernoullipolymult.summable_chapter7Entry14Term, MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry14Bernoullipolymult.chapter7StieltjesApprox_eq_entry13Bernoullipolyadd, MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry14Bernoullipolymult.ramanujan_part1_ch7_entry14_bernoullipolymult
statement: formalized
proof: formalized
---

# Stieltjes constants

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/stieltjes-constants/index.html).

## Stieltjes constants exist, and the zeroth is Euler's constant

There is exactly one sequence
of real numbers $(c_k)_{k \ge 0}$ such that, for every $k \ge 0$,

$$\sum_{j=1}^{m} \frac{(\log j)^k}{j} - \frac{(\log m)^{k+1}}{k+1} \longrightarrow c_k
  \quad (m \to \infty),$$

and $c_0 = \gamma$, where $\gamma$ is Euler's constant.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 7, Entry 13.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry13Bernoullipolyadd.ramanujan_part1_ch7_entry13_bernoullipolyadd`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch7Entry13Bernoullipolyadd.lean, line 301](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch7Entry13Bernoullipolyadd.lean#L301). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/stieltjes-constants/index.html#ramanujan-part1-ch7-entry13-bernoullipol).

## Laurent expansion of $\zeta$ at $s = 1$

Let $(c_k)_{k \ge 0}$ be real numbers such that,
for every $k \ge 0$, $\sum_{j=1}^{m} (\log j)^k / j - (\log m)^{k+1} / (k+1)$ tends to $c_k$ as
$m \to \infty$. Then for every complex $s \ne 1$ the series

$$\sum_{k=0}^{\infty} \frac{(-1)^k c_k}{k!} (s-1)^k$$

converges absolutely, and its sum is $\zeta(s) - \frac{1}{s-1}$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 7, Entry 13.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry13Bernoullirecurrence.ramanujan_part1_ch7_entry13_bernoullirecurrence`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch7Entry13Bernoullirecurrence.lean, line 1016](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch7Entry13Bernoullirecurrence.lean#L1016). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/stieltjes-constants/index.html#ramanujan-part1-ch7-entry13-bernoullirec).

## Expansion of $\sum 1/(n^{s+1} \log n)$ in the Stieltjes constants

Let $(c_k)_{k \ge 0}$ be
real numbers such that, for every $k \ge 0$,
$\sum_{j=1}^{m} (\log j)^k / j - (\log m)^{k+1} / (k+1)$ tends to $c_k$ as $m \to \infty$, and put
$A_k = (-1)^k c_k / k!$. Then the series $\sum_{n \ge 2} \frac{1}{n^2 \log n}$ and
$\sum_{k \ge 1} \frac{A_k}{k+1}$ converge absolutely, and for every real $s > 0$ the series
$\sum_{n \ge 2} \frac{1}{n^{s+1} \log n}$ and $\sum_{k \ge 1} \frac{A_k s^{k+1}}{k+1}$ converge
absolutely and

$$\sum_{n=2}^{\infty} \frac{1}{n^{s+1} \log n} = -\log s + C + (1 - \gamma) s
  - \sum_{k=1}^{\infty} \frac{A_k s^{k+1}}{k+1},$$

where $\gamma$ is Euler's constant and
$C = \sum_{n \ge 2} \frac{1}{n^2 \log n} - 1 + \gamma + \sum_{k \ge 1} \frac{A_k}{k+1}$.

Proof outline: the limits $c_k$ are the Stieltjes constants, and
$\zeta(1+s) - 1/s = \sum_{k \ge 0} A_k s^k$. Both sides are differentiated termwise in $s$, their
derivatives agree on $s > 0$, and the two sides agree at $s = 1$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 7.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry14Bernoulliasymptotic.ramanujan_part1_ch7_entry14_bernoulliasymptotic`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch7Entry14Bernoulliasymptotic.lean, line 536](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch7Entry14Bernoulliasymptotic.lean#L536). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/stieltjes-constants/index.html#ramanujan-part1-ch7-entry14-bernoulliasy).

## Two definitions of the normalized Stieltjes coefficients agree

For every real sequence
$(c_k)_{k \ge 0}$, the coefficients $A_k = (-1)^k c_k / k!$ defined for the asymptotic expansion of
$\sum 1/(n(n^x - 1))$ are, by definition, the coefficients $A_k$ used in the expansion of
$\sum 1/(n^{s+1} \log n)$ in the Stieltjes constants.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry14Bernoullipolymult.chapter7StieltjesA_eq_entry14Bernoulliasymptotic`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch7Entry14Bernoullipolymult.lean, line 518](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch7Entry14Bernoullipolymult.lean#L518). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/stieltjes-constants/index.html#chapter7-stieltjes-a-eq-entry14-bernoull).

## Convergence of $\sum 1/(n(n^x - 1))$

For every real $x > 0$ the series
$\sum_{n \ge 2} \frac{1}{n(n^x - 1)}$ converges absolutely.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry14Bernoullipolymult.summable_chapter7Entry14Term`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch7Entry14Bernoullipolymult.lean, line 538](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch7Entry14Bernoullipolymult.lean#L538). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/stieltjes-constants/index.html#summable-chapter7-entry14-term).

## Two definitions of the Stieltjes approximants agree

For all $k, m \ge 0$, the approximant
$\sum_{j=1}^{m} (\log j)^k / j - (\log m)^{k+1} / (k+1)$ defined for the asymptotic expansion of
$\sum 1/(n(n^x - 1))$ is, by definition, the approximant used for the existence of the Stieltjes
constants.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry14Bernoullipolymult.chapter7StieltjesApprox_eq_entry13Bernoullipolyadd`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch7Entry14Bernoullipolymult.lean, line 581](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch7Entry14Bernoullipolymult.lean#L581). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/stieltjes-constants/index.html#chapter7-stieltjes-approx-eq-entry13-ber).

## Asymptotic expansion of $\sum 1/(n(n^x - 1))$ as $x \to 0^+$

Let $a_0$ be a real number
such that $\sum_{n=2}^{m} \frac{1}{n \log n} - \log \log m$ tends to $a_0$ as $m \to \infty$, and
let $(c_k)_{k \ge 0}$ be real numbers such that, for every $k \ge 0$,
$\sum_{j=1}^{m} (\log j)^k / j - (\log m)^{k+1} / (k+1)$ tends to $c_k$ as $m \to \infty$. Then for
every real $x > 0$ the series $F(x) = \sum_{n \ge 2} \frac{1}{n(n^x - 1)}$ converges absolutely, and
for every $N \ge 0$,

$$F(x) = \frac{a_0 - \log x}{x} + \frac{1 - \gamma}{2}
  + \sum_{k=1}^{N} \frac{B_{2k}\, c_{2k-1}}{(2k)!} x^{2k-1} + O(x^{2N+1})
  \quad (x \to 0^+),$$

where $\gamma$ is Euler's constant and $B_{2k}$ are the Bernoulli numbers.

Proof: Truncated Laurent expansion of the exponential kernel, an exact partial-sum identity,
and a sum-versus-integral error bound, followed by passage to the defining limits.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 7.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry14Bernoullipolymult.ramanujan_part1_ch7_entry14_bernoullipolymult`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch7Entry14Bernoullipolymult.lean, line 1015](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch7Entry14Bernoullipolymult.lean#L1015). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/stieltjes-constants/index.html#ramanujan-part1-ch7-entry14-bernoullipol).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Stieltjes constants](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/stieltjes-constants/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/stieltjes-constants)
