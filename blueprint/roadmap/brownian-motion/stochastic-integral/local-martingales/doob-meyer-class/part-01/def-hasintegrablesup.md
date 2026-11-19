---
declaration: definition
origin: cited
lean: ProbabilityTheory.HasIntegrableSup
statement: formalized
---

# Integrable supremum

We say that a stochastic process is integrable if the map $(t,\omega) \mapsto X_t(\omega)$ is strongly measurable and for all $t$, $X_t$ is integrable. A process has an integrable supremum if $(\sup_{s \le t} \Vert X_s \Vert)_t$ is integrable.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`ProbabilityTheory.HasIntegrableSup`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.HasIntegrableSup).

## Sources

- [Brownian motion blueprint: chapters/local_martingales.tex, line 414](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/local_martingales.tex#L414)
