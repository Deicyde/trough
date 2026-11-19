---
declaration: lemma
origin: cited
lean: TileStructure.Forest.moderate_scale_change
statement: formalized
proof: formalized
---

# moderate scale change

If $J, J' \in \mathcal{J'}$ with

$$
B(J) \cap B(J') \ne \emptyset\,,
$$

then $|s(J) - s(J')| \le 1$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

*Proof of moderate scale change.* Suppose that $s(J') < s(J) - 1$. Then $s(J) > -S$. Thus, by the definition of $\mathcal{J}'$ there exists no ${\mathfrak p} \in \mathfrak{S}$ with

$$
{\mathcal{I}}({\mathfrak p}) \subset B(c(J), 100D^{s(J) + 1})\,.\qquad\text{(39)}
$$

Since $s(J') < s(J)$, there exists a cube $J'' \in \mathcal{D}$ with $J \subset J''$ and $s(J'') = s(J') + 1$. By the definition of $\mathcal{J}'$, there exists a tile ${\mathfrak p} \in \mathfrak{S}$ with

$$
{\mathcal{I}}({\mathfrak p}) \subset B(c(J''), 100 D^{s(J')+2})\,.\qquad\text{(40)}
$$

But by the triangle inequality and [(1)](../../proof-of-metric-space-carleson-overview/README.md), we have

$$
B(c(J''), 100 D^{s(J')+2}) \subset B(c(J), 100D^{s(J) + 1})\,,
$$

which contradicts (39) and (40).

## Lean

Formalized as [`TileStructure.Forest.moderate_scale_change`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.moderate_scale_change).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 5447](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L5447)
