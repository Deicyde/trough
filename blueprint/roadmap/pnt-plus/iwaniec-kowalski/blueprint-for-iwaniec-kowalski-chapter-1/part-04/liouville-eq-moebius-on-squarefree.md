---
declaration: theorem
origin: cited
lean: ArithmeticFunction.liouville_eq_moebius_on_squarefree
statement: formalized
proof: formalized
---

# liouville eq moebius on squarefree

The Liouville function agrees with the Möbius function on square-free numbers.

## Depends on

- [liouville](liouville.md)

## Proof

The Liouville function $\lambda(n)$ is defined as $(-1)^{\Omega(n)}$, where $\Omega(n)$ counts the total number of prime factors of $n$ with multiplicity. The Möbius function $\mu(n)$ is defined as $0$ if $n$ has a squared prime factor, and otherwise it is $(-1)^{\omega(n)}$, where $\omega(n)$ counts the number of distinct prime factors of $n$. For square-free numbers, we have $\Omega(n) = \omega(n)$, since there are no repeated prime factors. Therefore, for square-free numbers, we have $\lambda(n) = (-1)^{\omega(n)} = \mu(n)$, which shows that the Liouville function agrees with the Möbius function on square-free numbers.

## Lean

Formalized as [`ArithmeticFunction.liouville_eq_moebius_on_squarefree`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.liouville_eq_moebius_on_squarefree).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/b47896b36cc6e36559189281330930ecf25fae7a/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
