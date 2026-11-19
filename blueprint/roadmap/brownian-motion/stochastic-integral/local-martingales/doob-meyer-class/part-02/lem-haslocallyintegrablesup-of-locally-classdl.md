---
declaration: lemma
origin: cited
lean: ProbabilityTheory.hasLocallyIntegrableSup_of_locally_classDL
statement: formalized
proof: formalized
---

# hasLocallyIntegrableSup_of_locally_classDL

Assume $T$ has a bottom element and that its closed intervals are compact. Assume that the filtration is right-continuous. If a process is càdlàg and locally of class DL, then it has locally integrable supremum.

## Depends on

- [Class DL](../part-01/def-classdl.md)
- [Locally integrable supremum](../part-01/def-locallyintegrablesup.md)
- [Local property](../../local-properties/def-locally.md)
- [Cadlag function](../../../filtrations-processes-and-martingales/basic-definitions/part-01/def-iscadlag.md)
- [Right-continuous filtration](../../../filtrations-processes-and-martingales/right-continuous-filtrations/def-rightcontinuous.md)

## Proof depends on

- [Local implication from global implication](../../local-properties/lem-local-induction.md)
- [ClassDL.hasLocallyIntegrableSup](lem-classdl-haslocallyintegrablesup.md)
- [isStable_hasIntegrableSup](../part-01/lem-isstable-hasintegrablesup.md)

## Proof

Apply Lemma [Local implication from global implication](../../local-properties/lem-local-induction.md) using Lemma [ClassDL.hasLocallyIntegrableSup](lem-classdl-haslocallyintegrablesup.md) and Lemma [isStable_hasIntegrableSup](../part-01/lem-isstable-hasintegrablesup.md).

## Lean

Formalized as [`ProbabilityTheory.hasLocallyIntegrableSup_of_locally_classDL`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.hasLocallyIntegrableSup_of_locally_classDL).

## Sources

- [Brownian motion blueprint: chapters/local_martingales.tex, line 776](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/local_martingales.tex#L776)
