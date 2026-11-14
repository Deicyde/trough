---
declaration: lemma
origin: cited
lean: TileStructure.Forest.pointwise_tree_estimate
statement: formalized
proof: formalized
---

# pointwise tree estimate

Let ${\mathfrak u} \in {\mathfrak U}$ and $L \in \mathcal{L}({\mathfrak T}({\mathfrak u}))$. Let $x, x' \in L$. Then for all bounded functions $f$ with bounded support

$$
\left|\sum_{{\mathfrak p} \in {\mathfrak T}({\mathfrak u})} T_{{\mathfrak p}}[ e(-{\mathcal{Q}}({\mathfrak u}))f](x)\right|
$$

$$
\leq 2^{129a^3}(M_{\mathcal{B},1}+S_{1,{\mathfrak u}})P_{\mathcal{J}({\mathfrak T}({\mathfrak u}))}|f|(x')+|T_{\mathcal{N}}^{{\mathcal{Q}}({\mathfrak u})} P_{\mathcal{J}({\mathfrak T}({\mathfrak u}))}f(x')|,\qquad\text{(5)}
$$

## Depends on

- [first tree pointwise](first-tree-pointwise.md)
- [second tree pointwise](second-tree-pointwise.md)
- [third tree pointwise](third-tree-pointwise.md)

## Proof

By [(20)](../../proof-of-metric-space-carleson-overview/discrete-carleson.md), if $T_{{\mathfrak p}}[ e(-{\mathcal{Q}}({\mathfrak u}))f](x) \ne 0$, then $x \in E({\mathfrak p})$. Combining this with $|e({\mathcal{Q}}({\mathfrak u})(x))| = 1$, we obtain

$$
|\sum_{{\mathfrak p} \in {\mathfrak T}({\mathfrak u})} T_{{\mathfrak p}}[ e(-{\mathcal{Q}}({\mathfrak u}))f](x)|
$$

$$
\begin{gathered}
= \Bigg| \sum_{s \in \sigma({\mathfrak u}, x)} \int e(-{\mathcal{Q}}({\mathfrak u})(y) + {Q}(x)(y) + {\mathcal{Q}}({\mathfrak u})(x) -{Q}(x)(x))\times\\
K_s(x,y)f(y) \, \mathrm{d}\mu(y) \Bigg|\,.
\end{gathered}
$$

Using the triangle inequality, we bound this by the sum of three terms:

$$
\begin{gathered}
\le \Bigg| \sum_{s \in \sigma({\mathfrak u}, x)} \int (e(-{\mathcal{Q}}({\mathfrak u})(y) + {Q}(x)(y) + {\mathcal{Q}}({\mathfrak u})(x) -{Q}(x)(x))-1)\times\qquad\text{(6)}\\
K_s(x,y)f(y) \, \mathrm{d}\mu(y) \Bigg|
\end{gathered}
$$

$$
+ \Bigg| \sum_{s \in \sigma({\mathfrak u}, x)} \int K_s(x,y) P_{\mathcal{J}({\mathfrak T}({\mathfrak u}))} f(y) \, \mathrm{d}\mu(y) \Bigg|\qquad\text{(7)}
$$

$$
+ \Bigg| \sum_{s \in \sigma({\mathfrak u}, x)} \int K_s(x,y) (f(y) - P_{\mathcal{J}({\mathfrak T}({\mathfrak u}))} f(y)) \, \mathrm{d}\mu(y) \Bigg|\,.\qquad\text{(8)}
$$

The proof is completed using the bounds for these three terms proven respectively in [first tree pointwise](first-tree-pointwise.md), [second tree pointwise](second-tree-pointwise.md) and [third tree pointwise](third-tree-pointwise.md).

## Lean

Formalized as [`TileStructure.Forest.pointwise_tree_estimate`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.pointwise_tree_estimate).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 4501](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L4501)
