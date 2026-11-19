---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.integral_comp_eval
---

# integral_eval_pi

For $\mu_1, \ldots, \mu_d$ probability measures on $\mathbb{R}$ and $f : \mathbb{R} \to \mathbb{R}$ integrable with respect to $\mu_i$, we have

$$
\begin{aligned}
\int_x f(x_i) \, d(\mu_1 \times \ldots \times \mu_d)(x)
= \int_x f(x) \, d\mu_i
\: .
\end{aligned}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

As $f$ is integrable, we can use Fubini theorem to obtain that

$$
\int f(x_i) \, d(\mu_1 \times \ldots \times \mu_d)(x) = \int f(x) \, d\mu_i(x) \times \prod_{j \ne i} \int 1 \, d\mu_j(x) = \int f(x) \, d\mu_i(x)
$$

because the $\mu_j$s are probability measures.

## Lean

Formalized as [`MeasureTheory.integral_comp_eval`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.integral_comp_eval).

## Sources

- [Brownian motion blueprint: chapters/gaussian.tex, line 315](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/gaussian.tex#L315)
