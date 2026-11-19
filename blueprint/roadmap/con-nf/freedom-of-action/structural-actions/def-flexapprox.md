---
declaration: definition
origin: cited
lean: ConNF.BaseAction.FlexApprox
statement: formalized
---

# FlexApprox

Let $A : \beta \rightsquigarrow \bot$. An *$A$-flexible approximation* of a base action $\xi$ is a base approximation $\psi$ such that

1. $\xi^{\mathcal A} \leq \psi^{E{\mathcal A}}$;

2. if $L \in \operatorname{\mathsf{coim}} \psi^{\mathcal L}$, then $L$ is $A$-flexible;

3. if $(N_1, N_2) \in \xi^{\mathcal N}$ and $N_1^\circ$ is $A$-flexible, then $(N_1^\circ, N_2^\circ) \in \psi^{\mathcal L}$;

4. if $(N_1, N_2) \in \xi^{\mathcal N}$, then $N_1 \mathrel{\triangle} \operatorname{\mathsf{LS}}(N_1^\circ) \subseteq \operatorname{\mathsf{coim}} \psi^{\mathcal A}$ and $N_2 \mathrel{\triangle} \operatorname{\mathsf{LS}}(N_2^\circ) \subseteq \operatorname{\mathsf{coim}} \psi^{\mathcal A}$;

5. if $(N_1, N_2) \in \xi^{\mathcal N}$, then for each atom $a_2$,

    $$
    a_2 \in N_2 \leftrightarrow (\exists a_1 \in N_1,\, (a_1, a_2) \in \psi^{E{\mathcal A}}) \vee (a_2 \notin \operatorname{\mathsf{coim}} \psi^{E{\mathcal A}} \wedge a_2^\circ = N_2^\circ)
    $$

A *flexible approximation* of a $\beta$-action $\xi$ is a $\beta$-approximation $\psi$ such that for each $A : \beta \rightsquigarrow \bot$, the base approximation $\psi_A$ is an $A$-flexible approximation of $\xi_A$. Flexible approximations are coherent.

## Depends on

- [StrApprox.Coherent](../structural-approximations/def-strapprox-coherent.md)

## Lean

Formalized as [`ConNF.BaseAction.FlexApprox`](https://leanprover-community.github.io/con-nf/doc/find/#doc/ConNF.BaseAction.FlexApprox).

## Sources

- [Consistency of New Foundations blueprint: chapters/foa.tex, line 531](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/foa.tex#L531)
