---
declaration: lemma
origin: cited
lean: exists_surrounding_loops
statement: formalized
proof: formalized
---

# ∃\_surrounding_loops

In the setup of [Proposition ∃\_loops](../introduction/prop-loops.md), assume we have a continuous family $γ$ of loops defined near $K$ which is based at $β$, surrounds $g$ and such that each $γ_x^t$ takes values in $Ω_x$. Then there such a family which is defined on all of $E$ and agrees with $γ$ near $K$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [local_loops](lem-local-loops.md)
- [extend_loops](cor-extend-loops.md)
- [relative_inductive_construction_of_loc](../../from-local-to-global/lem-relative-inductive-construction-of-loc.md)

## Proof

[Lemma local_loops](lem-local-loops.md) proves the existence of local families of surrounding loops and [Corollary extend_loops](cor-extend-loops.md) allows to patch such families hence [Lemma relative_inductive_construction_of_loc](../../from-local-to-global/lem-relative-inductive-construction-of-loc.md) proves global existence.

## Lean

Formalized as [`exists_surrounding_loops`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/exists_surrounding_loops).

## Sources

- [Sphere eversion blueprint: loops.tex, line 550](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/loops.tex#L550)
