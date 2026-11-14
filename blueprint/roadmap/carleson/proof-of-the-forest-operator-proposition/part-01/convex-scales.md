---
declaration: lemma
origin: cited
lean: TileStructure.Forest.convex_scales
statement: formalized
proof: formalized
---

# convex scales

For each ${\mathfrak u} \in {\mathfrak U}$, we have

$$
\sigma({\mathfrak u}, x) = \mathbb{Z} \cap [\underline{\sigma} ({\mathfrak u}, x), \overline{\sigma} ({\mathfrak u}, x)]\,.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Let $s \in \mathbb{Z}$ with $\underline{\sigma} ({\mathfrak u}, x) \le s \le \overline{\sigma} ({\mathfrak u}, x)$. By definition of $\sigma$, there exists ${\mathfrak p} \in {\mathfrak T}({\mathfrak u})$ with ${\mathrm{s}}({\mathfrak p}) = \underline{\sigma} ({\mathfrak u}, x)$ and $x \in E({\mathfrak p})$, and there exists ${\mathfrak p}'' \in {\mathfrak T}({\mathfrak u})$ with ${\mathrm{s}}({\mathfrak p}'') = \overline{\sigma} ({\mathfrak u}, x)$ and $x \in E({\mathfrak p}'') \subset {\mathcal{I}}({\mathfrak p}'')$. By property [(7)](../../proof-of-metric-space-carleson-overview/README.md) of the dyadic grid, there exists a cube $I \in \mathcal{D}$ of scale $s$ with $x \in I$. By property [(13)](../../proof-of-metric-space-carleson-overview/README.md), there exists a tile ${\mathfrak p}' \in {\mathfrak P}(I)$ with ${Q}(x) \in {\Omega}({\mathfrak p}')$. By the dyadic property [(8)](../../proof-of-metric-space-carleson-overview/README.md) we have ${\mathcal{I}}({\mathfrak p}) \subset {\mathcal{I}}({\mathfrak p}') \subset {\mathcal{I}}({\mathfrak p}'')$, and by [(14)](../../proof-of-metric-space-carleson-overview/README.md), we have ${\Omega}({\mathfrak p}'') \subset {\Omega}({\mathfrak p}') \subset {\Omega}({\mathfrak p})$. Thus ${\mathfrak p} \le {\mathfrak p}' \le{\mathfrak p}''$, which gives with the convexity property [(31)](../../proof-of-metric-space-carleson-overview/README.md) of ${\mathfrak T}({\mathfrak u})$ that ${\mathfrak p}' \in {\mathfrak T}({\mathfrak u})$, so $s \in \sigma({\mathfrak u}, x)$.

## Lean

Formalized as [`TileStructure.Forest.convex_scales`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.convex_scales).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 4417](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L4417)
