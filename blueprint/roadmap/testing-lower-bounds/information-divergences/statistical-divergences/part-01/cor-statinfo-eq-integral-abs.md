---
declaration: corollary
origin: cited
lean: ProbabilityTheory.toReal_statInfo_eq_integral_abs
statement: formalized
proof: formalized
---

# statInfo_eq_integral_abs

For finite measures $\mu, \nu$ and $\xi \in \mathcal M(\{0,1\})$,

$$
\begin{aligned}
\mathcal I_\xi(\mu, \nu)
&= -\frac{1}{2} \left\vert\xi_0 \mu(\mathcal X) - \xi_1 \nu(\mathcal X)\right\vert + \frac{1}{2}\left( \nu\left[ x \mapsto \left\vert\xi_0\frac{d \mu}{d\nu}(x) - \xi_1 \right\vert \right]  + \xi_0 \mu_{\perp \nu}(\mathcal X)\right)
\: .
\end{aligned}
$$

## Depends on

- [statInfo](def-statinfo.md)

## Proof depends on

- [Integral form of the statistical information](thm-statinfo-eq-integral.md)

## Proof

Start from Theorem [Integral form of the statistical information](thm-statinfo-eq-integral.md), then use $\max\{a,b\} = \frac{1}{2}\left( a + b + \vert a - b \vert \right)$ . The two cases of Theorem [Integral form of the statistical information](thm-statinfo-eq-integral.md) lead to the same expression.

## Lean

Formalized as [`ProbabilityTheory.toReal_statInfo_eq_integral_abs`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.toReal_statInfo_eq_integral_abs).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/stat_div.tex, line 207](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/stat_div.tex#L207)
