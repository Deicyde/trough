---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.Filtration.IsRightContinuous.eq
---

# eqRightCont

If $\mathcal{F}$ is right-continuous, then for all $t \in T$, $\mathcal{F}_t = \mathcal{F}_{t+}$.

## Depends on

- [Right continuation](def-rightlimitfiltration.md)
- [Right-continuous filtration](def-rightcontinuous.md)

## Proof depends on

- [leRightCont](lem-lerightcont.md)

## Proof

This is a direct consequence of Definition [Right-continuous filtration](def-rightcontinuous.md) and Lemma [leRightCont](lem-lerightcont.md).

## Lean

Formalized as [`MeasureTheory.Filtration.IsRightContinuous.eq`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.Filtration.IsRightContinuous.eq).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 546](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L546)
