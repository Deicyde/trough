---
declaration: lemma
origin: cited
lean: TileStructure.Forest.adjoint_tree_control
statement: formalized
proof: formalized
---

# adjoint tree control

We have for all ${\mathfrak u} \in {\mathfrak U}$ and all bounded $g$ supported on $G$

$$
\|S_{2, {\mathfrak u}} g\|_2 \le 2^{182a^3} \|g\|_2\,.
$$

## Depends on

- [adjoint tree estimate](adjoint-tree-estimate.md)

## Proof

This follows immediately from Minkowski's inequality, [Hardy–Littlewood](../../proof-of-metric-space-carleson-overview/hardy-littlewood.md) and [adjoint tree estimate](adjoint-tree-estimate.md), using that $a \ge 4$.

## Lean

Formalized as [`TileStructure.Forest.adjoint_tree_control`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.adjoint_tree_control).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 5279](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L5279)
