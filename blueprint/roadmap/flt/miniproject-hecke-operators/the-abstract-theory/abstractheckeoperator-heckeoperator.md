---
declaration: lemma
origin: cited
lean: AbstractHeckeOperator.heckeOperator
statement: formalized
proof: formalized
---

# AbstractHeckeOperator.HeckeOperator

This function is well-defined (that is, independent of the choice of $g_i$), has image in $A^U$ and is $R$-linear.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Well-definedness is because if we change $g_i$ to $g'_i:=g_iv$ for some $v\in V$ then $g_ia=g_i'a$ because $a\in A^V$.

The image lands in $A^U$ because left multiplication by $u$ fixes $UgV$ and hence permutes the cosets $g_iV$.

Finally $R$-linearity is because the $G$-action is $R$-linear.

## Lean

Formalized as [`AbstractHeckeOperator.heckeOperator`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/AbstractHeckeOperator.heckeOperator).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/HeckeOperatorProject.tex, line 52](https://github.com/ImperialCollegeLondon/FLT/blob/019805815d7da565ed1e9f427b6fbd0cbc9d00d3/blueprint/src/chapter/HeckeOperatorProject.tex#L52)
