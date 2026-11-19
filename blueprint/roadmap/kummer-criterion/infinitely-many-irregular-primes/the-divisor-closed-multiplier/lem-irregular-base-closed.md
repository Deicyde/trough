---
declaration: lemma
origin: cited
lean: KummerCriterion.sub_one_dvd_m_of_prime_dvd_m
statement: formalized
proof: formalized
---

# irregular-base-closed

Let $m = C(S)\cdot 2^t$. Every prime $q$ dividing $m$ satisfies $(q-1)\mid m$.

## Depends on

- [irregular-base](def-irregular-base.md)

## Proof

If $q = 2$ this is trivial. Otherwise $q$ divides $M(S)!$, hence $q \le M(S)$, and as before $(q-1) \mid M(S)! \mid m$.

## Lean

Formalized as [`KummerCriterion.sub_one_dvd_m_of_prime_dvd_m`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.sub_one_dvd_m_of_prime_dvd_m).

## Sources

- [Kummer's criterion blueprint: subsections/irregular-primes-carlitz.tex, line 177](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/irregular-primes-carlitz.tex#L177)
