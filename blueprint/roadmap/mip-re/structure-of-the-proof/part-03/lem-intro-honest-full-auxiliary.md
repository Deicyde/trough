---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.Honest.hideOp_zero_eq_firstHideOp, MIPRE.Introspection.Honest.pauliX_hideOp_zero_commute, MIPRE.Introspection.Honest.pauliX_hideOp_zero_reject, MIPRE.Introspection.Honest.parsedPauliXOp_isPVM, MIPRE.Introspection.Honest.parsedPauliZOp_isPVM, MIPRE.Introspection.Honest.parsedPauliX_hide_commute, MIPRE.Introspection.Honest.parsedPauliZ_sample_commute, MIPRE.Introspection.Honest.parsedPauliX_hide_reject_zero, MIPRE.Introspection.Honest.parsedPauliZ_sample_reject_zero, MIPRE.Introspection.Honest.parsedHide_pauliX_reject_zero, MIPRE.Introspection.Honest.parsedSample_pauliZ_reject_zero, MIPRE.Introspection.Honest.auxOp_isPVM, MIPRE.Introspection.Honest.auxOp_commute, MIPRE.Introspection.Honest.auxOp_reject_zero, MIPRE.Introspection.Honest.auxStrategy_dimension, MIPRE.Introspection.Honest.auxStrategy_isPCC, MIPRE.Introspection.Honest.auxStrategy_value, MIPRE.Introspection.Honest.exists_auxPerfectPCC
statement: formalized
proof: formalized
---

# Perfect PCC strategy for the full auxiliary game

A perfect PCC source strategy extends to an explicit perfect PCC strategy for the induced game on every auxiliary type: Introspect, Sample, Read and all Hide levels, with the actual uniform ordered-edge law and full parsed answer alphabet. Its dimension is the seed cardinality times the source dimension. The recursive first Hide is exactly the full-register Pauli-$X$ coarse readout. The concrete parsed $X$/first-Hide and $Z$/Sample edges commute and have zero rejected products in both orientations. Construction of the honest strategy for all 26 Pauli types is still required for full typed completeness.

## Depends on

- [Honest operators on the complete parsed alphabet](lem-intro-honest-parsed.md)
- [Honest hiding marginals and edge compatibility](lem-intro-honest-hiding.md)
- [Honest sampling core and first hiding test](lem-intro-honest-core.md)

## Proof

Transport the local first-stage Fourier basis through the full-register coordinate equivalence. Assemble the previously constructed measurements on one register/source space. Analyze every edge of the induced auxiliary graph, including loops and the cross-introspection edge. Commuting effects establish PCC; vanishing rejected products establish value one.

## Lean

Formalized as [`MIPRE.Introspection.Honest.hideOp_zero_eq_firstHideOp`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.hideOp_zero_eq_firstHideOp), [`MIPRE.Introspection.Honest.pauliX_hideOp_zero_commute`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.pauliX_hideOp_zero_commute), [`MIPRE.Introspection.Honest.pauliX_hideOp_zero_reject`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.pauliX_hideOp_zero_reject), [`MIPRE.Introspection.Honest.parsedPauliXOp_isPVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.parsedPauliXOp_isPVM), [`MIPRE.Introspection.Honest.parsedPauliZOp_isPVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.parsedPauliZOp_isPVM), [`MIPRE.Introspection.Honest.parsedPauliX_hide_commute`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.parsedPauliX_hide_commute), [`MIPRE.Introspection.Honest.parsedPauliZ_sample_commute`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.parsedPauliZ_sample_commute), [`MIPRE.Introspection.Honest.parsedPauliX_hide_reject_zero`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.parsedPauliX_hide_reject_zero), [`MIPRE.Introspection.Honest.parsedPauliZ_sample_reject_zero`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.parsedPauliZ_sample_reject_zero), [`MIPRE.Introspection.Honest.parsedHide_pauliX_reject_zero`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.parsedHide_pauliX_reject_zero), [`MIPRE.Introspection.Honest.parsedSample_pauliZ_reject_zero`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.parsedSample_pauliZ_reject_zero), [`MIPRE.Introspection.Honest.auxOp_isPVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.auxOp_isPVM), [`MIPRE.Introspection.Honest.auxOp_commute`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.auxOp_commute), [`MIPRE.Introspection.Honest.auxOp_reject_zero`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.auxOp_reject_zero), [`MIPRE.Introspection.Honest.auxStrategy_dimension`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.auxStrategy_dimension), [`MIPRE.Introspection.Honest.auxStrategy_isPCC`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.auxStrategy_isPCC), [`MIPRE.Introspection.Honest.auxStrategy_value`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.auxStrategy_value), [`MIPRE.Introspection.Honest.exists_auxPerfectPCC`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.exists_auxPerfectPCC).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 2144](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L2144)
