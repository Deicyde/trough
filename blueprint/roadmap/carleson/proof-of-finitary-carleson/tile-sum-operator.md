---
declaration: lemma
origin: cited
lean: tile_sum_operator, integrable_tile_sum_operator
statement: formalized
proof: formalized
---

# tile sum operator

We have for all $x\in G\setminus G'$

$$
\sum_{{\mathfrak p}\in {\mathfrak P}}T_{{\mathfrak p}} f(x)= \sum_{s=\sigma_1(x)}^{\sigma_2(x)}
\int K_{s}(x,y) f(y) e({Q}(x)(y)-{Q}(x)(x))\, d\mu(y).\qquad\text{(1)}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Fix $x\in G\setminus G'$. Sorting the tiles ${\mathfrak p}$ on the left-hand-side of (1) by the value ${\mathrm{s}}({\mathfrak p})\in [-S,S]$, it suffices to prove for every $-S\le s\le S$ that

$$
\sum_{{\mathfrak p}\in {\mathfrak P}: {\mathrm{s}}({\mathfrak p})=s}T_{{\mathfrak p}} f(x)=0\qquad\text{(2)}
$$

if $s\not\in [\sigma_1(x), \sigma_2(x)]$ and

$$
\sum_{{\mathfrak p}\in {\mathfrak P}: {\mathrm{s}}({\mathfrak p})=s}T_{{\mathfrak p}} f(x)=
\int K_{s}(x,y) f(y) e({Q}(x)(y) - {Q}(x)(x))\, d\mu(y).\qquad\text{(3)}
$$

if $s\in [\sigma_1(x),\sigma_2(x)]$. If $s\not\in [\sigma_1(x), \sigma_2(x)]$, then by definition of $E({\mathfrak p})$ we have $x\not\in E({\mathfrak p})$ for any ${\mathfrak p}$ with ${\mathrm{s}}({\mathfrak p})=s$ and thus $T_{{\mathfrak p}} f(x)=0$. This proves (2).

Now assume $s\in [\sigma_1(x),\sigma_2(x)]$. By [(7)](../proof-of-metric-space-carleson-overview/README.md), [(9)](../proof-of-metric-space-carleson-overview/README.md), [(10)](../proof-of-metric-space-carleson-overview/README.md), the fact that $c(I_0) = o$ and $G\subset B(o,\frac 14 D^S)$, there is at least one $I\in \mathcal{D}$ with $s(I)=s$ and $x\in I$. By [(8)](../proof-of-metric-space-carleson-overview/README.md), this $I$ is unique. By [(13)](../proof-of-metric-space-carleson-overview/README.md), there is precisely one ${\mathfrak p}\in {\mathfrak P}(I)$ such that ${Q}(x)\in {\Omega}({\mathfrak p})$. Hence there is precisely one ${\mathfrak p}\in {\mathfrak P}$ with ${\mathrm{s}}({\mathfrak p})=s$ such that $x\in E({\mathfrak p})$. For this ${\mathfrak p}$, the value $T_{{\mathfrak p}}(x)$ by its definition in [(20)](../proof-of-metric-space-carleson-overview/discrete-carleson.md) equals the right-hand side of (3). This proves the lemma.

## Lean

Formalized as [`tile_sum_operator`](https://fpvandoorn.github.io/carleson/docs/find/#doc/tile_sum_operator), [`integrable_tile_sum_operator`](https://fpvandoorn.github.io/carleson/docs/find/#doc/integrable_tile_sum_operator).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 1266](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L1266)
