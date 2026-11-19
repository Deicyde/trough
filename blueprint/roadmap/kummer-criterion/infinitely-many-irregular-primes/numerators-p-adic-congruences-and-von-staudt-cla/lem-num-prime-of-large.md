---
declaration: lemma
origin: cited
lean: KummerCriterion.exists_prime_dvd_num_of_one_lt_abs
statement: formalized
proof: formalized
---

# num-prime-of-large

If a rational number $q$ has $|q| > 1$, then some prime divides $\operatorname{num}(q)$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Since $|q| > 1$, the numerator of $|q|$ strictly exceeds its denominator; in particular $|\operatorname{num}(q)| \ge 2$, so the numerator has a prime factor.

## Lean

Formalized as [`KummerCriterion.exists_prime_dvd_num_of_one_lt_abs`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.exists_prime_dvd_num_of_one_lt_abs).

## Sources

- [Kummer's criterion blueprint: subsections/irregular-primes-carlitz.tex, line 56](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/irregular-primes-carlitz.tex#L56)
