---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.Filtration.rightCont_eq_of_neBot_nhdsGT
---

# rightContNeBot

Suppose $T$ is a topological space with the topology being the order topology. Assume that $t \in T$ is not isolated on the right, meaning that for all neighbourhood $\mathcal{V}$ of $t$, $\mathcal{V} \cap \{u | u > t\} \ne \emptyset$. Then $\mathcal{F}_{t+} = \mathop{\Large\sqcap}_{u > t} \mathcal{F}_u$.

## Depends on

- [Right continuation](def-rightlimitfiltration.md)

## Proof depends on

- [rightContDef](lem-rightcontdef.md)

## Proof

This is a direct consequence of Lemma [rightContDef](lem-rightcontdef.md).

## Lean

Formalized as [`MeasureTheory.Filtration.rightCont_eq_of_neBot_nhdsGT`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.Filtration.rightCont_eq_of_neBot_nhdsGT).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 458](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L458)
