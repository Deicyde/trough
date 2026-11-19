---
declaration: lemma
origin: cited
lean: komlos_convex
statement: formalized
proof: formalized
---

# komlos_convex

Let $(f_n)_{n\in\mathbb{N}}$ be a sequence in a vector space $E$ and $\phi : E \to \mathbb{R}_+$ be a function such that $\phi(f_n)$ is a bounded sequence. For $\delta > 0$, let $S_\delta = \{(f, g) \mid \phi(f)/2 + \phi(g)/2 - \phi((f+g)/2) \ge \delta\}$. Then there exist $g_n\in convex(f_n,f_{n+1},\cdots)$ such that for all $\delta > 0$, for $N$ large enough and $n, m \ge N$, $(g_n, g_m) \notin S_\delta$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Let $B$ be the bound of $(\phi(f_n))_{n\in\mathbb{N}}$. Then for all $n\in\mathbb{N}$ and $g\in convex(f_n,f_{n+1},\cdots)$ we have $\phi(g)\le B$ by convexity of $\phi$. Let $r_n = \inf(\phi(g) \mid g\in convex(f_n, f_{n+1},\ldots))$. By construction $(r_n)_{n\in\mathbb{N}}$ is nondecreasing. Let $A = \sup_{n \ge 1} r_n$, which is finite (as $A \le B$) and for each $n$ we may pick some $g_n\in convex(f_n, f_{n+1},\ldots)$ such that $\phi(g_n) \le A+1/n$ by $\inf$ and $\sup$ definitions.

Let $\varepsilon \in (0, \delta/4)$. By properties of $\sup$ there exists $\bar{n}$ such that $r_{\bar{n}} \ge A-\varepsilon$ and such that $\frac{1}{\bar{n}} \le \varepsilon$. Let $m \ge k \ge \bar{n}$. We have $(g_k+g_m)/2 \in convex(f_k,f_{k+1},\ldots)$ and it follows since $(r_n)_{n\in\mathbb{N}}$ is nondecreasing that $\phi((g_k+g_m)/2) \ge A - \varepsilon$. Hence due to the ordering of $m,k,\bar{n}$,

$$
\begin{aligned}
\phi(g_k)/2 + \phi(g_m)/2 - \phi((g_k+g_m)/2)
&\le 2(A + \frac{1}{\bar{n}}) - 2(A - \varepsilon)
\\
&\le 4 \varepsilon
\\
&< \delta
\: .
\end{aligned}
$$

Thus, for $n, m \ge \bar{n}$, $(g_n, g_m) \notin S_\delta$.

## Lean

Formalized as [`komlos_convex`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/komlos_convex).

## Sources

- [Brownian motion blueprint: chapters/doob_meyer.tex, line 17](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/doob_meyer.tex#L17)
