---
declaration: lemma
origin: cited
lean: Cayley.rupPair_inner_gR, Cayley.rupPair_outer_gR, Cayley.shadow_mul_gR
statement: formalized
proof: formalized
---

# Symmetries

If $(R_o, R_i)$ is a Rupert pair, then so are $(R_o g_k, R_i)$ and $(R_o, R_i g_k)$.

## Depends on

- [shadow](../../rupert-pairs/shadows-and-the-separation-criterion/def-shadow.md)
- [noperthedron](../../the-noperthedron/definition-of-the-noperthedron/def-noperthedron.md)

## Proof

$g_k$ permutes the vertices of $\operatorname{\mathbf{P}}$, so $g_k \operatorname{\mathbf{P}} = \operatorname{\mathbf{P}}$ and $\mathrm{Sh}(R g_k) = \mathrm{Sh}(R)$.

## Lean

Formalized as [`Cayley.rupPair_inner_gR`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.rupPair_inner_gR), [`Cayley.rupPair_outer_gR`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.rupPair_outer_gR), [`Cayley.shadow_mul_gR`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.shadow_mul_gR).

## Sources

- [Noperthedron blueprint: chapters/reduction.tex, line 44](https://github.com/jcreedcmu/Noperthedron/blob/434011e647523fac1a7116a77df5ac6f283e3fbb/blueprint/src/chapters/reduction.tex#L44)
