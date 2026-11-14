---
declaration: proposition
origin: cited
lean: discrete_carleson
statement: formalized
proof: formalized
---

# discrete Carleson

Let $(\mathcal{D}, c, s)$ be a grid structure and

$$
({\mathfrak P},{\mathcal{I}},{\Omega},{\mathcal{Q}},{\mathrm{c}},{\mathrm{s}})
$$

a tile structure for this grid structure. Define for ${\mathfrak p}\in {\mathfrak P}$

$$
E({\mathfrak p})=\{x\in {\mathcal{I}}({\mathfrak p}): {Q}(x)\in {\Omega}({\mathfrak p}) , {\sigma_1}(x)\le {\mathrm{s}}({\mathfrak p})\le {\sigma_2}(x)\}\qquad\text{(19)}
$$

and

$$
T_{{\mathfrak p}} f(x)= \mathbf{1}_{E({\mathfrak p})}(x) \int K_{{\mathrm{s}}({\mathfrak p})}(x,y) f(y) e({Q}(x)(y)-{Q}(x)(x))\, d\mu(y).\qquad\text{(20)}
$$

Then there exists a Borel set $G'$ with $2\mu(G') \leq \mu(G)$ such that for all Borel functions $f:X\to {\mathbb{C}}$ with $|f|\le \mathbf{1}_F$ we have

$$
\int_{G \setminus G'} \left| \sum_{{\mathfrak p} \in {\mathfrak P}} T_{{\mathfrak p}} f (x) \right| \, \mathrm{d}\mu(x) \le \frac{2^{442a^3}}{(q-1)^5} \mu(G)^{1-\frac{1}{q}} \mu(F)^{\frac{1}{q}}\,.\qquad\text{(21)}
$$

## Depends on

- [exceptional set](../proof-of-discrete-carleson/part-01/exceptional-set.md)
- [forest union](../proof-of-discrete-carleson/part-01/forest-union.md)
- [forest complement](../proof-of-discrete-carleson/part-01/forest-complement.md)

## Proof

*Proof of discrete Carleson.* discrete Carleson follows by applying the triangle inequality to (21) according to the splitting in [forest union](../proof-of-discrete-carleson/part-01/forest-union.md) and [forest complement](../proof-of-discrete-carleson/part-01/forest-complement.md) and using both Lemmas as well as the bound on the set $G'$ given by [exceptional set](../proof-of-discrete-carleson/part-01/exceptional-set.md).

## Lean

Formalized as [`discrete_carleson`](https://fpvandoorn.github.io/carleson/docs/find/#doc/discrete_carleson).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 552](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L552)
