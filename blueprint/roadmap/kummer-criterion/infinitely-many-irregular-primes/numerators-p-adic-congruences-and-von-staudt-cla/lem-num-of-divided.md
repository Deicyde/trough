---
declaration: lemma
origin: cited
lean: KummerCriterion.dvd_num_of_dvd_div_nat_num
statement: formalized
proof: formalized
---

# num-of-divided

Let $q$ be a rational and $n$ a positive natural number. If $p\mid\operatorname{num}(q/n)$, then $p\mid\operatorname{num}(q)$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Dividing by $n$ can only cancel factors of the numerator.

## Lean

Formalized as [`KummerCriterion.dvd_num_of_dvd_div_nat_num`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.dvd_num_of_dvd_div_nat_num).

## Sources

- [Kummer's criterion blueprint: subsections/irregular-primes-carlitz.tex, line 77](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/irregular-primes-carlitz.tex#L77)
