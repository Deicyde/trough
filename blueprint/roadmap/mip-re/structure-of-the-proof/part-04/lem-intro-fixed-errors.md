---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.stateSqNorm_registeredExtendOp, MIPRE.Introspection.xSqNorm_registeredExtendOp, MIPRE.Introspection.bornProb_registeredExtendOp, MIPRE.Introspection.registeredReplacement_samePartyError_other, MIPRE.Introspection.registeredReplacement_crossError_other, MIPRE.Introspection.TypedEstimates.pauliAliceError_registeredReplacement, MIPRE.Introspection.TypedEstimates.pauliBobError_registeredExtension, MIPRE.Introspection.TypedEstimates.hidingAliceError_registeredReplacement, MIPRE.Introspection.TypedEstimates.hidingBobError_registeredExtension, MIPRE.Introspection.TypedEstimates.readAliceError_registeredReplacement, MIPRE.Introspection.TypedEstimates.readBobError_registeredExtension
statement: formalized
proof: formalized
---

# Preserving the fixed errors under replacement

Extending by the fixed auxiliary vector and reassociating the register preserves same-party error, cross-party error, and Born probabilities exactly. At every unchanged question the actual replacement has precisely this extension. In particular the primitive Pauli, hiding, and Read errors are unchanged when an Alice Introspect question is replaced.

## Depends on

- [A concrete strategy after one adaptive replacement](lem-intro-adaptive-strategy.md)
- [Full Read rigidity](lem-intro-read-rigidity.md)

## Proof

The deviation vectors are extended by an isometry. Register reassociation preserves their norms, and register ideals remain tensored with the enlarged auxiliary identity. Specialize the actual unchanged-question formula.

## Lean

Formalized as [`MIPRE.Introspection.stateSqNorm_registeredExtendOp`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.stateSqNorm_registeredExtendOp), [`MIPRE.Introspection.xSqNorm_registeredExtendOp`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.xSqNorm_registeredExtendOp), [`MIPRE.Introspection.bornProb_registeredExtendOp`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.bornProb_registeredExtendOp), [`MIPRE.Introspection.registeredReplacement_samePartyError_other`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.registeredReplacement_samePartyError_other), [`MIPRE.Introspection.registeredReplacement_crossError_other`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.registeredReplacement_crossError_other), [`MIPRE.Introspection.TypedEstimates.pauliAliceError_registeredReplacement`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.pauliAliceError_registeredReplacement), [`MIPRE.Introspection.TypedEstimates.pauliBobError_registeredExtension`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.pauliBobError_registeredExtension), [`MIPRE.Introspection.TypedEstimates.hidingAliceError_registeredReplacement`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.hidingAliceError_registeredReplacement), [`MIPRE.Introspection.TypedEstimates.hidingBobError_registeredExtension`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.hidingBobError_registeredExtension), [`MIPRE.Introspection.TypedEstimates.readAliceError_registeredReplacement`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.readAliceError_registeredReplacement), [`MIPRE.Introspection.TypedEstimates.readBobError_registeredExtension`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.readBobError_registeredExtension).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 2888](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L2888)
