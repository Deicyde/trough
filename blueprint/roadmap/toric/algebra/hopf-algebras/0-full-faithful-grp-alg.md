---
declaration: proposition
origin: cited
lean: MonoidAlgebra.mapDomainBialgHomMulEquiv, AddMonoidAlgebra.mapDomainBialgHomAddEquiv, commGrpAlg.fullyFaithful, commGrpAlg.instFull, commGrpAlg.instFaithful
statement: formalized
proof: formalized
---

# The group algebra functor is fully faithful

Let $R$ be a domain. The functor $G \rightsquigarrow R[G]$ from the category of groups to the category of Hopf algebras over $R$ is fully faithful.

## Depends on

- [The group algebra functor](0-grp-alg.md)

## Proof depends on

- [Group-like elements in a group algebra](0-grp-like-grp-alg.md)
- [Bialgebra homs preserve group-like elements](0-grp-like-map.md)

## Proof

The functor is clearly faithful. Now for the full part, if $f : R[G] \to R[H]$ is a Hopf algebra hom, then we get a series of maps

$$
G \simeq \text{ group-like elements of } R[G] \to \text{ group-like elements of } R[H] \simeq H
$$

and each map separately is clearly multiplicative.

## Lean

Formalized as [`MonoidAlgebra.mapDomainBialgHomMulEquiv`](https://yaeldillies.github.io/toric/docs/find/#doc/MonoidAlgebra.mapDomainBialgHomMulEquiv), [`AddMonoidAlgebra.mapDomainBialgHomAddEquiv`](https://yaeldillies.github.io/toric/docs/find/#doc/AddMonoidAlgebra.mapDomainBialgHomAddEquiv), [`commGrpAlg.fullyFaithful`](https://yaeldillies.github.io/toric/docs/find/#doc/commGrpAlg.fullyFaithful), [`commGrpAlg.instFull`](https://yaeldillies.github.io/toric/docs/find/#doc/commGrpAlg.instFull), [`commGrpAlg.instFaithful`](https://yaeldillies.github.io/toric/docs/find/#doc/commGrpAlg.instFaithful).

## Sources

- [Toric varieties blueprint: chapters/2-3-hopf-algebras.tex, line 619](https://github.com/YaelDillies/toric/blob/5956b80249ec5416a266f68b5142606b060d7628/blueprint/src/chapters/2-3-hopf-algebras.tex#L619)
