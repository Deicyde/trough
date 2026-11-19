---
declaration: lemma
origin: cited
lean: komlos_convex_weights
statement: formalized
proof: formalized
---

# komlos_convex_weights

Let $E$ be a Hilbert space and for $i \in \mathbb{N}$, let $(x_n^{(i)})_{n \in \mathbb{N}}$ be a bounded sequence in $E$. Then there exists a sequence of convex weights $(\lambda^{k,n}_\cdot)_{k, n \in \mathbb{N}}$ with $\lambda^{k,n}_m = 0$ for $m < n$ such that for all $k \in \mathbb{N}$, $\left(\sum_{m \ge n} \left((\lambda^{k,n}_\cdot) * \ldots * (\lambda^{1,\cdot}_\cdot)\right)_m x_m^{(k)}\right)_{n \in \mathbb{N}}$ converges.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [komlos_norm](lem-komlos-norm.md)
- [convex_weights_product](def-convex-weights-product.md)

## Proof

First by Lemma [komlos_norm](lem-komlos-norm.md) applied to $(x_n^{(1)})_{n\in\mathbb{N}}$ in the Hilbert space $E$, there exist $g_n^1 \in convex(x_n^{(1)}, x_{n+1}^{(1)}, \ldots)$ (call its weights $\lambda^{1,n}_n,\cdots,\lambda^{1,n}_{N^1_n}$) such that $g_n^1$ converges to some $g^1$.

Secondly define $\tilde{g}_n^1$, convex combination of $x_n^{(2)}, x_{n+1}^{(2)}, \ldots$ with weights $\lambda^{1,n}_n,\cdots,\lambda^{1,n}_{N^1_n}$. Applying lemma [komlos_norm](lem-komlos-norm.md) to $(\tilde{g}_n^1)_{n\in\mathbb{N}}$ gives us $g_n^2 \in convex(\tilde{g}_n^1, \tilde{g}_{n+1}^1, \ldots)$ (call its weights $\lambda^{2,n}_n,\cdots,\lambda^{2,n}_{N^2_n}$) such that $g_n^2$ converges to some $g^2$. $g_n^2$ is a convex combination of $x_n^{(2)}, x_{n+1}^{(2)}, \ldots$ with weights $(\lambda^{2,n}_\cdot) * (\lambda^{1,\cdot}_\cdot)$.

We continue iterating this process inductively. At iteration $k$ we have weights $(\lambda^{k,n}_\cdot * \ldots * \lambda^{1,\cdot}_\cdot)$. We define $\tilde{g}_n^k$ as the convex combination of $x_n^{(k+1)}, x_{n+1}^{(k+1)}, \ldots$ with those weights:

$$
\tilde{g}_n^k = \sum_{l} (\lambda^{k,n}_\cdot * \ldots * \lambda^{1,\cdot}_\cdot)_l x^{(k+1)}_l
$$

We apply Lemma [komlos_norm](lem-komlos-norm.md) to $(\tilde{g}_n^k)_{n\in\mathbb{N}}$ to get $g_n^{k+1} \in convex(\tilde{g}_n^k, \tilde{g}_{n+1}^k, \ldots)$ such that $g_n^{k+1}$ converges to some $g^{k+1}$. We denote its weights by $\lambda^{k+1,n}_n,\cdots,\lambda^{k+1,n}_{N^{k+1}_n}$ and can then write:

$$
\begin{aligned}
g_n^{k+1} & = \sum_{m} \lambda^{k+1,n}_m \tilde{g}_m^k
= \sum_{m} \lambda^{k+1,n}_m \left( \sum_{l} (\lambda^{k,m}_\cdot * \ldots * \lambda^{1,\cdot}_\cdot)_l x_l^{(k+1)} \right) \\
& = \sum_{l} \left( \sum_{m} \lambda^{k+1,n}_m (\lambda^{k,m}_\cdot * \ldots * \lambda^{1,\cdot}_\cdot)_l \right) x_l^{(k+1)} \\
& = \sum_{l} (\lambda^{k+1,n}_{\cdot} * (\lambda^{k,\cdot}_\cdot * \ldots * \lambda^{1,\cdot}_\cdot))_l x_l^{(k+1)}
\end{aligned}
$$

We have thus defined, for all $k, n \in \mathbb{N}$, convex weights $(\lambda^{k,n}_m)$ (that are zero for $m < n$) such that $\sum_{m \ge n}((\lambda^{k,n}_\cdot * \ldots * \lambda^{1, \cdot}_\cdot))_m x_m^{(k)}$ converges to $g^k$.

## Lean

Formalized as [`komlos_convex_weights`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/komlos_convex_weights).

## Sources

- [Brownian motion blueprint: chapters/doob_meyer.tex, line 102](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/doob_meyer.tex#L102)
