---
declaration: theorem
origin: cited
lean: KummerCriterion.exists_bernoulli_num_dvd_of_not_isRegularPrime
statement: formalized
proof: formalized
---

# bernoulli-witness-of-irregular

Conversely, if an odd prime $p$ is not regular, then there is a $k$ with $1\le k$, $2k\le p-3$ and $p\mid\operatorname{num}(B_{2k})$.

## Depends on

- [kummer-criterion](../../final-assembly/kummers-criterion/thm-kummer-criterion.md)

## Proof

Immediate from [Theorem kummer-criterion](../../final-assembly/kummers-criterion/thm-kummer-criterion.md).

## Lean

Formalized as [`KummerCriterion.exists_bernoulli_num_dvd_of_not_isRegularPrime`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.exists_bernoulli_num_dvd_of_not_isRegularPrime).

## Sources

- [Kummer's criterion blueprint: subsections/irregular-primes-carlitz.tex, line 32](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/irregular-primes-carlitz.tex#L32)
