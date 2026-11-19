---
declaration: lemma
origin: cited
lean: ProbabilityTheory.statInfo_eq_min_sub_lintegral, ProbabilityTheory.statInfo_eq_min_sub_lintegral', ProbabilityTheory.toReal_statInfo_eq_min_sub_integral
statement: formalized
proof: formalized
---

# statInfo_eq_sub_min

For finite measures $\mu, \nu$ and $\xi \in \mathcal M(\{0,1\})$, for any measure $\zeta$ with $\mu \ll \zeta$ and $\nu \ll \zeta$ ,

$$
\begin{aligned}
\mathcal I_\xi(\mu, \nu)
&= \min\{\xi_0\mu(\mathcal X), \xi_1\nu(\mathcal X)\} - \zeta\left[x \mapsto \min \left\{\xi_0\frac{d \mu}{d\zeta}(x), \xi_1\frac{d \nu}{d\zeta}(x)\right\}\right]
\: .
\end{aligned}
$$

This holds in particular for $\zeta = P \circ \xi$.

## Depends on

- [statInfo](def-statinfo.md)

## Proof depends on

- [bayesBinaryRisk_eq](../../../testing-estimation-risk/simple-binary-hypothesis-testing/thm-bayesbinaryrisk-eq.md)

## Proof

Apply Theorem [bayesBinaryRisk_eq](../../../testing-estimation-risk/simple-binary-hypothesis-testing/thm-bayesbinaryrisk-eq.md) to get that result for $\zeta = P \circ \xi$. Then for other $\zeta$ with $\mu \ll \zeta$ and $\nu \ll \zeta$ , use $\frac{d \mu}{d\zeta} = \frac{d \mu}{d(P \circ \xi)} / \frac{d (P \circ \xi)}{d\zeta}$ .

## Lean

Formalized as [`ProbabilityTheory.statInfo_eq_min_sub_lintegral`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.statInfo_eq_min_sub_lintegral), [`ProbabilityTheory.statInfo_eq_min_sub_lintegral'`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.statInfo_eq_min_sub_lintegral'), [`ProbabilityTheory.toReal_statInfo_eq_min_sub_integral`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.toReal_statInfo_eq_min_sub_integral).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/stat_div.tex, line 115](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/stat_div.tex#L115)
