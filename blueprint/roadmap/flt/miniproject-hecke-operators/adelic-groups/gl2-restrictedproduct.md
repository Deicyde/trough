---
declaration: theorem
origin: cited
lean: IsDedekindDomain.FiniteAdeleRing.GL2.restrictedProduct
statement: formalized
proof: formalized
---

# GL2.restrictedProduct

$G$ is isomorphic and homeomorphic to the restricted product of $GL_2(K_v)$ with respect to the compact open subgroups $GL_2(\mathcal{O}_v)$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [ContinuousMulEquiv.restrictedProductUnits](../restricted-products/continuousmulequiv-restrictedproductunits.md)
- [Homeomorph.restrictedProductMatrix](../restricted-products/homeomorph-restrictedproductmatrix.md)

## Proof

This follows from lemma [ContinuousMulEquiv.restrictedProductUnits](../restricted-products/continuousmulequiv-restrictedproductunits.md) and lemma [Homeomorph.restrictedProductMatrix](../restricted-products/homeomorph-restrictedproductmatrix.md).

## Lean

Formalized as [`IsDedekindDomain.FiniteAdeleRing.GL2.restrictedProduct`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/IsDedekindDomain.FiniteAdeleRing.GL2.restrictedProduct).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/HeckeOperatorProject.tex, line 487](https://github.com/ImperialCollegeLondon/FLT/blob/019805815d7da565ed1e9f427b6fbd0cbc9d00d3/blueprint/src/chapter/HeckeOperatorProject.tex#L487)
