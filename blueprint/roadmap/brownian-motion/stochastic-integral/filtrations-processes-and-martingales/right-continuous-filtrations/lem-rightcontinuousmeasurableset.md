---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.Filtration.IsRightContinuous.measurableSet
---

# rightContinuousMeasurableSet

If $\mathcal{F}$ is right-continuous, then for all $t \in T$, any set $A \subseteq \Omega$ which is $\mathcal{F}_t$-measurable is also $\mathcal{F}_{t+}$-measurable.

## Depends on

- [Right continuation](def-rightlimitfiltration.md)
- [Right-continuous filtration](def-rightcontinuous.md)

## Proof

This is a direct consequence of Definition [Right-continuous filtration](def-rightcontinuous.md).

## Lean

Formalized as [`MeasureTheory.Filtration.IsRightContinuous.measurableSet`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.Filtration.IsRightContinuous.measurableSet).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 572](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L572)
