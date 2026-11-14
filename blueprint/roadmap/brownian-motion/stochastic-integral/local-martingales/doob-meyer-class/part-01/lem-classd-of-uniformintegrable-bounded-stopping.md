---
declaration: lemma
origin: cited
lean: ProbabilityTheory.classD_of_uniformIntegrable_bounded_stoppingTime
statement: formalized
proof: formalized
---

# classD_of_uniformIntegrable_bounded_stoppingTime

If a stochastic process is progressively measurable and the set

$$
\begin{aligned}
\{X_\tau \mid \tau \text{ is a stopping time and } \exists t, \forall \omega, \tau(\omega) \le t\}
\end{aligned}
$$

is uniformly integrable, then the process is of class D.

## Depends on

- [Doob-Meyer class, class D](def-classd.md)

## Proof depends on

- [uniformIntegrableComp](../../../filtrations-processes-and-martingales/uniformly-integrable/lem-uniformintegrablecomp.md)

## Lean

Formalized as [`ProbabilityTheory.classD_of_uniformIntegrable_bounded_stoppingTime`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.classD_of_uniformIntegrable_bounded_stoppingTime).

## Sources

- [Brownian motion blueprint: chapters/local_martingales.tex, line 486](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/local_martingales.tex#L486)
