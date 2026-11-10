---
declaration: lemma
origin: cited
lean: Topology.IsOpenEmbedding.isHaarMeasure_comap
statement: formalized
proof: formalized
discussion: https://github.com/ImperialCollegeLondon/FLT/issues/507
---

# Topology.IsOpenEmbedding.isHaarMeasure_comap

Let $A$ and $B$ be locally compact topological groups and let $f:A\to B$ be both a group homomorphism and open embedding. The pullback along $f$ of a Haar measure on $B$ is a Haar measure on $A$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Translation-invariance is easy, compact sets are finite because continuous image of compact is compact, open sets are bounded because image of open is open.

## Lean

Formalized as [`Topology.IsOpenEmbedding.isHaarMeasure_comap`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/Topology.IsOpenEmbedding.isHaarMeasure_comap).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/HaarCharacterProject.tex, line 528](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/HaarCharacterProject.tex#L528)
