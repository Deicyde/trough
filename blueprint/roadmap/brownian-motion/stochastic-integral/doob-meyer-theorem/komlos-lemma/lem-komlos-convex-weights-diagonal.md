---
declaration: lemma
origin: cited
lean: komlos_convex_weights_diagonal
statement: formalized
proof: formalized
---

# komlos_convex_weights_diagonal

Let $E$ be a Hilbert space and for $i \in \mathbb{N}$, let $(x_n^{(i)})_{n \in \mathbb{N}}$ be a bounded sequence in $E$. Then there exists a sequence of convex weights $(\eta^n_\cdot)_{n \in \mathbb{N}}$ with $\eta^n_m = 0$ for $m < n$ such that for all $i \in \mathbb{N}$, the sequence $\left(\sum_{m \ge n} \eta^n_m x_m^{(i)}\right)_{n \in \mathbb{N}}$ converges.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [komlos_convex_weights](lem-komlos-convex-weights.md)
- [komlos_convex_weights_tendsto](lem-komlos-convex-weights-tendsto.md)

## Proof

Let $(\lambda^{k,n}_\cdot)_{k, n \in \mathbb{N}}$ be convex weights satisfying the conclusion of Lemma [komlos_convex_weights](lem-komlos-convex-weights.md), and let $(g^i)_{i\in \mathbb{N}}$ be the sequence of limits of the sums. Let $\eta^n_m = (\lambda^{n,n}_\cdot * \ldots * \lambda^{1,\cdot}_\cdot)_m$. We show that for all $i \in \mathbb{N}$, the sequence $\left(\sum_{m \ge n} \eta^n_m x_m^{(i)}\right)_{n \in \mathbb{N}}$ converges to $g^i$.

Let $i \in \mathbb{N}$. By Lemma [komlos_convex_weights_tendsto](lem-komlos-convex-weights-tendsto.md), for all $\varepsilon > 0$, there exists $\bar{n}$ such that for all $n \ge \bar{n}$, for all $k \ge i$, $\left\Vert\sum_{m \ge n} \left((\lambda^{k,n}_\cdot) * \ldots * (\lambda^{1,\cdot}_\cdot)\right)_m x_m^{(i)} - g^i\right\Vert \le \varepsilon$. Hence for $n \ge \max(\bar{n}, i)$,

$$
\begin{aligned}
\left\Vert\sum_{m \ge n} \eta^n_m x_m^{(i)} - g^i\right\Vert
&= \left\Vert\sum_{m \ge n} \left((\lambda^{n,n}_\cdot) * \ldots * (\lambda^{1,\cdot}_\cdot)\right)_m x_m^{(i)} - g^i\right\Vert
\le \varepsilon
\: .
\end{aligned}
$$

## Lean

Formalized as [`komlos_convex_weights_diagonal`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/komlos_convex_weights_diagonal).

## Sources

- [Brownian motion blueprint: chapters/doob_meyer.tex, line 152](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/doob_meyer.tex#L152)
