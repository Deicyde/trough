---
declaration: theorem
origin: cited
---

# IsDedekindDomain.AKLB.finitePresentation

$B$ is a finitely-presented $A$-module.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

$A$ is Noetherian as it is a Dedekind domain, so it suffices to prove that $B$ is finitely-generated as an $A$-module. But this is in mathlib already (a proof is around line 101 of BaseChange.lean in FLT at the time of writing).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/AdeleMiniproject.tex, line 500](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/AdeleMiniproject.tex#L500)
