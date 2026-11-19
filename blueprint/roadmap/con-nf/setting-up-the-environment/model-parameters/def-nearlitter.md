---
declaration: definition
origin: cited
lean: ConNF.NearLitter
statement: formalized
---

# near-litter

A *near-litter* is a pair $N = (L, s) : {\mathcal L} \times \operatorname{\mathsf{Set}} {\mathcal A}$ such that $s \mathrel{\overset{N}{\sim}} \operatorname{\mathsf{LS}}(L)$. (Like with atoms, this should be a structure. We should create an actual constructor, rather than using the $\langle - \rangle$ syntax.) We write $(-)^\circ : {\mathcal N} \to {\mathcal L}$ for the operation $(L, s) \mapsto L$. We write $a \in N$ for $a \in s$, where $N = (L, s)$. Near-litters satisfy extensionality: there is at most one choice of $L$ for each $s$. Each near-litter has size $\#\kappa$ when treated as a set of atoms. The type of all near-litters is denoted ${\mathcal N}$, and $\#{\mathcal N} = \#\mu$ (there are $\#\mu$ litters, and $\#\mu$ small sets of atoms by [mathlib](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/auxiliary.tex#L104); the latter observation should be its own lemma).

We have $M \mathrel{\overset{N}{\sim}} N$ if and only if $M^\circ = N^\circ$. If $M^\circ = N^\circ$, then $M \mathrel{\triangle} N$ is small and $M \cap N$ has size $\#\kappa$. If $M^\circ \neq N^\circ$, then $M \cap N$ has size $\#\kappa$ and $M \cap N$ is small.

## Depends on

- [litter](def-litter.md)
- [atom](def-atom.md)

## Lean

Formalized as [`ConNF.NearLitter`](https://leanprover-community.github.io/con-nf/doc/find/#doc/ConNF.NearLitter).

## Sources

- [Consistency of New Foundations blueprint: chapters/environment.tex, line 88](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/environment.tex#L88)
