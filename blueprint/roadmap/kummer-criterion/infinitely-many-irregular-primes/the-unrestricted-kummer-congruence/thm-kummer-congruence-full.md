---
declaration: theorem
origin: cited
lean: KummerCriterion.bernoulli_div_sModEq_of_modEq_full
statement: formalized
proof: formalized
---

# kummer-congruence-full

Let $p$ be an odd prime and $m, n$ positive even indices with $m \equiv n \pmod{p-1}$ and $(p-1)\nmid n$. Then

$$
\frac{B_m}{m} \;\equiv\; \frac{B_n}{n} \pmod{p}.
$$

## Depends on

- [kummer-congruence-gefive](thm-kummer-congruence-gefive.md)

## Proof

It remains to lift the restriction $p \ge 5$ of [Theorem kummer-congruence-gefive](thm-kummer-congruence-gefive.md) to all odd primes. The only other odd prime is $p = 3$, where $p - 1 = 2$ divides every even index; the hypothesis $(p-1)\nmid n$ is then unsatisfiable, so there is nothing left to prove.

## Lean

Formalized as [`KummerCriterion.bernoulli_div_sModEq_of_modEq_full`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.bernoulli_div_sModEq_of_modEq_full).

## Sources

- [Kummer's criterion blueprint: subsections/irregular-primes-carlitz.tex, line 236](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/irregular-primes-carlitz.tex#L236)
