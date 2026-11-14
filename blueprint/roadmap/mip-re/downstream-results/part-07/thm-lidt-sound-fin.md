---
declaration: theorem
origin: cited
lean: MIPRE.LIDT.Simul.soundFin
statement: formalized
proof: formalized
---

# The low-individual-degree test is sound in dyadic pairs

The seeded CL test is sound in dyadic pairs (Definition [The low-individual-degree test is sound in dyadic pairs](../part-05/def-lidt-sound-fin.md)).

## Depends on

- [The low-individual-degree test is sound in dyadic pairs](../part-05/def-lidt-sound-fin.md)
- [The canonical-line theorem in a dyadic pair](../part-06/lem-co-lidt-canonical-line.md)
- [Soundness in a model from the canonical-line theorem in it](../part-06/lem-lidt-sound-in-of-model-lidt.md)

## Proof

In a dyadic pair the canonical-line theorem holds (Lemma [The canonical-line theorem in a dyadic pair](../part-06/lem-co-lidt-canonical-line.md)), and it gives the soundness of the seeded test there (Lemma [Soundness in a model from the canonical-line theorem in it](../part-06/lem-lidt-sound-in-of-model-lidt.md)).

## Lean

Formalized as [`MIPRE.LIDT.Simul.soundFin`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Simul.soundFin).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 4246](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L4246)
