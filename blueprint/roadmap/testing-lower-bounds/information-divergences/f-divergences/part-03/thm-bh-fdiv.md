---
declaration: theorem
origin: cited
lean: ProbabilityTheory.apply_one_add_tv_add_apply_one_sub_tv_le_fDiv, ProbabilityTheory.conj_one_add_tv_add_conj_one_sub_tv_le_fDiv
statement: formalized
proof: formalized
---

# bh_fDiv

Let $\mu, \nu \in \mathcal P(\mathcal X)$. If $f(1) = 0$,

$$
\begin{aligned}
D_f(\mu, \nu)
&\ge f(1 + \operatorname{TV}(\mu, \nu)) + f(1 - \operatorname{TV}(\mu, \nu))
\: , \\
\text{ and }
D_f(\mu, \nu)
&\ge (1 + \operatorname{TV}(\mu, \nu))f\left(\frac{1}{1 + \operatorname{TV}(\mu, \nu)}\right) + (1 - \operatorname{TV}(\mu, \nu))f\left(\frac{1}{1 - \operatorname{TV}(\mu, \nu)}\right)
\: .
\end{aligned}
$$

## Depends on

- [f-divergence](../part-01/def-fdiv.md)
- [TV](../../statistical-divergences/part-01/def-tv.md)

## Proof

Let $V: x \mapsto \max\left\{0, \frac{d\mu}{d\nu}(x) - 1\right\}$ and $W: x \mapsto \max\left\{0, 1 - \frac{d\mu}{d\nu}(x)\right\}$ . Then one of $1+V$ and $1-W$ is equal to $\frac{d\mu}{d\nu}$ and the other is equal to 1. Since $f(1) = 0$, we obtain $f(\frac{d\mu}{d\nu}) = f(1+V) + f(1-W)$ . The $f$-divergence is then

$$
\begin{aligned}
D_f(\mu, \nu)
&= \nu[f(\frac{d\mu}{d\nu})] + f'(\infty)\mu_{\perp \nu}(\mathcal X)
\\
&= \nu\left[f(1+V) + f'(\infty)\mu_{\perp \nu}(\mathcal X)\right] + \nu\left[f(1 - W)\right]
\: .
\end{aligned}
$$

By convexity of $f$, $f(1+V) + f'(\infty)\mu_{\perp \nu}(\mathcal X) \ge f(1+V + \mu_{\perp \nu}(\mathcal X))$ . Using convexity again, we get

$$
\begin{aligned}
D_f(\mu, \nu)
&\ge f(1+ \nu[V] + \mu_{\perp \nu}(\mathcal X)) + f(1 - \nu[W])
\: .
\end{aligned}
$$

By Lemma [Integral form of the total variation distance](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/stat_div.tex#L589), $\nu[V] + \mu_{\perp \nu}(\mathcal X) = \nu[W] = \operatorname{TV}(\mu, \nu)$. We obtain the first equality.

To get the second equality, remark that $D_f(\mu, \nu) = D_{x\mapsto xf(1/x)}(\nu, \mu)$ (Lemma [fDiv_symm](../part-01/lem-fdiv-symm.md)), apply the first inequality to that function and use the symmetry of $\operatorname{TV}$.

## Lean

Formalized as [`ProbabilityTheory.apply_one_add_tv_add_apply_one_sub_tv_le_fDiv`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.apply_one_add_tv_add_apply_one_sub_tv_le_fDiv), [`ProbabilityTheory.conj_one_add_tv_add_conj_one_sub_tv_le_fDiv`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.conj_one_add_tv_add_conj_one_sub_tv_le_fDiv).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/f_divergence.tex, line 1591](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/f_divergence.tex#L1591)
