---
declaration: lemma
origin: cited
lean: ProbabilityTheory.tv_eq_tvDist_sub_abs, ProbabilityTheory.tvDist_eq_two_mul_tv, ProbabilityTheory.tv_eq_tvDist_div_two
statement: formalized
proof: formalized
---

# tv_eq_tvDist

For finite measures $\mu, \nu$,

$$
\begin{aligned}
\operatorname{TV}(\mu, \nu)
&= \frac{1}{2} \left( \vert \mu - \nu \vert(\mathcal X) - \left\vert \mu(\mathcal X) - \nu(\mathcal X)\right\vert \right)
\: .
\end{aligned}
$$

In particular, if $\mu(\mathcal X) = \nu(\mathcal X)$ (for example for probability measures) then $\operatorname{TV}(\mu, \nu) = \frac{1}{2} \vert \mu - \nu \vert(\mathcal X)$.

## Depends on

- [TV](../part-01/def-tv.md)
- [Total variation distance of Mathlib](../part-01/def-tvdist.md)

## Proof depends on

- [statInfo_eq_integral_abs](../part-01/cor-statinfo-eq-integral-abs.md)
- [tvDist_eq_integral_abs](../part-01/lem-tvdist-eq-integral-abs.md)

## Proof

Corollary [statInfo_eq_integral_abs](../part-01/cor-statinfo-eq-integral-abs.md) for $\xi = (1,1)$ gives

$$
\begin{aligned}
\operatorname{TV}(\mu, \nu)
&= -\frac{1}{2} \left\vert \mu(\mathcal X) - \nu(\mathcal X)\right\vert + \frac{1}{2}\left( \nu\left[ x \mapsto \left\vert \frac{d \mu}{d\nu}(x) - 1 \right\vert \right]  + \mu_{\perp \nu}(\mathcal X)\right)
\: ,
\end{aligned}
$$

and the term in parentheses is $\vert \mu - \nu \vert(\mathcal X)$ by Lemma [tvDist_eq_integral_abs](../part-01/lem-tvdist-eq-integral-abs.md).

## Lean

Formalized as [`ProbabilityTheory.tv_eq_tvDist_sub_abs`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.tv_eq_tvDist_sub_abs), [`ProbabilityTheory.tvDist_eq_two_mul_tv`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.tvDist_eq_two_mul_tv), [`ProbabilityTheory.tv_eq_tvDist_div_two`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.tv_eq_tvDist_div_two).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/stat_div.tex, line 657](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/stat_div.tex#L657)
