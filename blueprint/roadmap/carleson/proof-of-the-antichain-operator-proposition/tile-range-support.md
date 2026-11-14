---
declaration: lemma
origin: cited
lean: Tile.range_support
statement: formalized
proof: formalized
---

# tile range support

For each ${\mathfrak p}\in {\mathfrak P}$, and each $y\in X$, we have that

$$
T_{{\mathfrak p}}^* g(y)\neq 0\qquad\text{(33)}
$$

implies

$$
y\in B({\mathrm{c}}({\mathfrak p}),5D^{{\mathrm{s}}({\mathfrak p})})\, .\qquad\text{(34)}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Fix ${\mathfrak p}$ and $y$ with (33). Then there exists $x\in E({\mathfrak p})$ with

$$
\overline{K_{{\mathrm{s}}({\mathfrak p})}(x,y)}e(-{Q}(x)(y)
+{Q}(x)(x))g(x) \neq 0\, .
$$

As $E({\mathfrak p})\subset {\mathcal{I}}({\mathfrak p})$ and by the squeezing property [(10)](../proof-of-metric-space-carleson-overview/README.md), we have

$$
\rho(x,{\mathrm{c}}({\mathfrak p})) < 4D^{{\mathrm{s}}({\mathfrak p})}\, .
$$

As $K_{{\mathrm{s}}({\mathfrak p})}(x,y)\neq 0$, we have by [(65)](../proof-of-metric-space-carleson-overview/kernel-summand.md) that

$$
\rho(x,y)\le \frac 12 D^{{\mathrm{s}}({\mathfrak p})}\, .
$$

Now (34) follows by the triangle inequality.

## Lean

Formalized as [`Tile.range_support`](https://fpvandoorn.github.io/carleson/docs/find/#doc/Tile.range_support).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 3831](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L3831)
