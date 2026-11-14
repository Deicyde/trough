---
declaration: proposition
origin: cited
lean: finitary_carleson
statement: formalized
proof: formalized
---

# finitary Carleson

Let ${\sigma_1},\sigma_2\colon X\to \mathbb{Z}$ be measurable functions with finite range and ${\sigma_1}\leq \sigma_2$. Let $F,G$ be bounded Borel sets in $X$. Then there is a Borel set $G'$ in $X$ with $2\mu(G')\leq \mu(G)$ such that for all Borel functions $f:X\to {\mathbb{C}}$ with $|f|\le \mathbf{1}_F$.

$$
\int_{G \setminus G'} \left|\sum_{s={\sigma_1}(x)}^{{\sigma_2}(x)} \int K_s(x,y) f(y) e({Q}(x)(y)) \, \mathrm{d}\mu(y) \right| \mathrm{d}\mu(x)
$$

$$
\le \frac{2^{442a^3}}{(q-1)^5} \mu(G)^{1-\frac{1}{q}} \mu(F)^{\frac 1 q}\,.\qquad\text{(6)}
$$

## Depends on

- [discrete Carleson](discrete-carleson.md)
- [grid existence](../proof-of-finitary-carleson/grid-existence.md)
- [tile structure](../proof-of-finitary-carleson/tile-structure.md)
- [tile sum operator](../proof-of-finitary-carleson/tile-sum-operator.md)

## Proof

*Proof of finitary Carleson.* We now estimate with [tile sum operator](../proof-of-finitary-carleson/tile-sum-operator.md) and [discrete Carleson](discrete-carleson.md)

$$
\int_{G \setminus G'} \left|\sum_{s={\sigma_1}(x)}^{{\sigma_2}(x)} \int K_s(x,y) f(y) e({Q}(x)(y)) \, \mathrm{d}\mu(y)\right| \mathrm{d}\mu(x)
$$

$$
=\int_{G \setminus G'} \left|\sum_{s={\sigma_1}(x)}^{{\sigma_2}(x)} \int K_s(x,y) f(y) e({Q}(x)(y) - {Q}(x)(x))\mathrm{d}\mu(y)\right| \mathrm{d}\mu(x)
$$

$$
=\int_{G \setminus G'} \left|\sum_{{\mathfrak p}\in {\mathfrak P}}T_{{\mathfrak p}} f(x)\right| \mathrm{d}\mu(x)
\le \frac{2^{442a^3}}{(q-1)^5} \mu(G)^{1 - \frac{1}{q}} \mu(F)^{\frac{1}{q}} \,.
$$

This proves (6) for the chosen set $G'$ and arbitrary $f$ and thus completes the proof of Proposition finitary Carleson.

## Lean

Formalized as [`finitary_carleson`](https://fpvandoorn.github.io/carleson/docs/find/#doc/finitary_carleson).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 444](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L444)
