---
declaration: lemma
origin: cited
lean: ProbabilityTheory.ElementaryPredictableSet.measurableSet_predictable
statement: formalized
proof: formalized
---

# predictableSet_elementaryPredictableSet

An elementary predictable set is measurable with respect to the predictable $\sigma$-algebra.

## Depends on

- [Elementary predictable set](def-elementarypredictableset.md)
- [Predictable $\sigma$-algebra](../../filtrations-processes-and-martingales/predictable-processes/def-predictablemeasurablespace.md)

## Proof depends on

- [predictable_Ioc_prod](../../filtrations-processes-and-martingales/predictable-processes/lem-predictable-ioc-prod.md)

## Proof

It is a union of sets of the form ${0} \times B$ with $B \in \mathcal{F}_0$ or of the form $(s, t] \times B$ with $B \in \mathcal{F}_s$, which are measurable by Lemma [predictable_Ioc_prod](../../filtrations-processes-and-martingales/predictable-processes/lem-predictable-ioc-prod.md).

## Lean

Formalized as [`ProbabilityTheory.ElementaryPredictableSet.measurableSet_predictable`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.ElementaryPredictableSet.measurableSet_predictable).

## Sources

- [Brownian motion blueprint: chapters/elementary.tex, line 232](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/elementary.tex#L232)
