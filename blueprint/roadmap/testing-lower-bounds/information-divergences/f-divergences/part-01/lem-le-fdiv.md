---
declaration: lemma
origin: cited
lean: ProbabilityTheory.le_fDiv
statement: formalized
proof: formalized
---

# le_fDiv

Let $\mu, \nu$ be two finite measures on the same space $\mathcal X$. Then $\nu(\mathcal X) f(\mu(\mathcal X)/\nu(\mathcal X)) \le D_f(\mu, \nu)$. In particular, if $\nu$ is a probability measure, $f(\mu(\mathcal X)) \le D_f(\mu, \nu)$.

## Depends on

- [f-divergence](def-fdiv.md)

## Proof depends on

- [fDiv_eq_add_withDensity_derivAtTop](lem-fdiv-eq-add-withdensity-derivattop.md)
- [Superseded by Lemma le_fDiv](lem-le-fdiv-of-ac.md)

## Proof

By convexity, then Lemma [Superseded by Lemma le_fDiv](lem-le-fdiv-of-ac.md) and finally Lemma [fDiv_eq_add_withDensity_derivAtTop](lem-fdiv-eq-add-withdensity-derivattop.md),

$$
\begin{aligned}
\nu(\mathcal X) f(\mu(\mathcal X)/\nu(\mathcal X))
&\le \nu(\mathcal X) f(\frac{d\mu}{d\nu}\cdot \nu (\mathcal X)/\nu(\mathcal X)) + f'(\infty)\mu_{\perp}(\mathcal X)
\\
&\le D_f(\frac{d\mu}{d\nu}\cdot \nu , \nu) + f'(\infty)\mu_{\perp}(\mathcal X)
\\
&= D_f(\mu, \nu)
\: .
\end{aligned}
$$

## Lean

Formalized as [`ProbabilityTheory.le_fDiv`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.le_fDiv).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/f_divergence.tex, line 316](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/f_divergence.tex#L316)
