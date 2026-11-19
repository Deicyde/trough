---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.completeOptionPOVM_isPVM, MIPRE.Introspection.option_valid_acceptance_le_complete, MIPRE.Introspection.readoutAcceptance_le_completedValue, MIPRE.Introspection.IntroPrefixInvariant.terminal_parsed_pair, MIPRE.Introspection.TypedExtraction.exists_strategy_of_terminal_invariants
statement: formalized
proof: formalized
---

# Ordinary-answer extraction from actual terminal invariants

For a nonempty ordinary answer alphabet, both actual terminal invariants construct an original-game strategy. If the final parsed-game failure is at most $e$, its value is at least $1-|E|e$. Each malformed auxiliary outcome is completed to a fixed ordinary answer; its mass need not vanish.

## Depends on

- [Terminal conditional readouts with malformed answers](lem-intro-terminal-invariant.md)
- [Quantitative extraction from the concrete typed game](../part-04/lem-intro-typed-final-extraction.md)

## Proof

The valid full-option outcome has a unique parsed-answer preimage. Its terminal effect is the actual conditional question readout. Map the malformed auxiliary outcome to a fixed answer; coarse-graining preserves projectivity, and newly accepted Born probabilities are nonnegative. The actual cross-edge mass and the exact common-seed question law give the value bound.

## Lean

Formalized as [`MIPRE.Introspection.completeOptionPOVM_isPVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.completeOptionPOVM_isPVM), [`MIPRE.Introspection.option_valid_acceptance_le_complete`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.option_valid_acceptance_le_complete), [`MIPRE.Introspection.readoutAcceptance_le_completedValue`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.readoutAcceptance_le_completedValue), [`MIPRE.Introspection.IntroPrefixInvariant.terminal_parsed_pair`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.IntroPrefixInvariant.terminal_parsed_pair), [`MIPRE.Introspection.TypedExtraction.exists_strategy_of_terminal_invariants`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedExtraction.exists_strategy_of_terminal_invariants).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 3091](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L3091)
