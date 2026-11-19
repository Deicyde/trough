---
declaration: definition
origin: cited
lean: ConNF.Support.Strong
statement: formalized
---

# Strong

A $\beta$-support $S$ is *strong* if:

- for every pair of near-litters $N_1, N_2 \in \operatorname{\mathsf{im}} S_A^{\mathcal N}$, we have $\operatorname{\mathsf{interf}}(N_1, N_2) \subseteq \operatorname{\mathsf{im}} S_A^{\mathcal A}$; and
- for every inflexible path $I = (\gamma,\delta,\varepsilon,A)$ and $t : \mathsf{Tang}_\delta$, if there is a near-litter $N \in \operatorname{\mathsf{im}} S_{{A_\varepsilon}_\bot}^{\mathcal N}$ with $N^\circ = f_{\delta,\varepsilon}(t)$, then $\operatorname{\mathsf{supp}}(t) \preceq S_{A_\delta}$.

## Depends on

- [structural support](../../setting-up-the-environment/the-structural-hierarchy/def-strsupport.md)
- [inflexible path](../../setting-up-the-environment/hypotheses-of-the-recursion/def-inflexiblepath.md)
- [Interference](../../freedom-of-action/base-actions/def-interference.md)

## Lean

Formalized as [`ConNF.Support.Strong`](https://leanprover-community.github.io/con-nf/doc/find/#doc/ConNF.Support.Strong).

## Sources

- [Consistency of New Foundations blueprint: chapters/counting.tex, line 10](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/counting.tex#L10)
