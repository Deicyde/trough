---
declaration: lemma
origin: cited
lean: Submonoid.units_isOpen
statement: formalized
proof: formalized
discussion: https://github.com/ImperialCollegeLondon/FLT/issues/587
---

# Submonoid.units_isOpen

If $M$ is a topological monoid and $U$ is an open submonoid, then the units $U^\times$ of $U$ are naturally an open subgroup of $M^\times$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

We have $U\times U$ is an open subset of $M\times M$, and if we imagine $M^\times$ embedded in $M\times M$ as explained in the remark above, then the intersection of this subgroup with $U\times U$ is open in $M^\times$ and consists of the elements of $M^\times$ which are in $U$ and whose inverse is also in $U$, which is easily checked to be the copy of $U^\times$ we're talking about.

## Lean

Formalized as [`Submonoid.units_isOpen`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/Submonoid.units_isOpen).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/HeckeOperatorProject.tex, line 248](https://github.com/ImperialCollegeLondon/FLT/blob/019805815d7da565ed1e9f427b6fbd0cbc9d00d3/blueprint/src/chapter/HeckeOperatorProject.tex#L248)
