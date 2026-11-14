---
declaration: lemma
origin: cited
lean: MeasureTheory.Martingale.classD_iff_uniformIntegrable
statement: formalized
proof: formalized
---

# Martingale.classD_iff_uniformIntegrable

A right-continuous martingale is of class D if and only if it is uniformly integrable.

## Depends on

- [Martingale](../../../../../mathlib/overview/probability-theory/stochastic-processes/martingale.md)
- [Doob-Meyer class, class D](def-classd.md)
- [Right continuous function](../../../filtrations-processes-and-martingales/basic-definitions/part-01/def-rightcontinuous.md)

## Proof depends on

- [Submartingale.classD_iff_uniformIntegrable](lem-submartingale-classd-iff-uniformintegrable.md)
- [uniformIntegrableIffNorm](../../../filtrations-processes-and-martingales/uniformly-integrable/lem-uniformintegrableiffnorm.md)
- [classD_iff_norm](lem-classd-iff-norm.md)
- [Martingale.submartingale_norm](../../../filtrations-processes-and-martingales/basic-definitions/part-01/cor-martingale-submartingale-norm.md)

## Proof

Applying Lemma [classD_iff_norm](lem-classd-iff-norm.md) and Lemma [uniformIntegrableIffNorm](../../../filtrations-processes-and-martingales/uniformly-integrable/lem-uniformintegrableiffnorm.md), it suffices to show the result for the norm of the martingale. That norm is a nonnegative right-continuous submartingale by Lemma [Martingale.submartingale_norm](../../../filtrations-processes-and-martingales/basic-definitions/part-01/cor-martingale-submartingale-norm.md) so this follows from Lemma [Submartingale.classD_iff_uniformIntegrable](lem-submartingale-classd-iff-uniformintegrable.md).

## Lean

Formalized as [`MeasureTheory.Martingale.classD_iff_uniformIntegrable`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.Martingale.classD_iff_uniformIntegrable).

## Sources

- [Brownian motion blueprint: chapters/local_martingales.tex, line 559](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/local_martingales.tex#L559)
