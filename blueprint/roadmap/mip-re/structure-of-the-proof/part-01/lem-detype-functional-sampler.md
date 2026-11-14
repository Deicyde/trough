---
declaration: lemma
origin: cited
lean: MIPRE.CL.Detyping.sampler, MIPRE.CL.Detyping.sampler_dim, MIPRE.CL.Detyping.samplerProg_closed, MIPRE.CL.Detyping.samplerProg_halts, MIPRE.CL.Detyping.samplerProg_dimension, MIPRE.CL.Detyping.samplerProg_marginal, MIPRE.CL.Detyping.samplerProg_linear, MIPRE.CL.Detyping.samplerProg_factor, MIPRE.CL.Detyping.sampler_haltsWithin, MIPRE.CL.Detyping.sampler_timeBoundAt_uniform_degree, MIPRE.CL.Detyping.sampler_timeBound
statement: formalized
proof: formalized
---

# Executable detyping sampler

An actual ambient typed sampler with $\ell>0$ levels and a fixed finite type graph gives an actual ambient sampler with $\ell+2$ levels and dimension $4|T|+s(n)$. Its closed program answers the dimension, marginal, linear and factor queries of the detyped presentation, and halts on every malformed query. A polynomial runtime bound transfers from the given typed sampler, with an explicit coefficient and a query degree independent of the index. The constants depend on the fixed graph; uniform polynomial compilation time and description size in a variable graph are not asserted.

## Depends on

- [Detyped conditionally linear functions](lem-detype-cl.md)
- [Register embeddings and detyped query routing](lem-detype-queries.md)
- [Typed sampler and its distribution](def-typed-sampler-interface.md)
- [Effective indexing and padding arithmetic](../part-07/lem-pcp-padding-programs.md)

## Proof

Parse the raw query totally. The first two levels use the graph sampler; later levels either return the zero branch or forward one correctly typed query. The graph prefix supplies the selected type. A context-preserving one-call program reattaches the graph result. The proved query identities identify every returned bit string with the constructed CL presentation. The program's evaluation cost is bounded by a polynomial combining routing, the forwarded call, the returned data size and postprocessing. Bounding that polynomial's degree supplies the uniform query exponent.

## Lean

Formalized as [`MIPRE.CL.Detyping.sampler`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.sampler), [`MIPRE.CL.Detyping.sampler_dim`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.sampler_dim), [`MIPRE.CL.Detyping.samplerProg_closed`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.samplerProg_closed), [`MIPRE.CL.Detyping.samplerProg_halts`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.samplerProg_halts), [`MIPRE.CL.Detyping.samplerProg_dimension`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.samplerProg_dimension), [`MIPRE.CL.Detyping.samplerProg_marginal`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.samplerProg_marginal), [`MIPRE.CL.Detyping.samplerProg_linear`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.samplerProg_linear), [`MIPRE.CL.Detyping.samplerProg_factor`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.samplerProg_factor), [`MIPRE.CL.Detyping.sampler_haltsWithin`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.sampler_haltsWithin), [`MIPRE.CL.Detyping.sampler_timeBoundAt_uniform_degree`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.sampler_timeBoundAt_uniform_degree), [`MIPRE.CL.Detyping.sampler_timeBound`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.sampler_timeBound).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 575](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L575)
