---
declaration: lemma
origin: cited
lean: ProbabilityTheory.locally_classDL_iff_hasLocallyIntegrableSup
statement: formalized
proof: formalized
---

# locally_classDL_iff_locallyIntegrableSup

Assume $T$ has a bottom element and that its closed intervals are compact, and that the filtration is right-continuous. If $X$ is a càdlàg process, then it is locally of class DL if and only if it has locally integrable supremum.

## Depends on

- [Class DL](../part-01/def-classdl.md)
- [Locally integrable supremum](../part-01/def-locallyintegrablesup.md)
- [Local property](../../local-properties/def-locally.md)
- [Cadlag function](../../../filtrations-processes-and-martingales/basic-definitions/part-01/def-iscadlag.md)
- [Right-continuous filtration](../../../filtrations-processes-and-martingales/right-continuous-filtrations/def-rightcontinuous.md)

## Proof depends on

- [hasLocallyIntegrableSup_of_locally_classDL](lem-haslocallyintegrablesup-of-locally-classdl.md)
- [HasLocallyIntegrableSup.locally_classDL](lem-haslocallyintegrablesup-locally-classdl.md)

## Proof

The two directions are proved in Lemmas [hasLocallyIntegrableSup_of_locally_classDL](lem-haslocallyintegrablesup-of-locally-classdl.md) and [HasLocallyIntegrableSup.locally_classDL](lem-haslocallyintegrablesup-locally-classdl.md).

## Lean

Formalized as [`ProbabilityTheory.locally_classDL_iff_hasLocallyIntegrableSup`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.locally_classDL_iff_hasLocallyIntegrableSup).

## Sources

- [Brownian motion blueprint: chapters/local_martingales.tex, line 792](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/local_martingales.tex#L792)
