---
declaration: lemma
origin: cited
lean: TendstoUniformly_convexTail
statement: formalized
proof: formalized
---

# convex_of_converg_seq_is_converg

Let $(x_n)_{n \in \mathbb{N}}$ be a sequence in a real vector space converging to $x$. Let $\mathcal{C}((x_n))$ be the set of sequences $(y_n)_{n \in \mathbb{N}}$ such that for all $n$, $y_n \in convex(x_n, x_{n+1}, \ldots)$. Then we have uniform convergence over $\mathcal{C}((x_n))$: for all $\varepsilon > 0$, there exists $\bar{n}$ such that for all $n \ge \bar{n}$, for all $(y_n)_{n \in \mathbb{N}} \in \mathcal{C}((x_n))$, $\Vert y_n - x \Vert \le \varepsilon$;

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Let $\varepsilon>0$. By convergence of $x_n$, there exists $\bar{n}$ such that for all $n \ge \bar{n}$, $\Vert x_n-x \Vert \le \varepsilon$. Let $a_{n, m}$ be convex weights such that $y_n = \sum_{m = n}^{N_n} a_{n, m} x_m$. By triangular inequality it follows that for $n \ge \bar{n}$,

$$
\begin{aligned}
\Vert y_n - x \Vert
= \left\Vert \sum_{m = n}^{N_n} a_{n, m} x_m - x \right\Vert
= \left\Vert \sum_{m = n}^{N_n} a_{n, m} (x_m - x) \right\Vert
\le \sum_{m = n}^{N_n} a_{n, m} \Vert x_m - x \Vert
\le \varepsilon
\: .
\end{aligned}
$$

## Lean

Formalized as [`TendstoUniformly_convexTail`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/TendstoUniformly_convexTail).

## Sources

- [Brownian motion blueprint: chapters/doob_meyer.tex, line 72](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/doob_meyer.tex#L72)
