---
declaration: corollary
origin: cited
lean: MIPRE.mipco_eq_core_of_lidt
statement: formalized
proof: formalized
---

# $\mathrm{MIP}^{\mathrm{co}} = \mathrm{coRE}$, from the co-soundness of the low-individual-degree test

If the seeded CL test is sound in the commuting-operator model (Definition [The low-individual-degree test is sound in a model](../part-03/def-lidt-sound-in.md)), then $\mathrm{MIP}^{\mathrm{co}} = \mathrm{coRE}$.

## Depends on

- [$\mathrm{MIP}^{\mathrm{co}} = \mathrm{coRE}$, from the co-soundness of the Pauli basis test and of the low-individual-degree test](../part-02/cor-mipco-from-stages.md)
- [The Pauli basis test is sound in the commuting-operator model, given the seeded test](lem-qld-sound-co.md)

## Proof

The Pauli basis test is then sound in the commuting-operator model (Lemma [The Pauli basis test is sound in the commuting-operator model, given the seeded test](lem-qld-sound-co.md)), so both hypotheses of Corollary [$\mathrm{MIP}^{\mathrm{co}} = \mathrm{coRE}$, from the co-soundness of the Pauli basis test and of the low-individual-degree test](../part-02/cor-mipco-from-stages.md) hold.

## Lean

Formalized as [`MIPRE.mipco_eq_core_of_lidt`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.mipco_eq_core_of_lidt).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 2747](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L2747)
