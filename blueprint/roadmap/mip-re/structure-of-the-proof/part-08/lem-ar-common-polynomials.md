---
declaration: lemma
origin: cited
lean: MIPRE.AnswerReduction.exists_ext1, MIPRE.AnswerReduction.ext1_spec, MIPRE.AnswerReduction.sum_deltaSim1_le, MIPRE.LIDT.Simul.sum_deltaSim_le
statement: formalized
proof: formalized
---

# Common individual polynomial measurements

For each seed, extract the input and proof polynomial PVMs, averaged with the source's conditional question laws. One common family $G_i$ can be used on both copies, for $i=1,\ldots,5$. To derive this, choose one side's LDT output, use swap invariance of the state to transport its point relation, then point self-consistency and polynomial separation to obtain cross-copy consistency; average the resulting errors using Jensen. Identical point operators alone do not make the two existential LDT outputs identical. The resulting evaluation and full-polynomial consistency error is denoted $\kappa=O(\sqrt E+\rho)$ with $E,\rho$ as below. The Lean keeps one extracted family per player, $G^A_i$ and $G^B_i$, with their consistency, rather than a single common family; the errors are averaged over the seed by concavity of $\varepsilon\mapsto\varepsilon^{b'}$. It extracts in a bipartite model in which the seeded test is sound (Definition [The low-individual-degree test is sound in a model](../../downstream-results/part-03/def-lidt-sound-in.md)), a hypothesis the tensor-product model satisfies by the theorem itself (Lemma [The low-individual-degree test is sound in the tensor-product model](../../downstream-results/part-03/lem-lidt-sound-in-tensor.md)).

## Depends on

- [Schwartz–Zippel](../../background-results/part-05/lem-schwartz-zippel.md)
- [The low-individual-degree test is sound in a model](../../downstream-results/part-03/def-lidt-sound-in.md)

## Proof depends on

- [Global PCP consistency tests](lem-ar-global-tests.md)

## Proof

For each seed and copy, the seeded low-degree test's soundness extracts the measurements (`exists_ext1`, `ext1_spec`), with error $\delta_{\mathrm{sim}}$ at the copy's failure; in the Lean the restricted strategy is a projective strategy in the model, and the soundness is the model's (Definition [The low-individual-degree test is sound in a model](../../downstream-results/part-03/def-lidt-sound-in.md)); $\varepsilon\mapsto\varepsilon^{b'}$ is concave, so the errors average over the seed to $\delta_{\mathrm{sim}}$ at the average failure (`sum_deltaSim_le`, `sum_deltaSim1_le`).

## Lean

Formalized as [`MIPRE.AnswerReduction.exists_ext1`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.exists_ext1), [`MIPRE.AnswerReduction.ext1_spec`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.ext1_spec), [`MIPRE.AnswerReduction.sum_deltaSim1_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.sum_deltaSim1_le), [`MIPRE.LIDT.Simul.sum_deltaSim_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Simul.sum_deltaSim_le).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 5803](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L5803)
