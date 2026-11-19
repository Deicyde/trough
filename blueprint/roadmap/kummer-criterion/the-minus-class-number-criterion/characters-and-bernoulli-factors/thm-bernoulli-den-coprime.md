---
declaration: theorem
origin: cited
lean: KummerCriterion.prime_not_dvd_bernoulli_den_of_lt_sub_one
statement: formalized
proof: formalized
---

# bernoulli-den-coprime

For $0\lt n\lt p-1$, the prime $p$ does not divide the denominator of $B_n$.

## Depends on

- [bernoulli-padicInt-below](thm-bernoulli-padicint-below.md)

## Proof

This is the rational form of [Theorem bernoulli-padicInt-below](thm-bernoulli-padicint-below.md): a rational number lies in $\mathbb{Z}_p$ exactly when its reduced denominator is prime to $p$.

## Lean

Formalized as [`KummerCriterion.prime_not_dvd_bernoulli_den_of_lt_sub_one`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.prime_not_dvd_bernoulli_den_of_lt_sub_one).

## Sources

- [Kummer's criterion blueprint: subsections/hminus-formula.tex, line 73](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/hminus-formula.tex#L73)
