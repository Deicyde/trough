---
declaration: lemma
origin: cited
lean: ProbabilityTheory.isStable_stronglyMeasurable_uncurry
statement: formalized
---

# isStable_stronglyMeasurable_uncurry

The class of processes for which the induced map $(t,\omega)\mapsto X_t(\omega)$ is strongly measurable is stable.

## Depends on

- [stable](../../local-properties/def-stable.md)

## Proof

The stopped process at $\tau$ is obtained by precomposition with $(t, \omega) \mapsto (\min (\tau(\omega), t), \omega)$. Precomposing a strongly measurable function with a measurable function gives a strongly measurable function. On a second-countable space, the minimum of two functions is measurable, and by assumption $\tau$ is measurable. The result follows from this.

## Lean

Stated as [`ProbabilityTheory.isStable_stronglyMeasurable_uncurry`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.isStable_stronglyMeasurable_uncurry); the blueprint marks no proof of it as formalized.

## Sources

- [Brownian motion blueprint: chapters/local_martingales.tex, line 573](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/local_martingales.tex#L573)
