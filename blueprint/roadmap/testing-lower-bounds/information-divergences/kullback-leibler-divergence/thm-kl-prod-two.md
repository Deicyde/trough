---
declaration: theorem
origin: cited
lean: ProbabilityTheory.klDiv_prod_two
statement: formalized
proof: formalized
---

# Tensorization

For $\mu_1$ a probability measure on $\mathcal X$, $\nu_1$ a finite measure on $\mathcal{X}$ and $\mu_2, \nu_2$ two probability measures on $\mathcal Y$,

$$
\begin{aligned}
\operatorname{KL}(\mu_1 \times \mu_2, \nu_1 \times \nu_2) = \operatorname{KL}(\mu_1, \nu_1) + \operatorname{KL}(\mu_2 \times \nu_2) \: .
\end{aligned}
$$

## Depends on

- [Kullback-Leibler divergence](def-kl.md)

## Proof depends on

- [kl_prod_two'](lem-kl-prod-two.md)

## Proof

This is a particular case of Lemma [kl_prod_two'](lem-kl-prod-two.md).

## Lean

Formalized as [`ProbabilityTheory.klDiv_prod_two`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.klDiv_prod_two).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/kl_divergence.tex, line 344](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/kl_divergence.tex#L344)
