---
declaration: definition
origin: cited
lean: ConNF.StrSet
statement: formalized
---

# structural set

The type of *$\alpha$-structural sets*, denoted $\mathsf{StrSet}_\alpha$, is defined by well-founded recursion on $\lambda^\bot$.

- $\mathsf{StrSet}_\bot := {\mathcal A}$;
- $\mathsf{StrSet}_\alpha := \prod_{\beta : \lambda^\bot} \beta < \alpha \to \operatorname{\mathsf{Set}} \mathsf{StrSet}_\beta$ where $\alpha : \lambda$.

These equalities will in fact only be equivalences in the formalisation. We define the action of $\alpha$-permutations (more precisely, inhabitants of some type with a $\texttt{StrPermClass}_\alpha$ instance) on $\alpha$-structural sets by well-founded recursion.

- $\pi(x) = \pi_{\operatorname{\mathsf{nil}}(\bot)}(x)$ if $\alpha \equiv \bot$;
- $\pi(x) = (\beta, h \mapsto \pi_h[x(\beta, h)])$ if $\alpha : \lambda$.

## Depends on

- [structural permutation](def-strperm.md)

## Lean

Formalized as [`ConNF.StrSet`](https://leanprover-community.github.io/con-nf/doc/find/#doc/ConNF.StrSet).

## Sources

- [Consistency of New Foundations blueprint: chapters/environment.tex, line 273](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/environment.tex#L273)
