---
declaration: lemma
origin: cited
lean: Submonoid.units_isCompact
statement: formalized
discussion: https://github.com/ImperialCollegeLondon/FLT/issues/588
---

# Submonoid.units_isCompact

If $M$ is a Hausdorff topological monoid and $U$ is a compact submonoid, then the units $U^\times$ of $U$ are naturally a compact subgroup of $M^\times$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

First I claim that $M^\times$ embedded in $M\times M$ via $g\mapsto (g,g^{-1})$ is a closed subset of $M\times M$. Indeed, if $p:M\times M\to M$ is $(a,b)\mapsto ab$ and $q:M\times M\to M$ is $(a,b)\mapsto ba$, then $p$ and $q$ are continuous, $M^\times\subseteq M\times M$ is the intersection $p^{-1}\{1\}\cap q^{-1}\{1\}$, and $\{1\}$ is closed because $M$ is Hausdorff.

We have $U\times U$ is a compact subset of $M\times M$, and so $U^\times=M^\times\cap U\times U$ is a closed subspace of a compact space and is thus compact.

## Lean

Stated as [`Submonoid.units_isCompact`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/Submonoid.units_isCompact); the blueprint marks no proof of it as formalized.

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/HeckeOperatorProject.tex, line 273](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/HeckeOperatorProject.tex#L273)
