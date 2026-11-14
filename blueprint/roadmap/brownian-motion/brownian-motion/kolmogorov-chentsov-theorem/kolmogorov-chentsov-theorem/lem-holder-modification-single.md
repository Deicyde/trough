---
declaration: lemma
origin: cited
lean: ProbabilityTheory.exists_modification_holder_aux
statement: formalized
proof: formalized
---

# holder_modification_single

Under the assumptions of Theorem [countable_set_bound](thm-countable-set-bound.md), for $E$ a complete space and $\beta \in (0, (q - d)/p)$, there exists a modification $Y$ of $X$ (i.e., a process $Y$ with $\mathbb{P}(Y_t \ne X_t) = 0$ for all $t$) such that the paths of $Y$ are Hölder continuous of order $\beta$.

## Depends on

- [Kolmogorov condition](../chaining-for-stochastic-processes-under-kolmogor/part-01/def-iskolmogorovprocess.md)
- [Bounded internal covering number](../covers-and-covering-numbers/part-01/def-hasboundedinternalcoveringnumber.md)

## Proof depends on

- [countable_set_bound](thm-countable-set-bound.md)
- [L_lt_top](lem-l-lt-top.md)

## Proof

Let $T'$ be a countable dense subset of $T$. Let $A$ be the event

$$
\begin{aligned}
\left\{\sup_{s, t \in T';\: s \ne t} \frac{d_E(X_s, X_t)^p}{d_T(s, t)^{\beta p}} < \infty \right\}
\: .
\end{aligned}
$$

As a consequence of Theorem [countable_set_bound](thm-countable-set-bound.md), we have $\mathbb{P}(A) = 1$.

On the event $A$, $(X_t)_{t \in T'}$ has Hölder continuous paths of order $\beta$. Let $x_0 \in E$ be arbitrary and let $Y: T \to \Omega \to E$ be the process defined by

$$
\begin{aligned}
Y_t(\omega)
&= \begin{cases}
\lim_{s \to t, s \in T'} X_s(\omega) & \text{if } \omega \in A \\
x_0 & \text{otherwise}
\end{cases}
\: .
\end{aligned}
$$

Then $Y$ has Hölder continuous paths of order $\beta$ almost surely.

We can show that $(Y_s, Y_t)$ is $\mathbb{P}$-a.e. measurable for all $s, t \in T$.

It remains to show that $Y$ is a modification of $X$. Let then $t \in T$ and let $(t_n)_{n \in \mathbb{N}}$ be a sequence in $T'$ that converges to $t$. We want to show that $\mathbb{P}(Y_t \ne X_t) = 0$. It suffices to show that $\mathbb{P}(d_E(Y_t, X_t) > 0) = 0$, which itself would follow from $\mathbb{P}(d_E(Y_t, X_t) > \varepsilon) = 0$ for all $\varepsilon > 0$.

$$
\begin{aligned}
\mathbb{P}(d_E(Y_t, X_t) > \varepsilon)
&\le \mathbb{P}(d_E(Y_t, X_{t_n}) + d_E(X_{t_n}, X_t) > \varepsilon)
\\
&\le \mathbb{P}(d_E(Y_t, X_{t_n}) > \varepsilon/2) + \mathbb{P}(d_E(X_{t_n}, X_t) > \varepsilon/2)
\: .
\end{aligned}
$$

TODO

## Lean

Formalized as [`ProbabilityTheory.exists_modification_holder_aux`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.exists_modification_holder_aux).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 1708](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L1708)
