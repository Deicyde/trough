---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.isPredictable_predictablePart
---

# predictable_predictablePart

The predictable part of a process is predictable.

## Depends on

- [Predictable part](def-predictablepart.md)
- [Predictable process](../../filtrations-processes-and-martingales/predictable-processes/def-predictable.md)

## Proof depends on

- [predictable_nat_iff](../../filtrations-processes-and-martingales/predictable-processes/lem-predictable-nat-iff.md)
- [predictablePart_zero](lem-predictablepart-zero.md)
- [adapted_predictablePart](lem-adapted-predictablepart.md)

## Proof

By Lemma [predictable_nat_iff](../../filtrations-processes-and-martingales/predictable-processes/lem-predictable-nat-iff.md), the process $A$ is predictable if $A_0$ is $\mathcal{F}_0$-measurable and for all integer $n$, $A_{n+1}$ is $\mathcal{F}_n$-measurable. As $A_0 = 0$ from Lemma [predictablePart_zero](lem-predictablepart-zero.md), it is $\mathcal{F}_0$-measurable. Lemma [adapted_predictablePart](lem-adapted-predictablepart.md) allows to conclude the proof.

## Lean

Formalized as [`MeasureTheory.isPredictable_predictablePart`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.isPredictable_predictablePart).

## Sources

- [Brownian motion blueprint: chapters/doob_meyer.tex, line 478](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/doob_meyer.tex#L478)
