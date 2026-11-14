---
declaration: definition
origin: cited
lean: ConNF.BaseApprox.nearLitters
statement: formalized
---

# near-litter graph of an approximation

The *near-litter graph* of $\psi$ is the relation $\psi^{\mathcal N}$ given by setting $(N_1, N_2) \in \psi^{\mathcal N}$ if and only if $(N_1^\circ, N_2^\circ) \in \psi^{\mathcal L}$, $N_1$ and $N_2$ are subsets of $\operatorname{\mathsf{coim}} \psi^{\mathcal A}$, and the image of $\psi^{\mathcal A}$ on $N_1$ is $N_2$ (or equivalently, by [Proposition relation_results](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/auxiliary.tex#L33), the coimage of $\psi^{\mathcal A}$ on $N_2$ is $N_1$).

## Depends on

- [atom graph of an approximation](def-atomgraph.md)

## Lean

Formalized as [`ConNF.BaseApprox.nearLitters`](https://leanprover-community.github.io/con-nf/doc/find/#doc/ConNF.BaseApprox.nearLitters).

## Sources

- [Consistency of New Foundations blueprint: chapters/foa.tex, line 79](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/foa.tex#L79)
