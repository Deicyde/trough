---
declaration: lemma
origin: cited
lean: ProbabilityTheory.isStable_submartingale
statement: formalized
---

# stable_IsSubmartingale

The class of cadlag submartingales is stable. That is, if $M$ is a cadlag submartingale and $\tau$ is a stopping time, then the stopped process $M^{\tau}\mathbb{I}_{\tau > 0}$ is also a cadlag submartingale.

## Depends on

- [Submartingale](../../filtrations-processes-and-martingales/basic-definitions/part-01/def-submartingale.md)
- [stable](../local-properties/def-stable.md)
- [Cadlag function](../../filtrations-processes-and-martingales/basic-definitions/part-01/def-iscadlag.md)

## Proof depends on

- [optionalSamplingSubmartingale](../../filtrations-processes-and-martingales/optional-sampling/lem-optionalsamplingsubmartingale.md)

## Lean

Stated as [`ProbabilityTheory.isStable_submartingale`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.isStable_submartingale); the blueprint marks no proof of it as formalized.

## Sources

- [Brownian motion blueprint: chapters/local_martingales.tex, line 388](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/local_martingales.tex#L388)
