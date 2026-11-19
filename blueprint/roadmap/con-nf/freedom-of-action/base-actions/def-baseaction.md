---
declaration: definition
origin: cited
lean: ConNF.BaseAction
statement: formalized
---

# BaseAction

A *base action* is a pair $\xi = (\xi^{\mathcal A}, \xi^{\mathcal N})$ such that $\xi^{\mathcal A}$ and $\xi^{\mathcal N}$ are relations of atoms and near-litters respectively ([Definition relation_props](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/auxiliary.tex#L3)), such that

- $\xi^{\mathcal A}$ and $\xi^{\mathcal N}$ are defined on small sets;

- $\xi^{\mathcal A}$ is one-to-one;

- if $(a_1, a_2) \in \xi^{\mathcal A}$ and $(N_1, N_2) \in \xi^{\mathcal N}$, then $a_1 \in N_1$ if and only if $a_2 \in N_2$;

- if $(N_1, N_3), (N_2, N_4) \in \xi^{\mathcal N}$, then $N_1^\circ = N_2^\circ$ if and only if $N_3^\circ = N_4^\circ$;

- for each $(N_1, N_3), (N_2, N_4) \in \xi^{\mathcal N}$,

    $$
    \operatorname{\mathsf{interf}}(N_1, N_2) \subseteq \operatorname{\mathsf{coim}} \xi^{\mathcal A};\quad \operatorname{\mathsf{interf}}(N_3, N_4) \subseteq \operatorname{\mathsf{im}} \xi^{\mathcal A}
    $$

Note that these conditions imply that $\xi^{\mathcal N}$ is one-to-one. We define the one-to-one relation $\xi^{\mathcal L}$ by the constructor

$$
(N_1, N_2) \in \xi^{\mathcal N} \to (N_1^\circ, N_2^\circ) \in \xi^{\mathcal L}
$$

The partial order on base actions is defined by $\xi \leq \zeta$ if and only if $\xi^{\mathcal A} \leq \zeta^{\mathcal A}$ and $\xi^{\mathcal N} = \zeta^{\mathcal N}$. (We should make utilities for constructing extensions of base actions, reducing the proof obligations of showing that these are base actions (e.g. removing the last two bullet points and not needing to prove results we already know about $\xi$).) The inverse of $\xi$ is $((\xi^{\mathcal A})^{-1}, (\xi^{\mathcal N})^{-1})$. They act on base supports in the natural way.

## Depends on

- [Interference](def-interference.md)
- [base support](../../setting-up-the-environment/the-structural-hierarchy/def-basesupport.md)

## Lean

Formalized as [`ConNF.BaseAction`](https://leanprover-community.github.io/con-nf/doc/find/#doc/ConNF.BaseAction).

## Sources

- [Consistency of New Foundations blueprint: chapters/foa.tex, line 409](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/foa.tex#L409)
