---
declaration: section
origin: cited
lean: MetaMathlibExt.franel_landau, MetaMathlibExt.zeta_three_infinite_product_formulas, MathlibExt.NumberTheory.LagariasWanted.NumberTheory.riemann_hypothesis_iff_lagarias_elementary_criterion, meromorphicOn_riemannZeta, MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry2Faulhaber.ramanujan_part1_ch7_entry2_faulhaber
statement: formalized
---

# Riemann zeta function: its own results

5 results, 3 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/index.html).

Continuation and zeros of ζ, zero-free regions, moments and subconvexity, RH criteria (Robin, Lagarias), de Bruijn–Newman constant, zeta values.

## Franel–Landau theorem

For a natural number $N$, let
$F_N(0) < F_N(1) < \dots < F_N(L_N - 1)$ be the terms of the Farey sequence of order $N$, and for
$k < L_N$ let $\delta_{N,k} = F_N(k) - k/(L_N - 1)$. The Riemann hypothesis holds if and only if
for every real $\varepsilon > 0$,
$\sum_{k=0}^{L_N - 1} \delta_{N,k}^2 = O(N^{-1+\varepsilon})$ as $N \to \infty$.

## Sources

- https://en.wikipedia.org/wiki/Farey_sequence.

Stated but not proved: `MetaMathlibExt.franel_landau` is written with `theorem_wanted` in [WantedExt/NumberTheory/FranelLandauTheoremWanted.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FranelLandauTheoremWanted.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/index.html#franel-landau).

## Kachi–Tzermias infinite products for $\zeta(3)$

Let $\zeta$ be the Riemann zeta function
and, for $n \ge 1$, put $a_n = \left(1 - \frac{1}{n+1}\right)^{(-1)^n n(n+1)/2}$. Then, as
$m \to \infty$,

$$\prod_{n=1}^{2m+1} e^{-1/4} a_n \to \exp\left(\frac{7\zeta(3)}{4\pi^2} + \frac{1}{4}\right),
\qquad \prod_{n=1}^{2m} e^{1/4} a_n \to \exp\left(\frac{7\zeta(3)}{4\pi^2} - \frac{1}{4}\right),$$

and

$$\left(\prod_{n=1}^{m} \frac{(2n)^{(2n)^2}}{(2n-1)^{(2n-1)^2}}\right)^4
\left(\frac{(2m+2)^{4m+5}}{(2m+1)^{12m+9}}\right)^m \to \exp\left(\frac{7\zeta(3)}{\pi^2}\right).$$

## Sources

- Yasuyuki Kachi and Pavlos Tzermias, "Infinite Products Involving zeta(3) and Catalan's Constant," Journal of Integer Sequences 15 (2012), Article 12.9.4, Proposition `zeta3`, equations `zeta3i`–`zeta3iii`, lines 124–144, <https://cs.uwaterloo.ca/journals/JIS/VOL15/Tzermias/tzermias2.tex>.

Formalized by `MetaMathlibExt.zeta_three_infinite_product_formulas`, a theorem declared in [MathlibExt/NumberTheory/ZetaThreeProductFormulas.lean, line 1364](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ZetaThreeProductFormulas.lean#L1364). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/index.html#zeta-three-infinite-product-formulas).

## Lagarias' elementary criterion for the Riemann hypothesis

The Riemann hypothesis holds
(every zero $s$ of the Riemann zeta function with $s \ne 1$ that is not one of the trivial zeros
$-2, -4, -6, \dots$ has real part $1/2$) if and only if, for every positive integer $n$,

$$\sigma(n) \le H_n + e^{H_n} \log H_n,$$

where $\sigma(n)$ is the sum of the positive divisors of $n$ and $H_n = \sum_{k=1}^{n} 1/k$ is
the $n$-th harmonic number.

## Sources

- https://arxiv.org/abs/math/0008177. Problem `riemann_hypothesis_iff_lagarias_elementary_criterion` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.NumberTheory.LagariasWanted.NumberTheory.riemann_hypothesis_iff_lagarias_elementary_criterion` is written with `theorem_wanted` in [WantedExt/NumberTheory/LagariasWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LagariasWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/index.html#riemann-hypothesis-iff-lagarias-elementa).

## Meromorphy of the Riemann zeta function

The Riemann zeta function $\zeta$ is
meromorphic on all of $\mathbb{C}$.

Formalized by `meromorphicOn_riemannZeta`, a theorem declared in [MathlibExt/NumberTheory/LSeries/RiemannZeta.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/LSeries/RiemannZeta.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/index.html#meromorphic-on-riemann-zeta).

## Ramanujan's formula for the alternating zeta function at $-r$

Let
$\eta(s) = (1 - 2^{1-s})\,\zeta(s)$ for $s \ne 1$ and $\eta(1) = \log 2$, where $\zeta$ is the
Riemann zeta function, and let $B^*(z) = 2\,\Gamma(z + 1)\,\zeta(z) / (2\pi)^z$. Then for every
$s \in \mathbb{C}$ with $\mathrm{Re}\, s > 0$ the partial sums $\sum_{j=0}^{N-1} (-1)^j / (j+1)^s$
tend to $\eta(s)$ as $N \to \infty$; the functions $r \mapsto \eta(-r)$ and
$r \mapsto (2^{r+1} - 1)\, B^*(r + 1) \sin(\pi r/2) / (r + 1)$ are meromorphic on $\mathbb{C}$;
and these two functions agree outside a closed discrete subset of $\mathbb{C}$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 7.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry2Faulhaber.ramanujan_part1_ch7_entry2_faulhaber`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch7Entry2Faulhaber.lean, line 1080](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch7Entry2Faulhaber.lean#L1080). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/index.html#ramanujan-part1-ch7-entry2-faulhaber).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Riemann zeta function](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/zeta-l-functions/riemann-zeta)
