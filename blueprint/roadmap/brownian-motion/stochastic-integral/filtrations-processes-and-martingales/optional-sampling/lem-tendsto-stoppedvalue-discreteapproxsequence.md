---
declaration: lemma
origin: cited
lean: MeasureTheory.tendsto_stoppedValue_discreteApproxSequence
statement: formalized
proof: formalized
---

# tendsto_stoppedValue_discreteApproxSequence

Given a right continuous process $X$ and a discrete approximation sequence $(\tau_n)$ of the stopping time $\tau$, we have that

$$
\lim_{n \to \infty} X_{\tau_n} = X_\tau \text{ a.s.}
$$

## Depends on

- [Stopping time](../../../../mathlib/overview/probability-theory/stochastic-processes/stopping-time.md)
- [Discrete approximation sequence](def-approxseq.md)
- [Right continuous function](../basic-definitions/part-01/def-rightcontinuous.md)

## Proof

This follows directly as $X$ is right continuous and $\tau_n \downarrow \tau$ a.s.

## Lean

Formalized as [`MeasureTheory.tendsto_stoppedValue_discreteApproxSequence`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.tendsto_stoppedValue_discreteApproxSequence).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 1000](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L1000)
