---
declaration: lemma
origin: cited
lean: TileStructure.Forest.boundary_overlap
statement: formalized
proof: formalized
---

# boundary overlap

For every cube $I \in \mathcal{D}$, there exist at most $2^{9a}$ cubes $J \in \mathcal{D}$ with $s(J) = s(I)$ and $B(c(I), 16D^{s(I)}) \cap B(c(J), 16 D^{s(J)}) \ne \emptyset$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Suppose that $B(c(I), 16 D^{s(I)}) \cap B(c(J), 16 D^{s(J)}) \ne \emptyset$ and $s(I) = s(J)$. Then $B(c(I), 33 D^{s(I)}) \subset B(c(J), 128 D^{s(J)})$. Hence by the doubling property [(5)](../../introduction/README.md)

$$
2^{9a}\mu(B(c(J), \frac{1}{4}D^{s(J)})) \ge \mu(B(c(I), 33 D^{s(I)}))\,,
$$

and by the triangle inequality, $B(c(J), \frac{1}{4}D^{s(J)})$ is contained in $B(c(I), 33 D^{s(I)})$.

If $\mathcal{C}$ is any finite collection of cubes $J \in \mathcal{D}$ satisfying $s(J) = s(I)$ and

$$
B(c(I), 16 D^{s(I)}) \cap B(c(J), 16 D^{s(J)}) \ne\emptyset\ ,
$$

then it follows from [(10)](../../proof-of-metric-space-carleson-overview/README.md) and pairwise disjointedness of cubes of the same scale [(8)](../../proof-of-metric-space-carleson-overview/README.md) that the balls $B(c(J), \frac{1}{4} D^{s(J)})$ are pairwise disjoint. Hence

$$
\begin{aligned}
\mu(B(c(I), 33 D^{s(I)})) &\ge \sum_{J \in \mathcal{C}} \mu(B(c(J), \frac{1}{4}D^{s(J)}))\\
&\ge |\mathcal{C}| 2^{-9a} \mu(B(c(I), 33 D^{s(I)}))\,.
\end{aligned}
$$

Since $\mu$ is doubling and $\mu \ne 0$, we have $\mu(B(c(I), 33D^{s(I)})) > 0$. The lemma follows after dividing by $2^{-9a}\mu(B(c(I), 33D^{s(I)}))$.

## Lean

Formalized as [`TileStructure.Forest.boundary_overlap`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.boundary_overlap).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 4889](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L4889)
