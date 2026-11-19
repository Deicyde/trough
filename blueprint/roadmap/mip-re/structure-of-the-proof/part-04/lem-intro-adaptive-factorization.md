---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.Honest.hidingPrefixOp_factor, MIPRE.Introspection.Honest.readDualOp_eq_registerDual, MIPRE.Introspection.Honest.dualRegister_cons_succ, MIPRE.Introspection.Honest.synX_split_second, MIPRE.Introspection.Honest.readDualOp_prefix_factor, MIPRE.Introspection.readDualOp_stage_factor, MIPRE.Introspection.adaptiveZ_readout_factor
statement: formalized
proof: formalized
---

# Concrete adaptive Z and dual-X factorization

The actual prefix projector, adaptive computational readout, and Read dual marginal factor on their concrete selected registers. The Read factorization holds for every claimed prefix, including off-image labels. On canonical selected-coordinate labels its residual operator is precisely the linear dual-X readout required by mixing.

## Depends on

- [Full Read rigidity](lem-intro-read-rigidity.md)
- [Actual adaptive prefix law and residual registers](lem-intro-adaptive-prefix.md)

## Proof

Follow the existing recursive Hide PVM through its coarse marginal. Summing earlier dual answers leaves the Z prefix. Split the X spectral projectors on the actual coordinate partition and identify the recursive dual map with the selected local linear map.

## Lean

Formalized as [`MIPRE.Introspection.Honest.hidingPrefixOp_factor`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.hidingPrefixOp_factor), [`MIPRE.Introspection.Honest.readDualOp_eq_registerDual`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.readDualOp_eq_registerDual), [`MIPRE.Introspection.Honest.dualRegister_cons_succ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.dualRegister_cons_succ), [`MIPRE.Introspection.Honest.synX_split_second`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.synX_split_second), [`MIPRE.Introspection.Honest.readDualOp_prefix_factor`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.readDualOp_prefix_factor), [`MIPRE.Introspection.readDualOp_stage_factor`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.readDualOp_stage_factor), [`MIPRE.Introspection.adaptiveZ_readout_factor`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.adaptiveZ_readout_factor).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 2663](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L2663)
