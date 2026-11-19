---
declaration: definition
origin: cited
lean: ProbabilityTheory.SimpleProcess.integral
statement: formalized
---

# Elementary stochastic integral

Let $V \in \mathcal{E}_{T, E}$ be a simple process and let $X$ be a stochastic process with values in a normed space $F$. Let $B$ be a continuous bilinear map from $E \times F$ to another normed space $G$. The *general elementary stochastic integral* process $V \bullet_B X : T \to \Omega \to G$ is defined by

$$
\begin{aligned}
(V \bullet_B X)_t
&= \sum_{k=1}^{n} B (\eta_k, X^t_{t_k} - X^t_{s_k})
\: .
\end{aligned}
$$

## Depends on

- [Simple process](../simple-processes-and-elementary-predictable-sets/def-simpleprocess.md)

## Lean

Formalized as [`ProbabilityTheory.SimpleProcess.integral`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.SimpleProcess.integral).

## Sources

- [Brownian motion blueprint: chapters/elementary.tex, line 368](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/elementary.tex#L368)
