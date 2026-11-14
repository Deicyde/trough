---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.PauliSampler.sampler, MIPRE.Introspection.PauliSampler.fullCompiler_apply, MIPRE.Introspection.PauliSampler.finalCompiler_apply, MIPRE.Introspection.PauliSampler.finalSampler_dim_zero, MIPRE.Introspection.PauliSampler.finalSampler_uniform_bound
statement: formalized
proof: formalized
---

# The canonical sampler at every index

The effective odd-degree field, self-dual basis and explicit dyadic selector give an index-dependent Pauli typed sampler. Extending and detyping it gives a five-level sampler whose program is computed uniformly from binary $\lambda$. For every input and index its dimension and runtime coefficient are bounded by $(\lambda n+1)^C$, at a fixed input-size degree $C$. When $\lambda n=0$, the final sampler has dimension zero.

## Depends on

- [Executable binary Pauli queries](lem-intro-executable-pauli-queries.md)

## Proof depends on

- [Executable detyping sampler](../part-01/lem-detype-functional-sampler.md)
- [Efficient s-m-n](../../computability/lem-smn.md)

## Proof

Compute unary field and register parameters within the polynomial sampler budget, then compose the checked uniform Pauli query router with the typed and graph routers. At positive indices, absorb their fixed polynomial costs into one exponent. Separate constant-time branches at zero parameter or zero index supply the exact all-index bound.

## Lean

Formalized as [`MIPRE.Introspection.PauliSampler.sampler`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.PauliSampler.sampler), [`MIPRE.Introspection.PauliSampler.fullCompiler_apply`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.PauliSampler.fullCompiler_apply), [`MIPRE.Introspection.PauliSampler.finalCompiler_apply`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.PauliSampler.finalCompiler_apply), [`MIPRE.Introspection.PauliSampler.finalSampler_dim_zero`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.PauliSampler.finalSampler_dim_zero), [`MIPRE.Introspection.PauliSampler.finalSampler_uniform_bound`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.PauliSampler.finalSampler_uniform_bound).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 3818](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L3818)
