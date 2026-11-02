---
declaration: theorem
origin: cited
lean: ArithmeticFunction.sum_moebius_pmul_eq_prod_one_sub
statement: formalized
proof: formalized
---

# sum moebius pmul eq prod one sub

If $g$ is a multiplicative arithmetic function, then for any $n \neq 0$, $\sum_{d | n} \mu(d) \cdot g(d) = \prod_{p | n} (1 - g(p))$.

```
Upstream issue has been created #1240.
```

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [sum divisors mul of coprime](sum-divisors-mul-of-coprime.md)

## Proof

Multiply out and collect terms.

## Lean

Formalized as [`ArithmeticFunction.sum_moebius_pmul_eq_prod_one_sub`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.sum_moebius_pmul_eq_prod_one_sub).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
