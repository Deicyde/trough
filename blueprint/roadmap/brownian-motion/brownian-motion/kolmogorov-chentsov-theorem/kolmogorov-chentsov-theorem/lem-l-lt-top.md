---
declaration: lemma
origin: cited
lean: ProbabilityTheory.constL_lt_top
statement: formalized
proof: formalized
---

# L_lt_top

For $c_1 < \infty$, $p> 0$, $q > d > 0$ and $\beta \in (0, (q-d)/p)$, the constant $L(c_1, d, p, q, \beta)$ is finite.

## Depends on

- [L](def-l.md)

## Proof

Let $a_k = 2^{2p+5q+1} M c_1 (c_1^{1/d}+1)^{q-d} 2^{k (\beta p - (q-d))} \left(4^d \left(\max\left\{0, \log_2(c_1) + (k + 2)d \right\}\right)^q + C_p\right)$. Then $L(c_1, d, p, q, \beta) = \sum_{k=0}^\infty a_k$. To show that the sum is finite, we can use the ratio test.

$$
\begin{aligned}
\frac{\vert a_{k+1} \vert}{\vert a_k \vert}
&= 2^{\beta p - (q - d)}
\frac{\left(4^d \left(\max\left\{0, \log_2(c_1) + (k + 3)d \right\}\right)^q + C_p\right)}
{\left(4^d \left(\max\left\{0, \log_2(c_1) + (k + 2)d \right\}\right)^q + C_p\right)}
\end{aligned}
$$

The limit at infinity of that ratio is $2^{\beta p - (q - d)} < 1$, hence the series $\sum_{k=0}^\infty a_k$ converges.

## Lean

Formalized as [`ProbabilityTheory.constL_lt_top`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.constL_lt_top).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 1599](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L1599)
