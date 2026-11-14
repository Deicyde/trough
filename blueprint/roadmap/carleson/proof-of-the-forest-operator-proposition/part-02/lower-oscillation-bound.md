---
declaration: lemma
origin: cited
lean: TileStructure.Forest.lower_oscillation_bound
statement: formalized
proof: formalized
---

# lower oscillation bound

For all $J \in \mathcal{J}'$, we have that

$$
d_{B(J)}({\mathcal{Q}}({\mathfrak u}_1), {\mathcal{Q}}({\mathfrak u}_2)) \ge 2^{-201a^3} 2^{Zn/2}\,.
$$

## Depends on

- [overlap implies distance](../part-01/overlap-implies-distance.md)

## Proof

Since $\emptyset \ne {\mathfrak T}({\mathfrak u}_1) \subset \mathfrak{S}$ by [overlap implies distance](../part-01/overlap-implies-distance.md), there exists at least one tile ${\mathfrak p} \in \mathcal{S}$ with ${\mathcal{I}}({\mathfrak p}) \subsetneq {\mathcal{I}}({\mathfrak u}_1)$. Thus ${\mathcal{I}}({\mathfrak u}_1) \notin \mathcal{J}'$, so $J \subsetneq {\mathcal{I}}({\mathfrak u}_1)$. Thus there exists a cube $J' \in \mathcal{D}$ with $J \subset J'$ and $s(J') = s(J) + 1$, by [(7)](../../proof-of-metric-space-carleson-overview/README.md) and [(8)](../../proof-of-metric-space-carleson-overview/README.md). By definition of $\mathcal{J'}$ and the triangle inequality, there exists ${\mathfrak p} \in \mathfrak{S}$ such that

$$
{\mathcal{I}}({\mathfrak p}) \subset B(c(J'), 100 D^{s(J') + 1}) \subset B(c(J), 128 D^{s(J)+2})\,.
$$

Thus, by definition of $\mathfrak{S}$:

$$
\begin{aligned}
2^{Zn/2} \le d_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak u}_1), {\mathcal{Q}}({\mathfrak u}_2)) \le d_{B(c(J), 128 D^{s(J)+2})}({\mathcal{Q}}({\mathfrak u}_1), {\mathcal{Q}}({\mathfrak u}_2))\,.
\end{aligned}
$$

By the doubling property [(8)](../../introduction/README.md), this is

$$
\le 2^{200a^3 + 4a} d_{B(J)}({\mathcal{Q}}({\mathfrak u}_1), {\mathcal{Q}}({\mathfrak u}_2))\,,
$$

which gives the lemma using $a \ge 4$.

## Lean

Formalized as [`TileStructure.Forest.lower_oscillation_bound`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.lower_oscillation_bound).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 5929](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L5929)
