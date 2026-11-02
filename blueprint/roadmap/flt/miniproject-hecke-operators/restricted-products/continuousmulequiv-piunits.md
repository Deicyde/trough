---
declaration: lemma
origin: cited
lean: ContinuousMulEquiv.piUnits
statement: formalized
proof: formalized
discussion: https://github.com/ImperialCollegeLondon/FLT/issues/581
---

# ContinuousMulEquiv.piUnits

If $U_i$ are topological monoids then the canonical group isomorphism $(\prod_i U_i)^\times=\prod_i(U_i^\times)$ is a homeomorphism.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

We prove that the maps in both directions are continuous. Let's start with the map from left to right.

A map into a product is continuous when the maps to the factors are continuous. A map into the units of a monoid is continuous when the two projection maps to the monoid (the inclusion and the map $u\mapsto u^{-1}$) are continuous (because $M^\times$ has the topology induced from $M\times M$). This reduces us to checking that the maps $(\prod_i U_i)^\times\to U_j$ sending $(u_i)$ to $u_j$ resp $u_j^{-1}$ are continuous. But the former map is the continuous inclusion $(\prod_i U_i)^\times\to\prod_i U_i$ followed by the continuous projection to $U_j$, and the latter map is the continuous inclusion $(\prod_i U_i)^\times\to\prod_i U_i$ sending $x$ to $x^{-1}$ followed by the projection.

To go the other way: because the units have the induced topology it suffices to check that the two maps $\prod_i(U_i^\times)\to\prod_i U_i$ sending $(u_i)$ to $(u_i)$ resp $(u_i^{-1})$ are continuous. A map to a product is continuous when the induced maps to the factors are. A projection from a project is continuous, and the identity and inverse are continuous maps $U_j^\times\to U_j$, and the maps we're concerned with are composites of these maps and are hence continuous.

## Lean

Formalized as [`ContinuousMulEquiv.piUnits`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/ContinuousMulEquiv.piUnits).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/HeckeOperatorProject.tex, line 296](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/HeckeOperatorProject.tex#L296)
