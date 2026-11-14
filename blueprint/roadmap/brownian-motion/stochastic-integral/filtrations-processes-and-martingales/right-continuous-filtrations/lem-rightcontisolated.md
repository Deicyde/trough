---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.Filtration.rightCont_eq_of_nhdsGT_eq_bot
---

# rightContIsolated

Suppose $T$ is a topological space with the topology being the order topology. Assume that $t \in T$ is isolated on the right, meaning that there exists a neighbourhood $\mathcal{V}$ of $t$ such that $\mathcal{V} \cap \{u \mid u > t\} = \emptyset$. Then $\mathcal{F}_{t+} = \mathcal{F}_t$.

## Depends on

- [Right continuation](def-rightlimitfiltration.md)

## Proof depends on

- [rightContDef](lem-rightcontdef.md)

## Proof

This is a direct consequence of Lemma [rightContDef](lem-rightcontdef.md).

## Lean

Formalized as [`MeasureTheory.Filtration.rightCont_eq_of_nhdsGT_eq_bot`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.Filtration.rightCont_eq_of_nhdsGT_eq_bot).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 406](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L406)
