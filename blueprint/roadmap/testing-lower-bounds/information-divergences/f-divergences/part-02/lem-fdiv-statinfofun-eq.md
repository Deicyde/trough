---
declaration: lemma
origin: cited
lean: ProbabilityTheory.fDiv_statInfoFun_eq_StatInfo_of_nonneg_of_le, ProbabilityTheory.fDiv_statInfoFun_eq_StatInfo_of_nonneg_of_gt
statement: formalized
proof: formalized
---

# fDiv_statInfoFun_eq

Let $a,b \in [0, +\infty)$ and let $\mu, \nu$ be two measures on $\mathcal X$.

$$
\begin{aligned}
D_{\phi_{a,b}}(\mu, \nu)
&= \text{sign}(b-a)\frac{1}{2}(a \mu(\mathcal X) - b \nu(\mathcal X)) + \frac{1}{2}\nu\left[ \left\vert a \frac{d\mu}{d\nu} - b \right\vert \right] + \frac{1}{2}a \mu_{\perp \nu}(\mathcal X)
\: ,
\end{aligned}
$$

in which $\text{sign}(b-a)$ is $1$ if $b-a > 0$ and $-1$ if $b-a \le 0$.

## Depends on

- [f-divergence](../part-01/def-fdiv.md)
- [statInfoFun](def-statinfofun.md)

## Proof

If $a \le b$,

$$
\begin{aligned}
D_{\phi_{a,b}}(\mu, \nu)
&= \nu\left[ \max\{0, a \frac{d\mu}{d\nu} - b\} \right] + a \mu_{\perp \nu}(\mathcal X)
\\
&= \frac{1}{2}(a \mu_{\parallel \nu}(\mathcal X) - b \nu(\mathcal X)) + \frac{1}{2}\nu\left[ \left\vert a \frac{d\mu}{d\nu} - b \right\vert \right] + a \mu_{\perp \nu}(\mathcal X)
\\
&= \frac{1}{2}(a \mu(\mathcal X) - b \nu(\mathcal X)) + \frac{1}{2}\nu\left[ \left\vert a \frac{d\mu}{d\nu} - b \right\vert \right] + \frac{1}{2}a \mu_{\perp \nu}(\mathcal X)
\: .
\end{aligned}
$$

Similar computations lead to the result for $b \le a$.

## Lean

Formalized as [`ProbabilityTheory.fDiv_statInfoFun_eq_StatInfo_of_nonneg_of_le`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.fDiv_statInfoFun_eq_StatInfo_of_nonneg_of_le), [`ProbabilityTheory.fDiv_statInfoFun_eq_StatInfo_of_nonneg_of_gt`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.fDiv_statInfoFun_eq_StatInfo_of_nonneg_of_gt).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/f_divergence.tex, line 1080](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/f_divergence.tex#L1080)
