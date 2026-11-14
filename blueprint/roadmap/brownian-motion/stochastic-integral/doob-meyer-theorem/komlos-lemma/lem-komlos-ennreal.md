---
declaration: lemma
origin: cited
lean: komlos_ennreal
statement: formalized
---

# Komlòs lemma - nonnegative, a.e. convergence

Let $(f_n)_{n\in\mathbb{N}}$ be a sequence of random variables with values in $[0, \infty]$. Then there exist random variables $g_n \in convex( f_n, f_{n+1}, \cdots)$ such that $(g_n)_{n\in\mathbb{N}}$ converges almost surely to a random variable $g$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [komlos_convex](lem-komlos-convex.md)

## Proof

Let $\phi : (\Omega \to [0, \infty]) \to [0, \infty]$ be defined by $\phi(X) = \mathbb{E}[e^{-X}]$. Then $\phi$ is convex and $\phi(f_n) \le 1$ for all $n$. By Lemma [komlos_convex](lem-komlos-convex.md), there exist $g_n \in convex( f_n, f_{n+1}, \cdots)$ such that for all $\delta>0$, for $N$ large enough and $n, m \ge N$,

$$
\begin{aligned}
\mathbb{E}[e^{-g_n}]/2 + \mathbb{E}[e^{-g_m}]/2 - \mathbb{E}[e^{-(g_n + g_m)/2}] < \delta
\: .
\end{aligned}
$$

For $\varepsilon > 0$, let $B_\varepsilon = \{(x, y) \in [0, \infty]^2 \mid \vert x - y \vert \ge \varepsilon \text{ and } \min\{x, y\} \le 1/\varepsilon \}$. Then for all $x, y$,

$$
\begin{aligned}
\left\vert e^{-x} - e^{-y} \right\vert
&\le \varepsilon + 2 e^{-1/\varepsilon} + 2 \mathbb{1}_{B_\varepsilon}(x, y)
\: .
\end{aligned}
$$

Hence for any pair of random variables $(X, Y)$ with values in $[0, \infty]$,

$$
\begin{aligned}
\mathbb{E}\left[\left\vert e^{-X} - e^{-Y} \right\vert\right]
&\le \varepsilon + 2 e^{-1/\varepsilon} + 2 P((X, Y) \in B_\varepsilon) \: .
\end{aligned}
$$

On the other hand, for $(x, y) \in B_\varepsilon$, there exists $\delta_\varepsilon > 0$ such that

$$
\begin{aligned}
e^{-x}/2 + e^{-y}/2 - e^{-(x + y)/2} \ge \delta_\varepsilon
\: .
\end{aligned}
$$

Thus,

$$
\begin{aligned}
P((X, Y) \in B_\varepsilon)
&\le \frac{1}{\delta_\varepsilon} \mathbb{E}\left[ e^{-X}/2 + e^{-Y}/2 - e^{-(X + Y)/2} \right]
\: .
\end{aligned}
$$

For $n, m \ge N$ large enough so that we can apply the first inequality of this proof with $\delta = \varepsilon \delta_\varepsilon$, we deduce that

$$
\begin{aligned}
\mathbb{E}\left[\left\vert e^{-g_n} - e^{-g_m} \right\vert\right]
&\le \varepsilon + 2 e^{-1/\varepsilon} + \frac{2}{\delta_\varepsilon} \mathbb{E}\left[ e^{-g_n}/2 + e^{-g_m}/2 - e^{-(g_n + g_m)/2} \right] \\
&\le \varepsilon + 2 e^{-1/\varepsilon} + 2 \varepsilon
\: .
\end{aligned}
$$

As $\varepsilon$ is arbitrary, we deduce that $(e^{-g_n})_{n\in\mathbb{N}}$ is a Cauchy sequence in $L^1$ and thus converges in $L^1$ to some random variable $h$. Therefore, it has a subsequence $(e^{-g_{n_k}})_{k\in\mathbb{N}}$ converging almost surely to $h$. Finally, the subsequence of $g_n$ converges almost surely to $g = -\log(h)$.

## Lean

Stated as [`komlos_ennreal`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/komlos_ennreal); the blueprint marks no proof of it as formalized.

## Sources

- [Brownian motion blueprint: chapters/doob_meyer.tex, line 215](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/doob_meyer.tex#L215)
