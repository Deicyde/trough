---
declaration: lemma
origin: cited
lean: TileStructure.Forest.nontangential_operator_bound
statement: formalized
proof: formalized
---

# nontangential operator bound

For all bounded $f$ with bounded support and all ${\vartheta} \in {\Theta}$

$$
\|T_{\mathcal{N}}^{{\vartheta}} f\|_2 \le 2^{102a^3} \|f\|_2\,.
$$

## Depends on

- [Hardy–Littlewood](../../proof-of-metric-space-carleson-overview/hardy-littlewood.md)

## Proof

*Proof of nontangential operator bound.* Fix $s_1, s_2$. By [(4)](../../proof-of-metric-space-carleson-overview/README.md) we have for all $x \in (0, \infty)$

$$
\sum_{s = s_1}^{s_2} \psi(D^{-s}x) = 1 - \sum_{s < s_1} \psi(D^{-s}x) - \sum_{s > s_1} \psi(D^{-s}x)\,.
$$

Since $\psi$ is supported in $[\frac{1}{4D}, \frac{1}{2}]$, the two sums on the right hand side are zero for all $x \in [\frac{1}{2}D^{s_1-1}, \frac{1}{4} D^{s_2 - 1}]$, hence

$$
x \in [\frac{1}{2}D^{s_1-1}, \frac{1}{4} D^{s_2}] \implies \sum_{s = s_1}^{s_2} \psi(D^{-s}x) = 1\,.
$$

Since $\psi$ is supported in $[\frac{1}{4D}, \frac{1}{2}]$, we further have

$$
x \notin [\frac{1}{4}D^{s_1 - 1}, \frac{1}{2}D^{s_2}] \implies \sum_{s = s_1}^{s_2} \psi(D^{-s}x) = 0\,.
$$

Finally, since $\psi \ge 0$ and $\sum_{s \in \mathbb{Z}} \psi(D^{-s}x) = 1$, we have for all $x$

$$
0 \le \sum_{s = s_1}^{s_2} \psi(D^{-s}x) \le 1\,.
$$

Let $x' \in I_{s_1}(x)$ and suppose that $D^{s_2 - 1} \le R_Q({\vartheta}, x')$. By the triangle inequality and [(10)](../../proof-of-metric-space-carleson-overview/README.md), it holds that $\rho(x,x') \le 8D^{s_1}$. We have

$$
\Bigg|\sum_{s = s_1}^{s_2} \int K_s(x',y) f(y) \, \mathrm{d}\mu(y)\Bigg|
$$

$$
= \Bigg|\int \sum_{s = s_1}^{s_2} \psi(D^{-s}\rho(x',y)) K(x',y) f(y) \, \mathrm{d}\mu(y)\Bigg|
$$

$$
\le \Bigg| \int_{8D^{s_1} < \rho(x',y) \le \frac{1}{4}D^{s_2-1}} K(x',y) f(y) \, \mathrm{d}\mu(y) \Bigg|\qquad\text{(11)}
$$

$$
+ \int_{\frac{1}{4}D^{s_1-1} \le \rho(x',y) \le 8D^{s_1}} |K(x', y)| |f(y)| \, \mathrm{d}\mu(y)\qquad\text{(12)}
$$

$$
+ \int_{\frac{1}{4}D^{s_2-1} \le \rho(x',y) \le \frac{1}{2}D^{s_2}} |K(x', y)| |f(y)| \, \mathrm{d}\mu(y)\,.\qquad\text{(13)}
$$

The first term (11) is at most $2T_{{Q}}^{\vartheta} f(x)$, using with $R_1 := 8D^{s_1}$, $R_2 := \frac{1}{4}D^{s_2-1}$ and $R_1 < R_2 < R_{{Q}}({\vartheta},x')$ the triangle inequality in the form

$$
\left|\int_{R_1 < \rho(x',y) \le R_2} K(x',y) f(y) \, \mathrm{d}\mu(y) \right|
$$

$$
\le \left|\int_{R_1 < \rho(x',y) < R_{{Q}}({\vartheta},x')} K(x',y) f(y) \, \mathrm{d}\mu(y) \right|
$$

$$
+ \left|\int_{R_2 < \rho(x',y) < R_{{Q}}({\vartheta},x')} K(x',y) f(y) \, \mathrm{d}\mu(y) \right|.
$$

The other two terms will be estimated by the finitary maximal function from [Hardy–Littlewood](../../proof-of-metric-space-carleson-overview/hardy-littlewood.md). For the second term (12) we use [(14)](../../introduction/README.md) which implies that for all $y$ with $\rho(x', y) \ge \frac{1}{4}D^{s_1 - 1}$, we have

$$
|K(x', y)| \le \frac{2^{a^3}}{\mu(B(x', \frac{1}{4}D^{s_1 - 1}))}\,.
$$

Using $D=2^{100a^2}$ and the doubling property [(5)](../../introduction/README.md) $7 +100a^2$ times estimates the last display by

$$
\le \frac{2^{7a+101a^3}}{\mu(B(x', 32D^{s_1}))}\, .\qquad\text{(14)}
$$

By the triangle inequality and [(10)](../../proof-of-metric-space-carleson-overview/README.md), we have

$$
B(x', 8D^{s_1}) \subset B(c(I_{s_1}(x)), 16D^{s(I_{s_1}(x))}) \subset B(x', 32D^{s_1})\,.
$$

Combining this with (14), we conclude that (12) is at most

$$
2^{7a + 101a^3} M_{\mathcal{B},1} f(x)\,.
$$

For (13) we argue similarly. We have for all $y$ with $\rho(x', y) \ge \frac{1}{4}D^{s_2-1}$

$$
|K(x', y)| \le \frac{2^{a^3}}{\mu(B(x', \frac{1}{4}D^{s_2-1}))}\,.
$$

Using the doubling property [(5)](../../introduction/README.md) $7 + 100a^2$ times estimates the last display by

$$
\le \frac{2^{7a + 101a^3}}{\mu(B(x', 32 D^{s_2}))}\, .
$$

Note that by [(8)](../../proof-of-metric-space-carleson-overview/README.md) we have $I_{s_1}(x) \subset I_{s_2}(x)$, in particular $x' \in I_{s_2}(x)$. By the triangle inequality and [(10)](../../proof-of-metric-space-carleson-overview/README.md), we have

$$
B(x', 8D^{s_2}) \subset B(c(I_{s_2}(x)), 16D^{s(I_{s_2}(x))}) \subset B(x', 32D^{s_2})\,.
$$

Combining this, (13) is at most

$$
2^{7a+101a^3} M_{\mathcal{B},1} f(x)\,.
$$

Using $a \ge 4$, taking a supremum over all $x' \in I_{s_1}(x)$ and then a supremum over all $-S \le s_1 < s_2 \le S$, we obtain

$$
T_{\mathcal{N}} f(x) \le 2T_{{Q}}^{\vartheta} f(x) + 2^{102a^3} M_{\mathcal{B},1} f(x)\,.
$$

The lemma now follows from assumption [(22)](../../introduction/linearised-metric-carleson.md), [Hardy–Littlewood](../../proof-of-metric-space-carleson-overview/hardy-littlewood.md) and $a \ge 4$.

## Lean

Formalized as [`TileStructure.Forest.nontangential_operator_bound`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.nontangential_operator_bound).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 4713](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L4713)
