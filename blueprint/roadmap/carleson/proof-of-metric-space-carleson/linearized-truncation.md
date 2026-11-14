---
declaration: lemma
origin: cited
lean: linearized_truncation
statement: formalized
proof: formalized
---

# linearized truncation

Let $\sigma_1,\sigma_2\colon X\to \mathbb{Z}$ be measurable functions with finite range and $\sigma_1\leq \sigma_2$. Then we have

$$
\int \mathbf{1}_{G}(x)
\left| {T}_{2,\sigma_1,\sigma_2}f(x)\right|\, d\mu(x)
\le \frac{2^{442a^3+2}}{(q-1)^6} \mu(G)^{1-\frac{1}{q}} \mu(F)^{\frac{1}{q}},\qquad\text{(9)}
$$

with

$$
{T}_{2,\sigma_1,\sigma_2}f(x)=\sum_{\sigma_1(x) \le s\le \sigma_2(x)}
\int K_s(x,y) f(y) e({Q}(x)(y)) \, \mathrm{d}\mu(y)\,.\qquad\text{(10)}
$$

## Depends on

- [finitary Carleson](../proof-of-metric-space-carleson-overview/finitary-carleson.md)

## Proof

*Proof of linearized truncation.* Fix $\sigma_1$, $\sigma_2$ and ${Q}$ as in the lemma. Applying [finitary Carleson](../proof-of-metric-space-carleson-overview/finitary-carleson.md) recursively, we obtain a sequence of sets $G_n$ with $G_0=G$ and, for each $n\ge 0$, $G_{n+1} \subset G_n$, $\mu(G_{n})\le 2^{-n} \mu(G)$ and

$$
\int \mathbf{1}_{G_{n}\setminus G_{n+1}}(x)
\left| {T}_{2,\sigma_1,\sigma_2} f(x) \right|\, d\mu(x)
$$

$$
\le \frac{2^{442a^3}}{(q-1)^5} \mu(G_n)^{1 - \frac{1}{q}} \mu(F)^{\frac{1}{q}}.
$$

Adding the first $n$ of these inequalities, we obtain by bounding a geometric series

$$
\int \mathbf{1}_{G\setminus G_{n}}(x)
\left| {T}_{2,\sigma_1,\sigma_2}f(x) \right|\, d\mu(x)
\le \frac{2^{442a^3+2}}{(q-1)^6} \mu(G)^{1-\frac{1}{q}} \mu(F)^{\frac{1}{q}}.\qquad\text{(11)}
$$

As the integrand is non-negative and non-decreasing in $n$, we obtain by the monotone convergence theorem

$$
\int \mathbf{1}_{G}(x)
\left| {T}_{2,\sigma_1,\sigma_2}f(x) \right|\, d\mu(x)
\le \frac{2^{442a^3+2}}{(q-1)^6} \mu(G)^{1-\frac{1}{q}} \mu(F)^{\frac{1}{q}}.\qquad\text{(12)}
$$

This completes the proof of linearized truncation and thus [metric space Carleson](../introduction/metric-space-carleson.md).

## Lean

Formalized as [`linearized_truncation`](https://fpvandoorn.github.io/carleson/docs/find/#doc/linearized_truncation).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 1179](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L1179)
