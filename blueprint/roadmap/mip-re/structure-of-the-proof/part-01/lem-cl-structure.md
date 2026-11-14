---
declaration: lemma
origin: cited
lean: MIPRE.CL.CLFun.truncate, MIPRE.CL.CLFun.factorAt, MIPRE.CL.CLFun.mapAt, MIPRE.CL.CLFun.factorOfPrefix, MIPRE.CL.CLFun.mapOfPrefix, MIPRE.CL.CLFun.ExactlyOn, MIPRE.CL.CLFun.SupportedOn.eval_truncate_eq_sum, MIPRE.CL.CLFun.SupportedOn.disjoint_factorAt, MIPRE.CL.CLFun.SupportedOn.factorAt_subset, MIPRE.CL.CLFun.ExactlyOn.biUnion_factorAt, MIPRE.CL.CLFun.SupportedOn.factorOfPrefix_eval, MIPRE.CL.CLFun.SupportedOn.mapOfPrefix_eval
statement: formalized
proof: formalized
---

# Structure of a CL function

Let $L$ be an $\ell$-level CL function on $V$, given with its decomposition data. For $k \in \{1, \ldots, \ell\}$ there are a $k$-level CL function $L_{\leq k} : V \to V$ on $V$, the *$k$-th marginal* (with $L_{\le 0} = 0$ and $L_{\lt k} = L_{\le k-1}$), and, for every prefix $u \in L_{\lt k}(V)$, a register subspace $V_{k,u}$ of $V$, the *$k$-th factor space*, and a linear map $L_{k,u} : V_{k,u} \to V_{k,u}$, the *$k$-th linear map*, such that for all $x \in V$, writing $u_i = L_{\lt i}(x)$:

1. $L_{\leq k}(x) = \sum_{i=1}^{k} L_{i,u_i}\bigl(x^{V_{i,u_i}}\bigr)$, and $L = L_{\le \ell}$;
2. the factor spaces $V_{1,u_1}, \ldots, V_{\ell,u_\ell}$ are pairwise disjoint register subspaces of $V$, and $V = \bigoplus_{i=1}^{\ell} V_{i,u_i}$ when the data are *exact*, that is, when the last level of every branch leaves no coordinate over.

## Depends on

- [Conditionally linear function](def-cl-function.md)

## Proof

This is `lem:cl-kth` of `linear.tex`, by induction on the level. In Lean the marginal is `CLFun.truncate`; the factor space and the linear map of a stage are computed both along a run (`factorAt`, `mapAt`) and from the prefix alone (`factorOfPrefix`, `mapOfPrefix`), and the two agree (`factorOfPrefix_eval`, `mapOfPrefix_eval`): that is what makes the paper's indexing by prefixes well defined, and it is the fact the queries of a sampler rest on. Exactness is `CLFun.ExactlyOn`. The paper states the lemma as an equivalence, with the data normalized so that the factor spaces always exhaust $V$; the formalization keeps the paper's own inductive definition, under which a level-$0$ remainder is allowed, and records exactness as the separate predicate that samplers are required to satisfy.

## Lean

Formalized as [`MIPRE.CL.CLFun.truncate`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.CLFun.truncate), [`MIPRE.CL.CLFun.factorAt`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.CLFun.factorAt), [`MIPRE.CL.CLFun.mapAt`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.CLFun.mapAt), [`MIPRE.CL.CLFun.factorOfPrefix`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.CLFun.factorOfPrefix), [`MIPRE.CL.CLFun.mapOfPrefix`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.CLFun.mapOfPrefix), [`MIPRE.CL.CLFun.ExactlyOn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.CLFun.ExactlyOn), [`MIPRE.CL.CLFun.SupportedOn.eval_truncate_eq_sum`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.CLFun.SupportedOn.eval_truncate_eq_sum), [`MIPRE.CL.CLFun.SupportedOn.disjoint_factorAt`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.CLFun.SupportedOn.disjoint_factorAt), [`MIPRE.CL.CLFun.SupportedOn.factorAt_subset`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.CLFun.SupportedOn.factorAt_subset), [`MIPRE.CL.CLFun.ExactlyOn.biUnion_factorAt`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.CLFun.ExactlyOn.biUnion_factorAt), [`MIPRE.CL.CLFun.SupportedOn.factorOfPrefix_eval`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.CLFun.SupportedOn.factorOfPrefix_eval), [`MIPRE.CL.CLFun.SupportedOn.mapOfPrefix_eval`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.CLFun.SupportedOn.mapOfPrefix_eval).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 150](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L150)
