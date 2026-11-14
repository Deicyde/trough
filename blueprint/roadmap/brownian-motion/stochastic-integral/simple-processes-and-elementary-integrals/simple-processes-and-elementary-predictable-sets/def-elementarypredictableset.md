---
declaration: definition
origin: cited
lean: ProbabilityTheory.ElementaryPredictableSet
statement: formalized
---

# Elementary predictable set

A set $A \subseteq T \times \Omega$ is an *elementary predictable set* if it is a finite union of sets of the form ${0} \times B$ for $B \in \mathcal{F}_0$ or of the form $(s, t] \times B$ with $0 \le s < t$ in $T$ and $B \in \mathcal{F}_s$ .

## Depends on

- [Filtration](../../filtrations-processes-and-martingales/basic-definitions/part-01/def-filtration.md)

## Lean

Formalized as [`ProbabilityTheory.ElementaryPredictableSet`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.ElementaryPredictableSet).

## Sources

- [Brownian motion blueprint: chapters/elementary.tex, line 184](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/elementary.tex#L184)
