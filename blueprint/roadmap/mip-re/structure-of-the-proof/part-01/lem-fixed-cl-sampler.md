---
declaration: lemma
origin: cited
lean: MIPRE.CL.FixedSampler.sampler, MIPRE.CL.FixedSampler.sampler_timeBound, MIPRE.CL.Graph.sampler, MIPRE.CL.Graph.sampler_dim, MIPRE.CL.Graph.sampler_timeBound, MIPRE.CL.TypedSampler.specialize, MIPRE.CL.TypedSampler.specialize_timeBoundAt
statement: formalized
proof: formalized
---

# Executable fixed CL samplers

Every fixed finite CL presentation with a full register partition has an actual ambient sampler program, with all marginal, linear and factor query clauses and halting on malformed inputs. In particular the fixed graph presentation has a two-level sampler of dimension $4|T|$. Its runtime is polynomial in the raw query size, uniformly in the index. A single executable typed sampler can also be specialized to any fixed type, with explicit runtime transfer. These fixed-table bounds may depend on the whole finite presentation; they do not assert polynomial compilation time in a variable graph's size.

## Depends on

- [Sampler](../../foundations/part-03/def-sampler.md)
- [Graph rejection sampling](lem-detype-graph.md)
- [Register embeddings and detyped query routing](lem-detype-queries.md)
- [Typed sampler and its distribution](def-typed-sampler-interface.md)
- [Effective indexing and padding arithmetic](../part-07/lem-pcp-padding-programs.md)

## Proof

Compile a finite table of all legal queries and use a total fallback elsewhere. For type specialization, a total raw-data adapter inserts the fixed type tag before calling the original program; the original halting theorem applies to every adapted raw query. The program evaluations and cost bounds are checked.

## Lean

Formalized as [`MIPRE.CL.FixedSampler.sampler`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.FixedSampler.sampler), [`MIPRE.CL.FixedSampler.sampler_timeBound`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.FixedSampler.sampler_timeBound), [`MIPRE.CL.Graph.sampler`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Graph.sampler), [`MIPRE.CL.Graph.sampler_dim`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Graph.sampler_dim), [`MIPRE.CL.Graph.sampler_timeBound`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Graph.sampler_timeBound), [`MIPRE.CL.TypedSampler.specialize`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.TypedSampler.specialize), [`MIPRE.CL.TypedSampler.specialize_timeBoundAt`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.TypedSampler.specialize_timeBoundAt).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 518](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L518)
