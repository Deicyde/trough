---
declaration: lemma
origin: cited
lean: Cayley.rupPair_inner_ZR, Cayley.shadow_ZR_mul
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

Formalized as [`Cayley.rupPair_inner_ZR`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.rupPair_inner_ZR), [`Cayley.shadow_ZR_mul`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.shadow_ZR_mul).

## Sources

- [Noperthedron blueprint: chapters/reduction.tex, line 72](https://github.com/jcreedcmu/Noperthedron/blob/0143f65be7f59b3ac09b99debb9c37944a0a2f4b/blueprint/src/chapters/reduction.tex#L72)
