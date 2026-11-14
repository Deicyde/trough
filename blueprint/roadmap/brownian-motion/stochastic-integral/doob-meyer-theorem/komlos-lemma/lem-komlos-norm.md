---
declaration: lemma
origin: cited
lean: komlos_norm
statement: formalized
proof: formalized
---

# komlos_norm

Let $H$ be a Hilbert space and $(f_n)_{n\in\mathbb{N}}$ a bounded sequence in $H$. Then there exist functions $g_n\in convex(f_n,f_{n+1},\cdots)$ such that $(g_n)_{n\in\mathbb{N}}$ converges in $H$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [komlos_convex](lem-komlos-convex.md)

## Proof

Consider $\phi : H \to \mathbb{R}_+$ defined by $\phi(f) = \|f\|_2^2$, which is convex. Then Lemma [komlos_convex](lem-komlos-convex.md) applied to $(f_n)_{n\in\mathbb{N}}$ and $\phi$ gives us functions $g_n\in convex(f_n,f_{n+1},\cdots)$ such that for every $\delta>0$ there exists $N$ such that for $n,m\geq N$, $(g_n,g_m)\notin S_\delta$. Thus for every $\delta>0$ there exists $N$ such that for $n,m\geq N$,

$$
\begin{aligned}
\|g_n\|_2^2/2 + \|g_m\|_2^2/2 - \|(g_n+g_m)/2\|_2^2
&< \delta
\: .
\end{aligned}
$$

But the left-hand side is equal to $\|g_n - g_m\|_2^2/4$ by the parallelogram identity, hence $(g_n)_{n\in\mathbb{N}}$ is a Cauchy sequence in $H$ and thus converges in $H$ by completeness.

## Lean

Formalized as [`komlos_norm`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/komlos_norm).

## Sources

- [Brownian motion blueprint: chapters/doob_meyer.tex, line 51](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/doob_meyer.tex#L51)
