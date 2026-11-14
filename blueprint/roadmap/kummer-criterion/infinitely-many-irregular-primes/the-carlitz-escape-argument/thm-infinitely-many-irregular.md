---
declaration: theorem
origin: cited
lean: KummerCriterion.infinite_not_isRegularPrime
statement: formalized
proof: formalized
---

# infinitely-many-irregular

There are infinitely many irregular primes.

## Depends on

- [carlitz-escape](thm-carlitz-escape.md)
- [infinite-of-escape](../from-bernoulli-numerators-to-irregular-primes/lem-infinite-of-escape.md)

## Proof

By [Theorem carlitz-escape](thm-carlitz-escape.md) no finite set contains all irregular primes, so the set is infinite by [Lemma infinite-of-escape](../from-bernoulli-numerators-to-irregular-primes/lem-infinite-of-escape.md).

## Lean

Formalized as [`KummerCriterion.infinite_not_isRegularPrime`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.infinite_not_isRegularPrime).

## Sources

- [Kummer's criterion blueprint: subsections/irregular-primes-carlitz.tex, line 321](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/irregular-primes-carlitz.tex#L321)
