---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.Honest.hideRegister_marginal, MIPRE.Introspection.Honest.hideOp_marginal, MIPRE.Introspection.Honest.pauliX_coordinateSplit, MIPRE.Introspection.Honest.stopHide_split, MIPRE.Introspection.Honest.readRegister_entry_supported, MIPRE.Introspection.Honest.hideRegister_entry_supported, MIPRE.Introspection.Honest.hidingNext_stop_join, MIPRE.Introspection.Honest.hidingNext_join, MIPRE.Introspection.Honest.hidingRead_join, MIPRE.Introspection.Honest.hideOp_commute_next, MIPRE.Introspection.Honest.hideOp_commute_read, MIPRE.Introspection.Honest.hideOp_reject_next_zero, MIPRE.Introspection.Honest.hideOp_reject_read_zero
statement: formalized
proof: formalized
---

# Honest hiding marginals and edge compatibility

The first marginal of honest Hide at index $k$ is exactly the readout of the CL presentation truncated at $k$. Nonzero Read and Hide effects force their reported vectors to be supported on the active register. The full Pauli-$X$ measurement factors under the actual local/tail coordinate split, and the stopping Hide measurement has the corresponding dual-linear-X/tail form. Neighboring hiding effects commute; for $k+1\lt \ell$, every answer pair rejected by the actual adjacent-hiding check has zero product. For $k+1=\ell$, the terminal Hide and Read effects commute and every rejected terminal comparison has zero product. These statements include all outcome labels.

## Depends on

- [Adaptive honest Read and Hide measurements](lem-intro-honest-adaptive.md)
- [The parsed introspection decision predicate](../part-02/lem-intro-parsed-predicate.md)

## Proof

Induct on the CL tree. The common local Z/dual-X PVM annihilates unequal local labels before the tail relation is used. At the first stage, the exact product selects the common dual output and the exact stopping-tail answer. At later stages, nonzero tail effects supply their own support conditions; the actual verifier relations lift through the common local label. Both tail projections in the adjacent comparison use the later reported question. The terminal stage identifies the common prefix and complete dual output.

## Lean

Formalized as [`MIPRE.Introspection.Honest.hideRegister_marginal`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.hideRegister_marginal), [`MIPRE.Introspection.Honest.hideOp_marginal`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.hideOp_marginal), [`MIPRE.Introspection.Honest.pauliX_coordinateSplit`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.pauliX_coordinateSplit), [`MIPRE.Introspection.Honest.stopHide_split`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.stopHide_split), [`MIPRE.Introspection.Honest.readRegister_entry_supported`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.readRegister_entry_supported), [`MIPRE.Introspection.Honest.hideRegister_entry_supported`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.hideRegister_entry_supported), [`MIPRE.Introspection.Honest.hidingNext_stop_join`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.hidingNext_stop_join), [`MIPRE.Introspection.Honest.hidingNext_join`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.hidingNext_join), [`MIPRE.Introspection.Honest.hidingRead_join`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.hidingRead_join), [`MIPRE.Introspection.Honest.hideOp_commute_next`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.hideOp_commute_next), [`MIPRE.Introspection.Honest.hideOp_commute_read`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.hideOp_commute_read), [`MIPRE.Introspection.Honest.hideOp_reject_next_zero`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.hideOp_reject_next_zero), [`MIPRE.Introspection.Honest.hideOp_reject_read_zero`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.hideOp_reject_read_zero).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 2036](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L2036)
