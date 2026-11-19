---
declaration: definition
origin: cited
lean: MIPRE.LCS.SolutionGroup
statement: formalized
---

# Solution group

The *solution group* of an LCS instance is the group presented by generators $g_1, \dots, g_s$ and $J$ subject to the relations: all generators are involutions, $J$ is central, variables occurring in a common equation commute, and $\prod_{j \in V_i} g_j = J^{b_i}$ for each equation $i$. Operator solutions of the system correspond to representations sending $J \mapsto -I$ (in Lean, `MIPRE.LCS.SolutionGroup.solutionGroupRepresentationOfEPRLoss`).

## Depends on

- [LCS instance](def-lcs-instance.md)

## Lean

Formalized as [`MIPRE.LCS.SolutionGroup`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LCS.SolutionGroup).

## Sources

- [MIP* = RE blueprint: content/02_foundations.tex, line 365](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/02_foundations.tex#L365)
