---
declaration: corollary
origin: cited
lean: KummerCriterion.exists_large_even_multiple_abs_bernoulli_div_self_gt_one
statement: formalized
proof: formalized
---

# bernoulli-large-multiple

For every positive even $C$ there is a $t$ with $\left|B_{m}/m\right| > 1$ for $m = C\cdot 2^t$.

## Depends on

- [bernoulli-growth-tendsto](thm-bernoulli-growth-tendsto.md)

## Proof

The indices $C \cdot 2^t$ are even and tend to infinity, so [Theorem bernoulli-growth-tendsto](thm-bernoulli-growth-tendsto.md) applies along this subsequence.

## Lean

Formalized as [`KummerCriterion.exists_large_even_multiple_abs_bernoulli_div_self_gt_one`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.exists_large_even_multiple_abs_bernoulli_div_self_gt_one).

## Sources

- [Kummer's criterion blueprint: subsections/irregular-primes-carlitz.tex, line 145](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/irregular-primes-carlitz.tex#L145)
