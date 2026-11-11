---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry1Powersum.ramanujan_part1_ch7_entry1_powersum, MathlibExt.Analysis.Ramanujan.Part1Ch8.Entry19Gaussdigamma.ramanujan_part1_ch8_entry19_gaussdigamma, MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry27Clausen.ramanujan_part1_ch9_entry27_clausen
statement: formalized
---

# Asymptotic expansions of power sums

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansions-of-power-sums/index.html).

## Ramanujan's asymptotic expansion of power sums

Let $r \in \mathbb{C}$ with $r \ne -1$,
and let $N$ be a positive integer with $\mathrm{Re}\, r < 2N$. For natural $n$ put
$A_N(n) = \zeta(-r) + \frac{n^{r+1}}{r+1} + \frac{n^r}{2} + \sum_{k=1}^{N} T_k(n)$, where
$T_k(n) = \frac{B_{2k}}{(2k)!}\, r(r-1)\cdots(r-2k+2)\, n^{r-2k+1}$ (a product of $2k - 1$
factors), $\zeta$ is the Riemann zeta function, $B_{2k}$ are the Bernoulli numbers and complex
powers are principal. Then $\sum_{k=1}^{n} k^r - A_N(n) = O(n^{\mathrm{Re}\, r - 2N})$ as
$n \to \infty$.

Proof: Euler--Maclaurin gives the expansion with an integrable periodic-kernel tail. The constant is
identified with the Riemann zeta function first in its convergent half-plane, then everywhere needed
by analytic continuation.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 7, Entry 1.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry1Powersum.ramanujan_part1_ch7_entry1_powersum`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch7Entry1Powersum.lean, line 1049](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch7Entry1Powersum.lean#L1049). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansions-of-power-sums/index.html#ramanujan-part1-ch7-entry1-powersum).

## Ramanujan's asymptotic expansion of a binomial combination of log-power sums

For natural
numbers $m$ and $x$ let $S_m(x) = \sum_{k=1}^{x} (\log k)^m$, let $c_m = (-1)^m \zeta^{(m)}(0)$,
where $\zeta^{(m)}(0)$ is the $m$-th derivative at $0$ of the real function
$s \mapsto \operatorname{Re} \zeta(s)$, and let $\psi_m(x) = S_m(x) - c_m$. Let $n$ be a natural
number. Then for every $m \le n$,

$$S_m(x) - \int_1^x (\log t)^m \, dt - \frac{(\log x)^m}{2} + (-1)^{m+1} m! \to c_m$$

as $x \to \infty$ through the natural numbers, and

$$\sum_{k=0}^{n} (-1)^{n+k} \binom{n}{k} (\log x)^k \psi_{n-k}(x) = n! \, x -
\frac{B_{n+1}}{(n+1) x^n} - \frac{n B_{n+2}}{2 (n+2) x^{n+1}} -
\frac{n (n + 5/3) B_{n+3}}{8 (n+3) x^{n+2}} + O\left(\frac{1}{x^{n+3}}\right)$$

as $x \to \infty$ through the natural numbers, where $B_j$ are the Bernoulli numbers with
$B_1 = -1/2$.

Proof: Analytic continuation of ζ to `re s > -1` by Euler–Maclaurin, Cauchy estimates for the
remainder's derivatives, and the Euler–Maclaurin tail expansion of the log-power sums.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 8.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch8.Entry19Gaussdigamma.ramanujan_part1_ch8_entry19_gaussdigamma`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch8Entry19Gaussdigamma.lean, line 2236](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch8Entry19Gaussdigamma.lean#L2236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansions-of-power-sums/index.html#ramanujan-part1-ch8-entry19-gaussdigamma).

## Asymptotic expansion of partial sums of powers times logarithms

Let $r > -1$ be a real
number. For a natural number $n$ write $\varphi_r(n) = \sum_{k=1}^{n} k^r \log k$ and
$S_r(n) = \sum_{k=1}^{n} k^r$, and for a natural number $m$ let
$D_m(r) = \sum_{j=0}^{m} \prod_{0 \le q \le m,\ q \ne j} (r - q)$, the derivative of
$r(r-1)\cdots(r-m)$ with respect to $r$. Let $B_j$ be the Bernoulli numbers and $\zeta$ the Riemann
zeta function. Then there is a real constant $C$ such that for every natural number $N$, as
$n \to \infty$ through the natural numbers,

$$
\varphi_r(n) - \log n \, \bigl(S_r(n) - \zeta(-r)\bigr) = C - \frac{n^{r+1}}{(r+1)^2} +
\sum_{k=1}^{N} \frac{B_{2k}}{(2k)!} D_{2k-2}(r) \, n^{r-2k+1} + O\bigl(n^{r-2N-1}\bigr).
$$

Moreover, if $r > 0$, then $\Gamma(r+1) > 0$, the series $\sum_{n \ge 1} \log n / n^{r+1}$
converges, and

$$
C = \frac{2\Gamma(r+1)\zeta(r+1)}{(2\pi)^{r+1}} \Bigl(\sin\frac{\pi r}{2} \Bigl(\log(2\pi) -
\frac{\Gamma'(r+1)}{\Gamma(r+1)}\Bigr) - \frac{\pi}{2} \cos\frac{\pi r}{2}\Bigr) +
\frac{2\Gamma(r+1)\sin\frac{\pi r}{2}}{(2\pi)^{r+1}} \sum_{n=1}^{\infty} \frac{\log n}{n^{r+1}}.
$$

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 9.

Stated but not proved: `MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry27Clausen.ramanujan_part1_ch9_entry27_clausen` is written with `theorem_wanted` in [WantedExt/Analysis/Ramanujan/Part1Ch9Wanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Ramanujan/Part1Ch9Wanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansions-of-power-sums/index.html#ramanujan-part1-ch9-entry27-clausen).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Asymptotic expansions of power sums](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansions-of-power-sums/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/asymptotic-analysis/asymptotic-expansions-of-power-sums)
