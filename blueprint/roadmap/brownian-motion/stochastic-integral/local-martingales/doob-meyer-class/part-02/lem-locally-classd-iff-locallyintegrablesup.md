---
declaration: lemma
origin: cited
lean: ProbabilityTheory.locally_classD_iff_hasLocallyIntegrableSup
statement: formalized
proof: formalized
---

# locally_classD_iff_locallyIntegrableSup

Assume $T$ has a bottom element and that its closed intervals are compact, and that the filtration is right-continuous. A càdlàg process is locally of class D if and only if it has locally integrable supremum.

## Depends on

- [Doob-Meyer class, class D](../part-01/def-classd.md)
- [Locally integrable supremum](../part-01/def-locallyintegrablesup.md)
- [Local property](../../local-properties/def-locally.md)
- [Cadlag function](../../../filtrations-processes-and-martingales/basic-definitions/part-01/def-iscadlag.md)
- [Right-continuous filtration](../../../filtrations-processes-and-martingales/right-continuous-filtrations/def-rightcontinuous.md)

## Proof depends on

- [locally_classD_iff_locally_classDL](lem-locally-classd-iff-locally-classdl.md)
- [locally_classDL_iff_locallyIntegrableSup](lem-locally-classdl-iff-locallyintegrablesup.md)

## Proof

This follows from Lemmas [locally_classD_iff_locally_classDL](lem-locally-classd-iff-locally-classdl.md) and [locally_classDL_iff_locallyIntegrableSup](lem-locally-classdl-iff-locallyintegrablesup.md).

## Lean

Formalized as [`ProbabilityTheory.locally_classD_iff_hasLocallyIntegrableSup`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.locally_classD_iff_hasLocallyIntegrableSup).

## Sources

- [Brownian motion blueprint: chapters/local_martingales.tex, line 823](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/local_martingales.tex#L823)
