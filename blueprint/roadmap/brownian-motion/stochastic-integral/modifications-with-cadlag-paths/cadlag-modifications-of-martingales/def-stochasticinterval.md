---
declaration: definition
origin: cited
lean: ProbabilityTheory.stochIcc, ProbabilityTheory.stochIco, ProbabilityTheory.stochIoc, ProbabilityTheory.stochIoo, ProbabilityTheory.stochGraph
statement: formalized
---

# Stochastic intervals

Let $T$ be a time domain and let $\sigma, \tau$ be functions $\Omega \to T \cup \{\infty\}$. We define

$$
\begin{aligned}
[\![\sigma, \tau]\!]
&= \{(t, \omega) \in T \times \Omega \mid \sigma(\omega) \le t \le \tau(\omega)\}
\:, \\
[\![\sigma, \tau[\![
&= \{(t, \omega) \in T \times \Omega \mid \sigma(\omega) \le t < \tau(\omega)\}
\:, \\
]\!]\sigma, \tau]\!]
&= \{(t, \omega) \in T \times \Omega \mid \sigma(\omega) < t \le \tau(\omega)\}
\:, \\
]\!]\sigma, \tau[\![
&= \{(t, \omega) \in T \times \Omega \mid \sigma(\omega) < t < \tau(\omega)\}
\:, \\
[\![\sigma]\!]
&= \{(t, \omega) \in T \times \Omega \mid \sigma(\omega) = t\} = [\![\sigma, \sigma]\!]
\:.
\end{aligned}
$$

We call those stochastic intervals. Note that these are subsets of $T \times \Omega$, not of $(T \cup \{\infty\}) \times \Omega$. $[\![\sigma]\!]$ is called the graph of $\sigma$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`ProbabilityTheory.stochIcc`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.stochIcc), [`ProbabilityTheory.stochIco`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.stochIco), [`ProbabilityTheory.stochIoc`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.stochIoc), [`ProbabilityTheory.stochIoo`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.stochIoo), [`ProbabilityTheory.stochGraph`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.stochGraph).

## Sources

- [Brownian motion blueprint: chapters/cadlag.tex, line 8](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/cadlag.tex#L8)
