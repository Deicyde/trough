---
declaration: lemma
origin: cited
lean: TileStructure.Forest.rowDecomp, TileStructure.Forest.biUnion_rowDecomp, TileStructure.Forest.pairwiseDisjoint_rowDecomp
statement: formalized
proof: formalized
---

# forest row decomposition

Let $({\mathfrak U}, {\mathfrak T})$ be an $n$-forest. Then there exists a decomposition

$$
{\mathfrak U} = \dot{\bigcup_{1 \le j \le 2^n}} {\mathfrak U}_j
$$

such that for all $j = 1, \dotsc, 2^n$ the pair $({\mathfrak U}_j, {\mathfrak T}|_{{\mathfrak U}_j})$ is an $n$-row.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Define recursively ${\mathfrak U}_j$ to be a maximal disjoint set of tiles ${\mathfrak u}$ in

$$
{\mathfrak U} \setminus \bigcup_{j' < j} {\mathfrak U}_{j'}
$$

with inclusion maximal ${\mathcal{I}}({\mathfrak u})$. Properties [(30)](../../proof-of-metric-space-carleson-overview/README.md), -[(35)](../../proof-of-metric-space-carleson-overview/README.md) for $({\mathfrak U}_j, {\mathfrak T}|_{{\mathfrak U}_k})$ follow immediately from the corresponding properties for $({\mathfrak U}, {\mathfrak T})$, and the cubes ${\mathcal{I}}({\mathfrak u}), {\mathfrak u} \in {\mathfrak U}_j$ are disjoint by definition. The collections ${\mathfrak U}_j$ are also disjoint by definition.

Now we show by induction on $j$ that each point is contained in at most $2^n - j$ cubes ${\mathcal{I}}({\mathfrak u})$ with ${\mathfrak u} \in {\mathfrak U} \setminus \bigcup_{j' \le j} {\mathfrak U}_{j'}$. This implies that $\bigcup_{j = 1}^{2^n} {\mathfrak U}_j = {\mathfrak U}$, which completes the proof of the Lemma. For $j = 0$ each point is contained in at most $2^n$ cubes by [(32)](../../proof-of-metric-space-carleson-overview/README.md). For larger $j$, if $x$ is contained in any cube ${\mathcal{I}}({\mathfrak u})$ with ${\mathfrak u} \in {\mathfrak U} \setminus \bigcup_{j' < j} {\mathfrak U}_{j'}$, then it is contained in a maximal such cube. Thus it is contained in a cube in ${\mathcal{I}}({\mathfrak u})$ with ${\mathfrak u} \in {\mathfrak U}_j$. Thus the number ${\mathfrak u} \in {\mathfrak U} \setminus \bigcup_{j' \le j} {\mathfrak U}_{j'}$ with $x\in {\mathcal{I}}({\mathfrak u})$ is zero, or is less than the number of ${\mathfrak u} \in {\mathfrak U} \setminus \bigcup_{j' \le j-1} {\mathfrak U}_{j'}$ with $x \in {\mathcal{I}}({\mathfrak u})$ by at least one.

## Lean

Formalized as [`TileStructure.Forest.rowDecomp`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.rowDecomp), [`TileStructure.Forest.biUnion_rowDecomp`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.biUnion_rowDecomp), [`TileStructure.Forest.pairwiseDisjoint_rowDecomp`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.pairwiseDisjoint_rowDecomp).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 6237](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L6237)
