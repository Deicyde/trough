---
declaration: lemma
origin: cited
lean: MeasureTheory.IsStronglyProgressive.isStoppingTime_leastGT
statement: formalized
proof: formalized
---

# isStoppingTime_leastGT

Let $T$ be a conditionally complete linear order with a bottom element, which is a Polish space for its order topology, on which we put the Borel $\sigma$-algebra. Let $R$ be a preorder with a metrizable topology for which sets of the form $\{x \in R \mid x \ge a\}$ are closed, with its Borel $\sigma$-algebra. If $X : T \to Ω \to R$ is a progressively measurable process with respect to a filtration satisfying the usual conditions, then for any $a \in R$, the random time $\tau_{X > a}$ is a stopping time.

## Depends on

- [Stopping time](../../../../mathlib/overview/probability-theory/stochastic-processes/stopping-time.md)
- [leastGT](def-leastgt.md)

## Proof depends on

- [hitting_is_stopping_time](thm-hitting-is-stopping-time.md)

## Proof

This is a direct application of Theorem [hitting_is_stopping_time](thm-hitting-is-stopping-time.md) with the set $B = (a, +\infty)$.

## Lean

Formalized as [`MeasureTheory.IsStronglyProgressive.isStoppingTime_leastGT`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.IsStronglyProgressive.isStoppingTime_leastGT).

## Sources

- [Brownian motion blueprint: chapters/debut.tex, line 802](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/debut.tex#L802)
