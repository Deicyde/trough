---
declaration: definition
origin: cited
lean: ConNF.TypedNearLitters
statement: formalized
---

# typed near-litter

Let $\alpha$ be a proper type index with model data, and suppose that $\mathsf{Tang}_\alpha$ has a position function. We say that $\alpha$ has *typed near-litters* if there is an embedding $\operatorname{\mathsf{typed}}_\alpha : {\mathcal N} \to \mathsf{TSet}_\alpha$ such that

- if $\rho : \mathsf{AllPerm}_\alpha$ and $N : {\mathcal N}$, then $\rho(\operatorname{\mathsf{typed}}_\alpha(N)) = \operatorname{\mathsf{typed}}_\alpha(\rho_\bot(N))$; and
- if $N$ is a near-litter and $t$ is an $\alpha$-tangle such that $\operatorname{\mathsf{set}}(t) = \operatorname{\mathsf{typed}}_\alpha(N)$, we have $\iota(N) \leq \iota(t)$.

Objects of the form $\operatorname{\mathsf{typed}}_\alpha$ are called *typed near-litters*.

## Depends on

- [model data](def-modeldata.md)
- [tangle](def-tangle.md)

## Lean

Formalized as [`ConNF.TypedNearLitters`](https://leanprover-community.github.io/con-nf/doc/find/#doc/ConNF.TypedNearLitters).

## Sources

- [Consistency of New Foundations blueprint: chapters/environment.tex, line 405](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/environment.tex#L405)
