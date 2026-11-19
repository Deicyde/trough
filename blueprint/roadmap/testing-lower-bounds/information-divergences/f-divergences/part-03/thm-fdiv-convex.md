---
declaration: theorem
origin: cited
lean: ProbabilityTheory.fDiv_convex
statement: formalized
proof: formalized
---

# Joint convexity

The function $(\mu, \nu) \mapsto D_f(\mu, \nu)$ is convex.

## Depends on

- [f-divergence](../part-01/def-fdiv.md)

## Proof depends on

- [Conditioning increases f-divergence](thm-fdiv-comp-le-condfdiv-2.md)

## Proof

Let $\mu_0, \mu_1, \nu_0, \nu_1$ be four measures. Let $\lambda \in [0,1]$. Let $\xi$ be the probability measure on $\{0,1\}$ with $\xi(\{1\}) = \lambda$. Let $\kappa$ be the kernel $\{0,1\} \rightsquigarrow \mathcal X$ defined by $\kappa(0) = \mu_0$ and $\kappa(1) = \mu_1$. Let $\eta$ be the kernel $\{0,1\} \rightsquigarrow \mathcal X$ defined by $\eta(0) = \nu_0$ and $\eta(1) = \nu_1$.

$$
\begin{aligned}
D_f(\xi \otimes \kappa, \xi \otimes \eta)
&= D_f(\kappa, \eta \mid \xi)
= (1 - \lambda) D_f(\mu_0, \nu_0) + \lambda D_f(\mu_1, \nu_1)
\: , \\
D_f(\kappa \circ \xi, \eta \circ \xi)
&= D_f((1 - \lambda)\mu_0 + \lambda \mu_1, (1 - \lambda)\nu_0 + \lambda \nu_1)
\: .
\end{aligned}
$$

By Theorem [Conditioning increases f-divergence](thm-fdiv-comp-le-condfdiv-2.md), $D_f(\kappa \circ \xi, \eta \circ \xi) \le D_f(\xi \otimes \kappa, \xi \otimes \eta)$.

## Lean

Formalized as [`ProbabilityTheory.fDiv_convex`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.fDiv_convex).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/f_divergence.tex, line 1471](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/f_divergence.tex#L1471)
