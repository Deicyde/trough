---
declaration: lemma
origin: cited
lean: IsDedekindDomain.M2.localFullLevel.isOpen
statement: formalized
proof: formalized
---

# M2.localFullLevel.isOpen

$M_2(\mathcal{O}_v)$ is an open subring of $M_2(K_v)$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [NumberField.isOpenAdicCompletionIntegers](numberfield-isopenadiccompletionintegers.md)

## Proof

Topologically $M_2(\mathcal{O}_v)\cong \mathcal{O}_v^4$ as a subset of $K_v^4$ so this follows because a product of compacts is compact and a product of opens is open.

## Lean

Formalized as [`IsDedekindDomain.M2.localFullLevel.isOpen`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/IsDedekindDomain.M2.localFullLevel.isOpen).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/HeckeOperatorProject.tex, line 377](https://github.com/ImperialCollegeLondon/FLT/blob/019805815d7da565ed1e9f427b6fbd0cbc9d00d3/blueprint/src/chapter/HeckeOperatorProject.tex#L377)
