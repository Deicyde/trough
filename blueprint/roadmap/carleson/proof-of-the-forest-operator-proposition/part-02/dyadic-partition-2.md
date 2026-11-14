---
declaration: lemma
origin: cited
lean: TileStructure.Forest.union_𝓙₆, TileStructure.Forest.pairwiseDisjoint_𝓙₆
statement: formalized
proof: formalized
---

# dyadic partition 2

We have

$$
{\mathcal{I}}({\mathfrak u}_1) = \dot{\bigcup_{J \in \mathcal{J}'}} J\,.
$$

## Depends on

- [dyadic partitions](../part-01/dyadic-partitions.md)

## Proof

By [dyadic partitions](../part-01/dyadic-partitions.md), it remains only to show that each $J \in \mathcal{J}({\mathfrak T}({\mathfrak u}_1))$ with $J \cap {\mathcal{I}}({\mathfrak u}_1) \ne \emptyset$ is in $\mathcal{J}'$. But if $J \notin \mathcal{J}'$, then by [(8)](../../proof-of-metric-space-carleson-overview/README.md) ${\mathcal{I}}({\mathfrak u}_1) \subsetneq J$. Pick ${\mathfrak p} \in {\mathfrak T}({\mathfrak u}_1)$. Then ${\mathcal{I}}({\mathfrak p}) \subsetneq J$. This contradicts the definition of $\mathcal{J}({\mathfrak T}({\mathfrak u}_1))$.

## Lean

Formalized as [`TileStructure.Forest.union_𝓙₆`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.union_𝓙₆), [`TileStructure.Forest.pairwiseDisjoint_𝓙₆`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.pairwiseDisjoint_𝓙₆).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 6007](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L6007)
