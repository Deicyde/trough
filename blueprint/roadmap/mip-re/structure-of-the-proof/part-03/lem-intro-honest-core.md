---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.Honest.coreOp_isPVM, MIPRE.Introspection.Honest.coreOp_commute, MIPRE.Introspection.Honest.coreStrategy_dimension, MIPRE.Introspection.Honest.exists_corePerfectPCC, MIPRE.Introspection.Honest.pauliZ_sample_commute, MIPRE.Introspection.Honest.sample_typed_reject_zero, MIPRE.Introspection.Honest.firstHideOp_isPVM, MIPRE.Introspection.Honest.pauli_firstHide_commute, MIPRE.Introspection.Honest.firstHide_typed_reject_zero
statement: formalized
proof: formalized
---

# Honest sampling core and first hiding test

A perfect PCC strategy for the source game gives an actual perfect PCC strategy for the induced four-type Introspect/Sample game, including its loops, sampling edges and cross-introspection edge. Its dimension is the source dimension times the seed alphabet size. Honest Pauli-$Z$/Sample and Pauli-$X$/first-Hide effects commute and their products vanish whenever the full parsed test rejects. All outcome labels are retained. The extension to all adaptive Read and Hide types is proved in Lemma [Perfect PCC strategy for the full auxiliary game](lem-intro-honest-full-auxiliary.md). The complete Pauli subgame remains a separate construction.

## Depends on

- [The parsed introspection decision predicate](../part-02/lem-intro-parsed-predicate.md)
- [Exact final strategy extraction](lem-intro-final-extraction.md)
- [PCC strategy](../../foundations/part-01/def-pcc.md)

## Proof depends on

- [Pauli mixing with a retained classical fibre](../part-02/lem-pauli-mixing.md)
- [A perfect strategy rejects nothing on the support](../../foundations/part-01/lem-perfect-rejects-nothing.md)

## Proof

Tensor the source measurements with diagonal seed-fibre projectors. Disjoint fibres annihilate, so source PCC is needed only for question pairs arising from a common seed. The first hiding PVM is the coarse-graining of the full Pauli-$X$ measurement that reports the first dual readout and the untouched tail. Check the actual parsed predicate on every constructor.

## Lean

Formalized as [`MIPRE.Introspection.Honest.coreOp_isPVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.coreOp_isPVM), [`MIPRE.Introspection.Honest.coreOp_commute`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.coreOp_commute), [`MIPRE.Introspection.Honest.coreStrategy_dimension`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.coreStrategy_dimension), [`MIPRE.Introspection.Honest.exists_corePerfectPCC`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.exists_corePerfectPCC), [`MIPRE.Introspection.Honest.pauliZ_sample_commute`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.pauliZ_sample_commute), [`MIPRE.Introspection.Honest.sample_typed_reject_zero`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.sample_typed_reject_zero), [`MIPRE.Introspection.Honest.firstHideOp_isPVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.firstHideOp_isPVM), [`MIPRE.Introspection.Honest.pauli_firstHide_commute`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.pauli_firstHide_commute), [`MIPRE.Introspection.Honest.firstHide_typed_reject_zero`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.firstHide_typed_reject_zero).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 2003](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L2003)
