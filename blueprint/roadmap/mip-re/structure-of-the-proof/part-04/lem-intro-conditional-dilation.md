---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.qform_πA_expandA, MIPRE.Introspection.stateSqNorm_expandA_diagonal, MIPRE.Introspection.dilated_pvm_distance, MIPRE.Introspection.conditionalDilationOp_isPVM, MIPRE.Introspection.conditionalDilationOp_compress, MIPRE.Introspection.conditionalDilationOp_born, MIPRE.Introspection.regExchange, MIPRE.Introspection.regExchange_W_ψ, MIPRE.Introspection.exists_conditional_projective_dilation, MIPRE.Introspection.exists_varying_conditional_projective_dilation
statement: formalized
proof: formalized
---

# Conditional projectivization on a common ancilla

A family of residual POVMs admits simultaneous projective dilations with one fixed ancilla state for every question and prefix. Prefix projectors are left intact. Compression and Born probabilities are exact, and an original PVM at averaged squared distance $\delta$ from the product POVM is at averaged squared distance at most $2\sqrt{\delta}$ from the dilated PVM on the enlarged state. A dependent-family version allows all local register carriers and transported states to vary with the prefix, while retaining the same ancilla alphabet and state. Explicit reassociation preserves the original EPR factor. The Lean states it in a bipartite model: the ancilla is a one-sided extension (Definition [The one-sided ancilla extension](../../downstream-results/part-03/def-one-sided-extension.md)) by the ancilla of a Kraus dilation in a fixed basis state (Lemma [Projective dilation against a fixed state, in a star-ordered ring](../../downstream-results/part-03/lem-kraus-dilation.md)), whose size depends on the POVMs, and so on the question in the dependent-family version, and the reassociation exchanges the two layers of the register model.

## Depends on

- [State-dependent POVM distance](../../foundations/part-02/def-state-distance.md)
- [The register model](../../downstream-results/part-03/def-register-model.md)
- [Projective dilation against a fixed state, in a star-ordered ring](../../downstream-results/part-03/lem-kraus-dilation.md)

## Proof depends on

- [Pauli mixing with a retained classical fibre](../part-02/lem-pauli-mixing.md)
- [The one-sided ancilla extension](../../downstream-results/part-03/lem-one-sided-extension.md)

## Proof

Apply simultaneous Naimark dilation only to the residual factor. Compression identifies the mixed quadratic forms, and PVM normalization plus Cauchy–Schwarz bounds the resulting distance. Jensen combines the local bounds. For varying carriers, choose each local dilation and apply the same weighted estimate. Reassembly via the adaptive register permutations remains an obligation of the global induction.

## Lean

Formalized as [`MIPRE.Introspection.qform_πA_expandA`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.qform_πA_expandA), [`MIPRE.Introspection.stateSqNorm_expandA_diagonal`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.stateSqNorm_expandA_diagonal), [`MIPRE.Introspection.dilated_pvm_distance`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.dilated_pvm_distance), [`MIPRE.Introspection.conditionalDilationOp_isPVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.conditionalDilationOp_isPVM), [`MIPRE.Introspection.conditionalDilationOp_compress`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.conditionalDilationOp_compress), [`MIPRE.Introspection.conditionalDilationOp_born`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.conditionalDilationOp_born), [`MIPRE.Introspection.regExchange`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.regExchange), [`MIPRE.Introspection.regExchange_W_ψ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.regExchange_W_ψ), [`MIPRE.Introspection.exists_conditional_projective_dilation`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.exists_conditional_projective_dilation), [`MIPRE.Introspection.exists_varying_conditional_projective_dilation`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.exists_varying_conditional_projective_dilation).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 2516](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L2516)
