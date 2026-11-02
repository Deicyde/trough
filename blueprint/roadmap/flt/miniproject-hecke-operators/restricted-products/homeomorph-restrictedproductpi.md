---
declaration: corollary
origin: cited
lean: Homeomorph.restrictedProductPi
statement: formalized
proof: formalized
discussion: https://github.com/ImperialCollegeLondon/FLT/issues/570
---

# Homeomorph.restrictedProductPi

Restricted products (with respect to open subspaces) commute with finite products. In other words, if $j$ runs through a finite set $J$ and $i$ runs through an arbitrary set $I$, and if $X_{ji}$ are topological spaces equipped with open subspaces $Y_{ji}$, then the obvious bijection $\prod'_i(\prod_j X_{ji})=\prod_j\left(\prod'_i X_{ji}\right)$ is a homeomorphism.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Homeomorph.restrictedProductProd](homeomorph-restrictedproductprod.md)

## Proof

Induction on the size of the finite set, using lemma [Homeomorph.restrictedProductProd](homeomorph-restrictedproductprod.md) to get you started.

## Lean

Formalized as [`Homeomorph.restrictedProductPi`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/Homeomorph.restrictedProductPi).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/HeckeOperatorProject.tex, line 206](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/HeckeOperatorProject.tex#L206)
