---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.Complete.pauliOp_X, MIPRE.Introspection.Complete.pauliOp_Z, MIPRE.Introspection.Complete.sampleOp_commute, MIPRE.Introspection.Complete.sampleOp_reject, MIPRE.Introspection.Complete.strategy_isPCC, MIPRE.Introspection.Complete.strategy_value, MIPRE.Introspection.Complete.exists_perfectPCC, MIPRE.Introspection.BinaryComplete.pauliOp_X, MIPRE.Introspection.BinaryComplete.pauliOp_Z, MIPRE.Introspection.BinaryComplete.strategy_isPCC, MIPRE.Introspection.BinaryComplete.strategy_value, MIPRE.Introspection.BinaryComplete.exists_perfectPCC
statement: formalized
proof: formalized
---

# Concrete completeness for the full typed introspection game

A perfect PCC source strategy gives a perfect PCC strategy for the actual full parsed introspection game, including all Pauli and auxiliary types. The field-register construction has local dimension $2|F|^{2^m}D$, where $D$ is the source dimension. A supplied self-dual binary basis transports the construction to arbitrary binary CL source functions on $2^m t$ coordinates, with dimension $2\cdot2^{2^m t}D$. The binary source functions need not be linear over the larger field.

## Depends on

- [The actual three-level Pauli question sampler](lem-intro-pauli-cl-content.md)
- [PCC strategy](../../foundations/part-01/def-pcc.md)
- [Concrete typed sampling and terminal hiding estimates](../part-03/lem-intro-typed-estimates.md)
- [Qudits are qubits, in characteristic two](../../foundations/part-02/lem-pauli-binary.md)

## Proof depends on

- [Perfect PCC strategy for the full auxiliary game](../part-03/lem-intro-honest-full-auxiliary.md)
- [All honest Pauli measurements and their tested edge identities](lem-intro-honest-pauli-measurements.md)
- [Cool closeness fact, and the marginal step](../../foundations/part-02/lem-cool-closeness-fact.md)

## Proof

Put the explicit Pauli PVMs, the auxiliary PVMs, the source strategy and one extra qubit on a common carrier. Check the X/Hide and Z/Sample anchor edges using the exact distinguished Pauli projectors. A positive question pair retains a common content sample; every graph edge then has commuting effects and zero product on rejected answers. Normalized trace gives perfect acceptance. For binary sources, conjugate the quantum register through the self-dual basis before composing the auxiliary measurements.

## Lean

Formalized as [`MIPRE.Introspection.Complete.pauliOp_X`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Complete.pauliOp_X), [`MIPRE.Introspection.Complete.pauliOp_Z`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Complete.pauliOp_Z), [`MIPRE.Introspection.Complete.sampleOp_commute`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Complete.sampleOp_commute), [`MIPRE.Introspection.Complete.sampleOp_reject`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Complete.sampleOp_reject), [`MIPRE.Introspection.Complete.strategy_isPCC`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Complete.strategy_isPCC), [`MIPRE.Introspection.Complete.strategy_value`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Complete.strategy_value), [`MIPRE.Introspection.Complete.exists_perfectPCC`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Complete.exists_perfectPCC), [`MIPRE.Introspection.BinaryComplete.pauliOp_X`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.BinaryComplete.pauliOp_X), [`MIPRE.Introspection.BinaryComplete.pauliOp_Z`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.BinaryComplete.pauliOp_Z), [`MIPRE.Introspection.BinaryComplete.strategy_isPCC`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.BinaryComplete.strategy_isPCC), [`MIPRE.Introspection.BinaryComplete.strategy_value`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.BinaryComplete.strategy_value), [`MIPRE.Introspection.BinaryComplete.exists_perfectPCC`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.BinaryComplete.exists_perfectPCC).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 3473](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L3473)
