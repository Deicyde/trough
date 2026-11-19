---
declaration: proposition
origin: cited
lean: CategoryTheory.Functor.essImage_mapGrp
statement: formalized
proof: formalized
---

# Essential image of a functor on monoid/group objects

If $F : C \to D$ is a fully faithful functor between cartesian-monoidal categories, then $\operatorname{Grp}(F) : \operatorname{Grp}(C) \hom \operatorname{Grp}(D)$ has the same essential image as $F$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Equivalences lift to monoid/group object categories](0-grp-equiv.md)

## Proof

Transfer all diagrams.

## Lean

Formalized as [`CategoryTheory.Functor.essImage_mapGrp`](https://yaeldillies.github.io/toric/docs/find/#doc/CategoryTheory.Functor.essImage_mapGrp).

## Sources

- [Toric varieties blueprint: chapters/1-2-obj.tex, line 45](https://github.com/YaelDillies/toric/blob/5956b80249ec5416a266f68b5142606b060d7628/blueprint/src/chapters/1-2-obj.tex#L45)
