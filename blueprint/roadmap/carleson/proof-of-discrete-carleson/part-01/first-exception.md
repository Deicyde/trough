---
declaration: lemma
origin: cited
lean: first_exception
statement: formalized
proof: formalized
---

# first exception

We have

$$
\mu(G_1)\le 2^{-5}\mu(G)\, .
$$

## Depends on

- [Hardy–Littlewood](../../proof-of-metric-space-carleson-overview/hardy-littlewood.md)

## Proof

Let

$$
K = 2^{2a+5}\frac{\mu(F)}{\mu(G)}\,.
$$

For each ${\mathfrak p}\in {\mathfrak P}_{F,G}$ pick a $r({\mathfrak p})>4D^{{\mathrm{s}}({\mathfrak p})}$ with

$$
{\mu(F\cap B({\mathrm{c}}({\mathfrak p}),r({\mathfrak p})))}\ge K{\mu(B({\mathrm{c}}({\mathfrak p}),r({\mathfrak p})))}\, .
$$

This ball exists by definition of ${\mathfrak P}_{F,G}$ and $\operatorname{\operatorname{dens}}_2$. By applying [Hardy–Littlewood](../../proof-of-metric-space-carleson-overview/hardy-littlewood.md) to the collection of balls

$$
\mathcal{B} = \{B({\mathrm{c}}({\mathfrak p}),r({\mathfrak p})) \ : \ {\mathfrak p} \in {\mathfrak P}_{F,G}\}
$$

and the function $u = \mathbf{1}_F$, we obtain

$$
\mu(\bigcup \mathcal{B}) \le 2^{2a} K^{-1} \mu(F)\,.
$$

We conclude with [(10)](../../proof-of-metric-space-carleson-overview/README.md) and $r({\mathfrak p})>4D^{{\mathrm{s}}({\mathfrak p})}$

$$
\mu(G_1)= \mu(\bigcup_{{\mathfrak p}\in {\mathfrak P}_{F,G}} {\mathcal{I}}({\mathfrak p}))
\le \mu(\bigcup \mathcal{B})\le 2^{2a} K^{-1} \mu (F) = 2^{-5}\mu(G)\,.
$$

## Lean

Formalized as [`first_exception`](https://fpvandoorn.github.io/carleson/docs/find/#doc/first_exception).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 2197](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L2197)
