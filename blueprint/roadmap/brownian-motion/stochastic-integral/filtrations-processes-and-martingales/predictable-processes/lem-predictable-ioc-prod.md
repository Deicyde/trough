---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.measurableSet_predictable_Ioc_prod
---

# predictable_Ioc_prod

Sets of the form $(s, t] \times A$ for any $A \in \mathcal{F}_s$ is measurable with respect to the predictable $\sigma$-algebra.

## Depends on

- [Predictable $\sigma$-algebra](def-predictablemeasurablespace.md)

## Proof

For $t \le s$, the set in question is empty and thusly, trivially measurable. On the other hand, for $s < t$, measurability follows as $(s, t] \times A = (s, \infty) \times A \setminus (t, \infty) \times A$.

## Lean

Formalized as [`MeasureTheory.measurableSet_predictable_Ioc_prod`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.measurableSet_predictable_Ioc_prod).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 655](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L655)
