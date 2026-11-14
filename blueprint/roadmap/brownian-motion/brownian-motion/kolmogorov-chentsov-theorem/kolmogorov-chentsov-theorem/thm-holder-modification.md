---
declaration: theorem
origin: cited
lean: ProbabilityTheory.exists_modification_holder
statement: formalized
proof: formalized
---

# holder_modification

Under the assumptions of Theorem [countable_set_bound](thm-countable-set-bound.md), for $E$ a complete space, there exists a modification $Y$ of $X$ (i.e., a process $Y$ with $\mathbb{P}(Y_t \ne X_t) = 0$ for all $t$) such that the paths of $Y$ are Hölder continuous of all orders $\gamma \in (0, (q - d)/p)$.

## Depends on

- [Kolmogorov condition](../chaining-for-stochastic-processes-under-kolmogor/part-01/def-iskolmogorovprocess.md)
- [Bounded internal covering number](../covers-and-covering-numbers/part-01/def-hasboundedinternalcoveringnumber.md)

## Proof depends on

- [holder_modification_single](lem-holder-modification-single.md)
- [indistinguishable_of_modification_of_continuous](../../stochastic-processes/lem-indistinguishable-of-modification-of-continu.md)

## Proof

Let $(\beta_n)$ be an increasing sequence of numbers in $(0, (q - d)/p)$ such that $\beta_n \to (q - d)/p$. For each $n$, let $Y^n$ be the modification of $X$ given by Lemma [holder_modification_single](lem-holder-modification-single.md) for $\beta = \beta_n$. Then by Lemma [indistinguishable_of_modification_of_continuous](../../stochastic-processes/lem-indistinguishable-of-modification-of-continu.md), the processes $Y^0$ and $Y^n$ are indistinguishable for all $n$. That is, there exists an event $A_n$ such that $\mathbb{P}(A_n) = 1$ and such that for all $\omega \in A_n$, $Y^0_t(\omega) = Y^n_t(\omega)$ for all $t \in T$.

Let $A = \bigcap_{n \in \mathbb{N}} A_n$ and let $x_0 \in E$ be arbitrary. Then $\mathbb{P}(A) = 1$ and the process $Y(\omega) = Y^0(\omega)$ for $\omega \in A$ and $Y(\omega) = x_0$ for $\omega \notin A$ has paths that are Hölder continuous of all orders $\gamma \in (0, (q - d)/p)$.

## Lean

Formalized as [`ProbabilityTheory.exists_modification_holder`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.exists_modification_holder).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 1756](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L1756)
