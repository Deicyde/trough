---
declaration: definition
origin: cited
lean: MIPRE.CL.Detyping.TypedDecider, MIPRE.CL.Detyping.TypedDecider.Accepts, MIPRE.CL.Detyping.TypedDecider.Total, MIPRE.CL.Detyping.CutoffProgram
statement: formalized
---

# Typed decider and normal verifier

A typed decider receives $(n,t,x,u,y,a,b)$; a timeout rejects regardless of the output tape. A typed normal verifier is over $\mathbb{F}_2$ and first uses the sampler's dimension query to check $t,u\in T$ and $|x|=|y|=s(n)$. In timeout-counter form, its bound dominates this preliminary computation. For finite decider runtime the answer alphabet consists of strings of length at most $\mathsf{TIME}_D(n)$, and the decision predicate is total. In the ambient model there is no timeout counter: totality is a hypothesis on the typed decider, supplied by the clock of Lemma [Total clocking of arbitrary typed decision programs](lem-detype-total-clock.md), and the answer bound is the executable inner and outer cut of Lemma [Executable detyping decider with two answer cuts](lem-detype-executable-decider.md).

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`MIPRE.CL.Detyping.TypedDecider`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.TypedDecider), [`MIPRE.CL.Detyping.TypedDecider.Accepts`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.TypedDecider.Accepts), [`MIPRE.CL.Detyping.TypedDecider.Total`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.TypedDecider.Total), [`MIPRE.CL.Detyping.CutoffProgram`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.CutoffProgram).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 361](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L361)
