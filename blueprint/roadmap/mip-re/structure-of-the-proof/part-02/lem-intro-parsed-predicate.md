---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.CLChecks.prefixRegister_subset, MIPRE.Introspection.CLChecks.proj_prefixRegister, MIPRE.Introspection.CLChecks.prefixRegister_full, MIPRE.Introspection.CLChecks.sampling_prefix, MIPRE.Introspection.CLChecks.hidingPauli_coarse, MIPRE.Introspection.CLChecks.hidingNext_coarse, MIPRE.Introspection.TypedPredicate.check, MIPRE.Introspection.TypedPredicate.check_formats, MIPRE.Introspection.TypedPredicate.check_consistency, MIPRE.Introspection.TypedPredicate.check_sampling, MIPRE.Introspection.TypedPredicate.check_sampling_prefix, MIPRE.Introspection.TypedPredicate.check_reading, MIPRE.Introspection.TypedPredicate.check_game, MIPRE.Introspection.TypedPredicate.check_game_reversed
statement: formalized
proof: formalized
---

# The parsed introspection decision predicate

Construct the finite predicate on parsed answers, with format and consistency checks, both orientations of the sampling and hiding tests, and the original decision predicate on the cross-introspection edge. The original CL family, original predicate, Pauli predicate and projection of Pauli answers to the original register are explicit parameters. The Pauli predicate is instantiated at the actual Pauli question contents. Accepted sampling answers satisfy every prefix comparison on the whole answer alphabet. Hiding projections use the registers selected by the later answer, as required by the adaptive construction. For every claimed output, the prefix is exactly its projection onto the selected register; at full length, this register is the complete partition. The cross-introspection check retains the original Alice/Bob argument order in either orientation. This is the parsed semantic predicate; byte parsing, global cutoffs and clocked program calls remain separate construction work.

## Depends on

- [Introspection type graph and typed CL family](lem-intro-type-presentation.md)
- [Conditionally linear function](../part-01/def-cl-function.md)

## Proof depends on

- [Sampling and hiding subtest estimates](../part-03/lem-intro-subtest-estimates.md)

## Proof

Use a sum of the four answer formats. Dispatch by question constructors and check both orientations. Compute claimed-output prefixes by coordinate restriction, and dual readouts in the selected local register. Unfolding the checks gives the accepted-answer implications; the CL prefix theorem gives the marginal identity without assuming that a claimed answer is in the image.

## Lean

Formalized as [`MIPRE.Introspection.CLChecks.prefixRegister_subset`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.CLChecks.prefixRegister_subset), [`MIPRE.Introspection.CLChecks.proj_prefixRegister`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.CLChecks.proj_prefixRegister), [`MIPRE.Introspection.CLChecks.prefixRegister_full`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.CLChecks.prefixRegister_full), [`MIPRE.Introspection.CLChecks.sampling_prefix`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.CLChecks.sampling_prefix), [`MIPRE.Introspection.CLChecks.hidingPauli_coarse`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.CLChecks.hidingPauli_coarse), [`MIPRE.Introspection.CLChecks.hidingNext_coarse`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.CLChecks.hidingNext_coarse), [`MIPRE.Introspection.TypedPredicate.check`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedPredicate.check), [`MIPRE.Introspection.TypedPredicate.check_formats`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedPredicate.check_formats), [`MIPRE.Introspection.TypedPredicate.check_consistency`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedPredicate.check_consistency), [`MIPRE.Introspection.TypedPredicate.check_sampling`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedPredicate.check_sampling), [`MIPRE.Introspection.TypedPredicate.check_sampling_prefix`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedPredicate.check_sampling_prefix), [`MIPRE.Introspection.TypedPredicate.check_reading`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedPredicate.check_reading), [`MIPRE.Introspection.TypedPredicate.check_game`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedPredicate.check_game), [`MIPRE.Introspection.TypedPredicate.check_game_reversed`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedPredicate.check_game_reversed).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 1092](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L1092)
