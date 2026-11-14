---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.Filtration.rightCont_eq_of_exists_gt
---

# rightContExistsGt

If $T$ is a linear order and there exists $u > t$ such that $(t, u) = \emptyset$, then $\mathcal{F}_{t+} = \mathcal{F}_t$.

## Depends on

- [Right continuation](def-rightlimitfiltration.md)

## Proof depends on

- [rightContIsolated](lem-rightcontisolated.md)

## Proof

Endow $T$ with the order topology. The hypothesis implies that $t$ is isolated on the right in this topology, so we can conclude by Lemma [rightContIsolated](lem-rightcontisolated.md).

## Lean

Formalized as [`MeasureTheory.Filtration.rightCont_eq_of_exists_gt`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.Filtration.rightCont_eq_of_exists_gt).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 445](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L445)
