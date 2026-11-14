---
declaration: definition
origin: cited
lean: ConNF.TypeIndex
statement: formalized
---

# type index

The type of *type indices* is $\lambda^\bot := \texttt{WithBot}(\lambda)$: the collection of *proper type indices* $\lambda$ together with a designated symbol $\bot$ which is smaller than all proper type indices. Note that $\operatorname{\mathsf{ot}}(\lambda^\bot) = \operatorname{\mathsf{ot}}(\lambda)$, and hence that for each $\alpha : \lambda^\bot$,

$$
\#\{ \beta : \lambda^\bot \mid \beta < \alpha \} \leq \#\{ \beta : \lambda^\bot \mid \beta \leq \alpha \} < \operatorname{\mathsf{cof}}(\operatorname{\mathsf{ord}}(\#\mu))
$$

## Depends on

- [model parameters](def-params.md)

## Lean

Formalized as [`ConNF.TypeIndex`](https://leanprover-community.github.io/con-nf/doc/find/#doc/ConNF.TypeIndex).

## Sources

- [Consistency of New Foundations blueprint: chapters/environment.tex, line 50](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/environment.tex#L50)
