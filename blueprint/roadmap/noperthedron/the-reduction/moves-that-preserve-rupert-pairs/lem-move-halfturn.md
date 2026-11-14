---
declaration: lemma
origin: cited
lean: Cayley.rupPair_inner_RzPi, Cayley.shadow_RzPi_mul
statement: formalized
proof: formalized
---

# Inner half-turn

If $(R_o, R_i)$ is a Rupert pair, then so is $(R_o, R_z(\pi) R_i)$.

## Depends on

- [shadow](../../rupert-pairs/shadows-and-the-separation-criterion/def-shadow.md)
- [nopert_point_symmetric](../../the-noperthedron/definition-of-the-noperthedron/lemma-nopert-point-symmetric.md)

## Proof

$R_z(\pi)$ negates the screen and $\operatorname{\mathbf{P}} = -\operatorname{\mathbf{P}}$, so $\mathrm{Sh}(R_z(\pi) R) = -\mathrm{Sh}(R) = \mathrm{Sh}(R)$.

## Lean

Formalized as [`Cayley.rupPair_inner_RzPi`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.rupPair_inner_RzPi), [`Cayley.shadow_RzPi_mul`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.shadow_RzPi_mul).

## Sources

- [Noperthedron blueprint: chapters/reduction.tex, line 57](https://github.com/jcreedcmu/Noperthedron/blob/434011e647523fac1a7116a77df5ac6f283e3fbb/blueprint/src/chapters/reduction.tex#L57)
