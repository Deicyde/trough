---
declaration: corollary
origin: cited
lean: MIPRE.mipco_eq_core_of_stages, MIPRE.gapCompressionCo
statement: formalized
proof: formalized
---

# $\mathrm{MIP}^{\mathrm{co}} = \mathrm{coRE}$, from the co-soundness of the Pauli basis test and of the low-individual-degree test

If the Pauli basis test is sound in the commuting-operator model (Definition [The Pauli basis test is sound in a model](../part-03/def-qld-sound-in.md)) and the seeded CL test is sound in the commuting-operator model (Definition [The low-individual-degree test is sound in a model](../part-03/def-lidt-sound-in.md)), then $\mathrm{MIP}^{\mathrm{co}} = \mathrm{coRE}$. The first hypothesis follows from the second (Lemma [The Pauli basis test is sound in the commuting-operator model, given the seeded test](../part-04/lem-qld-sound-co.md)), so the second suffices (Corollary [$\mathrm{MIP}^{\mathrm{co}} = \mathrm{coRE}$, from the co-soundness of the low-individual-degree test](../part-04/cor-mipco-from-lidt.md)).

## Depends on

- [$\mathrm{MIP}^{\mathrm{co}} = \mathrm{coRE}$, from co-soundness](thm-mipco-eq-core.md)
- [Compression is sound in every model in which its stages are](thm-pipeline-sound-in.md)
- [Parallel repetition is sound in ${\omega^{\mathrm{co}}}$](thm-parallel-repetition-co.md)
- [Answer reduction is sound in ${\omega^{\mathrm{co}}}$, given the low-individual-degree test](../part-03/thm-ar-sound-co.md)
- [Introspection is sound in ${\omega^{\mathrm{co}}}$, given the Pauli basis test](../part-04/thm-intro-sound-co.md)

## Proof

Build the gap compression of Theorem [Gap-preserving compression from ambient stage contracts](../../structure-of-the-proof/part-09/thm-compression.md) from the introspection, which is sound in ${\omega^{\mathrm{co}}}$ by Theorem [Introspection is sound in ${\omega^{\mathrm{co}}}$, given the Pauli basis test](../part-04/thm-intro-sound-co.md), the answer reduction, which is sound in ${\omega^{\mathrm{co}}}$ by Theorem [Answer reduction is sound in ${\omega^{\mathrm{co}}}$, given the low-individual-degree test](../part-03/thm-ar-sound-co.md), and the parallel repetition of Theorem [Parallel repetition is sound in ${\omega^{\mathrm{co}}}$](thm-parallel-repetition-co.md), which is sound in ${\omega^{\mathrm{co}}}$: it is the compression of Theorem [Ambient compression inhabitation target](../../structure-of-the-proof/part-09/thm-compression-target.md) with the number of repetitions chosen against the smaller of the two repetition constants. It is sound in ${\omega^{\mathrm{co}}}$ by Theorem [Compression is sound in every model in which its stages are](thm-pipeline-sound-in.md), and the argument of Theorem [$\mathrm{MIP}^{\mathrm{co}} = \mathrm{coRE}$, from co-soundness](thm-mipco-eq-core.md), which uses of the compression only its soundness in ${\omega^{\mathrm{co}}}$ and its tensor completeness, applies to it.

## Lean

Formalized as [`MIPRE.mipco_eq_core_of_stages`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.mipco_eq_core_of_stages), [`MIPRE.gapCompressionCo`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.gapCompressionCo).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 979](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L979)
