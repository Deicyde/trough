---
declaration: lemma
origin: cited
lean: TileStructure.Forest.third_tree_pointwise
statement: formalized
proof: formalized
---

# third tree pointwise

For all ${\mathfrak u} \in {\mathfrak U}$, all $L \in \mathcal{L}({\mathfrak T}({\mathfrak u}))$, all $x, x' \in L$ and all bounded $f$ with bounded support, we have

$$
\Bigg| \sum_{s \in \sigma({\mathfrak u}, x)} \int K_s(x,y) (f(y) - P_{\mathcal{J}({\mathfrak T}({\mathfrak u}))} f(y)) \, \mathrm{d}\mu(y) \Bigg|
$$

$$
\le 2^{128a^3} S_{1,{\mathfrak u}} P_{\mathcal{J}({\mathfrak T}({\mathfrak u}))}|f|(x')\,.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

We have for $J \in \mathcal{J}({\mathfrak T}({\mathfrak u}))$:

$$
\int_J K_{s}(x,y)(1 - P_{\mathcal{J}({\mathfrak T}({\mathfrak u}))})f(y) \, \mathrm{d}\mu(y)
$$

$$
= \int_J \frac{1}{\mu(J)} \int_J K_s(x,y) - K_s(x,z) \, \mathrm{d}\mu(z) \,f(y) \, \mathrm{d}\mu(y)\,.\qquad\text{(9)}
$$

By [(67)](../../proof-of-metric-space-carleson-overview/kernel-summand.md) and [(10)](../../proof-of-metric-space-carleson-overview/README.md), we have for $y, z \in J$

$$
|K_s(x,y) - K_s(x,z)| \le \frac{2^{127a^3}}{\mu(B(x, D^s))} \left(\frac{8 D^{s(J)}}{D^s}\right)^{1/a}\,.
$$

Suppose that $s \in \sigma({\mathfrak u}, x)$. If $K_s(x,y) \ne 0$ for some $y \in J \in \mathcal{J}({\mathfrak T}({\mathfrak u}))$ then, by [(65)](../../proof-of-metric-space-carleson-overview/kernel-summand.md), $y \in B(x, 0.5 D^s) \cap J \ne \emptyset$. Let ${\mathfrak p} \in {\mathfrak T}({\mathfrak u})$ with ${\mathrm{s}}({\mathfrak p}) = s$ and $x \in E({\mathfrak p})$. Then $B({\mathrm{c}}({\mathfrak p}_s), 4.5D^s) \cap J \ne \emptyset$ by the triangle inequality. If $s(J) \ge s$ and $s(J) > -S$, then it follows from the triangle inequality, [(10)](../../proof-of-metric-space-carleson-overview/README.md) and [(1)](../../proof-of-metric-space-carleson-overview/README.md) that ${\mathcal{I}}({\mathfrak p}) \subset B(c(J), 100 D^{s(J)+1})$, contradicting $J \in \mathcal{J}(\mathfrak{T}({\mathfrak u}))$. Thus $s(J) \le s - 1$ or $s(J) = -S$. If $s(J) = -S$ and $s(J) > s - 1$, then $s = -S$. So in both cases, $s(J) \le s$. It then follows from the triangle inequality and [(10)](../../proof-of-metric-space-carleson-overview/README.md) that $J \subset B(x, 16 D^s)$.

Thus, we can estimate [(8)](pointwise-tree-estimate.md) by

$$
2^{127a^3 + 3/a}\sum_{{\mathfrak p}\in \mathfrak{T}}\frac{\mathbf{1}_{E({\mathfrak p})}(x)}{\mu(B(x,D^{{\mathrm{s}}({\mathfrak p})}))}\sum_{\substack{J\in \mathcal{J}({\mathfrak T}({\mathfrak u}))\\J\subset B(x, 16D^{{\mathrm{s}}({\mathfrak p})})\\ s(J) \le {\mathrm{s}}({\mathfrak p})}} D^{(s(J) - {\mathrm{s}}({\mathfrak p}))/a} \int_J |f|\,.
$$

$$
= 2^{127a^3 + 3/a}\sum_{I \in \mathcal{D}} \sum_{\substack{{\mathfrak p}\in \mathfrak{T}\\ {\mathcal{I}}({\mathfrak p}) = I}}\frac{\mathbf{1}_{E({\mathfrak p})}(x)}{\mu(B(x, D^{s(I)}))}\sum_{\substack{J\in \mathcal{J}({\mathfrak T}({\mathfrak u}))\\J\subset B(x, 16 D^{s(I)})\\ s(J) \le s(I)}} D^{(s(J) - s(I))/a} \int_J |f|\,.
$$

By [(13)](../../proof-of-metric-space-carleson-overview/README.md) and [(19)](../../proof-of-metric-space-carleson-overview/discrete-carleson.md), the sets $E({\mathfrak p})$ for tiles ${\mathfrak p}$ with ${\mathcal{I}}({\mathfrak p}) = I$ are pairwise disjoint. It follows from the definition of $\mathcal{L}({\mathfrak T}({\mathfrak u}))$ that $x \in {\mathcal{I}}({\mathfrak p})$ if and only if $x' \in {\mathcal{I}}({\mathfrak p})$, thus we can estimate the sum over $\mathbf{1}_{E({\mathfrak p})}(x)$ by $\mathbf{1}_{I}(x')$. If $x \in E({\mathfrak p})$ then in particular $x \in {\mathcal{I}}({\mathfrak p})$, so by [(10)](../../proof-of-metric-space-carleson-overview/README.md) $B(c(I),16D^{s(I)}) \subset B(x, 32D^{s(I)})$. By the doubling property [(5)](../../introduction/README.md)

$$
\mu(B(c(I), 16D^{s(I)})) \le 2^{5a} \mu(B(x, D^{s(I)}))\,.
$$

Since $a \ge 4$ we can continue our estimate with

$$
\le 2^{128a^3}\sum_{I \in \mathcal{D}} \frac{\mathbf{1}_{I}(x')}{\mu(B(c(I), 16D^{s(I)}))}\sum_{\substack{J\in \mathcal{J}({\mathfrak T}({\mathfrak u}))\\J\subset B(x, 16 D^{s(I)})\\ s(J) \le s(I)}} D^{(s(J) - s(I))/a} \int_J |f|
$$

$$
= 2^{128a^3} S_{1,{\mathfrak u}} P_{\mathcal{J}({\mathfrak T}({\mathfrak u}))}|f|(x')\,.
$$

This completes the proof.

## Lean

Formalized as [`TileStructure.Forest.third_tree_pointwise`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.third_tree_pointwise).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 4639](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L4639)
