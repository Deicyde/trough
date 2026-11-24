---
declaration: definition
origin: cited
lean: ConNF.BaseAction.Nice
statement: formalized
---

# BaseAction.Nice

A base action $\xi$ is *nice* if whenever $(N_1, N_2) \in \xi^{\mathcal N}$,

$$
N_1 \mathrel{\triangle} \operatorname{\mathsf{LS}}(N_1^\circ) \subseteq \operatorname{\mathsf{coim}} \xi^{\mathcal A};\quad N_2 \mathrel{\triangle} \operatorname{\mathsf{LS}}(N_2^\circ) \subseteq \operatorname{\mathsf{im}} \xi^{\mathcal A}
$$

## Depends on

- [BaseAction](def-baseaction.md)

## Lean

Formalized as [`ConNF.BaseAction.Nice`](https://leanprover-community.github.io/con-nf/doc/find/#doc/ConNF.BaseAction.Nice).

## Sources

- [Consistency of New Foundations blueprint: chapters/foa.tex, line 431](https://github.com/leanprover-community/con-nf/blob/73f4033c7db83bce99c327606ad1ed9e947cd7f9/blueprint/src/chapters/foa.tex#L431)
