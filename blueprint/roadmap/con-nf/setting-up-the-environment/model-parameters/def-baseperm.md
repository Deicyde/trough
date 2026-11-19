---
declaration: definition
origin: cited
lean: ConNF.BasePerm
statement: formalized
---

# base permutation

A *base permutation* is a pair $\pi = (\pi^{\mathcal A}, \pi^{\mathcal L})$, where $\pi^{\mathcal A}$ is a permutation ${\mathcal A} \simeq {\mathcal A}$ and $\pi^{\mathcal L}$ is a permutation ${\mathcal L} \simeq {\mathcal L}$, such that

$$
\pi^{\mathcal A}[\operatorname{\mathsf{LS}}(L)] \mathrel{\overset{N}{\sim}} \operatorname{\mathsf{LS}}(\pi^{\mathcal L}(L))
$$

Base permutations have a natural group structure, they act on atoms by $\pi^{\mathcal A}$, they act on litters by $\pi^{\mathcal L}$, and they act on near-litters by (We need to emphasise these properties, rather than emphasising the real definition $\pi(N) = (\pi(N^\circ), \pi[N])$.)

$$
\pi(N)^\circ = \pi(N^\circ);\quad a \in \pi(N) \leftrightarrow a \in \pi[N]
$$

Base permutations are determined by their action on atoms. We should avoid directly referencing $\pi^{\mathcal A}$ and $\pi^{\mathcal L}$ whenever possible.

## Depends on

- [atom](def-atom.md)
- [litter](def-litter.md)
- [near-litter](def-nearlitter.md)

## Lean

Formalized as [`ConNF.BasePerm`](https://leanprover-community.github.io/con-nf/doc/find/#doc/ConNF.BasePerm).

## Sources

- [Consistency of New Foundations blueprint: chapters/environment.tex, line 104](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/environment.tex#L104)
