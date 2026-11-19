---
declaration: theorem
origin: cited
lean: MIPRE.mipco_eq_core, MIPRE.gapCompressionCo_sound, MIPRE.halting_reduction_commuting, MIPRE.core_subset_mipco
statement: formalized
proof: formalized
---

# $\mathrm{MIP}^{\mathrm{co}} = \mathrm{coRE}$

The compression of Corollary [$\mathrm{MIP}^{\mathrm{co}} = \mathrm{coRE}$, from the co-soundness of the Pauli basis test and of the low-individual-degree test](../part-02/cor-mipco-from-stages.md) is sound in ${\omega^{\mathrm{co}}}$ (Definition [Soundness of compression in a value model](../part-01/def-compression-co-sound.md)). Hence there is a computable map $\mathcal{M} \mapsto \mathfrak{G}_\mathcal{M}$ from machines to game descriptions such that ${\omega^{\mathrm{co}}}(\mathfrak{G}_\mathcal{M}) \leq \frac12$ if $\mathcal{M}$ halts on the empty input and ${\omega^{\mathrm{co}}}(\mathfrak{G}_\mathcal{M}) = 1$ otherwise, and $\mathrm{MIP}^{\mathrm{co}} = \mathrm{coRE}$, for the class of Definition [The class $\mathrm{MIP}^{\mathrm{co}}$](../part-01/def-mipco.md).

## Depends on

- [$\mathrm{MIP}^{\mathrm{co}} = \mathrm{coRE}$, from the soundness of the low-individual-degree test in dyadic pairs](../part-05/cor-mipco-from-lidt-fin.md)
- [The low-individual-degree test is sound in dyadic pairs](thm-lidt-sound-fin.md)
- [Halting reduces to the commuting-operator value, from co-soundness](../part-02/thm-halting-co.md)
- [$\mathrm{MIP}^{\mathrm{co}} = \mathrm{coRE}$, from co-soundness](../part-02/thm-mipco-eq-core.md)

## Proof

The hypothesis of Corollary [$\mathrm{MIP}^{\mathrm{co}} = \mathrm{coRE}$, from the soundness of the low-individual-degree test in dyadic pairs](../part-05/cor-mipco-from-lidt-fin.md) is Theorem [The low-individual-degree test is sound in dyadic pairs](thm-lidt-sound-fin.md), which gives the soundness. The halting reduction is then Theorem [Halting reduces to the commuting-operator value, from co-soundness](../part-02/thm-halting-co.md), and $\mathrm{MIP}^{\mathrm{co}} = \mathrm{coRE}$ Theorem [$\mathrm{MIP}^{\mathrm{co}} = \mathrm{coRE}$, from co-soundness](../part-02/thm-mipco-eq-core.md).

## Lean

Formalized as [`MIPRE.mipco_eq_core`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.mipco_eq_core), [`MIPRE.gapCompressionCo_sound`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.gapCompressionCo_sound), [`MIPRE.halting_reduction_commuting`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.halting_reduction_commuting), [`MIPRE.core_subset_mipco`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.core_subset_mipco).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 4260](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L4260)
