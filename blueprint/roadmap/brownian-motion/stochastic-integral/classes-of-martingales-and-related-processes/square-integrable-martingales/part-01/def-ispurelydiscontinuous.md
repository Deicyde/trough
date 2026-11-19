---
declaration: definition
origin: cited
lean: ProbabilityTheory.IsPurelyDiscontinuous
statement: formalized
---

# IsPurelyDiscontinuous

A stochastic process $X$ is purely discontinuous if it is a square integrable martingale such that for any continuous square integrable martingale $Y$,

$$
P[\langle X_\infty, Y_\infty\rangle] = 0.
$$

## Depends on

- [Square integrable martingales](def-issquareintegrable.md)

## Lean

Formalized as [`ProbabilityTheory.IsPurelyDiscontinuous`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.IsPurelyDiscontinuous).

## Sources

- [Brownian motion blueprint: chapters/martingale_classes.tex, line 436](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/martingale_classes.tex#L436)
