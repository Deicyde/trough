---
declaration: definition
origin: cited
lean: ConNF.Tangle
statement: formalized
---

# tangle

Let $\alpha$ be a type index with model data. An *$\alpha$-tangle* is a pair $t = (x, S)$ where $x$ is a tangled set of type $\alpha$ and $S$ is an $\alpha$-support for $x$. We define $\operatorname{\mathsf{set}}(t) = x$ and $\operatorname{\mathsf{supp}}(t) = S$. The type of $\alpha$-tangles is denoted $\mathsf{Tang}_\alpha$. Allowable permutations $\rho$ act on tangles by $\rho((x, S)) = (\rho(x), \rho(S))$, and so $\operatorname{\mathsf{supp}}(t)$ supports $t$ for its action under the allowable permutations. Therefore, each tangled set $x$ is of the form $\operatorname{\mathsf{set}}(t)$ for some tangle $t$.

## Depends on

- [model data](def-modeldata.md)

## Lean

Formalized as [`ConNF.Tangle`](https://leanprover-community.github.io/con-nf/doc/find/#doc/ConNF.Tangle).

## Sources

- [Consistency of New Foundations blueprint: chapters/environment.tex, line 366](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/environment.tex#L366)
