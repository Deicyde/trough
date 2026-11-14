---
declaration: definition
origin: cited
lean: ConNF.Inflexible
statement: formalized
---

# Inflexible

Let $A$ be a $\beta$-extended type index. A litter $L$ is *$A$-inflexible* if there is an inflexible $\beta$-path $I$ such that $A = ((A_I)_{\varepsilon_I})_\bot$ and $L = f_{\delta_I, \varepsilon_I}(t)$ for some $t : \mathsf{Tang}_{\delta_I}$. The coderivative operation works in the obvious way. A litter can be $A$-inflexible in at most one way. (We should make $A$-inflexibility into a subsingleton structure.)

We say that a $L$ is *$A$-flexible* if it is not $A$-inflexible. (This is not data, but a proposition.) If $L$ is $B_A$-flexible, then $L$ is $A$-flexible.

## Depends on

- [inflexible path](../../setting-up-the-environment/hypotheses-of-the-recursion/def-inflexiblepath.md)

## Lean

Formalized as [`ConNF.Inflexible`](https://leanprover-community.github.io/con-nf/doc/find/#doc/ConNF.Inflexible).

## Sources

- [Consistency of New Foundations blueprint: chapters/foa.tex, line 178](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/foa.tex#L178)
