---
declaration: lemma
origin: cited
lean: ProbabilityTheory.le_fDiv_of_ac
statement: formalized
proof: formalized
---

# Superseded by Lemma le_fDiv

Let $\mu, \nu$ be two finite measures on the same space $\mathcal X$, such that $\mu \ll \nu$. Then $\nu(\mathcal X) f(\mu(\mathcal X)/\nu(\mathcal X)) \le D_f(\mu, \nu)$.

## Depends on

- [f-divergence](def-fdiv.md)

## Proof

Since $\mu \ll \nu$ the $f$-divergence is only the integral part. If $\nu = 0$ there is nothing to prove. Otherwise, by Jensen's inequality for the probability measure $\nu / \nu(\mathcal X)$,

$$
\begin{aligned}
D_f(\mu, \nu)
&= \nu(\mathcal X) \frac{1}{\nu(\mathcal X)}\nu\left[ f\left( \frac{d\mu}{d\nu} \right) \right]
\ge \nu(\mathcal X) f\left( \frac{1}{\nu(\mathcal X)}\nu\left[\frac{d\mu}{d\nu} \right] \right)
= \nu(\mathcal X) f(\mu(\mathcal X)/\nu(\mathcal X))
\: .
\end{aligned}
$$

## Lean

Formalized as [`ProbabilityTheory.le_fDiv_of_ac`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.le_fDiv_of_ac).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/f_divergence.tex, line 295](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/f_divergence.tex#L295)
