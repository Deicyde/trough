---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.CLChecks.factorOfPrefix_outputPrefix, MIPRE.Introspection.CLChecks.factorOfPrefix_subset_prefixRegister, MIPRE.Introspection.TypedEstimates.check_hiding_next_dual, MIPRE.Introspection.TypedEstimates.check_hiding_read_dual, MIPRE.Introspection.TypedEstimates.hiding_read_dual_chain_estimate, MIPRE.Introspection.Honest.readDualOp_isPVM, MIPRE.Introspection.Honest.readDualOp_registerState_mirror, MIPRE.Introspection.TypedEstimates.read_register_rigidity_alice, MIPRE.Introspection.TypedEstimates.read_register_rigidity_bob, MIPRE.Introspection.TypedEstimates.read_register_rigidity_of_pauli
statement: formalized
proof: formalized
---

# Full Read rigidity

Read's marginal consisting of a stage's preceding claimed prefix and its dual answer is rigid at every stage on both parties. Its ideal family is the concrete honest hiding family with its unused X tail summed out. Uniform Alice and Bob squared-error bounds are $(16\ell^2+8)e+4B$ and $(32\ell^2+20)e+8B$, respectively.

## Depends on

- [Full hiding rigidity](../part-03/lem-hide-rigidity.md)
- [Actual hiding-prefix propagation to Introspect](../part-03/lem-intro-actual-prefix-chain.md)

## Proof

Every later hiding test preserves this fixed prefix/dual pair, including claimed outputs outside the CL image. Telescope the actual chain to Read at this coarse alphabet, with quadratic path loss. Discard the hiding tail through cross-party projective consistency, then use the Read consistency loop and exact ideal mirror for the other party.

## Lean

Formalized as [`MIPRE.Introspection.CLChecks.factorOfPrefix_outputPrefix`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.CLChecks.factorOfPrefix_outputPrefix), [`MIPRE.Introspection.CLChecks.factorOfPrefix_subset_prefixRegister`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.CLChecks.factorOfPrefix_subset_prefixRegister), [`MIPRE.Introspection.TypedEstimates.check_hiding_next_dual`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.check_hiding_next_dual), [`MIPRE.Introspection.TypedEstimates.check_hiding_read_dual`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.check_hiding_read_dual), [`MIPRE.Introspection.TypedEstimates.hiding_read_dual_chain_estimate`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.hiding_read_dual_chain_estimate), [`MIPRE.Introspection.Honest.readDualOp_isPVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.readDualOp_isPVM), [`MIPRE.Introspection.Honest.readDualOp_registerState_mirror`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.readDualOp_registerState_mirror), [`MIPRE.Introspection.TypedEstimates.read_register_rigidity_alice`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.read_register_rigidity_alice), [`MIPRE.Introspection.TypedEstimates.read_register_rigidity_bob`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.read_register_rigidity_bob), [`MIPRE.Introspection.TypedEstimates.read_register_rigidity_of_pauli`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.read_register_rigidity_of_pauli).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 2439](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L2439)
