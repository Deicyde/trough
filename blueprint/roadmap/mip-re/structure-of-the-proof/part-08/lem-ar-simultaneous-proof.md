---
declaration: lemma
origin: cited
lean: MIPRE.AnswerReduction.exists_ext6, MIPRE.AnswerReduction.ext6_spec, MIPRE.AnswerReduction.sum_deltaSim6_le, MIPRE.AnswerReduction.sum_dis_JAe_GBe_le, MIPRE.AnswerReduction.sum_dis_GAe_JBe_le
statement: formalized
proof: formalized
---

# A simultaneous complete proof tuple

Use the simultaneous theorem at $(q,m',d,m'+6)$ to obtain a projective measurement $J$ of the entire tuple $(f_1,\ldots,f_5,c_0,\ldots,c_{m'})$. Write $M_i$ for individual point measurements, and $M_6$ for the complete proof-tuple point measurement. With seed averaging understood, retain all five relations: $M_i(y_i)$ is cross-party consistent with the $i$th evaluation coordinate of $M_6(z)$ for $i=3,4,5$ with error $O(\theta)$; $M_i(y)$ is consistent with $G_i$ evaluated at $y$; the two copies of $G_i$ are consistent; $M_6(z)$ is consistent with $J$ evaluated at $z$; and the two copies of the complete $J$ are consistent. The last four errors are $O(\kappa)$. Include player mirrors of the first, second and fourth. Individual evaluations without a projective complete-tuple output do not suffice for the next lemma.

## Depends on

- [Common individual polynomial measurements](lem-ar-common-polynomials.md)

## Proof depends on

- [Input-codeword consistency tests](lem-ar-input-tests.md)
- [Combined $XZ$ point measurements](../../background-results/part-02/lem-qld-combined-points.md)

## Proof

The simultaneous test at $(q,m',d,m'+6)$ extracts $J$ per seed (`exists_ext6`, `ext6_spec`), in the model as for the single copies, and averaged as for them (`sum_deltaSim6_le`). The relations chain by the triangle inequality for disagreement: one player's evaluated $J$ against the other's point of the sixth copy, that point against the other's point of copy $i$, and that against the other's evaluated $G_i$ (`sum_dis_JAe_GBe_le`, `sum_dis_GAe_JBe_le`).

## Lean

Formalized as [`MIPRE.AnswerReduction.exists_ext6`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.exists_ext6), [`MIPRE.AnswerReduction.ext6_spec`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.ext6_spec), [`MIPRE.AnswerReduction.sum_deltaSim6_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.sum_deltaSim6_le), [`MIPRE.AnswerReduction.sum_dis_JAe_GBe_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.sum_dis_JAe_GBe_le), [`MIPRE.AnswerReduction.sum_dis_GAe_JBe_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.sum_dis_GAe_JBe_le).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 5837](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L5837)
