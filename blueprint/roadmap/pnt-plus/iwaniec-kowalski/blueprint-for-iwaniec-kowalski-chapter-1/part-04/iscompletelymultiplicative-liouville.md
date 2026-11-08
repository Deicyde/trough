---
declaration: theorem
origin: cited
lean: ArithmeticFunction.isCompletelyMultiplicative_liouville
statement: formalized
---

# isCompletelyMultiplicative liouville

The Liouville function is completely multiplicative.

## Depends on

- [liouville](liouville.md)
- [IsCompletelyMultiplicative](iscompletelymultiplicative.md)

## Proof

The Liouville function $\lambda(n)$ is defined as $(-1)^{\Omega(n)}$, where $\Omega(n)$ counts the total number of prime factors of $n$ with multiplicity. To show that $\lambda$ is completely multiplicative, we need to verify that $\lambda(1) = 1$ and that $\lambda(ab) = \lambda(a)\lambda(b)$ for all natural numbers $a$ and $b$.

## Lean

Stated as [`ArithmeticFunction.isCompletelyMultiplicative_liouville`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.isCompletelyMultiplicative_liouville); the blueprint does not mark its proof formalized.

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
