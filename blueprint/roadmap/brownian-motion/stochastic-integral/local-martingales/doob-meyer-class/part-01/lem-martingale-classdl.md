---
declaration: lemma
origin: cited
lean: MeasureTheory.Martingale.classDL
statement: formalized
proof: formalized
---

# Martingale.classDL

Every càdlàg martingale is of class DL.

## Depends on

- [Martingale](../../../../../mathlib/overview/probability-theory/stochastic-processes/martingale.md)
- [Class DL](def-classdl.md)
- [Cadlag function](../../../filtrations-processes-and-martingales/basic-definitions/part-01/def-iscadlag.md)

## Proof depends on

- [Submartingale.classDL](lem-submartingale-classdl.md)
- [Martingale.submartingale_convex_comp](../../../filtrations-processes-and-martingales/basic-definitions/part-01/lem-martingale-submartingale-convex-comp.md)
- [uniformIntegrableIffNorm](../../../filtrations-processes-and-martingales/uniformly-integrable/lem-uniformintegrableiffnorm.md)

## Proof

Let $X$ be càdlàg martingale. By Lemma [Martingale.submartingale_convex_comp](../../../filtrations-processes-and-martingales/basic-definitions/part-01/lem-martingale-submartingale-convex-comp.md), $(|X_t|)_{t \in T}$ is a nonnegative càdlàg submartingale, and the result follows from Lemma [Submartingale.classDL](lem-submartingale-classdl.md) along with Lemma [uniformIntegrableIffNorm](../../../filtrations-processes-and-martingales/uniformly-integrable/lem-uniformintegrableiffnorm.md).

## Lean

Formalized as [`MeasureTheory.Martingale.classDL`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.Martingale.classDL).

## Sources

- [Brownian motion blueprint: chapters/local_martingales.tex, line 546](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/local_martingales.tex#L546)
