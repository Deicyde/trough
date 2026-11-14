---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.adaptiveDualLabel_injective, MIPRE.Introspection.adaptiveX_reassembled_commutator_le, MIPRE.Introspection.TypedEstimates.introspect_adaptiveX_commutator, MIPRE.Introspection.option_readout_commutator_sum, MIPRE.Introspection.TypedEstimates.introspect_adaptiveZ_commutator
statement: formalized
proof: formalized
---

# Actual Sample and Read tests control conditional commutators

For a current product-form Introspect family, the actual parsed-game Sample and Read tests and the proved rigidity bounds control its prefix-weighted local Z and dual-X commutators, with the same constants as their full-carrier bounds. The current product form is an induction hypothesis; the commutator estimate is derived. Malformed outcomes remain in the common residual answer alphabet.

## Depends on

- [Actual coarse commutators for product-form induction](lem-intro-actual-product-commutators.md)
- [Concrete adaptive Z and dual-X factorization](lem-intro-adaptive-factorization.md)
- [Projective reassembly across adaptive prefixes](lem-intro-adaptive-reassembly.md)

## Proof

Embed each selected-coordinate label injectively into the actual option-valued Read alphabet. Keep these nonnegative terms of the global commutator sum and apply the exact factorization and weighted reassembled-commutator identity. For Z, remove only the impossible ideal dummy outcome and use the exact adaptive computational-readout factorization.

## Lean

Formalized as [`MIPRE.Introspection.adaptiveDualLabel_injective`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.adaptiveDualLabel_injective), [`MIPRE.Introspection.adaptiveX_reassembled_commutator_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.adaptiveX_reassembled_commutator_le), [`MIPRE.Introspection.TypedEstimates.introspect_adaptiveX_commutator`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.introspect_adaptiveX_commutator), [`MIPRE.Introspection.option_readout_commutator_sum`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.option_readout_commutator_sum), [`MIPRE.Introspection.TypedEstimates.introspect_adaptiveZ_commutator`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.introspect_adaptiveZ_commutator).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 2752](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L2752)
