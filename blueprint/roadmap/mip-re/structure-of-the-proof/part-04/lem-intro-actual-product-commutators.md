---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.TypedEstimates.introspect_read_full_estimate, MIPRE.Introspection.TypedEstimates.introspect_dual_commutator, MIPRE.Introspection.TypedEstimates.introspect_coarseZ_commutator_bob, MIPRE.Introspection.TypedEstimates.introspect_coarseZ_commutator_alice
statement: formalized
proof: formalized
---

# Actual coarse commutators for product-form induction

The actual Read joint measurement yields a commutator bound for the full Introspect question/answer and each ideal prefix/dual family. The Sample joint measurement yields the corresponding bound with any finite coarsening of the computational readout, including adaptive prefix and selected-coordinate maps. Both follow from game success and the proved rigidity estimates.

## Depends on

- [Full Read rigidity](lem-intro-read-rigidity.md)
- [Initializing hiding from the actual Pauli tests](../part-03/lem-intro-hiding-initialization.md)
- [Product-form stage from coarse tests](lem-intro-coarse-product-stage.md)

## Proof

Choose the coarse joint outcome before applying commutation analysis. Its first marginal is tested against Introspect; its second is compared with the proved ideal Read or Sample readout. Removing prefix projectors and constructing the evolving residual strategy remain obligations of the product-form induction.

## Lean

Formalized as [`MIPRE.Introspection.TypedEstimates.introspect_read_full_estimate`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.introspect_read_full_estimate), [`MIPRE.Introspection.TypedEstimates.introspect_dual_commutator`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.introspect_dual_commutator), [`MIPRE.Introspection.TypedEstimates.introspect_coarseZ_commutator_bob`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.introspect_coarseZ_commutator_bob), [`MIPRE.Introspection.TypedEstimates.introspect_coarseZ_commutator_alice`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.introspect_coarseZ_commutator_alice).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 2468](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L2468)
