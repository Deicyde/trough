---
declaration: lemma
origin: cited
lean: ProbabilityTheory.klDiv_eq_fDiv
statement: formalized
proof: formalized
---

# condKL_eq_condFDiv

$\operatorname{KL}(\kappa, \eta \mid \mu) = D_f(\kappa, \eta \mid \mu)$ for $f: x \mapsto x \log x$.

## Depends on

- [Conditional Kullback-Leibler divergence](def-condkl.md)
- [Conditional f-divergence](../f-divergences/part-01/def-condfdiv.md)

## Proof

Simple computation.

## Lean

Formalized as [`ProbabilityTheory.klDiv_eq_fDiv`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.klDiv_eq_fDiv).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/kl_divergence.tex, line 42](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/kl_divergence.tex#L42)
