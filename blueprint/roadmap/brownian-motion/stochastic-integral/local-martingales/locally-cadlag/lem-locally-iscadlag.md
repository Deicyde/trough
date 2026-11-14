---
declaration: lemma
origin: cited
lean: ProbabilityTheory.Locally.isCadlag
statement: formalized
proof: formalized
---

# locally_isCadlag

A stochastic process $X$ is locally cadlag if and only if it is cadlag almost surely.

## Depends on

- [Local property](../local-properties/def-locally.md)
- [Cadlag function](../../filtrations-processes-and-martingales/basic-definitions/part-01/def-iscadlag.md)

## Proof depends on

- [locally_of_ae](lem-locally-of-ae.md)
- [locally_rightContinuous](lem-locally-rightcontinuous.md)
- [locally_leftLimit](lem-locally-leftlimit.md)

## Proof

The forward direction follows from Lemmas [locally_rightContinuous](lem-locally-rightcontinuous.md) and [locally_leftLimit](lem-locally-leftlimit.md) while the reverse direction follows from Lemma [locally_of_ae](lem-locally-of-ae.md).

## Lean

Formalized as [`ProbabilityTheory.Locally.isCadlag`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.Locally.isCadlag).

## Sources

- [Brownian motion blueprint: chapters/local_martingales.tex, line 272](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/local_martingales.tex#L272)
