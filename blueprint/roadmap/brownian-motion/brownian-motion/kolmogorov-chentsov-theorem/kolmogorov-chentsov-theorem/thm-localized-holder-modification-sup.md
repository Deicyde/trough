---
declaration: theorem
origin: cited
lean: ProbabilityTheory.exists_modification_holder_iSup
statement: formalized
proof: formalized
---

# localized_holder_modification_sup

Let $T$ be a metric space with a cover $(T_n)$ with bounded covering numbers with constants $c_n$ and the same exponent $d$. Let $(p_n, q_n)_{n \in \mathbb{N}}$ be a sequence of pairs of positive numbers such that $q_n > d$ for all $n \in \mathbb{N}$. Let $X : T \to \Omega \to E$ be a process that satisfies the Kolmogorov condition with exponents $(p_n, q_n)$ for all $n \in \mathbb{N}$. Then $X$ has a modification $Y$ such that almost surely the paths of $Y$ are locally Hölder continuous of all orders $\gamma \in (0, \sup_n (q_n - d)/p_n)$.

## Depends on

- [Kolmogorov condition](../chaining-for-stochastic-processes-under-kolmogor/part-01/def-iskolmogorovprocess.md)
- [Cover with bounded covering numbers](def-hasboundedcoveringnumbercover.md)

## Proof depends on

- [localized_holder_modification](thm-localized-holder-modification.md)

## Proof

For each $n$, by Theorem [localized_holder_modification](thm-localized-holder-modification.md) there is a modification $Y_n$ of $X$ such that the paths of $Y_n$ are locally Hölder continuous of all orders $\gamma \in (0, (q_n - d)/p_n)$. By Lemma [indistinguishable_of_modification_of_continuous](../../stochastic-processes/lem-indistinguishable-of-modification-of-continu.md), any two processes $Y_n, Y_m$ are indistinguishable. That is, almost surely $Y_n = Y_m$. Since there are countably many such almost sure equalities, we get that almost surely there is equality for all $n, m$. Let then $Y$ be the process equal to $Y_0$ on the event that the equalities hold, and equal to an arbitrary point $x_0 \in E$ otherwise. Then first, $Y$ is a modification of $X$. Then for any $\gamma < \sup_n (q_n - d)/p_n$ there is $n$ such that $\gamma < (q_n - d)/p_n$ and thus since $Y = Y_n$ the paths of $Y$ are locally Hölder continuous of order $\gamma$ almost surely.

## Lean

Formalized as [`ProbabilityTheory.exists_modification_holder_iSup`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.exists_modification_holder_iSup).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 1830](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L1830)
