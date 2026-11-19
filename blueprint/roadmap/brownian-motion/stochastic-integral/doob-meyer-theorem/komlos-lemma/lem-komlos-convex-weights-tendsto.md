---
declaration: lemma
origin: cited
lean: komlos_uniform_convergence
statement: formalized
proof: formalized
---

# komlos_convex_weights_tendsto

Let $E$ be a Hilbert space and for $i \in \mathbb{N}$, let $(x_n^{(i)})_{n \in \mathbb{N}}$ be a bounded sequence in $E$. Let $(\lambda^{k,n}_\cdot)_{k, n \in \mathbb{N}}$ be convex weights satisfying the conclusion of Lemma [komlos_convex_weights](lem-komlos-convex-weights.md), and let $(g^i)_{i\in \mathbb{N}}$ be the sequence of limits of the sums.

Then for every $k \ge i$, the sequence $\left(\sum_{m \ge n} \left((\lambda^{k,n}_\cdot) * \ldots * (\lambda^{1,\cdot}_\cdot)\right)_m x_m^{(i)}\right)_{n \in \mathbb{N}}$ converges to $g^i$, uniformly in $k$.

## Depends on

- [komlos_convex_weights](lem-komlos-convex-weights.md)

## Proof depends on

- [convex_of_converg_seq_is_converg](lem-convex-of-converg-seq-is-converg.md)

## Proof

Let $i \in \mathbb{N}$. By Lemma [convex_of_converg_seq_is_converg](lem-convex-of-converg-seq-is-converg.md), there is uniform convergence over all convex combinations of the sequence $\left(\sum_{m \ge n} \left((\lambda^{i,n}_\cdot) * \ldots * (\lambda^{1,\cdot}_\cdot)\right)_m x_m^{(i)}\right)_{n \in \mathbb{N}}$ to $g^i$. All sums $\sum_{m \ge n} \left((\lambda^{k,n}_\cdot) * \ldots * (\lambda^{1,\cdot}_\cdot)\right)_m x_m^{(i)}$ for $k \ge i$ are convex combinations of $\sum_{m \ge n} \left((\lambda^{i,n}_\cdot) * \ldots * (\lambda^{1,\cdot}_\cdot)\right)_m x_m^{(i)}$, hence they converge to $g^i$ uniformly in $k$.

## Lean

Formalized as [`komlos_uniform_convergence`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/komlos_uniform_convergence).

## Sources

- [Brownian motion blueprint: chapters/doob_meyer.tex, line 134](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/doob_meyer.tex#L134)
