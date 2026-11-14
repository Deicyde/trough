---
declaration: lemma
origin: cited
lean: indistinguishable_of_modification
statement: formalized
proof: formalized
---

# indistinguishable_of_modification_of_continuous

Let $T$ and $E$ be topological spaces and suppose that $T$ is separable Hausdorff. Let $X, Y : T \to \Omega \to E$ be two stochastic processes that are modifications of each other and are almost surely continuous. Then $X$ and $Y$ are indistinguishable.

## Depends on

Its statement uses no other node that has an article here.

## Proof

Since $T$ is separable, it has a countable dense subset $D$. Since $D$ is countable,

$$
\begin{aligned}
(\forall t \in D, \mathbb{P}\text{-a.e.}, X_t = Y_t)
\iff (\mathbb{P}\text{-a.e.}, \forall t \in D, X_t = Y_t)
\end{aligned}
$$

Hence by the modification property we have that almost surely, for all $t \in D$, $X_t = Y_t$. Then almost surely $X$ and $Y$ are continuous functions which are equal on a dense subset of $T$: those two functions are equal everywhere.

## Lean

Formalized as [`indistinguishable_of_modification`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/indistinguishable_of_modification).

## Sources

- [Brownian motion blueprint: chapters/process.tex, line 74](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/process.tex#L74)
