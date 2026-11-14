---
declaration: corollary
origin: cited
lean: ProbabilityTheory.neg_log_one_sub_sq_tv_le_klDiv
statement: formalized
proof: formalized
---

# Bretagnolle-Huber inequality

TODO: move this somewhere after the definition of $KL$.

For $\mu, \nu \in \mathcal P(\mathcal X)$,

$$
\begin{aligned}
\operatorname{KL}(\mu, \nu)
&\ge - \log(1 - \operatorname{TV}^2(\mu, \nu))
\: , \\
\text{or equivalently, }
\operatorname{TV}(\mu, \nu)
&\le \sqrt{1 - \exp\left(-\operatorname{KL}(\mu, \nu) \right)}
\: .
\end{aligned}
$$

## Depends on

- [Kullback-Leibler divergence](../../kullback-leibler-divergence/def-kl.md)
- [TV](../../statistical-divergences/part-01/def-tv.md)

## Proof depends on

- [bh_fDiv](thm-bh-fdiv.md)

## Proof

Use the second inequality of Theorem [bh_fDiv](thm-bh-fdiv.md), for $f: x \mapsto x \log x$ .

## Lean

Formalized as [`ProbabilityTheory.neg_log_one_sub_sq_tv_le_klDiv`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.neg_log_one_sub_sq_tv_le_klDiv).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/f_divergence.tex, line 1632](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/f_divergence.tex#L1632)
