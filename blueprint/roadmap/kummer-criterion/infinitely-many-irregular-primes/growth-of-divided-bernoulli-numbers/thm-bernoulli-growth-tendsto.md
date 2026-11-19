---
declaration: theorem
origin: cited
lean: KummerCriterion.tendsto_abs_bernoulli_div_self_even
statement: formalized
proof: formalized
---

# bernoulli-growth-tendsto

$\left|B_{2k}/2k\right| \to \infty$ as $k \to \infty$.

## Depends on

- [bernoulli-growth-bound](thm-bernoulli-growth-bound.md)

## Proof

The lower bound of [Theorem bernoulli-growth-bound](thm-bernoulli-growth-bound.md) tends to infinity: factorial growth beats the geometric factor $(2\pi^2)^{k}$ in the denominator.

## Lean

Formalized as [`KummerCriterion.tendsto_abs_bernoulli_div_self_even`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.tendsto_abs_bernoulli_div_self_even).

## Sources

- [Kummer's criterion blueprint: subsections/irregular-primes-carlitz.tex, line 134](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/irregular-primes-carlitz.tex#L134)
