---
declaration: lemma
origin: cited
lean: maximal_bound_antichain
statement: formalized
proof: formalized
---

# maximal bound antichain

Let $x\in X$. Then

$$
| \sum_{{\mathfrak p} \in \mathfrak{A}}T_{{\mathfrak p}} f(x)|\le 2^{102 a^3} M_{\mathcal{B}} f (x) \, .\qquad\text{(1)}
$$

## Depends on

- [tile disjointness](tile-disjointness.md)

## Proof

Fix $x\in X$. By [tile disjointness](tile-disjointness.md), there is at most one ${\mathfrak p} \in \mathfrak{A}$ such that $T_{{\mathfrak p}} f(x)$ is not zero. If there is no such ${\mathfrak p}$, the estimate (1) follows.

Assume there is such a ${\mathfrak p}$. By definition of $T_{{\mathfrak p}}$ we have $x\in E({\mathfrak p})\subset {\mathcal{I}}({\mathfrak p})$ and by the squeezing property [(10)](../proof-of-metric-space-carleson-overview/README.md)

$$
\rho(x, {\mathrm{c}}({\mathfrak p}))\le 4D^{{\mathrm{s}}({\mathfrak p})}\, .\qquad\text{(2)}
$$

Let $y\in X$ with $K_{{\mathrm{s}}({\mathfrak p})}(x,y)\neq 0$. By Definition [(5)](../proof-of-metric-space-carleson-overview/README.md) of $K_{{\mathrm{s}}({\mathfrak p})}$ we have

$$
\frac{1}{4} D^{{\mathrm{s}}({\mathfrak p})-1}
\leq \rho(x,y) \leq \frac{1}{2} D^{{\mathrm{s}}({\mathfrak p})}\, .\qquad\text{(3)}
$$

The triangle inequality with (2) and (3) implies

$$
\rho({\mathrm{c}}({\mathfrak p}),y) < 8D^{{\mathrm{s}}({\mathfrak p})}\, .
$$

Using the kernel bound [(14)](../introduction/README.md) and the lower bound in [(65)](../proof-of-metric-space-carleson-overview/kernel-summand.md) we obtain

$$
|K_{{\mathrm{s}}({\mathfrak p})}(x,y)|\le \frac{2^{a^3}}{\mu(B(x,\frac 14 D^{{{\mathrm{s}}({\mathfrak p})}-1}))}\, .
$$

Using $D=2^{100a^2}$ and the doubling property [(5)](../introduction/README.md) $5 +100a^2$ times estimates the last display by

$$
\le \frac{2^{5a+101a^3}}{\mu(B(x, 8D^{{\mathrm{s}}({\mathfrak p})}))}\,
$$

which, thanks to the closeness of the points $x$ and ${\mathrm{c}}({\mathfrak p})$ shown in (2), is in turn bounded by

$$
\le \frac{2^{6a+101a^3}}{\mu(B({\mathrm{c}}({\mathfrak p}), 8D^{{\mathrm{s}}({\mathfrak p})}))}\, .
$$

Using that $|e({\vartheta})|$ is bounded by $1$ for every ${\vartheta}\in {\Theta}$, we estimate with the triangle inequality and the above information

$$
| T_{{\mathfrak p}} f(x)|
\le \frac{2^{6a+101 a^3}}{\mu(B({\mathrm{c}}({\mathfrak p}), 8D^{{\mathrm{s}}({\mathfrak p})}))} \int _{\mu(B({\mathrm{c}}({\mathfrak p}), 8D^{{\mathrm{s}}({\mathfrak p})}))} |f(y)|\, dy
$$

This together with $a\ge 4$ proves the Lemma.

## Lean

Formalized as [`maximal_bound_antichain`](https://fpvandoorn.github.io/carleson/docs/find/#doc/maximal_bound_antichain).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 3458](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L3458)
