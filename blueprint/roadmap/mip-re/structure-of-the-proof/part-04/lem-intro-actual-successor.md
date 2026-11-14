---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.exists_initial_residual, MIPRE.Introspection.initialIntroPrefixInvariant, MIPRE.Introspection.nextPrefixDecodedPOVM_some_support, MIPRE.Introspection.registeredReplacement_nextOption_mats, MIPRE.Introspection.canonicalizeIntro_adaptive_selected, MIPRE.Introspection.registeredReplacement_canonicalizeIntro, MIPRE.Introspection.introSuccessorFamily_isPVM, MIPRE.Introspection.introSuccessorInvariant, MIPRE.Introspection.TypedEstimates.introBobZError, MIPRE.Introspection.TypedEstimates.introAliceZError, MIPRE.Introspection.TypedEstimates.exists_intro_successor
statement: formalized
proof: formalized
---

# Initializing and advancing the actual prefix invariant

Every projective full-answer Introspect measurement has the initial prefix invariant on its original auxiliary space. At each subsequent stage, the actual game tests construct a projective replacement with the next prefix form and valid-answer support. Its failure increases by at most the proved stage loss. Every other question is its original identity extension, and all fixed Alice hiding errors are preserved exactly. The raw selected measurement identity follows from canonicalization and decoder recovery.

## Depends on

- [Refining and updating the actual Introspect answer](lem-intro-answer-refinement.md)
- [Constructing the next-prefix residual invariant](lem-intro-next-invariant.md)
- [One stage budget from the actual game tests](lem-intro-game-stage.md)
- [Preserving the fixed errors under replacement](lem-intro-fixed-errors.md)

## Proof

At stage zero the visited register is empty; only prefix zero survives. Transport the original measurement to its remaining-register carrier and use a deterministic malformed answer on other branches. At a successor, decode each refined residual before reassembly. Canonicalization preserves game value and is overwritten at the selected question by replacement. Attainable next prefixes satisfy the decoder's coordinate identity; all other residuals report the malformed answer. Apply the actual stage bounds and the quantitative replacement theorem.

## Lean

Formalized as [`MIPRE.Introspection.exists_initial_residual`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.exists_initial_residual), [`MIPRE.Introspection.initialIntroPrefixInvariant`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.initialIntroPrefixInvariant), [`MIPRE.Introspection.nextPrefixDecodedPOVM_some_support`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.nextPrefixDecodedPOVM_some_support), [`MIPRE.Introspection.registeredReplacement_nextOption_mats`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.registeredReplacement_nextOption_mats), [`MIPRE.Introspection.canonicalizeIntro_adaptive_selected`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.canonicalizeIntro_adaptive_selected), [`MIPRE.Introspection.registeredReplacement_canonicalizeIntro`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.registeredReplacement_canonicalizeIntro), [`MIPRE.Introspection.introSuccessorFamily_isPVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.introSuccessorFamily_isPVM), [`MIPRE.Introspection.introSuccessorInvariant`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.introSuccessorInvariant), [`MIPRE.Introspection.TypedEstimates.introBobZError`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.introBobZError), [`MIPRE.Introspection.TypedEstimates.introAliceZError`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.introAliceZError), [`MIPRE.Introspection.TypedEstimates.exists_intro_successor`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.exists_intro_successor).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 2916](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L2916)
