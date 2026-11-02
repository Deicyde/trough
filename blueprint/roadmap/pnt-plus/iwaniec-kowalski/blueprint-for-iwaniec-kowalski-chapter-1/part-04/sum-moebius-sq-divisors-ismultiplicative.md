---
declaration: theorem
origin: cited
lean: ArithmeticFunction.sum_moebius_sq_divisors_IsMultiplicative
statement: formalized
proof: formalized
---

# sum-moebius-sq-divisors-is-multiplicative

The function $n \mapsto \sum_{d^2|n} \mu(d)$ is multiplicative.

## Depends on

- [sum-moebius-sq-divisors](sum-moebius-sq-divisors.md)

## Proof depends on

- [pow-divisors-mul](pow-divisors-mul.md)
- [pow-divisors-mul-injective](pow-divisors-mul-injective.md)

## Proof

We will show that for coprime $m$ and $n$, we have $\sum_{d^2|mn} \mu(d) = \sum_{d^2|m} \mu(d) \cdot \sum_{d^2|n} \mu(d)$. This follows from Lemma pow-divisors-mul: the divisors $d$ of $mn$ with $d^2 \mid mn$ factor uniquely as $d=ab$ with $a^2 \mid m$ and $b^2 \mid n$. Multiplicativity of $\mu$ then factors the sum.

## Lean

Formalized as [`ArithmeticFunction.sum_moebius_sq_divisors_IsMultiplicative`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.sum_moebius_sq_divisors_IsMultiplicative).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
