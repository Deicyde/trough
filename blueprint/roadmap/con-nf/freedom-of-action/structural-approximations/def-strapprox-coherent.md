---
declaration: definition
origin: cited
lean: ConNF.StrApprox.CoherentAt, ConNF.StrApprox.Coherent
statement: formalized
---

# StrApprox.Coherent

A $\beta$-approximation $\psi$ is *coherent* at $(A, L_1, L_2)$ if:

- If $L_1$ is $A$-inflexible with inflexible $\beta$-path $I = (\gamma, \delta, \varepsilon, B)$ and tangle $t : \mathsf{Tang}_\delta$, then there is some $\delta$-allowable permutation $\rho$ such that

    $$
    (\psi_B)_\delta(\operatorname{\mathsf{supp}}(t)) = \rho(\operatorname{\mathsf{supp}}(t))
    $$

    and

    $$
    L_2 = f_{\delta,\varepsilon}(\rho(t))
    $$

    (and hence all $\delta$-allowable permutations $\rho$ such that $(\psi_B)_\delta(\operatorname{\mathsf{supp}}(t)) = \rho(\operatorname{\mathsf{supp}}(t))$ satisfy $L_2 = f_{\delta,\varepsilon}(\rho(t))$).

- If $L_1$ is $A$-flexible, then $L_2$ is $A$-flexible.

We say that $\psi$ is *coherent* if whenever $(L_1, L_2) \in \psi_A^{\mathcal L}$, $\psi$ is coherent at $(A, L_1, L_2)$.

## Depends on

- [StrApprox](def-strapprox.md)
- [Inflexible](def-inflexible.md)

## Lean

Formalized as [`ConNF.StrApprox.CoherentAt`](https://leanprover-community.github.io/con-nf/doc/find/#doc/ConNF.StrApprox.CoherentAt), [`ConNF.StrApprox.Coherent`](https://leanprover-community.github.io/con-nf/doc/find/#doc/ConNF.StrApprox.Coherent).

## Sources

- [Consistency of New Foundations blueprint: chapters/foa.tex, line 191](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/foa.tex#L191)
