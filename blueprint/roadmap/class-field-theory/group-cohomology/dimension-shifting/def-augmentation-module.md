---
declaration: definition
origin: cited
lean: Rep.aug
statement: formalized
---

# augmentation module

As an example we consider the case of the trivial representation $R$. The induced representation is then the group ring $RG$, which is referred to Mathlib as `Rep.leftRegular R G`; this is a free $R$-module with basis $\mathrm{single}(g,1)$ for $g \in G$. For simplicity we shall write $[g]$ for the basis vector $\mathrm{single}(g,1)$. The map $\mathrm{ind}_1'(R) \to R$ takes $\sum_{g\in G} x_g [g]$ to $\sum_{g \in G} x_g$. This map is commonly called the augmentation, and its kernel $\mathrm{down}(R)$ the *augmentation module*. We shall write $\mathrm{aug}(R,G)$ for this kernel. The kernel $\mathrm{aug}(R,G)$ is spanned by the elements $[g]-[1]$ for $g \in G$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`Rep.aug`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.aug).

## Sources

- [Class field theory blueprint: _2_cohomology.tex, line 1240](https://github.com/kbuzzard/ClassFieldTheory/blob/629ae9ed781748980bb51ab6f5f338ad9d6db3e8/blueprint/src/_2_cohomology.tex#L1240)
