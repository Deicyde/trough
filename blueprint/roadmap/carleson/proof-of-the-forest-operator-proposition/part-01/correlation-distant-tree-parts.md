---
declaration: lemma
origin: cited
lean: TileStructure.Forest.correlation_distant_tree_parts
statement: formalized
proof: formalized
---

# correlation distant tree parts

We have for all ${\mathfrak u}_1 \ne {\mathfrak u}_2 \in {\mathfrak U}$ with ${\mathcal{I}}({\mathfrak u}_1) \subset {\mathcal{I}}({\mathfrak u}_2)$ and all bounded $g_1, g_2$ with bounded support

$$
\left| \int_X \sum_{{\mathfrak p}_1 \in {\mathfrak T}({\mathfrak u}_1)} \sum_{{\mathfrak p}_2 \in {\mathfrak T}({\mathfrak u}_2) \cap \mathfrak{S}} T^*_{{\mathfrak p}_1}g_1 \overline{T^*_{{\mathfrak p}_2}g_2 }\,\mathrm{d}\mu \right|\qquad\text{(30)}
$$

$$
\le 2^{511a^3} 2^{-Zn/(4a^2 + 2a^3)} \prod_{j =1}^2 \| S_{2, {\mathfrak u}_j} g_j\|_{L^2({\mathcal{I}}({\mathfrak u}_1))}\,.\qquad\text{(31)}
$$

## Depends on

- [Holder van der Corput](../../proof-of-metric-space-carleson-overview/holder-van-der-corput.md)
- [Lipschitz partition unity](../part-02/lipschitz-partition-unity.md)
- [Holder correlation tree](../part-02/holder-correlation-tree.md)
- [lower oscillation bound](../part-02/lower-oscillation-bound.md)

## Proof

*Proof of correlation distant tree parts.* We have

$$
\eqref{eq-lhs-big-sep-tree} = \left| \int_{X} T_{{\mathfrak T}({\mathfrak u}_1)}^* g_1 \overline{T_{{\mathfrak T}({\mathfrak u}_2) \cap \mathfrak{S}}^* g_2 }\right|\,.
$$

By [adjoint tile support](adjoint-tile-support.md), the right hand side is supported in ${\mathcal{I}}({\mathfrak u}_1)$. Using [(36)](../part-02/lipschitz-partition-unity.md) of [Lipschitz partition unity](../part-02/lipschitz-partition-unity.md) and the definition [(41)](../part-02/README.md) of $h_J$, we thus have

$$
\le \sum_{J \in \mathcal{J}'} \left|\int_{X} e({\mathcal{Q}}({\mathfrak u}_2)(y) - {\mathcal{Q}}({\mathfrak u}_1)(y)) h_J(y) \, \mathrm{d}\mu(y) \right|\,.
$$

Using [Holder van der Corput](../../proof-of-metric-space-carleson-overview/holder-van-der-corput.md) with the ball $B(J)$, we bound this by

$$
\le 2^{7a} \sum_{J \in \mathcal{J}'} \mu(B(J)) \|h_J\|_{C^{\tau}(B'(J))} (1 + d_{B(J)}({\mathcal{Q}}({\mathfrak u}_2), {\mathcal{Q}}({\mathfrak u}_1)))^{-1/(2a^2+a^3)}\,.
$$

Using [Holder correlation tree](../part-02/holder-correlation-tree.md), [lower oscillation bound](../part-02/lower-oscillation-bound.md) and $a \ge 4$, we bound the above by

$$
\begin{gathered}
\le 2^{485a^3+7a+3a^3+3a} 2^{-Zn/(4a^2 + 2a^3)} \sum_{J \in \mathcal{J}'} \mu(B(J))\qquad\text{(32)}\\
\times \prod_{j=1}^2 (\inf_{B^\circ{}(J)} |T_{{\mathfrak T}({\mathfrak u}_j)}^* g_j| + \inf_J M_{\mathcal{B},1} g_j)\,.
\end{gathered}
$$

By the doubling property [(5)](../../introduction/README.md)

$$
\mu(B(J)) \le 2^{6a} \mu(B^\circ{}(J))\,,
$$

thus

$$
\mu(B(J)) \prod_{j=1}^2 (\inf_{B^\circ{}(J)} |T_{{\mathfrak T}({\mathfrak u}_j)}^* g_j| + \inf_J M_{\mathcal{B},1} g_j)
$$

$$
\le 2^{6a} \int_{B^\circ{}(J)} \prod_{j=1}^2 ( |T_{{\mathfrak T}({\mathfrak u}_j)}^* g_j|(x) + M_{\mathcal{B},1} g_j(x)) \, \mathrm{d}\mu(x)
$$

$$
\le 2^{6a} \int_J \prod_{j=1}^2 ( |T_{{\mathfrak T}({\mathfrak u}_j)}^* g_j|(x) + M_{\mathcal{B},1} g_j(x)) \, \mathrm{d}\mu(x)\,.
$$

Summing over $J \in \mathcal{J}'$, we obtain

$$
\eqref{eq-big-sep-1} \le 2^{499a^3} 2^{-Zn/(4a^2 + 2a^3)} \int_X \prod_{j=1}^2 ( |T_{{\mathfrak T}({\mathfrak u}_j)}^* g_j|(x) + M_{\mathcal{B},1} g_j(x)) \, \mathrm{d}\mu(x)\,.
$$

Applying the Cauchy-Schwarz inequality, correlation distant tree parts follows.

## Lean

Formalized as [`TileStructure.Forest.correlation_distant_tree_parts`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.correlation_distant_tree_parts).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 5327](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L5327)
