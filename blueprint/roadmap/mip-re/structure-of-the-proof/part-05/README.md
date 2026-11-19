---
navigation: transparent
---

# An explicit admissible error… to Introspection soundness from…

- [An explicit admissible error threshold for finite iteration](lem-intro-iteration-threshold.md)
- [Finite iteration of the actual Alice strategy](lem-intro-actual-iteration.md)
- [Terminal conditional readouts with malformed answers](lem-intro-terminal-invariant.md)
- [Player exchange and the actual Bob iteration](lem-intro-bob-iteration.md)
- [Both actual terminal measurements](lem-intro-two-sided-iteration.md)
- [Ordinary-answer extraction from actual terminal invariants](lem-intro-terminal-option-extraction.md)
- [A power bound for the entire finite recurrence](lem-intro-recurrence-power.md)
- [Finite-game soundness from the primitive Pauli guarantees](lem-intro-primitive-soundness.md)
- [Soundness on the approximately extracted state](lem-intro-extracted-state-soundness.md)
- [Local-isometry transport and image-complement completion](lem-intro-isometric-strategy.md)
- [Honest Magic Square extension of an anticommuting pair](lem-intro-honest-magic-square.md)
- [The actual three-level Pauli question sampler](lem-intro-pauli-cl-content.md)
- [All honest Pauli measurements and their tested edge identities](lem-intro-honest-pauli-measurements.md)
- [Perfect PCC completeness of the full Pauli game](lem-intro-honest-full-pauli.md)
- [Finite soundness from the valid-answer extraction interface](lem-intro-valid-isometric-soundness.md)
- [Executable canonical lines and explicit binary coordinates](lem-intro-executable-lines.md)
- [Concrete completeness for the full typed introspection game](lem-intro-full-typed-completeness.md)
- [Restriction to the actual Pauli game](lem-intro-pauli-restriction.md)
- [Pauli extraction for the introspection game](lem-intro-pauli-extraction.md)

Comments. This is the paper's use of `cor:pauli-binary` in the proof of `lem:intro-pauli-strat` (Lemma [Extracting a Pauli strategy](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L1635)): the conditioning on the Pauli block is the factor $N$, and the estimates are kept as distances, the form Lemma [Finite soundness from the valid-answer extraction interface](lem-intro-valid-isometric-soundness.md) consumes, rather than used to replace the strategy by an exact one. Theorem [Pauli basis test / quantum low individual degree test](../../background-results/part-01/thm-qld.md) gives all four Pauli estimates, as the paper states them; the extraction keeps the two the consumer uses, Alice's $X$ and Bob's $Z$. Reading the estimates at the valid answers costs nothing: the decoder of Lemma [The ambient compiler's resources and raw-game bridge](../part-06/lem-intro-ambient-kernel.md) makes the strategy's Pauli measurements supported on the full-register answers, so the answers read as one register label are that label's answer alone. Only the binary game is used for soundness; the field-register game of Lemma [Concrete completeness for the full typed introspection game](lem-intro-full-typed-completeness.md) serves completeness. `MIPRE/Background/Introspection/RestrictedSoundness.lean` and `RestrictedProfileSoundness.lean`.

- [Introspection soundness from the extracted Pauli strategy](lem-intro-extracted-soundness.md)
