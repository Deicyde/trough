---
declaration: lemma
origin: cited
lean: MIPRE.QLD.Honest.qldGame_positive_content, MIPRE.QLD.Honest.answerOp_commute, MIPRE.QLD.Honest.answerOp_reject, MIPRE.QLD.Honest.strategy_isPCC, MIPRE.QLD.Honest.strategy_value, MIPRE.QLD.Honest.exists_perfectPCC
statement: formalized
proof: formalized
---

# Perfect PCC completeness of the full Pauli game

For nonzero $m$, $m\mid|F|$, and $d\geq1$, the actual twenty-six-type Pauli game has a perfect PCC strategy in its doubled presentation, on local dimension twice the cardinality of the field register. All effects, commutation identities, and rejected-product identities are constructed for the actual question distribution and actual verifier predicate.

## Depends on

- [All honest Pauli measurements and their tested edge identities](lem-intro-honest-pauli-measurements.md)
- [PCC strategy](../../foundations/part-01/def-pcc.md)

## Proof

Positive question mass yields one common content sample and an actual ordered graph edge. A finite graph classification reduces forward edges to the previously checked identities. Reverse edges follow by symmetry of the predicate and commutation; loops use orthogonality of the same PVM. Number the register basis and package the projective families as a synchronous strategy for the doubled game. Zero rejected products give value one under normalized trace, and the tested commutations give PCC.

## Lean

Formalized as [`MIPRE.QLD.Honest.qldGame_positive_content`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.Honest.qldGame_positive_content), [`MIPRE.QLD.Honest.answerOp_commute`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.Honest.answerOp_commute), [`MIPRE.QLD.Honest.answerOp_reject`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.Honest.answerOp_reject), [`MIPRE.QLD.Honest.strategy_isPCC`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.Honest.strategy_isPCC), [`MIPRE.QLD.Honest.strategy_value`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.Honest.strategy_value), [`MIPRE.QLD.Honest.exists_perfectPCC`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.Honest.exists_perfectPCC).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 3364](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L3364)
