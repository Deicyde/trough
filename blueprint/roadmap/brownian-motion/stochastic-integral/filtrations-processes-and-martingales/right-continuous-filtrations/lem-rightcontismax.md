---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.Filtration.rightCont_eq_of_isMax
---

# rightContIsMax

If $t \in T$ is maximal, $\mathcal{F}_{t+} = \mathcal{F}_t$.

## Depends on

- [Right continuation](def-rightlimitfiltration.md)

## Proof depends on

- [rightContIsolated](lem-rightcontisolated.md)

## Proof

Endow $T$ with the order topology. As $t$ is maximal, it is isolated on the right for this topology, so we can conclude by Lemma [rightContIsolated](lem-rightcontisolated.md).

## Lean

Formalized as [`MeasureTheory.Filtration.rightCont_eq_of_isMax`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.Filtration.rightCont_eq_of_isMax).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 432](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L432)
