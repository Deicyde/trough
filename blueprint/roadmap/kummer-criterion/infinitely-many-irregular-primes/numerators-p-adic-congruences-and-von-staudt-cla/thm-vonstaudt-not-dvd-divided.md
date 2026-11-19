---
declaration: theorem
origin: cited
lean: KummerCriterion.not_dvd_num_bernoulli_div_self_of_sub_one_dvd
statement: formalized
proof: formalized
---

# vonstaudt-not-dvd-divided

Let $p$ be a prime and $n$ a positive even index with $(p-1)\mid n$. Then $p\nmid\operatorname{num}(B_n/n)$.

## Depends on

- [num-of-divided](lem-num-of-divided.md)

## Proof

By the von Staudt–Clausen theorem,

$$
B_n + \sum_{(q-1)\mid n} \frac{1}{q} \in \mathbb{Z},
$$

the sum running over primes $q$ with $(q-1)\mid n$. Since $(p-1)\mid n$, the prime $p$ occurs in the correction sum, so $B_n + 1/p$ has denominator prime to $p$. If $p$ divided $\operatorname{num}(B_n)$, then adding $1/p$ would produce a denominator divisible by $p$, a contradiction; by [Lemma num-of-divided](lem-num-of-divided.md) the same holds for the divided numerator.

## Lean

Formalized as [`KummerCriterion.not_dvd_num_bernoulli_div_self_of_sub_one_dvd`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.not_dvd_num_bernoulli_div_self_of_sub_one_dvd).

## Sources

- [Kummer's criterion blueprint: subsections/irregular-primes-carlitz.tex, line 86](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/irregular-primes-carlitz.tex#L86)
