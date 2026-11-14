---
declaration: lemma
origin: cited
lean: stdLocalisationData
statement: formalized
proof: formalized
---

# ex_localisation

Any continuous map between manifolds has some localisation data.

## Depends on

- [localisation_data](def-localisation-data.md)

## Proof depends on

- [nice_atlas](lem-nice-atlas.md)

## Proof

The preceding lemma (applied to the trivial cover of $N$ by itself) gives a family of $ψ : ι' × F → N$ of open smooth embeddings that the images of $B_F$ cover $N$. We then apply this lemma again to the cover of $M$ given by all $f⁻¹(ψ_j(B_F))$.

## Lean

Formalized as [`stdLocalisationData`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/stdLocalisationData).

## Sources

- [Sphere eversion blueprint: global_convex_integration.tex, line 186](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/global_convex_integration.tex#L186)
