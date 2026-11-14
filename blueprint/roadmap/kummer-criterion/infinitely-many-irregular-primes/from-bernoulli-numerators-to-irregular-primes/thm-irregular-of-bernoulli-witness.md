---
declaration: theorem
origin: cited
lean: KummerCriterion.not_isRegularPrime_of_bernoulli_num_dvd
statement: formalized
proof: formalized
---

# irregular-of-bernoulli-witness

Let $p$ be an odd prime. If there is a $k$ with $1\le k$, $2k\le p-3$ and $p\mid\operatorname{num}(B_{2k})$, then $p$ is not regular.

## Depends on

- [kummer-criterion](../../final-assembly/kummers-criterion/thm-kummer-criterion.md)

## Proof

Immediate from [Theorem kummer-criterion](../../final-assembly/kummers-criterion/thm-kummer-criterion.md).

## Lean

Formalized as [`KummerCriterion.not_isRegularPrime_of_bernoulli_num_dvd`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.not_isRegularPrime_of_bernoulli_num_dvd).

## Sources

- [Kummer's criterion blueprint: subsections/irregular-primes-carlitz.tex, line 22](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/irregular-primes-carlitz.tex#L22)
