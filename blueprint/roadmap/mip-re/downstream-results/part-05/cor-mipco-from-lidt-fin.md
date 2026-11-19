---
declaration: corollary
origin: cited
lean: MIPRE.mipco_eq_core_of_lidtFin, MIPRE.gapCompressionCo_sound_of_lidtFin
statement: formalized
proof: formalized
---

# $\mathrm{MIP}^{\mathrm{co}} = \mathrm{coRE}$, from the soundness of the low-individual-degree test in dyadic pairs

If the seeded CL test is sound in dyadic pairs (Definition [The low-individual-degree test is sound in dyadic pairs](def-lidt-sound-fin.md)), then the compression of Corollary [$\mathrm{MIP}^{\mathrm{co}} = \mathrm{coRE}$, from the co-soundness of the Pauli basis test and of the low-individual-degree test](../part-02/cor-mipco-from-stages.md) is sound in ${\omega^{\mathrm{co}}}$ (Definition [Soundness of compression in a value model](../part-01/def-compression-co-sound.md)), and $\mathrm{MIP}^{\mathrm{co}} = \mathrm{coRE}$.

## Depends on

- [$\mathrm{MIP}^{\mathrm{co}} = \mathrm{coRE}$, from the co-soundness of the Pauli basis test and of the low-individual-degree test](../part-02/cor-mipco-from-stages.md)
- [Answer reduction is sound in ${\omega^{\mathrm{co}}}$, given the test in dyadic pairs](thm-ar-sound-co-fin.md)
- [The Pauli basis test, given the seeded test in dyadic pairs](lem-qld-approx-co-fin.md)
- [${\omega^{\mathrm{co}}}$ is approached in dyadic pairs](lem-co-value-finite-pair.md)

## Proof

${\omega^{\mathrm{co}}}$ is approached in dyadic pairs (Lemma [${\omega^{\mathrm{co}}}$ is approached in dyadic pairs](lem-co-value-finite-pair.md)). Introspection is sound in ${\omega^{\mathrm{co}}}$ as soon as ${\omega^{\mathrm{co}}}$ is approached by projective strategies of models in which the Pauli basis test is sound (Theorem [Introspection is sound in ${\omega^{\mathrm{co}}}$, given the Pauli basis test](../part-04/thm-intro-sound-co.md)), which Lemma [The Pauli basis test, given the seeded test in dyadic pairs](lem-qld-approx-co-fin.md) then provides. Answer reduction is sound in ${\omega^{\mathrm{co}}}$ by Theorem [Answer reduction is sound in ${\omega^{\mathrm{co}}}$, given the test in dyadic pairs](thm-ar-sound-co-fin.md), and parallel repetition is (Theorem [Parallel repetition is sound in ${\omega^{\mathrm{co}}}$](../part-02/thm-parallel-repetition-co.md)). So the compression of Corollary [$\mathrm{MIP}^{\mathrm{co}} = \mathrm{coRE}$, from the co-soundness of the Pauli basis test and of the low-individual-degree test](../part-02/cor-mipco-from-stages.md) is sound in ${\omega^{\mathrm{co}}}$, which gives $\mathrm{MIP}^{\mathrm{co}} = \mathrm{coRE}$.

## Lean

Formalized as [`MIPRE.mipco_eq_core_of_lidtFin`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.mipco_eq_core_of_lidtFin), [`MIPRE.gapCompressionCo_sound_of_lidtFin`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.gapCompressionCo_sound_of_lidtFin).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 3156](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L3156)
