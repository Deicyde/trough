---
declaration: lemma
origin: cited
lean: MeasureTheory.Submartingale.classDL
statement: formalized
proof: formalized
---

# Submartingale.classDL

Every nonnegative right-continuous submartingale is of class DL.

## Depends on

- [Submartingale](../../../filtrations-processes-and-martingales/basic-definitions/part-01/def-submartingale.md)
- [Class DL](def-classdl.md)
- [Right continuous function](../../../filtrations-processes-and-martingales/basic-definitions/part-01/def-rightcontinuous.md)

## Proof depends on

- [optionalSamplingSubmartingale](../../../filtrations-processes-and-martingales/optional-sampling/lem-optionalsamplingsubmartingale.md)
- [uniformIntegrableDominated](../../../filtrations-processes-and-martingales/uniformly-integrable/lem-uniformintegrabledominated.md)
- [condExpUI](../../../filtrations-processes-and-martingales/uniformly-integrable/lem-condexpui.md)

## Proof

Let $t \in T$ and $\tau \le t$ be a stopping time. By Lemma [optionalSamplingSubmartingale](../../../filtrations-processes-and-martingales/optional-sampling/lem-optionalsamplingsubmartingale.md) and nonnegativity we get that $0 \le X_\tau \le P[X_t \mid X_\tau]$. As $X$ is a submartingale, $X_t$ is integrable, thus $\{X_t\}$ is uniformly integrable, and we can conclude from Lemma [uniformIntegrableDominated](../../../filtrations-processes-and-martingales/uniformly-integrable/lem-uniformintegrabledominated.md) and Lemma [condExpUI](../../../filtrations-processes-and-martingales/uniformly-integrable/lem-condexpui.md).

## Lean

Formalized as [`MeasureTheory.Submartingale.classDL`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.Submartingale.classDL).

## Sources

- [Brownian motion blueprint: chapters/local_martingales.tex, line 516](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/local_martingales.tex#L516)
