---
declaration: lemma
origin: cited
lean: ProbabilityTheory.stochIoc.exists_elementaryPredictableSet
statement: formalized
proof: formalized
---

# elementaryPredictableSet_stochasticInterval

If $\sigma$ and $\tau$ are stopping times on $\mathbb{N}$, with $\tau$ bounded, then the stochastic interval $]\!]\sigma, \tau]\!]$ is an elementary predictable set.

## Depends on

- [Stochastic intervals](def-stochasticinterval.md)
- [Elementary predictable set](../../simple-processes-and-elementary-integrals/simple-processes-and-elementary-predictable-sets/def-elementarypredictableset.md)
- [Stopping time](../../../../mathlib/overview/probability-theory/stochastic-processes/stopping-time.md)

## Proof

Let $n$ be an upper bound for $\tau$. To see that the stochastic interval is an elementary predictable set, note that it can be written as a finite disjoint union of sets

$$
\begin{aligned}
\{\sigma(\omega) < t \le \tau(\omega)\}
&= \bigcup_{k=1}^{n} \{k\} \times \{\sigma < k \le \tau\}
\\ &= \bigcup_{k=1}^{n} (k-1, k] \times \{\sigma \le k-1 < \tau\}
\end{aligned}
$$

where $\{\sigma \le k-1 < \tau\} \in \mathcal{F}_{k-1}$. Therefore this is an elementary predictable set.

## Lean

Formalized as [`ProbabilityTheory.stochIoc.exists_elementaryPredictableSet`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.stochIoc.exists_elementaryPredictableSet).

## Sources

- [Brownian motion blueprint: chapters/cadlag.tex, line 45](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/cadlag.tex#L45)
