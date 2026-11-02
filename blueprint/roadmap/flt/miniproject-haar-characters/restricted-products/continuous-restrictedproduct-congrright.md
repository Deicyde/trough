---
declaration: lemma
origin: cited
lean: Continuous.restrictedProduct_congrRight
statement: formalized
proof: formalized
discussion: https://github.com/ImperialCollegeLondon/FLT/issues/531
---

# Continuous.restrictedProduct\_congrRight

If the $A_i$ and $B_i$ are topological spaces and the $\phi_i$ are continuous functions, then the restricted product $\phi = \prod'_i\phi_i$ is a continuous function.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

We use the universal property RestrictedProduct.continuous\_dom of the topology in mathlib to reduce to the claim that for all finite $S$, the induced map $A_S:=\prod_{i\in S}A_i\times\prod_{i\notin S}C_i\to B$ is continuous. Because the inclusion $A_S\to A_T$ is continuous for $S\subseteq T$ we are reduced to checking this claim for $S$ sufficiently large that it contains all of the $i$ for which $\phi(C_i)\not=D_i$. For such $S$, this map $A_S\to B$ factors as $A_S\to B_S\to B$ and $B_S\to B$ is continuous, so it suffices to prove that $A_S\to B_S$ is continuous, but this is just a product of continuous maps.

## Lean

Formalized as [`Continuous.restrictedProduct_congrRight`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/Continuous.restrictedProduct_congrRight).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/HaarCharacterProject.tex, line 618](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/HaarCharacterProject.tex#L618)
