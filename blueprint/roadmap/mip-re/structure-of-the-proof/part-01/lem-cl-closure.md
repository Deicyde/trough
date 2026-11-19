---
declaration: lemma
origin: cited
lean: MIPRE.CL.CLFun.concat, MIPRE.CL.CLFun.directSum, MIPRE.CL.IsCLFun.succ, MIPRE.CL.IsCLFun.concat, MIPRE.CL.IsCLFun.directSum, MIPRE.CL.IsCLFun.directSum'
statement: formalized
proof: formalized
---

# Closure of CL functions

Let $V = U \oplus W$ be a decomposition of $V$ into complementary register subspaces.

1. (Levels.) Every $\ell$-level CL function is $(\ell+1)$-level.
2. (Concatenation.) If $L$ is a $k$-level CL function on $U$ and $R_u$ an $\ell$-level CL function on $W$ for each $u \in L(U)$, then $x \mapsto L(x^U) + R_{L(x^U)}(x^W)$ is a $(k+\ell)$-level CL function on $V$.
3. (Direct sums.) If $L$ is a $k$-level CL function on $U$ and $R$ an $\ell$-level CL function on $W$, then $x \mapsto L(x^U) + R(x^W)$ is a $\max(k,\ell)$-level CL function on $V$.

Concatenation and direct sums preserve exactness in the sense of Lemma [Structure of a CL function](lem-cl-structure.md).

## Depends on

- [Conditionally linear function](def-cl-function.md)

## Proof

`rk:higher-level`, `lem:cl-concat` and `lem:cl-func-prod` of `linear.tex`, the last for two summands, which iterates. The Lean constructions are on presentations and carry no hypotheses; that the supports are disjoint enters in the evaluation lemmas identifying the function presented.

## Lean

Formalized as [`MIPRE.CL.CLFun.concat`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.CLFun.concat), [`MIPRE.CL.CLFun.directSum`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.CLFun.directSum), [`MIPRE.CL.IsCLFun.succ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.IsCLFun.succ), [`MIPRE.CL.IsCLFun.concat`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.IsCLFun.concat), [`MIPRE.CL.IsCLFun.directSum`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.IsCLFun.directSum), [`MIPRE.CL.IsCLFun.directSum'`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.IsCLFun.directSum').

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 188](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L188)
