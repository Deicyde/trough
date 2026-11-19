---
declaration: lemma
origin: cited
lean: ProbabilityTheory.HasLocallyIntegrableSup.locally_classDL
statement: formalized
proof: formalized
---

# HasLocallyIntegrableSup.locally_classDL

Let $X$ be a progressively measurable stochastic process with locally integrable supremum. Then $X$ is locally of class DL.

## Depends on

- [Locally integrable supremum](../part-01/def-locallyintegrablesup.md)
- [Local property](../../local-properties/def-locally.md)
- [Class DL](../part-01/def-classdl.md)
- [Right-continuous filtration](../../../filtrations-processes-and-martingales/right-continuous-filtrations/def-rightcontinuous.md)

## Proof depends on

- [Integrable.classDL](../part-01/lem-integrable-classdl.md)
- [locally_mono](../../local-properties/lem-locally-mono.md)
- [isStable_isStronglyProgressive](../../locally-cadlag/lem-isstable-isstronglyprogressive.md)

## Proof

Combine Lemma [Integrable.classDL](../part-01/lem-integrable-classdl.md) and Lemma [locally_mono](../../local-properties/lem-locally-mono.md). Use Lemma [isStable_isStronglyProgressive](../../locally-cadlag/lem-isstable-isstronglyprogressive.md) to get progressive measurability of the stopped processes.

## Lean

Formalized as [`ProbabilityTheory.HasLocallyIntegrableSup.locally_classDL`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.HasLocallyIntegrableSup.locally_classDL).

## Sources

- [Brownian motion blueprint: chapters/local_martingales.tex, line 666](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/local_martingales.tex#L666)
