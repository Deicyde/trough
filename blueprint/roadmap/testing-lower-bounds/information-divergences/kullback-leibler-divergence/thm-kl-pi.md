---
declaration: theorem
origin: cited
lean: ProbabilityTheory.klDiv_pi
statement: formalized
proof: formalized
---

# Tensorization - finite product

Let $I$ be a finite index set. Let $(\mu_i)_{i \in I}, (\nu_i)_{i \in I}$ be probability measures on spaces $(\mathcal X_i)_{i \in I}$. Then

$$
\begin{aligned}
\operatorname{KL}(\prod_{i \in I} \mu_i, \prod_{i \in I} \nu_i) = \sum_{i \in I} \operatorname{KL}(\mu_i, \nu_i)
\: .
\end{aligned}
$$

## Depends on

- [Kullback-Leibler divergence](def-kl.md)

## Proof depends on

- [Tensorization](thm-kl-prod-two.md)

## Proof

Induction on the size of $I$, using Theorem [Tensorization](thm-kl-prod-two.md).

## Lean

Formalized as [`ProbabilityTheory.klDiv_pi`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.klDiv_pi).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/kl_divergence.tex, line 361](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/kl_divergence.tex#L361)
