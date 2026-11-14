---
declaration: lemma
origin: cited
lean: MeasureTheory.uniformIntegrable_of_dominated_singleton
statement: formalized
---

# uniformIntegrableDominatedSingleton

Let $(X_t)_{t \in T}$ be a family of random variables and $Y$ be a real random variable in $L^p$. If for all $t$, (possibly infinite) $\|X_t\| \le Y$ almost surely, then $X$ is uniformly integrable.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [uniformIntegrableDominated](lem-uniformintegrabledominated.md)

## Proof

Because $Y$ is in $L^p$, we deduce that $\{Y\}$ is uniformly integrable. The conclusion then follows from Lemma [uniformIntegrableDominated](lem-uniformintegrabledominated.md).

## Lean

Stated as [`MeasureTheory.uniformIntegrable_of_dominated_singleton`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.uniformIntegrable_of_dominated_singleton); the blueprint marks no proof of it as formalized.

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 811](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L811)
