---
declaration: lemma
origin: cited
lean: MeasureTheory.Submartingale.classD_iff_uniformIntegrable
statement: formalized
proof: formalized
---

# Submartingale.classD_iff_uniformIntegrable

A nonnegative right-continuous submartingale is of class D if and only if it is uniformly integrable.

## Depends on

- [Submartingale](../../../filtrations-processes-and-martingales/basic-definitions/part-01/def-submartingale.md)
- [Doob-Meyer class, class D](def-classd.md)
- [Right continuous function](../../../filtrations-processes-and-martingales/basic-definitions/part-01/def-rightcontinuous.md)

## Proof depends on

- [optionalSamplingSubmartingale](../../../filtrations-processes-and-martingales/optional-sampling/lem-optionalsamplingsubmartingale.md)
- [uniformIntegrable_of_tendsto_ae](../../../filtrations-processes-and-martingales/uniformly-integrable/lem-uniformintegrable-of-tendsto-ae.md)
- [uniformIntegrableComp](../../../filtrations-processes-and-martingales/uniformly-integrable/lem-uniformintegrablecomp.md)
- [ClassD.uniformIntegrable](lem-classd-uniformintegrable.md)

## Proof

Assume that $X$ is uniformly integrable. Just like what we did in the proof of Lemma [Submartingale.classDL](lem-submartingale-classdl.md), we use Lemma [optionalSamplingSubmartingale](../../../filtrations-processes-and-martingales/optional-sampling/lem-optionalsamplingsubmartingale.md) and Lemma [condExpUI](../../../filtrations-processes-and-martingales/uniformly-integrable/lem-condexpui.md) to deduce that $\{X_\tau|\exists t\in T, \tau\le t\}$ is uniformly integrable. Moreover, for any finite stopping time $\tau$, We have that $X_\tau = \lim_{n \to +\infty} X_{\tau \land n}$. Thanks to Lemma [uniformIntegrable_of_tendsto_ae](../../../filtrations-processes-and-martingales/uniformly-integrable/lem-uniformintegrable-of-tendsto-ae.md), we deduce that $X$ is of class D.

Conversely, if $X$ is of class D, then it is uniformly integrable by Lemma [ClassD.uniformIntegrable](lem-classd-uniformintegrable.md).

## Lean

Formalized as [`MeasureTheory.Submartingale.classD_iff_uniformIntegrable`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.Submartingale.classD_iff_uniformIntegrable).

## Sources

- [Brownian motion blueprint: chapters/local_martingales.tex, line 530](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/local_martingales.tex#L530)
