---
declaration: lemma
origin: cited
lean: Tile.correlation_le, Tile.correlation_zero_of_ne_subset
statement: formalized
proof: formalized
---

# tile correlation

Let ${\mathfrak p}, {\mathfrak p}'\in {\mathfrak P}$ with ${\mathrm{s}}({{\mathfrak p}'})\leq {\mathrm{s}}({{\mathfrak p}})$. Then

$$
\left|\int T^*_{{\mathfrak p}'}g\overline{T^*_{{\mathfrak p}}g}\right|\qquad\text{(19)}
$$

$$
\le 2^{232a^3}\frac{(1+d_{{\mathfrak p}'}({\mathcal{Q}}({\mathfrak p}'), {\mathcal{Q}}({\mathfrak p}))^{-1/(2a^2+a^3)}}{\mu({\mathcal{I}}({\mathfrak p}))}\int_{E({\mathfrak p}')}|g|\int_{E({\mathfrak p})}|g|\,.
$$

Moreover, the term (19) vanishes unless

$$
{\mathcal{I}}({\mathfrak p}') \subset B({\mathrm{c}}({\mathfrak p}), 14D^{{\mathrm{s}}({\mathfrak p})})\, .
$$

## Depends on

- [Holder van der Corput](../proof-of-metric-space-carleson-overview/holder-van-der-corput.md)
- [correlation kernel bound](correlation-kernel-bound.md)
- [tile-uncertainty](tile-uncertainty.md)
- [tile range support](tile-range-support.md)

## Proof

*Proof of tile correlation.* We begin with (19). By Lemma [tile range support](tile-range-support.md), the left-hand side of (19) vanishes if $B({\mathrm{c}}({\mathfrak p}'),5D^{{\mathrm{s}}({\mathfrak p}')}) \cap B({\mathrm{c}}({\mathfrak p}),5D^{{\mathrm{s}}({\mathfrak p})}) = \emptyset$. Thus we can assume for the remainder of the proof that

$$
B({\mathrm{c}}({\mathfrak p}'),5D^{{\mathrm{s}}({\mathfrak p}')}) \cap B({\mathrm{c}}({\mathfrak p}),5D^{{\mathrm{s}}({\mathfrak p})}) \neq \emptyset\,.\qquad\text{(20)}
$$

We expand the left-hand side of (19) as

$$
\left|\int \int_{E({\mathfrak p}')} \overline{K_{{\mathrm{s}}({\mathfrak p}')}(x_1,y)}e(-{Q}(x_1)(y)+
{Q}(x_1)(x_1))g(x_1)\, d\mu(x_1) \right.\qquad\text{(21)}
$$

$$
\times \left.\int_{E({\mathfrak p})} {K_{{\mathrm{s}}({\mathfrak p})}(x_2,y)}e({Q}(x_2)(y)
-{Q}(x_2)(x_2))\overline{g(x_2)}\, d\mu(x_2)\, d\mu(y)\right|\, .\qquad\text{(22)}
$$

By Fubini and the triangle inequality and the fact $|e({Q}(x_i)(x_i))|=1$ for $i=1,2$, we can estimate (21) and (22) from above by

$$
\int_{E({\mathfrak p}')} \int_{E({\mathfrak p})} {\bf I}(x_1, x_2)\, d\mu(x_1)d\mu(x_2)\,.\qquad\text{(23)}
$$

with

$$
{\bf I}(x_1, x_2):=
\left|\int
e(-{Q}(x_1)(y)+{Q}(x_2)(y))\varphi_{x_1,x_2}(y)
d\mu(y) \, g(x_1)g(x_2)\right|
$$

We estimate for fixed $x_1\in E({\mathfrak p}')$ and $x_2\in E({\mathfrak p})$ the inner integral of (23) with [Holder van der Corput](../proof-of-metric-space-carleson-overview/holder-van-der-corput.md). The function $\varphi:=\varphi_{x_1,x_2}$ satisfies the assumptions of [Holder van der Corput](../proof-of-metric-space-carleson-overview/holder-van-der-corput.md) with $z = x_1$ and $R = D^{s_1}$ by [correlation kernel bound](correlation-kernel-bound.md). We obtain with $B':= B(x_1, D^{{\mathrm{s}}({\mathfrak p}')})$,

$$
{\bf I}(x_1, x_2) \le 2^{8a} \mu(B') \|{\varphi}\|_{C^\tau(B')}
(1 + d_{B'}({Q}(x_1),{Q}(x_2)))^{-1/(2a^2+a^3)}|g(x_1)g(x_2)|
$$

$$
\le \frac{2^{231a^3+8a}}
{\mu(B(x_2, D^{{\mathrm{s}}({\mathfrak p})}))}
(1 + d_{B'}({Q}(x_1),{Q}(x_2)))^{-1/(2a^2+a^3)}\,.\qquad\text{(24)}
$$

Using (20), [Lemma tile-uncertainty](tile-uncertainty.md) and $a\ge 1$ estimates (24) by

$$
\le \frac{2^{231a^3 + 8a + 1}}
{\mu(B(x_2, D^{{\mathrm{s}}({\mathfrak p})}))}
(1+d_{{\mathfrak p}'}({\mathcal{Q}}({\mathfrak p}'), {\mathcal{Q}}({\mathfrak p})))^{-1/(2a^2+a^3)}|g(x_1)g(x_2)|\,.\qquad\text{(25)}
$$

As $x_2\in {\mathcal{I}}({\mathfrak p})$ by Definition [(19)](../proof-of-metric-space-carleson-overview/discrete-carleson.md) of $E$, we have by [(10)](../proof-of-metric-space-carleson-overview/README.md)

$$
\rho(x_2,{\mathrm{c}}({\mathfrak p})) < 4D^{{\mathrm{s}}({\mathfrak p})}
$$

and thus by [(10)](../proof-of-metric-space-carleson-overview/README.md) again and the triangle inequality

$$
{\mathcal{I}}({\mathfrak p})\subset B(x_2,8D^{{\mathrm{s}}({\mathfrak p})})\, .
$$

Using three iterations of the doubling property [(5)](../introduction/README.md) give

$$
\mu({\mathcal{I}}({\mathfrak p}))\le 2^{3a}\mu(B(x_2,D^{{\mathrm{s}}({\mathfrak p})}))\, .
$$

With $a\ge 4$ and (25) we conclude (19).

Now assume the left-hand side of (19) is not zero. There is a $y\in X$ with

$$
T^*_{{\mathfrak p}'}g(y)\overline{T^*_{{\mathfrak p}}g(y)}\neq 0
$$

By the triangle inequality and [tile range support](tile-range-support.md), we conclude

$$
\rho({\mathrm{c}}({\mathfrak p}),{\mathrm{c}}({\mathfrak p}'))\le \rho({\mathrm{c}}({\mathfrak p}),y) +\rho({\mathrm{c}}({\mathfrak p}'),y)
\le 5D^{{\mathrm{s}}({\mathfrak p})}+5D^{{\mathrm{s}}({\mathfrak p}')}\le 10 D^{{\mathrm{s}}({\mathfrak p})}\, .
$$

By the squeezing property [(10)](../proof-of-metric-space-carleson-overview/README.md) and the triangle inequality, we conclude

$$
{\mathcal{I}}({\mathfrak p}') \subset B({\mathrm{c}}({\mathfrak p}), 14D^{{\mathrm{s}}({\mathfrak p})})\, .
$$

This completes the proof of Lemma tile correlation.

## Lean

Formalized as [`Tile.correlation_le`](https://fpvandoorn.github.io/carleson/docs/find/#doc/Tile.correlation_le), [`Tile.correlation_zero_of_ne_subset`](https://fpvandoorn.github.io/carleson/docs/find/#doc/Tile.correlation_zero_of_ne_subset).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 3709](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L3709)
