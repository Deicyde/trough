---
declaration: lemma
origin: cited
lean: MIPRE.AnswerReduction.shoupField_classical, MIPRE.AnswerReduction.fieldLarge_classical
statement: formalized
proof: formalized
---

# Supplying ambient answer reduction

The ambient contract `MIPRE.AnswerReduction 5` is inhabited.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Answer-reduction construction](../part-08/lem-ar-construction.md)
- [Answer-reduction completeness](../part-08/lem-ar-completeness.md)
- [Answer-reduction quantitative assembly](../part-08/lem-ar-error-assembly.md)
- [Effective classical PCP parameters](../part-07/lem-pcp-effective-parameters.md)

## Proof

By the answer-reduced verifier over the classical PCP decider. The three hypotheses the construction and its analysis ask of the decider hold for it: its field is the Shoup field, by definition; its parameters are polynomial in $(\log n,\log T,Q,\sigma)$, the padded dimension being so and the field degree polylogarithmic in $Qm'$; and its field is eventually larger than every fixed power of $8(Q+1)m'$ (Lemma [Effective classical PCP parameters](../part-07/lem-pcp-effective-parameters.md)). The complexity clause and the answer cut below the output bound are Lemma [Answer-reduction construction](../part-08/lem-ar-construction.md), completeness is Lemma [Answer-reduction completeness](../part-08/lem-ar-completeness.md) at the cut and hence at the bound, and soundness is Lemma [Answer-reduction quantitative assembly](../part-08/lem-ar-error-assembly.md) at the bound. Runtime and answer-cut normalization (Remark [Runtime normalization obligation](../README.md)), the PCC bridge (Remark [Source PCC and the required representation bridge](../../foundations/README.md)) and the typed oracle interface (Remark [The specification and the earlier contract](../README.md)) are absorbed by the construction: the input's time bound is used semantically, the output rejects answers beyond its cut, and the typed oracularized game is the one Lemma [Decoding with the original answer cutoff](../part-08/lem-ar-decoding.md) plays.

## Lean

Formalized as [`MIPRE.AnswerReduction.shoupField_classical`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.shoupField_classical), [`MIPRE.AnswerReduction.fieldLarge_classical`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.fieldLarge_classical).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 6128](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L6128)
