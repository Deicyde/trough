---
declaration: theorem
origin: cited
lean: ArithmeticFunction.liouville
statement: formalized
proof: formalized
---

# liouville

Liouville function: $\lambda(n) = (-1)^{\Omega(n)}$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

The Liouville function $\lambda(n)$ is defined as $(-1)^{\Omega(n)}$, where $\Omega(n)$ is the total number of prime factors of $n$ counted with multiplicity. This means that for each prime factor of $n$, we contribute a factor of $-1$ to the product, and the overall sign of $\lambda(n)$ depends on whether the total number of prime factors is even or odd. Thus, we have $\lambda(n) = (-1)^{\Omega(n)}$ by definition.

## Lean

Formalized as [`ArithmeticFunction.liouville`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.liouville).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/b47896b36cc6e36559189281330930ecf25fae7a/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
