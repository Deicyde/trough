---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.Filtration.rightCont_eq_self
---

# rightContSuccOrder

Assume that $T$ is a linear order with successor. This means that for any $t$, there is an element $succ(t) \ge t$ such that for any $u > t$, $u \ge succ(t)$, and if $succ(t) \le t$, then $t$ is maximal. Then the right continuation of $\mathcal{F}$ is equal to $\mathcal{F}$.

## Depends on

- [Right continuation](def-rightlimitfiltration.md)

## Proof depends on

- [rightContIsolated](lem-rightcontisolated.md)

## Proof

Endow $T$ with the order topology. In a linear order with successor equipped with the order topology, every point is isolated on the right, so we can conclude by Lemma [rightContIsolated](lem-rightcontisolated.md).

## Lean

Formalized as [`MeasureTheory.Filtration.rightCont_eq_self`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.Filtration.rightCont_eq_self).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 419](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L419)
