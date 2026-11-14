---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.BasisProgram.toSelfDualProg_correct, MIPRE.Introspection.BasisProgram.fromSelfDualProg_correct, MIPRE.QLD.PauliCL.linearBits_correct, MIPRE.QLD.PauliCL.marginalBits_correct, MIPRE.QLD.PauliCL.factorBits_correct, MIPRE.QLD.PauliCL.SamplerProgram.query_dimension, MIPRE.QLD.PauliCL.SamplerProgram.query_marginal, MIPRE.QLD.PauliCL.SamplerProgram.query_linear, MIPRE.QLD.PauliCL.SamplerProgram.query_factor, MIPRE.QLD.PauliCL.SamplerProgram.query_runs
statement: formalized
proof: formalized
---

# Executable binary Pauli queries

For explicit unary field and selector widths and point dimension, uniform polynomial-time programs compute all three Pauli marginals, linear maps and factor indicators in the numbered binary register. For positive odd field degree and selector width at most field degree, these are the exact downsized CL queries in the effective self-dual basis. Linear and factor correctness hold for arbitrary prefixes. A total router handles the four query kinds and the fixed twenty-six type labels.

## Depends on

- [An executable balanced seed selector and line stages](lem-intro-executable-seeded-lines.md)
- [Effective normal element by fixed-space projections](../../background-results/part-05/lem-effective-normal-element.md)
- [Deterministic self-dual normal basis](../../background-results/part-04/lem-self-dual-basis.md)
- [Sampler](../../foundations/part-03/def-sampler.md)

## Proof depends on

- [Effective self-dualization of a supplied normal basis](../../background-results/part-05/lem-effective-normal-selfdualization.md)

## Proof

Construct the self-dual basis effectively and convert field rows in both directions. Pack the point, seed, direction and scalar registers in the proved coordinate order. Execute the appropriate stage maps and compose successive stages for marginals; factor indicators use the fixed register partition. The type decoder tabulates only the fixed finite type set. Canonical index-dependent parameter selection and the all-index sampler packaging are supplied by Lemma [The canonical sampler at every index](lem-intro-canonical-sampler.md).

## Lean

Formalized as [`MIPRE.Introspection.BasisProgram.toSelfDualProg_correct`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.BasisProgram.toSelfDualProg_correct), [`MIPRE.Introspection.BasisProgram.fromSelfDualProg_correct`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.BasisProgram.fromSelfDualProg_correct), [`MIPRE.QLD.PauliCL.linearBits_correct`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.PauliCL.linearBits_correct), [`MIPRE.QLD.PauliCL.marginalBits_correct`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.PauliCL.marginalBits_correct), [`MIPRE.QLD.PauliCL.factorBits_correct`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.PauliCL.factorBits_correct), [`MIPRE.QLD.PauliCL.SamplerProgram.query_dimension`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.PauliCL.SamplerProgram.query_dimension), [`MIPRE.QLD.PauliCL.SamplerProgram.query_marginal`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.PauliCL.SamplerProgram.query_marginal), [`MIPRE.QLD.PauliCL.SamplerProgram.query_linear`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.PauliCL.SamplerProgram.query_linear), [`MIPRE.QLD.PauliCL.SamplerProgram.query_factor`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.PauliCL.SamplerProgram.query_factor), [`MIPRE.QLD.PauliCL.SamplerProgram.query_runs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.PauliCL.SamplerProgram.query_runs).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 3678](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L3678)
