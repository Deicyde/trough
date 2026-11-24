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
- [rupert](../def-rupert.md)
- [Common centre](lem-common-center.md)
- [nopert_point_symmetric](../../the-noperthedron/definition-of-the-noperthedron/lemma-nopert-point-symmetric.md)

## Proof

By definition there are $R_i, R_o \in SO(3)$ and an offset $o$ with $o + \mathrm{Sh}(R_i) \subseteq \operatorname{int} \mathrm{Sh}(R_o)$. A shadow is a linear image of $\operatorname{\mathbf{P}}$, so it is convex and point-symmetric (Lemma [nopert_point_symmetric](../../the-noperthedron/definition-of-the-noperthedron/lemma-nopert-point-symmetric.md)), and so is its interior. Lemma [Common centre](lem-common-center.md) removes the offset.

## Lean

Formalized as [`Cayley.exists_rupPair`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.exists_rupPair).

## Sources

- [Noperthedron blueprint: chapters/prelims.tex, line 55](https://github.com/jcreedcmu/Noperthedron/blob/0143f65be7f59b3ac09b99debb9c37944a0a2f4b/blueprint/src/chapters/prelims.tex#L55)
