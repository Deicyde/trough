---
declaration: lemma
origin: cited
lean: AbstractHeckeOperator.comm
statement: formalized
proof: formalized
---

# AbstractHeckeOperator.comm

Say $g,h\in G$ and we have $UgU=\coprod_i g_iU$ and $UhU=\coprod_j h_j$ and we have $g_ih_j=h_jg_i$ for all $i,j$. Then $[UgU][UhU]=[UhU][UgU]$, that is, the Hecke operators acting on $A^U$ commute.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

We have $[UgU][UhU]a=\sum_ig_i(\sum_jh_ja)=\sum_{i,j}g_ih_ja$ and $[UhU][UgU]a=\sum_jh_j\sum_ig_ia=\sum_{j,i}h_jg_ia$ and these sums are equal because $g_ih_j=h_jg_i$.

## Lean

Formalized as [`AbstractHeckeOperator.comm`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/AbstractHeckeOperator.comm).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/HeckeOperatorProject.tex, line 76](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/HeckeOperatorProject.tex#L76)
