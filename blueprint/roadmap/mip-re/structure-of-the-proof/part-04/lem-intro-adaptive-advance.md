---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.advancePrefix_old_prefix, MIPRE.Introspection.advancePrefix_remaining, MIPRE.Introspection.advancePrefix_injective, MIPRE.Introspection.advancePrefix_eval, MIPRE.Introspection.adaptiveLinear_readout_factor, MIPRE.Introspection.advancePrefix_projector_assembly
statement: formalized
proof: formalized
---

# Advancing the actual prefix label

Adding the selected coordinate answer preserves the preceding claimed prefix and selects the intended next remaining register. On attainable old prefixes the extended label recovers both components and is injective. For the actual selected linear outcome it is precisely the next sampler prefix. Coarse assembly of the old prefix and current linear Z projector is exactly the next honest prefix projector.

## Depends on

- [Concrete adaptive Z and dual-X factorization](lem-intro-adaptive-factorization.md)

## Proof

Use locality of claimed-prefix extraction and disjointness of the current factor from visited coordinates. Recover the old prefix and selected coordinates, then identify the actual next sampler value using the sum of its stage maps.

## Lean

Formalized as [`MIPRE.Introspection.advancePrefix_old_prefix`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.advancePrefix_old_prefix), [`MIPRE.Introspection.advancePrefix_remaining`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.advancePrefix_remaining), [`MIPRE.Introspection.advancePrefix_injective`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.advancePrefix_injective), [`MIPRE.Introspection.advancePrefix_eval`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.advancePrefix_eval), [`MIPRE.Introspection.adaptiveLinear_readout_factor`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.adaptiveLinear_readout_factor), [`MIPRE.Introspection.advancePrefix_projector_assembly`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.advancePrefix_projector_assembly).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 2735](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L2735)
