---
declaration: lemma
origin: cited
lean: komlos_convergence_L2
statement: formalized
---

# komlos_convex_aux

Let $E$ be a Hilbert space and let $(f_n)_{n \in \mathbb{N}}$ be a sequence in $\Omega \to E$. For $i \in \mathbb{N}$, set $f_n^{(i)} = f_n \mathbb{1}_{(\Vert f_n \Vert \le i)}$, such that $f_n^{(i)} \in L^2(E)$. Then there exists a sequence of convex weights $\lambda_n^{n}, \ldots, \lambda_{N_n}^{n}$ such that the functions $\left(\lambda_n^{n} f_n^{(i)} + \ldots + \lambda_{N_n}^{n} f_{N_n}^{(i)} \right)_{n\in\mathbb{N}}$ converge in $L^2(E)$ for every $i \in \mathbb{N}$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [komlos_convex_weights_diagonal](lem-komlos-convex-weights-diagonal.md)

## Proof

Use Lemma [komlos_convex_weights_diagonal](lem-komlos-convex-weights-diagonal.md) in the Hilbert space $L^2(E)$ with the sequence of sequences $(f_n^{(i)})$, which are bounded in $L^2(E)$ for each $i \in \mathbb{N}$.

## Lean

Stated as [`komlos_convergence_L2`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/komlos_convergence_L2); the blueprint marks no proof of it as formalized.

## Sources

- [Brownian motion blueprint: chapters/doob_meyer.tex, line 178](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/doob_meyer.tex#L178)
