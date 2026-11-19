---
declaration: lemma
origin: cited
lean: ProbabilityTheory.SimpleProcess.integral_bot
statement: formalized
proof: formalized
---

# elemStochIntegralBilin_zero

$(V \bullet_B X)_0 = 0$ for every simple process $V$ and stochastic process $X$.

## Depends on

- [Elementary stochastic integral](def-elemstochintegralbilin.md)

## Proof

$$
\begin{aligned}
(V \bullet_B X)_0
&= \sum_{k=1}^{n} B (\eta_k, X^0_{t_k} - X^0_{s_k})
\\
&= \sum_{k=1}^{n} B (\eta_k, X_{0} - X_{0})
\\
&= \sum_{k=1}^{n} B (\eta_k, 0)
\\
&= 0
\: .
\end{aligned}
$$

## Lean

Formalized as [`ProbabilityTheory.SimpleProcess.integral_bot`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.SimpleProcess.integral_bot).

## Sources

- [Brownian motion blueprint: chapters/elementary.tex, line 431](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/elementary.tex#L431)
