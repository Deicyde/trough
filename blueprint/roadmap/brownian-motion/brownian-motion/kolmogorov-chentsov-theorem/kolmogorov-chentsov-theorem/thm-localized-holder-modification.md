---
declaration: theorem
origin: cited
lean: ProbabilityTheory.exists_modification_holder'
statement: formalized
proof: formalized
---

# localized_holder_modification

Let $T$ be a metric space with a cover $(T_n)$ with bounded covering numbers with constants $c_n$ and the same exponent $d$. Let $X : T \to \Omega \to E$ be a process that satisfies the Kolmogorov condition with exponents $(p, q)$ with $q > d$. Then $X$ has a modification $Y$ such that almost surely the paths of $Y$ are locally Hölder continuous of all orders $\gamma \in (0, (q - d)/p)$.

## Depends on

- [Kolmogorov condition](../chaining-for-stochastic-processes-under-kolmogor/part-01/def-iskolmogorovprocess.md)
- [Cover with bounded covering numbers](def-hasboundedcoveringnumbercover.md)

## Proof depends on

- [holder_modification](thm-holder-modification.md)
- [indistinguishable_of_modification_of_continuous](../../stochastic-processes/lem-indistinguishable-of-modification-of-continu.md)

## Proof

For each $n$, by Theorem [holder_modification](thm-holder-modification.md) there is a modification $Y_n$ of $X$ seen as a process on $T_n$ such that the paths of $Y_n$ are Hölder continuous of all orders $\gamma \in (0, (q - d)/p)$. By Lemma [indistinguishable_of_modification_of_continuous](../../stochastic-processes/lem-indistinguishable-of-modification-of-continu.md), $Y_n$ and $Y_{n+1}$ are indistinguishable on $T_n$. That is, almost surely $Y_n = Y_{n+1}$ on $T_n$. Since there are countably many such almost sure equalities, we get that almost surely there is equality for all $n$. Let $A$ be the event that this happens, let $x_0 \in E$ be arbitrary and define a process $Y : T \to \Omega \to E$ by

$$
\begin{aligned}
Y(t, \omega)
&= \begin{cases}
Y_n(t, \omega) & \text{if } \omega \in A \: , \: t \in T_n \setminus T_{n-1} \: ,
\\
x_0 & \text{if } \omega \notin A \: .
\end{cases}
\end{aligned}
$$

Then $Y$ is a modification of $X$ and has paths that are locally Hölder continuous of all orders $\gamma \in (0, (q - d)/p)$ almost surely.

## Lean

Formalized as [`ProbabilityTheory.exists_modification_holder'`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.exists_modification_holder').

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 1802](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L1802)
