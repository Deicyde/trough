---
declaration: definition
origin: cited
lean: ConNF.Small
statement: formalized
---

# small

A set $s : \operatorname{\mathsf{Set}}(\tau)$ is called *small* if $\#s < \#\kappa$. Smallness is stable under subset, intersection, small-indexed unions, symmetric difference, direct image, injective preimage, and many other operations (each of which should be its own lemma when formalised). Sets $s, t : \operatorname{\mathsf{Set}}(\tau)$ are called *near* if $s \mathrel{\triangle} t$ is small; in this case, we write $s \mathrel{\overset{N}{\sim}} t$. Nearness is an equivalence relation. If $s \mathrel{\overset{N}{\sim}} t$ and $u$ is small, then $s \mathrel{\overset{N}{\sim}} (t \mathbin{\diamond} u)$, where $\diamond$ is one of $\cup, \cap, \setminus, \mathrel{\triangle}$.

## Depends on

- [model parameters](def-params.md)

## Lean

Formalized as [`ConNF.Small`](https://leanprover-community.github.io/con-nf/doc/find/#doc/ConNF.Small).

## Sources

- [Consistency of New Foundations blueprint: chapters/environment.tex, line 59](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/environment.tex#L59)
