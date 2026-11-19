---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.isometricPOVM_isPVM, MIPRE.Introspection.isometricEffect_intertwine, MIPRE.Introspection.isometricState_unit, MIPRE.Introspection.povmValue_isometricState, MIPRE.Introspection.isometricState_map_alice_deviation, MIPRE.Introspection.isometricState_map_bob_deviation, MIPRE.Introspection.projector_mass_le_state_distance, MIPRE.Introspection.isometricComplement_alice_mass, MIPRE.Introspection.isometricComplement_bob_mass, MIPRE.Introspection.isometricEffect_alice_error_le, MIPRE.Introspection.isometricEffect_bob_error_le
statement: formalized
proof: formalized
---

# Local-isometry transport and image-complement completion

Rectangular local isometries transport any projective strategy to an actual projective strategy on the target spaces. Assigning the orthogonal image complement to a fixed outcome normalizes the measurements and preserves every Born probability and the whole game value on the embedded state. The exact operator intertwining also holds after arbitrary answer maps. On a target state at squared distance at most $\eta$ from the embedded state, image-complement mass is at most $\eta$. Thus a summed image-measurement error $\delta$ becomes at most $2\delta+2\eta$ after completion, on either party and without an outcome-count factor.

## Depends on

- [Local isometries of bipartite models](../../downstream-results/part-03/def-local-isometry.md)
- [The expanded state, and an inert ancilla](../../foundations/part-02/def-expanded-state.md)
- [Nonlocal game](../../foundations/part-01/def-game.md)

## Proof depends on

- [Naimark dilation of a question-indexed family](../../foundations/part-02/lem-naimark-dilation.md)

## Proof

The image and its orthogonal complement are orthogonal projections. Complete one outcome, then use the isometry identity to prove compression and intertwining exactly. A complement projection annihilates the embedded state and is a contraction, so its mass on a nearby state is bounded by squared vector distance. Only the chosen outcome receives this complement; the two-term squared triangle inequality gives the error bound.

## Lean

Formalized as [`MIPRE.Introspection.isometricPOVM_isPVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.isometricPOVM_isPVM), [`MIPRE.Introspection.isometricEffect_intertwine`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.isometricEffect_intertwine), [`MIPRE.Introspection.isometricState_unit`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.isometricState_unit), [`MIPRE.Introspection.povmValue_isometricState`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.povmValue_isometricState), [`MIPRE.Introspection.isometricState_map_alice_deviation`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.isometricState_map_alice_deviation), [`MIPRE.Introspection.isometricState_map_bob_deviation`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.isometricState_map_bob_deviation), [`MIPRE.Introspection.projector_mass_le_state_distance`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.projector_mass_le_state_distance), [`MIPRE.Introspection.isometricComplement_alice_mass`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.isometricComplement_alice_mass), [`MIPRE.Introspection.isometricComplement_bob_mass`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.isometricComplement_bob_mass), [`MIPRE.Introspection.isometricEffect_alice_error_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.isometricEffect_alice_error_le), [`MIPRE.Introspection.isometricEffect_bob_error_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.isometricEffect_bob_error_le).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 3206](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L3206)
