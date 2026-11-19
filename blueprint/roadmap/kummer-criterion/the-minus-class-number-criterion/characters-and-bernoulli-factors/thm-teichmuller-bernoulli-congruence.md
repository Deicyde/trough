---
declaration: theorem
origin: cited
lean: KummerCriterion.bernoulliGen_teichmuller_pow_sModEq_div
statement: formalized
proof: formalized
---

# teichmuller-bernoulli-congruence

For the odd exponents $j$ occurring in the relative class-number formula (odd $j$ with $j + 1$ divisible by neither $p$ nor $p-1$),

$$
B_{1,\omega^j}
\equiv \frac{B_{j+1}}{j+1}\pmod p .
$$

## Depends on

- [generalized-bernoulli](def-generalized-bernoulli.md)
- [teichmuller](def-teichmuller.md)

## Proof

This is the standard congruence linking generalised Bernoulli values of Teichmüller powers to classical Bernoulli numbers. Writing $B_{1,\omega^j} = \tfrac1p \sum_a \omega^j(a)\,a$ and using $\omega(a) \equiv a^{p^r}$ to high $p$-adic accuracy, the sum is compared with the power sum $\sum_a a^{\,j+1}$, which Faulhaber's formula relates to $B_{j+1}$; the hypothesis that $j+1$ is divisible by neither $p$ nor $p-1$ makes the comparison factor a $p$-adic unit and keeps the error terms in $p\mathbb{Z}_p$.

## Lean

Formalized as [`KummerCriterion.bernoulliGen_teichmuller_pow_sModEq_div`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.bernoulliGen_teichmuller_pow_sModEq_div).

## Sources

- [Kummer's criterion blueprint: subsections/hminus-formula.tex, line 98](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/hminus-formula.tex#L98)
