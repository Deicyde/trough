---
declaration: definition
origin: cited
lean: ConNF.instPreorderSupport
statement: formalized
---

# StrSupport.Occurs

We define a preorder $\preceq$ on base supports by $S \preceq T$ if and only if $\operatorname{\mathsf{im}} S^{\mathcal A} \subseteq \operatorname{\mathsf{im}} T^{\mathcal A}$ and $\operatorname{\mathsf{im}} S^{\mathcal N} \subseteq \operatorname{\mathsf{im}} T^{\mathcal N}$. For $\beta$-supports, we define $S \preceq T$ if and only if $S_A \preceq T_A$ for each $A$.

## Depends on

- [structural support](../../setting-up-the-environment/the-structural-hierarchy/def-strsupport.md)

## Lean

Formalized as [`ConNF.instPreorderSupport`](https://leanprover-community.github.io/con-nf/doc/find/#doc/ConNF.instPreorderSupport).

## Sources

- [Consistency of New Foundations blueprint: chapters/counting.tex, line 2](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/counting.tex#L2)
