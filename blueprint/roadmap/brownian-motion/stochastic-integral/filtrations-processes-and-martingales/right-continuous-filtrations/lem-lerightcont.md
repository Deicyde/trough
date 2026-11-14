---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.Filtration.le_rightCont
---

# leRightCont

The filtration $\mathcal{F}$ is contained in its right continuation.

## Depends on

- [Right continuation](def-rightlimitfiltration.md)

## Proof depends on

- [rightContDef](lem-rightcontdef.md)

## Proof

Endow $T$ with the order topology, and consider $t \in T$. Using Lemma [rightContDef](lem-rightcontdef.md), we split into two cases. If $t$ is isolated on the right, then $\mathcal{F}_{t+} = \mathcal{F}_t \supseteq \mathcal{F}_t$ and we are done. Otherwise, for all $u > t$, $\mathcal{F}_t \subseteq \mathcal{F}_u$, therefore $\mathcal{F}_t \subseteq \mathop{\Large\sqcap}_{u > t} \mathcal{F}_u$, and we are done.

## Lean

Formalized as [`MeasureTheory.Filtration.le_rightCont`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.Filtration.le_rightCont).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 497](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L497)
