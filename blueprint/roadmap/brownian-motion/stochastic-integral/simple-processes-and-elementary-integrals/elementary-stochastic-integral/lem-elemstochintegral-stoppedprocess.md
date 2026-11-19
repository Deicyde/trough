---
declaration: lemma
origin: cited
lean: ProbabilityTheory.SimpleProcess.stoppedProcess_integral
statement: formalized
proof: formalized
---

# elemStochIntegral_stoppedProcess

Let $X$ be a stochastic process, $V$ a simple process and $τ$ a stopping time. Then

$$
\begin{aligned}
(V \bullet_B X)^τ = V \bullet_B (X^τ)
\: .
\end{aligned}
$$

## Depends on

- [Stopped process](../../filtrations-processes-and-martingales/basic-definitions/part-02/def-stoppedprocess.md)

## Proof

$$
\begin{aligned}
(V \bullet_B X)^\tau_t
&= (V \bullet_B X)_{t \wedge \tau}
\\
&= \sum_{k=1}^{n} B (\eta_k, X^{t \wedge \tau}_{t_k} - X^{t \wedge \tau}_{s_k})
\\
&= \sum_{k=1}^{n} B (\eta_k, (X^{\tau})^t_{t_k} - (X^{\tau})^t_{s_k})
\\
&= (V \bullet_B (X^{\tau}))_t
\: .
\end{aligned}
$$

## Lean

Formalized as [`ProbabilityTheory.SimpleProcess.stoppedProcess_integral`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.SimpleProcess.stoppedProcess_integral).

## Sources

- [Brownian motion blueprint: chapters/elementary.tex, line 550](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/elementary.tex#L550)
