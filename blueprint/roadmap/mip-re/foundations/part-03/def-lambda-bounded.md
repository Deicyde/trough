---
declaration: definition
origin: cited
lean: MIPRE.Verifier.IsBounded
statement: formalized
---

# $\lambda$-bounded verifier in the ambient model

For $\lambda\in\mathbb{N}$, an ambient normal form verifier $\mathsf{V}=(\mathcal{S},\mathcal{D})$ is *$\lambda$-bounded* if $\left\vert {\mathsf{V}} \right\vert\leq\lambda$ and, for every $n\geq2$, $s(n)\leq n^\lambda$ and both programs halt within cost $n^\lambda(\left\vert {d} \right\vert+1)^\lambda$ on every encoded input $(n,d)$. Equivalently, both `Sampler.TimeBoundAt` and `Decider.TimeBoundAt` hold at parameters $(n,n^\lambda,\lambda)$. The parameter $\lambda$ controls the coefficient's growth in $n$ and bounds the polynomial degree in the auxiliary input size. The dimension bound is a separate clause; neither it nor an absolute-time bound is inferred from the relative cost predicates.

## Depends on

- [Normal form verifier in the ambient model](def-normal-verifier.md)

## Lean

Formalized as [`MIPRE.Verifier.IsBounded`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Verifier.IsBounded).

## Sources

- [MIP* = RE blueprint: content/02_foundations.tex, line 1556](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/02_foundations.tex#L1556)
