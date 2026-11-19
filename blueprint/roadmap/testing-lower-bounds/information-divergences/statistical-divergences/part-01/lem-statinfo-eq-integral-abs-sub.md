---
declaration: lemma
origin: cited
lean: ProbabilityTheory.toReal_statInfo_eq_integral_abs
statement: formalized
---

# statInfo_eq_integral_abs_sub

For finite measures $\mu, \nu$ and $\xi \in \mathcal M(\{0,1\})$, for any measure $\zeta$ with $\mu \ll \zeta$ and $\nu \ll \zeta$ ,

$$
\begin{aligned}
\mathcal I_\xi(\mu, \nu)
&= - \frac{1}{2} \left\vert \xi_0\mu(\mathcal X) - \xi_1\nu(\mathcal X) \right\vert +
\frac{1}{2} \zeta\left[x \mapsto \left\vert \xi_0\frac{d \mu}{d\zeta}(x) - \xi_1\frac{d \nu}{d\zeta}(x)\right\vert\right]
\: .
\end{aligned}
$$

This holds in particular for $\zeta = P \circ \xi$.

## Depends on

- [statInfo](def-statinfo.md)

## Proof depends on

- [bayesBinaryRisk_eq_abs](../../../testing-estimation-risk/simple-binary-hypothesis-testing/cor-bayesbinaryrisk-eq-abs.md)

## Proof

Apply Corollary [bayesBinaryRisk_eq_abs](../../../testing-estimation-risk/simple-binary-hypothesis-testing/cor-bayesbinaryrisk-eq-abs.md) and write $\min\{\xi_0\mu(\mathcal X), \xi_1\nu(\mathcal X)\} = \frac{1}{2}\left((P \circ \xi)(\mathcal X) - \left\vert \xi_0\mu(\mathcal X) - \xi_1\nu(\mathcal X) \right\vert \right)$ to get the result for $\zeta = P \circ \xi$. The result for other $\zeta$ follows from simple manipulations of Radon-Nikodym derivatives.

## Lean

Stated as [`ProbabilityTheory.toReal_statInfo_eq_integral_abs`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.toReal_statInfo_eq_integral_abs); the blueprint marks no proof of it as formalized.

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/stat_div.tex, line 135](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/stat_div.tex#L135)
