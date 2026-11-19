---
declaration: definition
origin: cited
lean: MIPRE.LIDT.Simul.SoundFin
statement: formalized
---

# The low-individual-degree test is sound in dyadic pairs

The seeded CL test is *sound in dyadic pairs* if it is sound (Definition [The low-individual-degree test is sound in a model](../part-03/def-lidt-sound-in.md)) in every dyadic pair (Definition [Dyadic pairs](def-dyadic-pair.md)). Dyadic pairs being finite pairs, this is weaker than soundness in every finite pair, so the conditional theorem it feeds (Corollary [$\mathrm{MIP}^{\mathrm{co}} = \mathrm{coRE}$, from the soundness of the low-individual-degree test in dyadic pairs](cor-mipco-from-lidt-fin.md)) is stronger.

## Depends on

- [The low-individual-degree test is sound in a model](../part-03/def-lidt-sound-in.md)
- [Dyadic pairs](def-dyadic-pair.md)

## Lean

Formalized as [`MIPRE.LIDT.Simul.SoundFin`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Simul.SoundFin).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 3106](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L3106)
