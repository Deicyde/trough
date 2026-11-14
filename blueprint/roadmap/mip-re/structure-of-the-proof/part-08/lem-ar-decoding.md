---
declaration: lemma
origin: cited
lean: MIPRE.AnswerReduction.MAo, MIPRE.AnswerReduction.MBo, MIPRE.AnswerReduction.decAns, MIPRE.AnswerReduction.pcpOf, MIPRE.AnswerReduction.pcpSound, MIPRE.AnswerReduction.one_sub_povmValue_decoded_le, MIPRE.AnswerReduction.val_ge_decoded, MIPRE.AnswerReduction.val_ge_of_typedGame
statement: formalized
proof: formalized
---

# Decoding with the original answer cutoff

Decode the polynomial strategy to the oracle strategy, applying the length-$B_D(n)$ prefix cutoff to each original answer. It preserves the simulated decider's output both before and after the oracle construction, and makes every decoded answer pass its bounded parser. Check all three oracle subtests. Group malformed or failed decodings into fixed legal outcomes so measurements remain complete. The final conversion to the input game yields deficit $O(\delta_3^{1/4})$. The Lean decodes without the sandwich and without a cutoff. An oracle measures the complete $J$ and answers the pair decoded from its first two answer polynomials, read on their blocks; an isolated player measures its own copy's $G$ and answers the decoded polynomial. The decoder returns the answer of length at most $2^{(\lambda n+1)^\mu}$ whose answer vector the polynomial's Boolean values are. No truncation is needed: the PCP's soundness gives accepted answers of length at most $T$, and an input within its budget rejects answers longer than $2^{(\lambda n+1)^\mu}$, so accepted answers already fit its alphabet, where the answer vector determines them. The oracle's game check fails only where $J$'s outcome is not placed on its blocks, or the PCP check rejects it at half the points; each ordered pair of roles fails at most by a game check and the disagreement of the polynomials. The decoded POVM strategy fails the typed oracularized game with probability at most $6$ times the combined error. Its measurements are coarse-grainings of the extracted projective ones, so it is a projective strategy in the model with no dilation, and oracularization soundness (one square root) gives $\omega(\mathsf{V}_n)\geq 1-24\sqrt{7\,\mathrm{err}}$ in every value model $\omega$ in which oracularization is sound (Definition [Oracularization is sound in a value model](../../downstream-results/part-02/def-oracular-sound-in.md)) and which dominates the model (Definition [Projective strategy in a bipartite model](../../downstream-results/part-02/def-model-proj-strategy.md)); in particular $\mathrm{val}^*(\mathsf{V}_n)$.

## Depends on

- [A simultaneous complete proof tuple](lem-ar-simultaneous-proof.md)
- [Schwartz–Zippel](../../background-results/part-05/lem-schwartz-zippel.md)
- [The bespoke PCP for deciders](../part-07/thm-pcp-decider.md)
- [Answer-reduction completeness](lem-ar-completeness.md)
- [Completing the pair measurement projectively](../../background-results/part-03/lem-qld-global-complete.md)

## Proof depends on

- [Oracularization is sound in both models](../../downstream-results/part-02/thm-oracularization-in-model.md)

## Proof

As described: the nine ordered pairs of roles are bounded pair by pair, and the bounds summed over the seed with the averaged extraction errors of Lemmas [Common individual polynomial measurements](lem-ar-common-polynomials.md) and [A simultaneous complete proof tuple](lem-ar-simultaneous-proof.md).

## Lean

Formalized as [`MIPRE.AnswerReduction.MAo`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.MAo), [`MIPRE.AnswerReduction.MBo`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.MBo), [`MIPRE.AnswerReduction.decAns`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.decAns), [`MIPRE.AnswerReduction.pcpOf`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.pcpOf), [`MIPRE.AnswerReduction.pcpSound`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.pcpSound), [`MIPRE.AnswerReduction.one_sub_povmValue_decoded_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.one_sub_povmValue_decoded_le), [`MIPRE.AnswerReduction.val_ge_decoded`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.val_ge_decoded), [`MIPRE.AnswerReduction.val_ge_of_typedGame`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.val_ge_of_typedGame).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 5908](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L5908)
