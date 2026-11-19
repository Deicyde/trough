---
declaration: lemma
origin: cited
lean: TileStructure.Forest.limited_scale_impact
statement: formalized
proof: formalized
---

# limited scale impact

Let ${\mathfrak p} \in {\mathfrak T}({\mathfrak u}_2) \setminus \mathfrak{S}$, $J \in \mathcal{J}'$ and suppose that

$$
B({\mathcal{I}}({\mathfrak p})) \cap B^\circ(J) \ne \emptyset\,.
$$

Then

$$
s(J) \le {\mathrm{s}}({\mathfrak p}) \le s(J) +3\,.
$$

## Depends on

- [overlap implies distance](../part-01/overlap-implies-distance.md)

## Proof

For the first estimate, assume that ${\mathrm{s}}({\mathfrak p}) < s(J)$, then in particular ${\mathrm{s}}({\mathfrak p}) \le {\mathrm{s}}({\mathfrak u}_1)$. Since ${\mathfrak p} \notin \mathfrak{S}$, we have by [overlap implies distance](../part-01/overlap-implies-distance.md) that ${\mathcal{I}}({\mathfrak p}) \cap {\mathcal{I}}({\mathfrak u}_1) = \emptyset$. Since $B\Big(c(J), \frac{1}{4} D^{s(J)}\Big) \subset {\mathcal{I}}(J) \subset {\mathcal{I}}({\mathfrak u}_1)$, this implies

$$
\rho(c(J), {\mathrm{c}}({\mathfrak p})) \ge \frac{1}{4}D^{s(J)}\,.
$$

On the other hand

$$
\rho(c(J), {\mathrm{c}}({\mathfrak p})) \le \frac{1}{8} D^{s(J)} + 8 D^{{\mathrm{s}}({\mathfrak p})}\,,
$$

by our assumption. Thus $D^{{\mathrm{s}}({\mathfrak p})} \ge 64^{-1} D^{s(J)}$, which contradicts [(1)](../../proof-of-metric-space-carleson-overview/README.md) and $a \ge 4$.

For the second estimate, assume that ${\mathrm{s}}({\mathfrak p}) > s(J) + 3$. Since $J \in \mathcal{J}'$, we have $J \subsetneq {\mathcal{I}}({\mathfrak u}_1)$. Thus there exists $J' \in \mathcal{D}$ with $J \subset J'$ and $s(J') = s(J) + 1$, by [(7)](../../proof-of-metric-space-carleson-overview/README.md) and [(8)](../../proof-of-metric-space-carleson-overview/README.md). By definition of $\mathcal{J}'$, there exists some ${\mathfrak p}' \in \mathfrak{S}$ such that ${\mathcal{I}}({\mathfrak p}') \subset B(c(J'), 100 D^{s(J) + 2})$. On the other hand, since $B({\mathcal{I}}({\mathfrak p})) \cap B^\circ(J) \ne \emptyset$, by the triangle inequality it holds that

$$
B(c(J'), 100 D^{s(J) + 3}) \subset B({\mathrm{c}}({\mathfrak p}), 10 D^{{\mathrm{s}}({\mathfrak p})})\,.
$$

Using the definition of $\mathfrak{S}$, we have

$$
2^{Zn/2} \le d_{{\mathfrak p}'}({\mathcal{Q}}({\mathfrak u}_1), {\mathcal{Q}}({\mathfrak u}_2)) \le d_{B(c(J'), 100 D^{s(J) + 2})}({\mathcal{Q}}({\mathfrak u}_1), {\mathcal{Q}}({\mathfrak u}_2))\,.
$$

By [(10)](../../introduction/README.md), this is

$$
\le 2^{-100a} d_{B(c(J'), 100 D^{s(J) + 3})}({\mathcal{Q}}({\mathfrak u}_1), {\mathcal{Q}}({\mathfrak u}_2))
$$

$$
\le 2^{-100a} d_{B({\mathrm{c}}({\mathfrak p}), 10 D^{{\mathrm{s}}({\mathfrak p})})}({\mathcal{Q}}({\mathfrak u}_1), {\mathcal{Q}}({\mathfrak u}_2))\,,
$$

and by [(8)](../../introduction/README.md) and the definition of $\mathfrak{S}$

$$
\le 2^{-94a} d_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak u}_1), {\mathcal{Q}}({\mathfrak u}_2)) \le 2^{-94a} 2^{Zn/2}\,.
$$

This is a contradiction, the second estimate follows.

## Lean

Formalized as [`TileStructure.Forest.limited_scale_impact`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.limited_scale_impact).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 5692](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L5692)
