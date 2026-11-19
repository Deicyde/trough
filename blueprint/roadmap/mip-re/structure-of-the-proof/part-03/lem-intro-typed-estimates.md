---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.TypedPredicate.check_directed, MIPRE.Introspection.TypedPredicate.check_directed_reversed, MIPRE.Introspection.TypedPredicate.check_hiding_read, MIPRE.Introspection.TypedPredicate.check_hiding_read_reversed, MIPRE.Introspection.TypedPredicate.check_hiding_next, MIPRE.Introspection.TypedPredicate.check_hiding_next_reversed, MIPRE.Introspection.TypedPredicate.check_hiding_pauli, MIPRE.Introspection.TypedPredicate.check_hiding_pauli_reversed, MIPRE.Introspection.TypedEstimates.questionCheck, MIPRE.Introspection.TypedEstimates.parsedGame, MIPRE.Introspection.TypedEstimates.aux_agreement_estimate, MIPRE.Introspection.TypedEstimates.sampling_prefix_estimate, MIPRE.Introspection.TypedEstimates.hiding_read_estimate, MIPRE.Introspection.TypedEstimates.hiding_read_same_side_estimate
statement: formalized
proof: formalized
---

# Concrete typed sampling and terminal hiding estimates

For the concrete parsed introspection game of failure at most $\varepsilon$, the sampling-prefix and terminal hiding/Read cross-party squared distances are at most $2|E|\varepsilon$, where $E$ is the set of ordered type edges. Comparing the terminal hiding and Read measurements on the same side costs at most $8|E|\varepsilon$. The predicates, question distribution, and Read consistency loop are those of the constructed game; no separate acceptance or selection-weight premise is assumed. Wrong answer constructors have a distinct coarse outcome, so the estimates include the whole answer alphabet. The Pauli subpredicate receives the actual Pauli question contents. The adjacent hiding induction and product-form rigidity remain separate.

## Depends on

- [The parsed introspection decision predicate](../part-02/lem-intro-parsed-predicate.md)
- [Introspection type graph and typed CL family](../part-02/lem-intro-type-presentation.md)
- [Sampling and hiding subtest estimates](lem-intro-subtest-estimates.md)

## Proof

Bound each fixed auxiliary edge's conditional failure using its exact mass $1/|E|$. The parsed acceptance checks imply the appropriate equality of coarse outcomes, so consistency gives the cross-party bounds. Use the Read consistency loop as the common opposite-party measurement for the same-side comparison. Both hiding orientations are proved directly from the predicate.

## Lean

Formalized as [`MIPRE.Introspection.TypedPredicate.check_directed`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedPredicate.check_directed), [`MIPRE.Introspection.TypedPredicate.check_directed_reversed`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedPredicate.check_directed_reversed), [`MIPRE.Introspection.TypedPredicate.check_hiding_read`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedPredicate.check_hiding_read), [`MIPRE.Introspection.TypedPredicate.check_hiding_read_reversed`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedPredicate.check_hiding_read_reversed), [`MIPRE.Introspection.TypedPredicate.check_hiding_next`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedPredicate.check_hiding_next), [`MIPRE.Introspection.TypedPredicate.check_hiding_next_reversed`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedPredicate.check_hiding_next_reversed), [`MIPRE.Introspection.TypedPredicate.check_hiding_pauli`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedPredicate.check_hiding_pauli), [`MIPRE.Introspection.TypedPredicate.check_hiding_pauli_reversed`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedPredicate.check_hiding_pauli_reversed), [`MIPRE.Introspection.TypedEstimates.questionCheck`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.questionCheck), [`MIPRE.Introspection.TypedEstimates.parsedGame`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.parsedGame), [`MIPRE.Introspection.TypedEstimates.aux_agreement_estimate`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.aux_agreement_estimate), [`MIPRE.Introspection.TypedEstimates.sampling_prefix_estimate`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.sampling_prefix_estimate), [`MIPRE.Introspection.TypedEstimates.hiding_read_estimate`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.hiding_read_estimate), [`MIPRE.Introspection.TypedEstimates.hiding_read_same_side_estimate`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.hiding_read_same_side_estimate).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 1701](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L1701)
