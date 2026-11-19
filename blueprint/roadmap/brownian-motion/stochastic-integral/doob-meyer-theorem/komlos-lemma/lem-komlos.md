---
declaration: lemma
origin: cited
lean: komlos_L1
statement: formalized
---

# Komlòs Lemma

Let $(f_n)_{n\in\mathbb{N}}$ be a uniformly integrable sequence of functions $\Omega \to E$, for $E$ a Hilbert space. Then there exist functions $g_n \in convex(f_n, f_{n+1}, \cdots)$ such that $(g_n)_{n\in\mathbb{N}}$ converges in $L^1$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [komlos_convex_aux](lem-komlos-convex-aux.md)

## Proof

For $i,n\in\mathbb{N}$ set $f_{n}^{(i)}:=f_n \mathbb{1}_{(|f_n|\leq i)}$ such that $f_{n}^{(i)}\in L^2$. Using [komlos_convex_aux](lem-komlos-convex-aux.md) there exist for every $n$ convex weights $\lambda_n^{n}, \ldots, \lambda_{N_n}^{n}$ such that the functions $\lambda_n^{n} f_n^{(i)} + \ldots+\lambda_{N_n}^{n} f_{N_n}^{(i)}$ converge in $L^2$ for every $i\in\mathbb{N}$. By uniform integrability, $\lim_{i\to \infty}\| f^{(i)}_n- f_n\|_1=0$, uniformly with respect to $n$. Hence, once again, uniformly with respect to $n$,

$$
\textstyle\lim_{i\to\infty}\|  (\lambda_n^{n} f_n^{(i)} + \ldots+\lambda_{N_n}^{n} f_{N_n}^{(i)})-(\lambda_n^{n} f_n + \ldots+\lambda_{N_n}^{n} f_{N_n})\|_1= 0.
$$

Thus $(\lambda_n^{n} f_n + \ldots+\lambda_{N_n}^{n} f_{N_n})_{n\geq 1}$ is a Cauchy sequence in $L^1$.

## Lean

Stated as [`komlos_L1`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/komlos_L1); the blueprint marks no proof of it as formalized.

## Sources

- [Brownian motion blueprint: chapters/doob_meyer.tex, line 194](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/doob_meyer.tex#L194)
