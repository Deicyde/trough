---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.Filtration.rightCont_eq
---

# rightContEq

If $T$ is a densely ordered linear order with no maximal element, then forall $t \in T$ we have $\mathcal{F}_{t+} = \mathop{\Large\sqcap}_{u > t} \mathcal{F}_u$.

## Depends on

- [Right continuation](def-rightlimitfiltration.md)

## Proof depends on

- [rightContNotIsMax](lem-rightcontnotismax.md)

## Proof

For all $t$, $t$ is not maximal, so we can conclude by Lemma [rightContNotIsMax](lem-rightcontnotismax.md).

## Lean

Formalized as [`MeasureTheory.Filtration.rightCont_eq`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.Filtration.rightCont_eq).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 484](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L484)
