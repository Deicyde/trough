---
declaration: definition
origin: cited
lean: MeasureTheory.IsPavingAnalytic, MeasureTheory.IsPavingAnalyticFor
statement: formalized
---

# Analytic set

Let $F$ be a paving of a type $\mathcal{X}$. A set $s$ of $\mathcal{X}$ is said to be $F$-analytic if there exists a type $\mathcal{K}$ and a compact system $K$ of $\mathcal{K}$ such that $s$ is the projection on $\mathcal{X}$ of a set in $(F \times K)_{\sigma \delta}$.

We denote the set of $F$-analytic sets by $\mathcal{A}(F)$.

## Depends on

- [IsCompactSystem](def-iscompactsystem.md)
- [countableSupClosure](def-countablesupclosure.md)
- [countableInfClosure](def-countableinfclosure.md)

## Lean

Formalized as [`MeasureTheory.IsPavingAnalytic`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.IsPavingAnalytic), [`MeasureTheory.IsPavingAnalyticFor`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.IsPavingAnalyticFor).

## Sources

- [Brownian motion blueprint: chapters/debut.tex, line 225](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/debut.tex#L225)
