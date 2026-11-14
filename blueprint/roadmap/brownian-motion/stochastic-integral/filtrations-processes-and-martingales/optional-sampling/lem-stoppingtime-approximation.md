---
declaration: lemma
origin: cited
lean: NNReal.approximable
statement: formalized
proof: formalized
---

# stoppingTime_approximation

$T = \mathbb{R}_+$ is an approximable time index. In particular, for any stopping time $\tau$ on $\overline{\mathbb{R}_+}$, defining $\tau_n = 2^{-n} \lceil 2^n \tau \rceil$, we have that $(\tau_n)$ is a discrete approximation sequence of $\tau$.

## Depends on

- [Stopping time](../../../../mathlib/overview/probability-theory/stochastic-processes/stopping-time.md)
- [Approximable time index](def-approximabletimeindex.md)

## Proof

Clearly $\tau_n \downarrow \tau$ as $n \to \infty$ and so it remains to show that each $\tau_n$ is a stopping time. Indeed,

$$
\{\tau_n \le t\} = \{\tau \le 2^{-n} \lfloor 2^n t\rfloor\}
\in \mathcal{F}_{2^{-n} \lfloor 2^n t\rfloor} \subseteq \mathcal{F}_t
$$

where the last inclusion follows as $2^{-n} \lfloor 2^n t\rfloor \le t$.

## Lean

Formalized as [`NNReal.approximable`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/NNReal.approximable).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 1056](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L1056)
