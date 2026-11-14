---
declaration: lemma
origin: cited
lean: ProbabilityTheory.isStable_isCadlag
statement: formalized
proof: formalized
---

# isStable_isCadlag

The class of cadlag processes is stable.

## Depends on

- [stable](../local-properties/def-stable.md)
- [Cadlag function](../../filtrations-processes-and-martingales/basic-definitions/part-01/def-iscadlag.md)

## Proof depends on

- [isStable_rightContinuous](lem-isstable-rightcontinuous.md)
- [isStable_left_limit](lem-isstable-left-limit.md)

## Proof

Follows from Lemmas [isStable_rightContinuous](lem-isstable-rightcontinuous.md) and [isStable_left_limit](lem-isstable-left-limit.md).

## Lean

Formalized as [`ProbabilityTheory.isStable_isCadlag`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.isStable_isCadlag).

## Sources

- [Brownian motion blueprint: chapters/local_martingales.tex, line 307](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/local_martingales.tex#L307)
