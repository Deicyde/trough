---
declaration: lemma
origin: cited
lean: ProbabilityTheory.tendsto_ae_condExp'
statement: formalized
---

# tendsto_ae_condExp

For $f : \Omega \to E$, we have almost surely that

$$
\lim_{t \to +\infty} P[f | \mathcal{F}_t] = P\left[f | \bigsqcup_t \mathcal{F}_t\right].
$$

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Stated as [`ProbabilityTheory.tendsto_ae_condExp'`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.tendsto_ae_condExp'); the blueprint marks no proof of it as formalized.

## Sources

- [Brownian motion blueprint: chapters/martingale_classes.tex, line 393](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/martingale_classes.tex#L393)
