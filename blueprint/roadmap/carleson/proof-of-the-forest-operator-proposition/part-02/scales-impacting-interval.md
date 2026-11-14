---
declaration: lemma
origin: cited
lean: TileStructure.Forest.scales_impacting_interval
statement: formalized
proof: formalized
---

# scales impacting interval

Let ${\mathfrak C} = {\mathfrak T}({\mathfrak u}_1)$ or ${\mathfrak C} = {\mathfrak T}({\mathfrak u}_2) \cap \mathfrak{S}$. Then for each $J \in \mathcal{J}'$ and ${\mathfrak p} \in {\mathfrak C}$ with $B({\mathcal{I}}({\mathfrak p})) \cap B'(J) \neq \emptyset$, we have ${\mathrm{s}}({\mathfrak p}) \ge s(J)$.

## Depends on

- [overlap implies distance](../part-01/overlap-implies-distance.md)

## Proof

By [overlap implies distance](../part-01/overlap-implies-distance.md), we have that in both cases, ${\mathfrak C} \subset \mathfrak{S}$. If ${\mathfrak p} \in {\mathfrak C}$ with $B({\mathcal{I}}({\mathfrak p})) \cap B'(J) \neq \emptyset$ and ${\mathrm{s}}({\mathfrak p}) < s(J)$, then ${\mathcal{I}}({\mathfrak p}) \subset B(c(J), 100 D^{s(J) + 1})$. Since ${\mathfrak p} \in \mathfrak{S}$, it follows from the definition of $\mathcal{J}'$ that $s(J) = -S$, which contradicts ${\mathrm{s}}({\mathfrak p}) < s(J)$.

## Lean

Formalized as [`TileStructure.Forest.scales_impacting_interval`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.scales_impacting_interval).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 5789](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L5789)
