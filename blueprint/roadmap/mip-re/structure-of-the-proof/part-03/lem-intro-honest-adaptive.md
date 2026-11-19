---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.Honest.readRegister_isPVM, MIPRE.Introspection.Honest.hideRegister_isPVM, MIPRE.Introspection.Honest.readOp_marginal, MIPRE.Introspection.Honest.fullReadOp_isPVM, MIPRE.Introspection.Honest.fullReadOp_marginal, MIPRE.Introspection.Honest.introspect_read_commute, MIPRE.Introspection.Honest.read_typed_reject_zero
statement: formalized
proof: formalized
---

# Adaptive honest Read and Hide measurements

Recursion on the original CL presentation constructs the honest register PVMs for Read and every Hide level, including adaptive branch-dependent registers. The Read first marginal is exactly the original CL question readout. Attaching the original question-dependent answer measurement gives the full Read PVM, whose Introspect marginal is exact. Its effects commute with Introspect, and every rejection by the actual parsed Introspect/Read test has zero operator product. The hiding edges are proved in Lemma [Honest hiding marginals and edge compatibility](lem-intro-honest-hiding.md); assembly with the full Pauli strategy remains an additional obligation.

## Depends on

- [Honest sampling core and first hiding test](lem-intro-honest-core.md)
- [Projectivity of sampling and hiding readouts](../part-02/lem-intro-linear-readout-projectivity.md)

## Proof

At a CL node, measure the commuting linear-Z and dual-linear-X outcomes on the selected register, and use the Z outcome to select the continuation on the complement. These factors are disjoint, so their controlled tensor product is a PVM. Nonzero matrix rows force the reported CL question; summing the dual outcome gives its exact computational readout projector. Then tensor the original answer PVM and use its orthogonality.

## Lean

Formalized as [`MIPRE.Introspection.Honest.readRegister_isPVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.readRegister_isPVM), [`MIPRE.Introspection.Honest.hideRegister_isPVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.hideRegister_isPVM), [`MIPRE.Introspection.Honest.readOp_marginal`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.readOp_marginal), [`MIPRE.Introspection.Honest.fullReadOp_isPVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.fullReadOp_isPVM), [`MIPRE.Introspection.Honest.fullReadOp_marginal`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.fullReadOp_marginal), [`MIPRE.Introspection.Honest.introspect_read_commute`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.introspect_read_commute), [`MIPRE.Introspection.Honest.read_typed_reject_zero`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.read_typed_reject_zero).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 2113](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L2113)
