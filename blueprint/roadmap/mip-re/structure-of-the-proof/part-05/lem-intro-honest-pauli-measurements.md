---
declaration: lemma
origin: cited
lean: MIPRE.QLD.Honest.probe_observable, MIPRE.QLD.Honest.probe_phase, MIPRE.QLD.Honest.answerOp_isPVM, MIPRE.QLD.Honest.answerOp_format_zero, MIPRE.QLD.Honest.answerOp_pauli, MIPRE.QLD.Honest.pvm_fibre_commute, MIPRE.QLD.Honest.pvm_fibre_reject, MIPRE.QLD.Honest.answerOp_aline_point_commute, MIPRE.QLD.Honest.answerOp_dline_point_commute, MIPRE.QLD.Honest.answerOp_pauli_point_commute, MIPRE.QLD.Honest.answerOp_aline_point_reject, MIPRE.QLD.Honest.answerOp_dline_point_reject, MIPRE.QLD.Honest.answerOp_pauli_point_reject, MIPRE.QLD.Honest.answerOp_point_pairB_commute, MIPRE.QLD.Honest.answerOp_point_pairB_reject, MIPRE.QLD.Honest.answerOp_point_var_commute, MIPRE.QLD.Honest.answerOp_point_var_reject, MIPRE.QLD.Honest.answerOp_con_var_commute, MIPRE.QLD.Honest.answerOp_con_var_reject, MIPRE.QLD.Honest.answerOp_pairB_pair_commute, MIPRE.QLD.Honest.answerOp_pairB_pair_reject
statement: formalized
proof: formalized
---

# All honest Pauli measurements and their tested edge identities

The honest field-register Pauli strategy, with one extra qubit, has explicit PVMs for all twenty-six question types and zero effects for malformed answers. Its full-Pauli measurements are the required register readouts. The actual trace probes are exactly the corresponding Weyl observables, and the verifier phase is their commutation phase. For degree bound at least one, the sampled low-degree, Pauli-point, pair, Magic Square, and distinguished-variable edges have commuting effects and zero product on every rejected answer pair.

## Depends on

- [Honest Magic Square extension of an anticommuting pair](lem-intro-honest-magic-square.md)

## Proof depends on

- [Admissible padded setup](../../background-results/part-03/lem-qld-global-setup.md)
- [Exact final strategy extraction](../part-03/lem-intro-final-extraction.md)

## Proof

Coarse-grain a common Pauli PVM for all same-basis questions. Its multilinear encoding restricts to an affine polynomial on an axis line and degree at most $m$ on any diagonal; evaluation at the sampled line parameter recovers the point value, even for zero direction. For zero phase use the commuting joint probe PVM, and for nonzero phase use the concrete Magic Square extension. Its distinguished cells preserve the original probes. Coarse-graining preserves commutation and zero rejected products.

## Lean

Formalized as [`MIPRE.QLD.Honest.probe_observable`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.Honest.probe_observable), [`MIPRE.QLD.Honest.probe_phase`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.Honest.probe_phase), [`MIPRE.QLD.Honest.answerOp_isPVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.Honest.answerOp_isPVM), [`MIPRE.QLD.Honest.answerOp_format_zero`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.Honest.answerOp_format_zero), [`MIPRE.QLD.Honest.answerOp_pauli`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.Honest.answerOp_pauli), [`MIPRE.QLD.Honest.pvm_fibre_commute`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.Honest.pvm_fibre_commute), [`MIPRE.QLD.Honest.pvm_fibre_reject`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.Honest.pvm_fibre_reject), [`MIPRE.QLD.Honest.answerOp_aline_point_commute`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.Honest.answerOp_aline_point_commute), [`MIPRE.QLD.Honest.answerOp_dline_point_commute`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.Honest.answerOp_dline_point_commute), [`MIPRE.QLD.Honest.answerOp_pauli_point_commute`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.Honest.answerOp_pauli_point_commute), [`MIPRE.QLD.Honest.answerOp_aline_point_reject`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.Honest.answerOp_aline_point_reject), [`MIPRE.QLD.Honest.answerOp_dline_point_reject`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.Honest.answerOp_dline_point_reject), [`MIPRE.QLD.Honest.answerOp_pauli_point_reject`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.Honest.answerOp_pauli_point_reject), [`MIPRE.QLD.Honest.answerOp_point_pairB_commute`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.Honest.answerOp_point_pairB_commute), [`MIPRE.QLD.Honest.answerOp_point_pairB_reject`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.Honest.answerOp_point_pairB_reject), [`MIPRE.QLD.Honest.answerOp_point_var_commute`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.Honest.answerOp_point_var_commute), [`MIPRE.QLD.Honest.answerOp_point_var_reject`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.Honest.answerOp_point_var_reject), [`MIPRE.QLD.Honest.answerOp_con_var_commute`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.Honest.answerOp_con_var_commute), [`MIPRE.QLD.Honest.answerOp_con_var_reject`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.Honest.answerOp_con_var_reject), [`MIPRE.QLD.Honest.answerOp_pairB_pair_commute`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.Honest.answerOp_pairB_pair_commute), [`MIPRE.QLD.Honest.answerOp_pairB_pair_reject`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.Honest.answerOp_pairB_pair_reject).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 3318](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L3318)
