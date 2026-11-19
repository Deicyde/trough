---
declaration: lemma
origin: cited
lean: MIPRE.LIDT.Simul.SoundCo.expand
statement: formalized
proof: formalized
---

# The seeded test in the extensions of a commuting-operator model

If the seeded CL test is sound in the commuting-operator model (Definition [The low-individual-degree test is sound in a model](../part-03/def-lidt-sound-in.md)), it is sound in every extension by a unit vector of the model of every commuting-operator strategy.

## Depends on

- [The low-individual-degree test is sound in a model](../part-03/def-lidt-sound-in.md)
- [An extension of a commuting-operator model is a commuting-operator model](lem-co-extension.md)
- [The seeded test, moved between models](lem-lidt-model-transport.md)

## Proof

The extension is isomorphic to the model of a commuting-operator strategy (Lemma [An extension of a commuting-operator model is a commuting-operator model](lem-co-extension.md)), in which the test is sound by hypothesis, and soundness passes along isomorphisms (Lemma [The seeded test, moved between models](lem-lidt-model-transport.md)).

## Lean

Formalized as [`MIPRE.LIDT.Simul.SoundCo.expand`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Simul.SoundCo.expand).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 2602](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L2602)
