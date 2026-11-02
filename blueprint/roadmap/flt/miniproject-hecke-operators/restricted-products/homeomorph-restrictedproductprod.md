---
declaration: lemma
origin: cited
lean: Homeomorph.restrictedProductProd
statement: formalized
proof: formalized
discussion: https://github.com/ImperialCollegeLondon/FLT/issues/568
---

# Homeomorph.restrictedProductProd

If $A_i$ is a family of topological spaces equipped with open subsets $B_i$, and if $C_i$ is a family of topological spaces equipped with open subsets $D_i$, and if we equip $A_i\times C_i$ with the open subset $B_i\times D_i$, then the natural bijection $\prod'_i(A_i\times C_i)=\left(\prod'_iA_i\right)\times\left(\prod'_iB_i\right)$ is a homeomorphism.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

We need to check continuity in both directions. The easy way is continuity of the map from the restricted product to the map from the binary product; the lemma RestrictedProduct.continuous\_dom in mathlib tells us that a map from a restricted product is continuous when its restriction to $\left(\prod_{i\in S}(A_i\times C_i)\right)\times\left(\prod_{i\notin S}(B_i\times D_i)\right)$ is continuous for all finite $S\subseteq I$; the universal property of the binary product tells us that the map into the binary product is continuous iff the maps into the factors are continuous, but the map into $\prod'_iX_i$ is a product of the natural maps from $\left(\prod_{i\in S}(A_i\times C_i)\right)\times\left(\prod_{i\notin S}(B_i\times D_i)\right)$ to $\left(\prod_{i\in S}A_i\right)\times\left(\prod_{i\notin S}B_i\right)$ and the inclusion, and both are known to be continuous (an arbitrary product of continuous maps is continuous, and the other claim is in the restricted product API in mathlib).

The harder direction is the other way, because we are working against both universal properties. The trick is RestrictedProduct.continuous\_dom\_prod in mathlib (this is where we assume $B_i$ and $D_i$ are open), which tells us that a map out of a binary product of restricted products is continuous when its restriction to $\left(\left(\prod_{i\in S}A_i\right)\times\left(\prod_{i\notin S}B_i\right)\right)\times \left(\left(\prod_{i\in S}C_i\right)\times\left(\prod_{i\notin S}D_i\right)\right)$ is, for all finite $S$ (note that the $S$ in the mathlib lemma is actually our $I-S$). The map from this to the restricted product factors through $\left(\prod_{i\in S}(A_i\times C_i)\right)\times\left(\prod_{i\notin S}(B_i\times D_i)\right)$; the first map is a homeomorphism (use the fact that $\prod_iX_i\times Y_i$ is homeomorphic to $\left(\prod_iX_i\right)\times\left(\prod_iY_i\right)$), and the second is continuous by definition of the topology on a restricted product.

## Lean

Formalized as [`Homeomorph.restrictedProductProd`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/Homeomorph.restrictedProductProd).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/HeckeOperatorProject.tex, line 160](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/HeckeOperatorProject.tex#L160)
