---
declaration: lemma
origin: cited
lean: TileStructure.Forest.biUnion_𝓙, TileStructure.Forest.pairwiseDisjoint_𝓙, TileStructure.Forest.biUnion_𝓛, TileStructure.Forest.pairwiseDisjoint_𝓛
statement: formalized
proof: formalized
---

# dyadic partitions

For each $\mathfrak{S} \subset {\mathfrak P}$, we have

$$
\bigcup_{I \in \mathcal{D}} I = \dot{\bigcup_{J \in \mathcal{J}(\mathfrak{S})}} J\qquad\text{(1)}
$$

and

$$
\bigcup_{I \in \mathcal{D}} I = \dot{\bigcup_{L \in \mathcal{L}(\mathfrak{S})}} L\,.\qquad\text{(2)}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Since $\mathcal{J}(\mathfrak{S})$ is the set of inclusion maximal cubes in $\mathcal{J}_0(\mathfrak{S})$, cubes in $\mathcal{J}(\mathfrak{S})$ are pairwise disjoint by [(8)](../../proof-of-metric-space-carleson-overview/README.md). The same applies to $\mathcal{L}(\mathfrak{S})$.

If $x \in \bigcup_{I \in \mathcal{D}} I$, then there exists by [(7)](../../proof-of-metric-space-carleson-overview/README.md) a cube $I \in \mathcal{D}$ with $x \in I$ and $s(I) = -S$. Then $I \in \mathcal{J}_0(\mathfrak{S})$. There exists an inclusion maximal cube in $\mathcal{J}_0(\mathfrak{S})$ containing $I$. This cube contains $x$ and is contained in $\mathcal{J}(\mathfrak{S})$. This shows one inclusion in (1), the other one follows from $\mathcal{J}(\mathfrak{S}) \subset \mathcal{D}$.

The proof of the two inclusions in (2) is similar.

## Lean

Formalized as [`TileStructure.Forest.biUnion_𝓙`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.biUnion_𝓙), [`TileStructure.Forest.pairwiseDisjoint_𝓙`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.pairwiseDisjoint_𝓙), [`TileStructure.Forest.biUnion_𝓛`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.biUnion_𝓛), [`TileStructure.Forest.pairwiseDisjoint_𝓛`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.pairwiseDisjoint_𝓛).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 4448](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L4448)
