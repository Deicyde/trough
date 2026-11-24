---
declaration: lemma
origin: cited
lean: IsDedekindDomain.M2.localFullLevel.isCompact
statement: formalized
proof: formalized
---

# M2.localFullLevel.isCompact

$M_2(\mathcal{O}_v)$ is a compact subring of $M_2(K_v)$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [NumberField.instCompactSpaceAdicCompletionIntegers](../../miniproject-adeles/local-compactness/numberfield-instcompactspaceadiccompletionintege.md)

## Proof

Topologically $M_2(\mathcal{O}_v)\cong \mathcal{O}_v^4$ as a subset of $K_v^4$ so this follows because a product of compacts is compact and a product of opens is open.

## Lean

Formalized as [`IsDedekindDomain.M2.localFullLevel.isCompact`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/IsDedekindDomain.M2.localFullLevel.isCompact).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/HeckeOperatorProject.tex, line 389](https://github.com/ImperialCollegeLondon/FLT/blob/019805815d7da565ed1e9f427b6fbd0cbc9d00d3/blueprint/src/chapter/HeckeOperatorProject.tex#L389)
