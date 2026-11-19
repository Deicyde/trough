---
declaration: definition
origin: cited
lean: ConNF.ModelData
statement: formalized
---

# model data

Let $\alpha$ be a type index. *Model data* at type $\alpha$ consists of: (A type theory problem with `export`ing this data is that under different assumptions, things like different spellings of $\mathsf{TSet}_\alpha$ might require case splitting on $\alpha$ before they become defeq (e.g. see the old version of `Model/FOA.lean`). There doesn't seem to be an easy way around this.)

- a $\mathsf{TSet}_\alpha$ called the type of *tangled sets* or *t-sets*, which will be our type of model elements at level $\alpha$, with an embedding $U_\alpha : \mathsf{TSet}_\alpha \to \mathsf{StrSet}_\alpha$;
- a group $\mathsf{AllPerm}_\alpha$ called the type of *allowable permutations*, with a $\texttt{StrPermClass}_\alpha$ instance and a specified action on $\mathsf{TSet}_\alpha$,

such that

- if $\rho : \mathsf{AllPerm}_\alpha$ and $x : \mathsf{TSet}_\alpha$, then $\rho(U_\alpha(x)) = U_\alpha(\rho(x))$;
- every t-set of type $\alpha$ has an $\alpha$-support ([structural support](../the-structural-hierarchy/def-strsupport.md)) for its action under the $\alpha$-allowable permutations.

## Depends on

- [structural support](../the-structural-hierarchy/def-strsupport.md)
- [structural set](../the-structural-hierarchy/def-strset.md)

## Lean

Formalized as [`ConNF.ModelData`](https://leanprover-community.github.io/con-nf/doc/find/#doc/ConNF.ModelData).

## Sources

- [Consistency of New Foundations blueprint: chapters/environment.tex, line 349](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/environment.tex#L349)
