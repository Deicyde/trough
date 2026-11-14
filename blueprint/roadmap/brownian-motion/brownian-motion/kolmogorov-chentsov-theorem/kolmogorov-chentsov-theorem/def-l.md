---
declaration: definition
origin: cited
lean: ProbabilityTheory.constL
statement: formalized
---

# L

We introduce the constant

$$
\begin{aligned}
L(c_1, d, p, q, \beta)
&= 2^{2p+5q+1} c_1 (c_1^{1/d}+1)^{q-d}
\\&\quad \times \sum_{k=0}^\infty 2^{k (\beta p - (q-d))}\left(4^d \left(\max\left\{0, \log_2(c_1) + (k + 2)d \right\}\right)^q
+ C_p\right)
\: .
\end{aligned}
$$

## Depends on

- [Cp](../chaining-for-stochastic-processes-under-kolmogor/part-02/def-cp.md)

## Lean

Formalized as [`ProbabilityTheory.constL`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.constL).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 1584](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L1584)
