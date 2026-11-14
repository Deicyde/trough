---
declaration: lemma
origin: cited
lean: Cayley.exists_rupPair
statement: formalized
proof: formalized
---

# exists_rup_pair

If $\operatorname{\mathbf{P}}$ is Rupert, then there is a Rupert pair $(R_o, R_i)$ with $R_o, R_i \in SO(3)$.

## Depends on

- [shadow](def-shadow.md)
- [Rupert Polyhedron iff Rupert Set](../rupert-sets/thm-rupert-iff-rupert-set.md)
- [rupert_implies_rot_rupert](../rupert-sets/thm-rupert-implies-rot-rupert.md)
- [nopert_point_symmetric](../../the-noperthedron/definition-of-the-noperthedron/lemma-nopert-point-symmetric.md)

## Proof

Combine Theorem [Rupert Polyhedron iff Rupert Set](../rupert-sets/thm-rupert-iff-rupert-set.md) and Theorem [rupert_implies_rot_rupert](../rupert-sets/thm-rupert-implies-rot-rupert.md); $\operatorname{\mathbf{P}}$ is point-symmetric (Lemma [nopert_point_symmetric](../../the-noperthedron/definition-of-the-noperthedron/lemma-nopert-point-symmetric.md)) and convex.

## Lean

Formalized as [`Cayley.exists_rupPair`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.exists_rupPair).

## Sources

- [Noperthedron blueprint: chapters/prelims.tex, line 73](https://github.com/jcreedcmu/Noperthedron/blob/434011e647523fac1a7116a77df5ac6f283e3fbb/blueprint/src/chapters/prelims.tex#L73)
