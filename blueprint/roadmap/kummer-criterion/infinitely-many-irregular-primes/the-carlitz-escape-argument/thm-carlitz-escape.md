---
declaration: theorem
origin: cited
lean: KummerCriterion.exists_not_isRegularPrime_not_mem_carlitz
statement: formalized
proof: formalized
---

# carlitz-escape

For every finite set $S$ of natural numbers there is an irregular prime $p \notin S$.

## Depends on

- [carlitz-numerator-prime](thm-carlitz-numerator-prime.md)
- [carlitz-criterion](thm-carlitz-criterion.md)

## Proof

Take the prime $p$ and the index $M$ of [Theorem carlitz-numerator-prime](thm-carlitz-numerator-prime.md). Then $p$ is irregular by [Theorem carlitz-criterion](thm-carlitz-criterion.md) and $p \notin S$.

## Lean

Formalized as [`KummerCriterion.exists_not_isRegularPrime_not_mem_carlitz`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.exists_not_isRegularPrime_not_mem_carlitz).

## Sources

- [Kummer's criterion blueprint: subsections/irregular-primes-carlitz.tex, line 310](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/irregular-primes-carlitz.tex#L310)
