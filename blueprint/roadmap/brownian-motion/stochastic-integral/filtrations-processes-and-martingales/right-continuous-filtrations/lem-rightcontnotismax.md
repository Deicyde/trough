---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.Filtration.rightCont_eq_of_not_isMax
---

# rightContNotIsMax

Assume that $T$ is a densely ordered linear order, meaning that for all $s < t$, there exists $u$ such that $s < u < t$. If $t$ is not maximal, then $\mathcal{F}_{t+} = \mathop{\Large\sqcap}_{u > t} \mathcal{F}_u$.

## Depends on

- [Right continuation](def-rightlimitfiltration.md)

## Proof depends on

- [rightContNeBot](lem-rightcontnebot.md)

## Proof

Endow $T$ with the order topology. In a densely ordered linear order, a point which is not maximal is not isolated on the right, so we can conclude by Lemma [rightContNeBot](lem-rightcontnebot.md).

## Lean

Formalized as [`MeasureTheory.Filtration.rightCont_eq_of_not_isMax`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.Filtration.rightCont_eq_of_not_isMax).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 471](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L471)
