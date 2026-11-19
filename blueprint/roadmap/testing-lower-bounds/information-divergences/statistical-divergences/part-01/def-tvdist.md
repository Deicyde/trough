---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.tvDist
---

# Total variation distance of Mathlib

For finite measures $\mu$ and $\nu$, Mathlib defines the total variation distance as $\vert \mu - \nu \vert(\mathcal X)$, the total mass of the variation of the signed measure $\mu - \nu$. On probability measures it takes values in $[0, 2]$, while $\operatorname{TV}$ takes values in $[0, 1]$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`MeasureTheory.tvDist`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/MeasureTheory.tvDist).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/stat_div.tex, line 630](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/stat_div.tex#L630)
