---
declaration: lemma
origin: cited
lean: ProbabilityTheory.sup_stoppedProcess_leastGE_le
statement: formalized
proof: formalized
---

# sup_stoppedProcess_le

For $Y$ a stochastic process, let $Y^*_t = \sup_{s \le t} \Vert Y_s \Vert$. Let $X$ be a stochastic process and let $\tau = \inf \{t \mid \Vert X_t \Vert \ge n\}$ for some $n \in \mathbb{R}$. Then

$$
\begin{aligned}
(X^{\tau})^*_t
\le n + \mathbb{1}_{\tau \le t} \Vert X_{\tau} \Vert
\: .
\end{aligned}
$$

## Depends on

- [Stopped process](../../../filtrations-processes-and-martingales/basic-definitions/part-02/def-stoppedprocess.md)

## Proof

If $\tau > t$, then for all $s \le t$, $\|X_s\| \le n$, and thus $(X^\tau)^*_t = \sup_{s \le t} \|X_{\tau \land s}\| \le n = n + \mathbb{1}_{\tau \le t} \|X_{\tau}\|$. Otherwise $(X^\tau)^*_t = \sup_{s \le \tau} \|X_s\|$. For $s < \tau$, $\|X_s\| \le n$, and $\|X_\tau\| \le \|X_\tau\|$ so $\sup_{s \le \tau} \|X_s\| \le n \lor \|X_\tau\| \le n + \|X_\tau\| = n + \mathbb{I}_{\tau \le t} \|X_\tau\|$.

## Lean

Formalized as [`ProbabilityTheory.sup_stoppedProcess_leastGE_le`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.sup_stoppedProcess_leastGE_le).

## Sources

- [Brownian motion blueprint: chapters/local_martingales.tex, line 743](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/local_martingales.tex#L743)
