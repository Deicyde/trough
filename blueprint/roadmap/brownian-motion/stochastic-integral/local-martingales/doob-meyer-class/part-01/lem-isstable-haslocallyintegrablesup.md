---
declaration: lemma
origin: cited
lean: ProbabilityTheory.isStable_hasLocallyIntegrableSup
statement: formalized
proof: formalized
---

# isStable_hasLocallyIntegrableSup

The class of process with locally integrable supremum is stable.

## Depends on

- [stable](../../local-properties/def-stable.md)
- [Locally integrable supremum](def-locallyintegrablesup.md)

## Proof depends on

- [isStable_hasIntegrableSup](lem-isstable-hasintegrablesup.md)
- [isStable_locally](../../local-properties/lem-isstable-locally.md)

## Proof

Apply Lemma [isStable_hasIntegrableSup](lem-isstable-hasintegrablesup.md) and Lemma [isStable_locally](../../local-properties/lem-isstable-locally.md).

## Lean

Formalized as [`ProbabilityTheory.isStable_hasLocallyIntegrableSup`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.isStable_hasLocallyIntegrableSup).

## Sources

- [Brownian motion blueprint: chapters/local_martingales.tex, line 599](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/local_martingales.tex#L599)
