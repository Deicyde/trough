---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.readout_isPVM, MIPRE.Introspection.bornProb_registerEPR_readout, MIPRE.Introspection.readout_eq_synOf, MIPRE.Introspection.sampled_dist_eq_clDist, MIPRE.Introspection.conditionalReadout_isPVM, MIPRE.Introspection.bornProb_conditionalReadout, MIPRE.Introspection.readoutAcceptance_eq_value, MIPRE.Introspection.val_ge_of_readoutAcceptance, MIPRE.Introspection.exists_strategy_of_readoutAcceptance, MIPRE.Introspection.verifier_readoutAcceptance_eq_value
statement: formalized
proof: formalized
---

# Exact final strategy extraction

For arbitrary finite question maps, computational readout of a shared EPR seed has exactly their common uniform-seed distribution. Tensor each question projector with a projective auxiliary measurement depending on that question. These form a joint PVM, and their accepted mass is exactly the value of the strategy using the auxiliary state and auxiliary measurements in the original game. Discarding the question EPR register incurs no further error or dimension factor. The identity is specialized to the actual CL distribution of a verifier. This assumes the terminal tensor-product measurement form, which the soundness induction below derives from arbitrary high-value introspection play. The Lean states it in the register model (Definition [The register model](../../downstream-results/part-03/def-register-model.md)) of an auxiliary model: the auxiliary measurements form a projective strategy of the auxiliary model (Definition [Projective strategy in a bipartite model](../../downstream-results/part-02/def-model-proj-strategy.md)), and every value model dominating that model has value at least the accepted mass, of which the quantum value is the case of a tensor-product model.

## Depends on

- [Conditionally linear function](../part-01/def-cl-function.md)
- [Tensor-product strategy](../../foundations/part-01/def-tensor-strategy.md)
- [Normal form verifier in the ambient model](../../foundations/part-03/def-normal-verifier.md)
- [Quantum value](../../foundations/part-01/def-q-value.md)
- [The maximally entangled state of the Weyl system](../../foundations/part-02/def-weyl-epr.md)
- [The expanded state, and an inert ancilla](../../foundations/part-02/def-expanded-state.md)
- [The register model](../../downstream-results/part-03/def-register-model.md)
- [Projective strategy in a bipartite model](../../downstream-results/part-02/def-model-proj-strategy.md)

## Proof depends on

- [The ancilla extension](../../downstream-results/part-02/lem-ancilla-extension.md)

## Proof

Evaluate the diagonal projectors on the normalized EPR state; the result is the normalized size of the common question fibre. Born probabilities factor over the EPR and auxiliary systems. Rearranging the finite acceptance sum gives the original strategy value. Package the auxiliary PVMs as a legal tensor strategy and compare with the supremum defining quantum value.

## Lean

Formalized as [`MIPRE.Introspection.readout_isPVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.readout_isPVM), [`MIPRE.Introspection.bornProb_registerEPR_readout`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.bornProb_registerEPR_readout), [`MIPRE.Introspection.readout_eq_synOf`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.readout_eq_synOf), [`MIPRE.Introspection.sampled_dist_eq_clDist`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.sampled_dist_eq_clDist), [`MIPRE.Introspection.conditionalReadout_isPVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.conditionalReadout_isPVM), [`MIPRE.Introspection.bornProb_conditionalReadout`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.bornProb_conditionalReadout), [`MIPRE.Introspection.readoutAcceptance_eq_value`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.readoutAcceptance_eq_value), [`MIPRE.Introspection.val_ge_of_readoutAcceptance`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.val_ge_of_readoutAcceptance), [`MIPRE.Introspection.exists_strategy_of_readoutAcceptance`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.exists_strategy_of_readoutAcceptance), [`MIPRE.Introspection.verifier_readoutAcceptance_eq_value`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.verifier_readoutAcceptance_eq_value).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 1791](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L1791)
