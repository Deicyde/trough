---
declaration: proposition
origin: cited
lean: CategoryTheory.Functor.Faithful.mapGrp, CategoryTheory.Functor.Full.mapGrp
statement: formalized
proof: formalized
---

# Fully faithful product-preserving functors lift to monoid/group objects

If a finite-products-preserving functor $F : C \to D$ is fully faithful, then so is $\operatorname{Grp}(F) : \operatorname{Grp} C \to \operatorname{Grp} D$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Faithfulness is immediate.

For fullness, assume $f : F(G) \to F(H)$ is a morphism. By fullness of $F$, find $g : G \to H$ such that $F(g) = f$. $g$ is a morphism because we can pull back each diagram from $D$ to $C$ along $F$ which is faithful.

## Lean

Formalized as [`CategoryTheory.Functor.Faithful.mapGrp`](https://yaeldillies.github.io/toric/docs/find/#doc/CategoryTheory.Functor.Faithful.mapGrp), [`CategoryTheory.Functor.Full.mapGrp`](https://yaeldillies.github.io/toric/docs/find/#doc/CategoryTheory.Functor.Full.mapGrp).

## Sources

- [Toric varieties blueprint: chapters/1-2-obj.tex, line 7](https://github.com/YaelDillies/toric/blob/5956b80249ec5416a266f68b5142606b060d7628/blueprint/src/chapters/1-2-obj.tex#L7)
