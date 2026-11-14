---
declaration: lemma
origin: cited
lean: TileStructure.Forest.first_tree_pointwise
statement: formalized
proof: formalized
---

# first tree pointwise

For all ${\mathfrak u} \in {\mathfrak U}$, all $L \in \mathcal{L}({\mathfrak T}({\mathfrak u}))$, all $x, x' \in L$ and all bounded $f$ with bounded support, we have

$$
\eqref{eq-term-A} \le 10 \cdot 2^{104a^3} M_{\mathcal{B}, 1}P_{\mathcal{J}({\mathfrak T}({\mathfrak u}))}|f|(x')\,.
$$

## Depends on

- [convex scales](convex-scales.md)
- [kernel summand](../../proof-of-metric-space-carleson-overview/kernel-summand.md)

## Proof

Let $s \in \sigma({\mathfrak u},x)$. If $x, y \in X$ are such that $K_s(x,y)\neq 0$, then, by [(65)](../../proof-of-metric-space-carleson-overview/kernel-summand.md), we have $\rho(x,y)\leq 1/2 D^s$. By $1$-Lipschitz continuity of the function $t \mapsto \exp(it) = e(t)$ and the property [(7)](../../introduction/README.md) of the metrics $d_B$, it follows that

$$
\begin{gathered}
|e(-{\mathcal{Q}}({\mathfrak u})(y)+{Q}(x)(y)+{\mathcal{Q}}({\mathfrak u})(x)-{Q}(x)(x))-1|\\
\leq d_{B(x, 1/2 D^{s})}({\mathcal{Q}}({\mathfrak u}), {Q}(x))\,.
\end{gathered}
$$

Let ${\mathfrak p}_s \in {\mathfrak T}({\mathfrak u})$ be a tile with ${\mathrm{s}}({\mathfrak p}_s) = s$ and $x \in E({\mathfrak p}_s)$, and let ${\mathfrak p}'$ be a tile with ${\mathrm{s}}({\mathfrak p}') = \overline{\sigma}({\mathfrak u}, x)$ and $x \in E({\mathfrak p}')$. Using the monotonicity property [(9)](../../introduction/README.md), the doubling property [(8)](../../introduction/README.md) repeatedly, the definition of $d_{{\mathfrak p}}$ and [monotone cube metrics](../../proof-of-metric-space-carleson-overview/monotone-cube-metrics.md), we can bound the previous display by

$$
d_{B(x, 4 D^{s})}({\mathcal{Q}}({\mathfrak u}), {Q}(x)) \leq 2^{4a} d_{{\mathfrak p}_s}({\mathcal{Q}}({\mathfrak u}), {Q}(x)) \le 2^{4a} 2^{s - \overline{\sigma}({\mathfrak u}, x)} d_{{\mathfrak p}'}({\mathcal{Q}}({\mathfrak u}), {Q}(x))\,.
$$

Since ${\mathcal{Q}}({\mathfrak u}) \in B_{{\mathfrak p}'}({\mathcal{Q}}({\mathfrak p}'), 4)$ by [(30)](../../proof-of-metric-space-carleson-overview/README.md) and ${Q}(x) \in \Omega({\mathfrak p}') \subset B_{{\mathfrak p}'}({\mathcal{Q}}({\mathfrak p}'), 1)$ by [(15)](../../proof-of-metric-space-carleson-overview/README.md), this is estimated by

$$
\le 5 \cdot 2^{4a} 2^{s - \overline{\sigma}({\mathfrak u}, x)} \,.
$$

Using [(66)](../../proof-of-metric-space-carleson-overview/kernel-summand.md), it follows that

$$
\eqref{eq-term-A} \le 5\cdot 2^{103a^3} \sum_{s\in\sigma(x)}2^{s - \overline{\sigma}({\mathfrak u}, x)} \frac{1}{\mu(B(x,D^s))}\int_{B(x,0.5D^{s})}|f(y)|\,\mathrm{d}\mu(y)\,.
$$

By [(1)](dyadic-partitions.md), the collection $\mathcal{J}$ is a partition of $\bigcup_{I \in \mathcal{D}} I$, so this is estimated by

$$
5\cdot 2^{103a^3} \sum_{s\in\sigma(x)}2^{s - \overline{\sigma}({\mathfrak u}, x)} \frac{1}{\mu(B(x,D^s))}\sum_{\substack{J \in \mathcal{J}({\mathfrak T}({\mathfrak u}))\\J \cap B(x, 0.5D^s) \ne \emptyset} }\int_{J}|f(y)|\,\mathrm{d}\mu(y)\,.
$$

This expression does not change if we replace $|f|$ by $P_{\mathcal{J}({\mathfrak T}({\mathfrak u}))}|f|$.

Let $J \in \mathcal{J}({\mathfrak T}({\mathfrak u}))$ with $B(x, 0.5 D^s) \cap J \ne \emptyset$. By the triangle inequality and since $x \in E({\mathfrak p}_s) \subset B({\mathrm{c}}({\mathfrak p}_s), 4D^{s})$, it follows that $B({\mathrm{c}}({\mathfrak p}_s), 4.5D^s) \cap J \ne \emptyset$. If $s(J) \ge s$ and $s(J) > -S$, then it follows from the triangle inequality, [(10)](../../proof-of-metric-space-carleson-overview/README.md) and [(1)](../../proof-of-metric-space-carleson-overview/README.md) that ${\mathcal{I}}({\mathfrak p}_s) \subset B(c(J), 100 D^{s(J)+1})$, contradicting $J \in \mathcal{J}(\mathfrak{T}({\mathfrak u}))$. Thus $s(J) \le s - 1$ or $s(J) = -S$. If $s(J) = -S$ and $s(J) > s - 1$, then $s = -S$. Thus we always have $s(J) \le s$. It then follows from the triangle inequality and [(10)](../../proof-of-metric-space-carleson-overview/README.md) that $J \subset B({\mathrm{c}}({\mathfrak p}_s), 16 D^s)$.

Thus we can continue our chain of estimates with

$$
5\cdot 2^{103a^3} \sum_{s\in\sigma(x)}2^{s - \overline{\sigma}({\mathfrak u}, x)} \frac{1}{\mu(B(x,D^s))}\int_{B({\mathrm{c}}({\mathfrak p}_s),16 D^s)}P_{\mathcal{J}({\mathfrak T}({\mathfrak u}))}|f(y)|\,\mathrm{d}\mu(y)\,.
$$

We have $B({\mathrm{c}}({\mathfrak p}_s), 16D^s)) \subset B(x, 32D^s)$, by [(10)](../../proof-of-metric-space-carleson-overview/README.md) and the triangle inequality, since $x \in {\mathcal{I}}({\mathfrak p}_s)$. Combining this with the doubling property [(5)](../../introduction/README.md), we obtain

$$
\mu(B({\mathrm{c}}({\mathfrak p}_s), 16D^s)) \le 2^{5a} \mu(B(x, D^s))\,.
$$

Since $a \ge 4$, it follows that [(6)](pointwise-tree-estimate.md) is bounded by

$$
5\cdot 2^{103a^3} \sum_{s\in\sigma(x)}2^{s - \overline{\sigma}({\mathfrak u}, x)} \frac{1}{\mu(B({\mathrm{c}}({\mathfrak p}_s),16D^s))}\int_{B({\mathrm{c}}({\mathfrak p}_s),16D^s)}P_{\mathcal{J}({\mathfrak T}({\mathfrak u}))}|f(y)|\,\mathrm{d}\mu(y)\,.
$$

Since $L \in \mathcal{L}({\mathfrak T}({\mathfrak u}))$ and $x\in L \cap {\mathcal{I}}({\mathfrak p}_s)$, we have $s(L) \le {\mathrm{s}}({\mathfrak p}_s)$. It follows by [(8)](../../proof-of-metric-space-carleson-overview/README.md) that $L \subset {\mathcal{I}}({\mathfrak p}_s)$, in particular $x' \in {\mathcal{I}}({\mathfrak p}_s) \subset B({\mathrm{c}}({\mathfrak p}_s), 16D^s)$. Thus

$$
\le 5\cdot 2^{104a^3} \sum_{s\in\sigma(x)}2^{s - \overline{\sigma}({\mathfrak u}, x)} M_{\mathcal{B}, 1}P_{\mathcal{J}({\mathfrak T}({\mathfrak u}))}|f|(x')
$$

$$
\le 10\cdot 2^{104a^3} M_{\mathcal{B}, 1}P_{\mathcal{J}({\mathfrak T}({\mathfrak u}))}|f|(x')\,.
$$

This completes the estimate for term [(6)](pointwise-tree-estimate.md).

## Lean

Formalized as [`TileStructure.Forest.first_tree_pointwise`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.first_tree_pointwise).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 4544](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L4544)
