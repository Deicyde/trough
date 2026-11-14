---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.CLChecks.prefixRegister_mono, MIPRE.Introspection.CLChecks.outputPrefix_outputPrefix, MIPRE.Introspection.CLChecks.prefixRegister_congr, MIPRE.Introspection.CLChecks.dualReadout_congr, MIPRE.Introspection.CLChecks.dualReadout_proj_compl_prefix, MIPRE.Introspection.CLChecks.tail_proj_tail, MIPRE.Introspection.TypedEstimates.hidingNextGuarded_factor, MIPRE.Introspection.TypedEstimates.hiding_next_accepts_guarded, MIPRE.Introspection.TypedEstimates.hiding_next_guarded_estimate, MIPRE.Introspection.TypedEstimates.hiding_next_normalizer_estimate
statement: formalized
proof: formalized
---

# Guarded maps on arbitrary hiding answers

The next hiding comparison factors through the preceding fine hiding label: its preceding question prefix, current dual output and remaining tail. The later question prefix is retained as the key. A dummy label handles malformed answers and disagreeing prefixes, so every keyed coarse family is complete. Success in the actual parsed adjacent-Hide test gives conditional squared error at most $2|E|\varepsilon$. With preceding fine error $\varepsilon_f$ and prefix-normalizer error $\eta$, replacement by a commuting ideal prefix costs at most $6|E|\varepsilon+3\eta+3\varepsilon_f$.

## Depends on

- [The parsed introspection decision predicate](../part-02/lem-intro-parsed-predicate.md)

## Proof depends on

- [Dimension-independent conditional normalizer replacement](lem-intro-conditional-normalizer.md)

## Proof

Claimed prefixes nest even outside the image of the CL map. Equal preceding prefixes select the same next register, and the next dual readout and tail depend only on the previously retained tail. The actual accepted-answer relation therefore supplies the guarded equality. Extract its probability from the uniform ordered-edge law and apply conditional consistency and the normalizer replacement of Lemma [Dimension-independent conditional normalizer replacement](lem-intro-conditional-normalizer.md).

## Lean

Formalized as [`MIPRE.Introspection.CLChecks.prefixRegister_mono`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.CLChecks.prefixRegister_mono), [`MIPRE.Introspection.CLChecks.outputPrefix_outputPrefix`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.CLChecks.outputPrefix_outputPrefix), [`MIPRE.Introspection.CLChecks.prefixRegister_congr`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.CLChecks.prefixRegister_congr), [`MIPRE.Introspection.CLChecks.dualReadout_congr`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.CLChecks.dualReadout_congr), [`MIPRE.Introspection.CLChecks.dualReadout_proj_compl_prefix`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.CLChecks.dualReadout_proj_compl_prefix), [`MIPRE.Introspection.CLChecks.tail_proj_tail`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.CLChecks.tail_proj_tail), [`MIPRE.Introspection.TypedEstimates.hidingNextGuarded_factor`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.hidingNextGuarded_factor), [`MIPRE.Introspection.TypedEstimates.hiding_next_accepts_guarded`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.hiding_next_accepts_guarded), [`MIPRE.Introspection.TypedEstimates.hiding_next_guarded_estimate`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.hiding_next_guarded_estimate), [`MIPRE.Introspection.TypedEstimates.hiding_next_normalizer_estimate`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.hiding_next_normalizer_estimate).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 2185](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L2185)
