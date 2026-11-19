---
declaration: theorem
origin: cited
lean: KummerCriterion.hMinus_formula_bernoulli_mod_p
statement: formalized
proof: formalized
---

# hminus-bernoulli-mod-p

There exists $z\in\mathbb{Z}_p$ such that, inside $\mathbb{Q}_p$,

$$
h^-(K)
=
\prod_{\substack{j\lt p-2\\ j\ \mathrm{odd}}}
\left(-\frac12\,\frac{B_{j+1}}{j+1}\right)
+ pz .
$$

## Depends on

- [hminus-teichmuller-mod-p](thm-hminus-teichmuller-mod-p.md)
- [teichmuller-bernoulli-congruence](../characters-and-bernoulli-factors/thm-teichmuller-bernoulli-congruence.md)
- [padic-bernoulli-factor](../characters-and-bernoulli-factors/lem-padic-bernoulli-factor.md)

## Proof

Replace each factor $B_{1,\omega^j}$ in [Theorem hminus-teichmuller-mod-p](thm-hminus-teichmuller-mod-p.md) by the congruent classical quotient $B_{j+1}/(j+1)$ from [Theorem teichmuller-bernoulli-congruence](../characters-and-bernoulli-factors/thm-teichmuller-bernoulli-congruence.md); for odd $j < p-2$ the index $j+1$ is even with $0 < j+1 < p-1$, so the hypotheses of the congruence hold. Each replacement changes the product by an element of $p\mathbb{Z}_p$ times a product of $p$-adic integers — integrality of the remaining factors is [Lemma padic-bernoulli-factor](../characters-and-bernoulli-factors/lem-padic-bernoulli-factor.md) — so all errors collect into a single multiple of $p$.

## Lean

Formalized as [`KummerCriterion.hMinus_formula_bernoulli_mod_p`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.hMinus_formula_bernoulli_mod_p).

## Sources

- [Kummer's criterion blueprint: subsections/hminus-formula.tex, line 256](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/hminus-formula.tex#L256)
