---
declaration: lemma
origin: cited
lean: TileStructure.Forest.adjoint_tile_support1, TileStructure.Forest.adjoint_tile_support2
statement: formalized
proof: formalized
---

# adjoint tile support

For each ${\mathfrak p} \in {\mathfrak P}$, we have

$$
T_{{\mathfrak p}}^* g = \mathbf{1}_{B({\mathrm{c}}({\mathfrak p}), 5D^{{\mathrm{s}}({\mathfrak p})})} T_{{\mathfrak p}}^* \mathbf{1}_{{\mathcal{I}}({\mathfrak p})} g\,.
$$

For each ${\mathfrak u} \in {\mathfrak U}$ and each ${\mathfrak p} \in {\mathfrak T}({\mathfrak u})$, we have

$$
T_{{\mathfrak p}}^* g = \mathbf{1}_{{\mathcal{I}}({\mathfrak u})} T_{{\mathfrak p}}^* \mathbf{1}_{{\mathcal{I}}({\mathfrak u})} g\,.
$$

## Depends on

- [kernel summand](../../proof-of-metric-space-carleson-overview/kernel-summand.md)

## Proof

By [(30)](../../proof-of-metric-space-carleson-overview/README.md), $E({\mathfrak p}) \subset {\mathcal{I}}({\mathfrak p}) \subset {\mathcal{I}}({\mathfrak u})$. Thus by [(25)](README.md)

$$
T_{{\mathfrak p}}^* g(x) = T_{{\mathfrak p}}^* (\mathbf{1}_{{\mathcal{I}}({\mathfrak p})} g)(x)
$$

$$
= \int_{E({\mathfrak p})} \overline{K_{{\mathrm{s}}({\mathfrak p})}(y,x)} e(-{Q}(y)(x) + {Q}(y)(y)) \mathbf{1}_{{\mathcal{I}}({\mathfrak p})}(y) g(y) \, \mathrm{d}\mu(y)\,.
$$

If this integral is not $0$, then there exists $y \in {\mathcal{I}}({\mathfrak p})$ such that $K_{{\mathrm{s}}({\mathfrak p})}(y,x) \ne 0$. By [(65)](../../proof-of-metric-space-carleson-overview/kernel-summand.md), [(10)](../../proof-of-metric-space-carleson-overview/README.md) and the triangle inequality, it follows that

$$
x \in B({\mathrm{c}}({\mathfrak p}), 5 D^{{\mathrm{s}}({\mathfrak p})})\, .
$$

Thus

$$
T_{{\mathfrak p}}^* g(x) = \mathbf{1}_{B({\mathrm{c}}({\mathfrak p}), 5D^{{\mathrm{s}}({\mathfrak p})})}(x) T_{{\mathfrak p}}^* (\mathbf{1}_{{\mathcal{I}}({\mathfrak p})} g)(x)\,.
$$

The second claimed equation follows now since ${\mathcal{I}}({\mathfrak p}) \subset {\mathcal{I}}({\mathfrak u})$ and by [(35)](../../proof-of-metric-space-carleson-overview/README.md) we have $B({\mathrm{c}}({\mathfrak p}), 5D^{{\mathrm{s}}({\mathfrak p})}) \subset {\mathcal{I}}({\mathfrak u})$.

## Lean

Formalized as [`TileStructure.Forest.adjoint_tile_support1`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.adjoint_tile_support1), [`TileStructure.Forest.adjoint_tile_support2`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.adjoint_tile_support2).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 5211](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L5211)
