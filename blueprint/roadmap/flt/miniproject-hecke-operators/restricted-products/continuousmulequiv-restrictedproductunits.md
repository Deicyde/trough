---
declaration: theorem
origin: cited
lean: ContinuousMulEquiv.restrictedProductUnits
statement: formalized
proof: formalized
discussion: https://github.com/ImperialCollegeLondon/FLT/issues/582
---

# ContinuousMulEquiv.restrictedProductUnits

If $M_i$ are a family of topological monoids equipped with open submonoids $U_i$, then the canonical map $(\prod'_iM_i)^\times\to\prod'_i(M_i^\times)$ is a homeomorphism.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [ContinuousMulEquiv.piUnits](continuousmulequiv-piunits.md)
- [Submonoid.units\_isOpen](submonoid-units-isopen.md)

## Proof

I don't know a clean way of showing that the map from left to right is continuous, so here is a “direct” proof that the map is a homeomorphism. It is certainly an abstract group isomorphism between topological groups. So to prove that it is a homeomorphism it suffices to prove that it is a homeomorphism near the identity, or equivalently that there are open neighbourhoods $X$ and $Y$ of the identity elements on each side such that the map induces a homeomorphism from $X$ to $Y$. We choose $(\prod_i U_i)^\times$ and $\prod_i (U_i^\times)$. Note that the former is open because of lemma [Submonoid.units\_isOpen](submonoid-units-isopen.md). The result now follows from the previous lemma [ContinuousMulEquiv.piUnits](continuousmulequiv-piunits.md).

## Lean

Formalized as [`ContinuousMulEquiv.restrictedProductUnits`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/ContinuousMulEquiv.restrictedProductUnits).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/HeckeOperatorProject.tex, line 329](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/HeckeOperatorProject.tex#L329)
