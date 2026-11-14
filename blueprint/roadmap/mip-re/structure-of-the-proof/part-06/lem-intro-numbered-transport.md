---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.ExplicitGame.game_mu, MIPRE.Introspection.ExplicitGame.game_D, MIPRE.Introspection.ExplicitGame.toLegacy_value, MIPRE.Introspection.ExplicitGame.pccToExplicit_isPCC, MIPRE.Introspection.AuxiliaryQuotient.value_le_decodedStrategy, MIPRE.Introspection.NumberedComplete.exists_perfectPCC_with_format, MIPRE.Introspection.NumberedSoundness.quantumValue_ge_of_qld, MIPRE.Introspection.NumberedSoundness.canonical_quantumValue_ge
statement: formalized
proof: formalized
---

# Full question transport and actual QLD extraction

Explicit seed relabelling intertwines the full typed question law and predicate, including mixed edges. Quotient dual decoding and finite-register reindexing preserve the required Pauli support. The actual QLD soundness theorem therefore supplies the extraction witness used by introspection, with its field-size tails absorbed at the canonical parameters. Honest completeness retains PCC, exact dimension and the executable guards' support.

## Depends on

- [Output relabelling for the explicit selector](lem-intro-explicit-selector-questions.md)
- [The Pauli basis test is sound in a model](../../downstream-results/part-03/def-qld-sound-in.md)
- [Introspection soundness from the extracted Pauli strategy](../part-05/lem-intro-extracted-soundness.md)

## Proof depends on

- [Finite soundness from the valid-answer extraction interface](../part-05/lem-intro-valid-isometric-soundness.md)
- [Concrete completeness for the full typed introspection game](../part-05/lem-intro-full-typed-completeness.md)
- [Restriction to the actual Pauli game](../part-05/lem-intro-pauli-restriction.md)
- [Post-processing and detyping, in a model](../../downstream-results/part-02/lem-transports-model.md)

## Proof

Transport the shared seed and each question's answer map explicitly. Relabel quotient coordinates before selecting local dual representatives. The distinguished full Pauli measurements remain fixed throughout, so decoder-enforced support passes to the actual QLD restriction. Apply QLD extraction, binary basis transport and the proved finite-game induction, then absorb the canonical field and register error terms.

## Lean

Formalized as [`MIPRE.Introspection.ExplicitGame.game_mu`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.ExplicitGame.game_mu), [`MIPRE.Introspection.ExplicitGame.game_D`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.ExplicitGame.game_D), [`MIPRE.Introspection.ExplicitGame.toLegacy_value`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.ExplicitGame.toLegacy_value), [`MIPRE.Introspection.ExplicitGame.pccToExplicit_isPCC`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.ExplicitGame.pccToExplicit_isPCC), [`MIPRE.Introspection.AuxiliaryQuotient.value_le_decodedStrategy`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.AuxiliaryQuotient.value_le_decodedStrategy), [`MIPRE.Introspection.NumberedComplete.exists_perfectPCC_with_format`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.NumberedComplete.exists_perfectPCC_with_format), [`MIPRE.Introspection.NumberedSoundness.quantumValue_ge_of_qld`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.NumberedSoundness.quantumValue_ge_of_qld), [`MIPRE.Introspection.NumberedSoundness.canonical_quantumValue_ge`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.NumberedSoundness.canonical_quantumValue_ge).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 3895](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L3895)
