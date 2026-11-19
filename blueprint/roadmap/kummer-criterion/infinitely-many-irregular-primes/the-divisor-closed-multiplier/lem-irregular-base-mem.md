---
declaration: lemma
origin: cited
lean: KummerCriterion.sub_one_dvd_irregularBase_of_mem
statement: formalized
proof: formalized
---

# irregular-base-mem

$C(S)$ is even and positive, and for every prime $q \in S$ one has $(q-1)\mid C(S)$.

## Depends on

- [irregular-base](def-irregular-base.md)

## Proof

$q \le M(S)$, so $q - 1$ is a positive integer at most $M(S)$ and therefore divides $M(S)!$.

## Lean

Formalized as [`KummerCriterion.sub_one_dvd_irregularBase_of_mem`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.sub_one_dvd_irregularBase_of_mem).

## Sources

- [Kummer's criterion blueprint: subsections/irregular-primes-carlitz.tex, line 166](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/irregular-primes-carlitz.tex#L166)
