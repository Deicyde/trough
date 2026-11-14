---
declaration: definition
origin: cited
lean: ConNF.Interference
statement: formalized
---

# Interference

The *interference* of near-litters $N_1, N_2$ is

$$
\operatorname{\mathsf{interf}}(N_1, N_2) = \begin{cases}
N_1 \mathrel{\triangle} N_2 & \text{if } N_1^\circ = N_2^\circ \\
N_1 \cap N_2 & \text{if } N_1^\circ \neq N_2^\circ
\end{cases}
$$

which is a small set of atoms.

## Depends on

- [near-litter](../../setting-up-the-environment/model-parameters/def-nearlitter.md)

## Lean

Formalized as [`ConNF.Interference`](https://leanprover-community.github.io/con-nf/doc/find/#doc/ConNF.Interference).

## Sources

- [Consistency of New Foundations blueprint: chapters/foa.tex, line 397](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/foa.tex#L397)
