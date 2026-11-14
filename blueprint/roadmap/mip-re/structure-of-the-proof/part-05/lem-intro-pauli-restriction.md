---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.completePauliPOVM_isPVM, MIPRE.Introspection.completePauliPOVM_mats_of_ne, MIPRE.Introspection.TypedEstimates.check_pauli_completed, MIPRE.Introspection.TypedEstimates.completed_pauli_condFail_le, MIPRE.Introspection.TypedEstimates.typed_edge_mean_failure_le, MIPRE.Introspection.PauliRestriction.strategy_failure_le, MIPRE.Introspection.PauliRestriction.strategy_pauliAns_A, MIPRE.Introspection.PauliRestriction.strategy_pauliAns_B
statement: formalized
proof: formalized
---

# Restriction to the actual Pauli game

Any actual projective strategy for the full parsed game restricts to a strategy for the actual QLD game in the same model, hence with the same state. If the original failure is at most $\varepsilon$, the restricted failure is at most the full ordered-edge count times $\varepsilon$. Completing malformed outer constructors at a scalar answer leaves every valid full-Pauli answer operator exactly unchanged, for both parties.

## Depends on

- [The actual three-level Pauli question sampler](lem-intro-pauli-cl-content.md)
- [Concrete typed sampling and terminal hiding estimates](../part-03/lem-intro-typed-estimates.md)

## Proof

Accepted parsed Pauli answers already satisfy the actual Pauli predicate, including on loops. Coarse-grain malformed outer answers to a fixed scalar answer, preserving projectivity and accepted probability. Conditioning on a full-graph edge bounds its shared-seed mean failure; average over the Pauli edges, then pull back along canonical question encoding. A valid full-Pauli answer differs from the scalar completion answer, so its fibre contains only its original raw constructor.

## Lean

Formalized as [`MIPRE.Introspection.completePauliPOVM_isPVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.completePauliPOVM_isPVM), [`MIPRE.Introspection.completePauliPOVM_mats_of_ne`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.completePauliPOVM_mats_of_ne), [`MIPRE.Introspection.TypedEstimates.check_pauli_completed`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.check_pauli_completed), [`MIPRE.Introspection.TypedEstimates.completed_pauli_condFail_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.completed_pauli_condFail_le), [`MIPRE.Introspection.TypedEstimates.typed_edge_mean_failure_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.typed_edge_mean_failure_le), [`MIPRE.Introspection.PauliRestriction.strategy_failure_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.PauliRestriction.strategy_failure_le), [`MIPRE.Introspection.PauliRestriction.strategy_pauliAns_A`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.PauliRestriction.strategy_pauliAns_A), [`MIPRE.Introspection.PauliRestriction.strategy_pauliAns_B`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.PauliRestriction.strategy_pauliAns_B).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 3509](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L3509)
