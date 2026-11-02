---
declaration: theorem
origin: cited
lean: ArithmeticFunction.sum_divisors_mul_of_coprime
statement: formalized
---

# sum divisors mul of coprime

If $f$ is a multiplicative arithmetic function, then for coprime, nonzero $a$ and $b$, we have that $\sum_{d | ab} f(d) = (\sum_{d | a} f(d)) \cdot (\sum_{d | b} f(d))$.

```
This has been upstreamed #36495.
```

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Since $f$ is multiplicative, we can express the sum over divisors of $ab$ in terms of the sums over divisors of $a$ and $b$. The key idea is to use the fact that the divisors of $ab$ can be expressed as products of divisors of $a$ and divisors of $b$, due to the coprimality condition. Specifically, each divisor $d$ of $ab$ can be uniquely written as $d = d_a * d_b$, where $d_a$ divides $a$ and $d_b$ divides $b$. Therefore, we can rewrite the sum as a double sum over the divisors of $a$ and $b$, which factorizes into the product of the two separate sums.

## Lean

Formalized as [`ArithmeticFunction.sum_divisors_mul_of_coprime`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.sum_divisors_mul_of_coprime).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
