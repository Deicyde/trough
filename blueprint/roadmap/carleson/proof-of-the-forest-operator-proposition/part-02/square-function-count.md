---
declaration: lemma
origin: cited
lean: TileStructure.Forest.square_function_count
statement: formalized
proof: formalized
---

# square function count

For each $J \in \mathcal{J}'$ and all $s$, we have

$$
\frac{1}{\mu(J)} \int_J \Bigg(\sum_{\substack{I \in \mathcal{D}, s(I) = s(J) - s\\ I \cap {\mathcal{I}}({\mathfrak u}_1) = \emptyset\\
J \cap B(I) \ne \emptyset}} \mathbf{1}_{B(I)}\bigg)^2 \, \mathrm{d}\mu \le 2^{14a+1} (8 D^{-s})^\kappa\,.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Since $J \in \mathcal{J}'$ we have $J \subset {\mathcal{I}}({\mathfrak u}_1)$. Thus, if $B(I) \cap J \ne \emptyset$ then

$$
B(I) \cap J \subset \{x \in J \ : \ \rho(x, X \setminus J) \le 8D^{s(I)}\}\,.\qquad\text{(58)}
$$

Furthermore, for each $s$ the balls $B(I)$ with $s(I) = s$ have bounded overlap: Consider the collection $\mathcal{D}_{s,x}$ of all $I \in \mathcal{D}$ with $x \in B(I)$ and $s(I) = s$. By [(10)](../../proof-of-metric-space-carleson-overview/README.md) and [(8)](../../proof-of-metric-space-carleson-overview/README.md), the balls $B(c(I), \frac{1}{4} D^{s(I)})$, $I \in \mathcal{D}_{s,x}$ are disjoint, and by the triangle inequality, they are contained in $B(x, 9 D^{s})$. By the doubling property [(5)](../../introduction/README.md), we have

$$
\mu(B(x, 9D^{s})) \le 2^{7a} \mu(B(c(I), \frac{1}{4} D^{s(I)}))
$$

for each $I \in \mathcal{D}_{s,x}$. Thus

$$
\mu(B(x, 9D^{s})) \ge \sum_{I \in \mathcal{D}_{s,x}} \mu(B(c(I), \frac{1}{4} D^{s(I)})) \ge 2^{-7a} |\mathcal{D}_{s,x}| \mu(B(x, 9D^{s}))\,.
$$

Dividing by the positive $\mu(B(x, 9D^{s}))$, we obtain that for each $x$

$$
\Bigg(\sum_{\substack{I \in \mathcal{D}, s(I) = s(J) - s\\ I \cap {\mathcal{I}}({\mathfrak u}_1) = \emptyset\\
J \cap B(I) \ne \emptyset}} \mathbf{1}_{B(I)}(x) \bigg)^2 \le |\mathcal{D}_{s(J) - s,x}|^2 \le 2^{14a} \,.\qquad\text{(59)}
$$

Combining (58), (59) and the small boundary property [(11)](../../proof-of-metric-space-carleson-overview/README.md), noting that $8D^{s(I)}=8D^{-s}D^{s(J)}$, the lemma follows.

## Lean

Formalized as [`TileStructure.Forest.square_function_count`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.square_function_count).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 6109](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L6109)
