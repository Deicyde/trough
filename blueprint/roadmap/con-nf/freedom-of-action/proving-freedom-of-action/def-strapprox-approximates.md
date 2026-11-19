---
declaration: definition
origin: cited
lean: ConNF.StrApprox.Approximates
statement: formalized
---

# approximates

We say that a $\beta$-approximation $\psi$ *approximates* a $\beta$-allowable permutation $\rho$ if $\psi_A^{\mathcal L} \leq \rho_A^{\mathcal L}$ and $\psi_A^{\mathcal A} \leq \rho_A^{\mathcal A}$ for each path $A : \beta \rightsquigarrow \bot$. If $\psi$ approximates $\rho$ then $\psi^n$ approximates $\rho^n$ for each $n : \mathbb Z$. (We should define what it means for a base approximation to approximate a near-litter permutation, and define this in terms of that.) A $\beta$-approximation $\psi$ *exactly approximates* a $\beta$-allowable permutation $\rho$ if $\psi$ approximates $\rho$, and in addition, if $a$ is an atom and $A : \beta \rightsquigarrow \bot$, then $a \notin \operatorname{\mathsf{coim}} \psi_A^{\mathcal A}$ implies $\rho(a)^\circ = \rho(a^\circ)$ and $\rho^{-1}(a)^\circ = \rho^{-1}(a^\circ)$.

## Depends on

- [StrApprox](../structural-approximations/def-strapprox.md)
- [atom graph of an approximation](../base-approximations/def-atomgraph.md)
- [atomGraph_inv](../base-approximations/prop-atomgraph-inv.md)
- [nearLitterGraph_permutative](../base-approximations/prop-nearlittergraph-permutative.md)

## Lean

Formalized as [`ConNF.StrApprox.Approximates`](https://leanprover-community.github.io/con-nf/doc/find/#doc/ConNF.StrApprox.Approximates).

## Sources

- [Consistency of New Foundations blueprint: chapters/foa.tex, line 291](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/foa.tex#L291)
