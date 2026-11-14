---
declaration: definition
origin: cited
lean: MIPRE.Introspection
statement: formalized
---

# Ambient introspection contract

The structure `MIPRE.Introspection` is an ambient contract, parametrized by $\ell$: the introspective sampler as a function of $\lambda$ alone with its program computable in polynomial time, the introspective decider's program as a polynomial-time function of the input programs and $\lambda$, the packaging as a $5$-level normal form verifier on every input, the complexity clauses for every input and index — sampler and decider runtime coefficients at most $(\lambda n + 1)^C$ and $2^{(\lambda n + 1)^C}$, respectively, both at input-size degree $C$, and $\left\vert {\mathcal{D}^{\textsc{Intro}}} \right\vert \leq C(\lambda + 1)^C$ for a constant $C$, the ambient analogue of $C_{\mathrm{intro}}$, with the decider rejecting answers longer than $2^{(\lambda n+1)^C}$. For ambient $\lambda$-bounded inputs, completeness transfers `HasPerfectPCC` from index $2^n$ at answer cut $(2^n)^\lambda$ to index $n$ at cut $2^{(\lambda n+1)^C}$. For $n\geq1$, soundness transfers a value greater than $1-\varepsilon$, for $\varepsilon>0$, at the output cut to a value at least $1-\delta(\varepsilon,n)$ at the input cut, where $\delta(\varepsilon,n)=a((\lambda n)^a\varepsilon^b+(\lambda n)^{-b})$, $a\geq1$ and $0\lt b\leq1$. The complexity clauses are stated in the vocabulary of resource budgets (`MIPRE.Budget`, `Verifier.Within`: the running-time coefficients of sampler and decider and their degree, the question dimension, and the answer length beyond which the decider rejects), which lets the exterior transformations be chained. The composition `MIPRE.GapCompression.ofPipeline` consumes an instance at $\ell = 7$. Here $\lambda$-boundedness is the ambient definition, not the source absolute-time hypothesis. This definition specifies the contract, without constructing an inhabitant. Since $\ell$ is fixed by the structure, its polynomial-time construction field does not assert a bound polynomial in binary $\ell$.

## Depends on

- [Normal form verifier in the ambient model](../../foundations/part-03/def-normal-verifier.md)
- [$\lambda$-bounded verifier in the ambient model](../../foundations/part-03/def-lambda-bounded.md)
- [PCC strategy](../../foundations/part-01/def-pcc.md)
- [Synchronous value](../../foundations/part-01/def-sync-value.md)
- [Quantum value](../../foundations/part-01/def-q-value.md)

## Lean

Formalized as [`MIPRE.Introspection`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 4019](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L4019)
