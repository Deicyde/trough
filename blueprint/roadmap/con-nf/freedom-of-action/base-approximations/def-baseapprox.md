---
declaration: definition
origin: cited
lean: ConNF.BaseApprox
statement: formalized
---

# base approximation

A *base approximation* is a pair $\psi = (\psi^{E{\mathcal A}}, \psi^{\mathcal L})$ such that $\psi^{E{\mathcal A}}$ and $\psi^{\mathcal L}$ are permutative relations of atoms and litters respectively ([Definition relation_props](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/auxiliary.tex#L3)), and for each litter $L$, the set

$$
\operatorname{\mathsf{LS}}(L) \cap \operatorname{\mathsf{coim}} \psi^{E{\mathcal A}}
$$

is small. The relation $\psi^{E{\mathcal A}}$ is called the *exceptional atom graph*, and $\psi^{\mathcal L}$ is called the *litter graph*. We make the following definitions.

- The *inverse* of a base approximation is $\psi^{-1} = ((\psi^{E{\mathcal A}})^{-1}, (\psi^{\mathcal L})^{-1})$.
- If $\psi$ and $\chi$ are base approximations where $\operatorname{\mathsf{coim}} \psi^{E{\mathcal A}} = \operatorname{\mathsf{coim}} \chi^{E{\mathcal A}}$ and $\operatorname{\mathsf{coim}} \psi^{\mathcal L} = \operatorname{\mathsf{coim}} \chi^{\mathcal L}$, then their *composition* $\psi \circ \chi$ is the base approximation $(\psi^{E{\mathcal A}} \circ \chi^{E{\mathcal A}}, \psi^{\mathcal L} \circ \chi^{\mathcal L})$.
- The *$\psi$-sublitter* of a litter $L$, written $L_\psi$, is the near-litter $(L, \operatorname{\mathsf{LS}}(L) \setminus \operatorname{\mathsf{coim}} \psi^{E{\mathcal A}})$.

## Depends on

- [near-litter](../../setting-up-the-environment/model-parameters/def-nearlitter.md)

## Lean

Formalized as [`ConNF.BaseApprox`](https://leanprover-community.github.io/con-nf/doc/find/#doc/ConNF.BaseApprox).

## Sources

- [Consistency of New Foundations blueprint: chapters/foa.tex, line 2](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/foa.tex#L2)
